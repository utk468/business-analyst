import { API_BASE, AGENTS_LIST } from './config.js?v=5';
import { getSystemStatus, submitBrief } from './api.js?v=5';
import { getCountryCurrency } from './utils.js?v=5';
function initApp() {
    fetchSystemStatus();
    if (document.getElementById("startup-form")) {
        initFormHandler();
    }
}
if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", initApp);
} else {
    initApp();
}
function fetchSystemStatus() {
    getSystemStatus()
        .then(data => {
            const dbBadge = document.getElementById("badge-db");
            const aiBadge = document.getElementById("badge-ai");
            if (dbBadge) {
                dbBadge.textContent = data.database_connected ? "MongoDB: Connected" : "MongoDB: Disconnected";
                dbBadge.className = "status-badge " + (data.database_connected ? "mongo" : "error");
            }
            if (aiBadge) {
                aiBadge.textContent = data.grok_active ? "Grok AI: Active" : "Grok AI: Key Missing";
                aiBadge.className = "status-badge " + (data.grok_active ? "grok" : "error");
            }
        })
        .catch(err => {
            console.error("Failed to query API status:", err);
            const dbBadge = document.getElementById("badge-db");
            const aiBadge = document.getElementById("badge-ai");
            if (dbBadge) {
                dbBadge.textContent = "Database Offline";
                dbBadge.className = "status-badge error";
            }
            if (aiBadge) {
                aiBadge.textContent = "AI Offline";
                aiBadge.className = "status-badge error";
            }
        });
}
function initFormHandler() {
    const form = document.getElementById("startup-form");
    const countryInput = document.getElementById("country");
    const budgetSelect = document.getElementById("budget");
    const staticInfo = document.getElementById("static-info");
    const runnerPanel = document.getElementById("runner-panel");
    const logTerminal = document.getElementById("log-terminal-el");
    const progressBar = document.getElementById("progress-bar-el");
    const currentAgentTitle = document.getElementById("current-agent-display");
    const spinner = document.getElementById("runner-spinner");
    const viewReportBtn = document.getElementById("view-report-btn");
    let logsRenderedCount = 0;
    function updateBudgetTiers(countryName) {
        const curr = getCountryCurrency(countryName);
        const budgets = curr.exampleBudgets || ["$10,000 - $25,000", "$25,000 - $100,000", "$100,000 - $500,000", "$500,000 - $2M+"];
        budgetSelect.innerHTML = `<option value="" disabled selected>Select Budget (${curr.code} ${curr.symbol})...</option>`;
        budgets.forEach(b => {
            const opt = document.createElement("option");
            opt.value = b;
            opt.textContent = b;
            budgetSelect.appendChild(opt);
        });
    }
    if (countryInput) {
        countryInput.addEventListener("input", () => {
            if (countryInput.value.trim().length >= 2) {
                updateBudgetTiers(countryInput.value);
            }
        });
        countryInput.addEventListener("change", () => {
            updateBudgetTiers(countryInput.value);
        });
    }
    form.addEventListener("submit", (e) => {
        e.preventDefault();
        const payload = {
            startup_idea: document.getElementById("startup_idea").value,
            industry: document.getElementById("industry").value,
            country: document.getElementById("country").value,
            target_audience: document.getElementById("target_audience").value,
            budget: document.getElementById("budget").value,
            business_stage: document.getElementById("business_stage").value,
            additional_information: document.getElementById("additional_information").value
        };
        Array.from(form.elements).forEach(el => el.disabled = true);
        const submitBtn = document.getElementById("submit-btn");
        submitBtn.style.opacity = "0.5";
        submitBtn.querySelector("span").textContent = "Analyzing Inputs...";
        staticInfo.style.display = "none";
        runnerPanel.style.display = "flex";
        submitBrief(payload)
            .then(data => {
                const taskId = data.task_id;
                setupEventSource(taskId);
            })
            .catch(err => {
                console.error("Submission failed:", err);
                appendLogLine(`[Error] Failed to initiate strategy task: ${err.message}`, "error");
                spinner.style.display = "none";
            });
    });
    function setupEventSource(taskId) {
        appendLogLine("[System] Establishing connection to multi-agent stream...", "system");
        const eventSource = new EventSource(`${API_BASE}/api/analyze/stream/${taskId}`);
        eventSource.onmessage = (event) => {
            const data = JSON.parse(event.data);
            progressBar.style.width = `${data.progress}%`;
            currentAgentTitle.textContent = data.current_agent;
            updateStepperUI(data.current_agent);
            if (data.logs && data.logs.length > logsRenderedCount) {
                for (let i = logsRenderedCount; i < data.logs.length; i++) {
                    const line = data.logs[i];
                    let type = "info";
                    if (line.startsWith("[System]")) type = "system";
                    if (line.startsWith("[Error]") || line.startsWith("[System Error]") || line.toLowerCase().includes("error") || line.includes("failed")) type = "error";
                    appendLogLine(line, type);
                }
                logsRenderedCount = data.logs.length;
            }
            if (data.completed) {
                spinner.style.display = "none";
                eventSource.close();
                if (data.error) {
                    appendLogLine(`[Error] Execution halted: ${data.error}`, "error");
                } else {
                    appendLogLine(`[System] Execution finished. Launching dashboard...`, "system");
                    progressBar.style.background = "var(--success)";
                    viewReportBtn.style.display = "flex";
                    viewReportBtn.onclick = () => {
                        window.location.href = `report.html?id=${data.report_id}`;
                    };
                }
            }
        };
        eventSource.onerror = (err) => {
            console.error("SSE stream error:", err);
            appendLogLine("[Error] Connection lost to analysis process. Trying to reconnect...", "error");
        };
    }
    function updateStepperUI(currentAgentName) {
        const currentIdx = AGENTS_LIST.indexOf(currentAgentName);
        for (let i = 0; i < AGENTS_LIST.length; i++) {
            const stepCard = document.getElementById(`step-${i}`);
            if (!stepCard) continue;
            if (i < currentIdx) {
                stepCard.className = "step-card completed";
            } else if (i === currentIdx) {
                stepCard.className = "step-card active";
                stepCard.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
            } else {
                stepCard.className = "step-card";
            }
        }
    }
    function appendLogLine(text, type = "info") {
        const div = document.createElement("div");
        div.className = `log-entry ${type}`;
        div.textContent = text;
        logTerminal.appendChild(div);
        logTerminal.scrollTop = logTerminal.scrollHeight;
    }
}
