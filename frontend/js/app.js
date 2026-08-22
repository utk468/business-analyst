import { API_BASE, AGENTS_LIST } from './config.js';
import { getSystemStatus, submitBrief } from './api.js';



// Initialize the application when the DOM is loaded
document.addEventListener("DOMContentLoaded", () => {
   // fetching the system status
    fetchSystemStatus();
    
     
    // initializing the form handler if the form is present
    if (document.getElementById("startup-form")) {
        initFormHandler();
    }
});




// fetchSystemStatus function fetches the status of the backend API
// and updates the status badges on the frontend.
function fetchSystemStatus() {
    getSystemStatus()
        .then(data => {
            const dbBadge = document.getElementById("badge-db");
            const aiBadge = document.getElementById("badge-ai");
            
            if (dbBadge) {
                dbBadge.textContent = data.storage;
                dbBadge.className = "status-badge " + (data.database_connected ? "mongo" : "local");
            }
            if (aiBadge) {
                aiBadge.textContent = data.grok_active ? "Grok AI: Active" : "Consulting Engine (Fallback)";
                aiBadge.className = "status-badge " + (data.grok_active ? "grok" : "fallback");
            }
        })


        .catch(err => {
            console.error("Failed to query API status:", err);
            const dbBadge = document.getElementById("badge-db");
            if (dbBadge) {
                dbBadge.textContent = "Offline";
                dbBadge.className = "status-badge error";
            }
        });

        
}






function initFormHandler() {
    const form = document.getElementById("startup-form");
    const staticInfo = document.getElementById("static-info");
    const runnerPanel = document.getElementById("runner-panel");
    const logTerminal = document.getElementById("log-terminal-el");
    const progressBar = document.getElementById("progress-bar-el");
    const currentAgentTitle = document.getElementById("current-agent-display");
    const spinner = document.getElementById("runner-spinner");

    const viewReportBtn = document.getElementById("view-report-btn");
    
    let logsRenderedCount = 0;
    


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
        
        // Firing request to the backend
        submitBrief(payload)
            .then(data => {
                // getting task id
                const taskId = data.task_id;
                // setting up event source to receive real-time logs
                setupEventSource(taskId);
            })
            .catch(err => {
                // handling submission errors
                console.error("Submission failed:", err);
                appendLogLine(`[Error] Failed to initiate strategy task: ${err.message}`, "error");
                spinner.style.display = "none";
            });
    });
    

    // setupEventSource is a helper function that handles
    //  the real-time streaming  of logs from the backend server 
    // to the frontend.
    function setupEventSource(taskId) {
        appendLogLine("[System] Establishing connection to multi-agent stream...", "system");
        // EventSource is a JavaScript API used to receive real-time
        // updates from a server using Server-Sent Events (SSE).
        const eventSource = new EventSource(`${API_BASE}/api/analyze/stream/${taskId}`);
        // onmessage is an event handler in JavaScript that runs automatically
        // whenever an EventSource receives a message from the server.
        eventSource.onmessage = (event) => {
            const data = JSON.parse(event.data);
            //  Update Progress Bar
            progressBar.style.width = `${data.progress}%`;
            //  Update Active Agent title
            currentAgentTitle.textContent = data.current_agent;
            //  Update Stepper layout
            updateStepperUI(data.current_agent);
        
            // 4. Update live logs terminal
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
            
            // 5. Complete Execution
            if (data.completed) {
                spinner.style.display = "none";
                // closing server connection
                eventSource.close();
                
                if (data.error) {
                    appendLogLine(`[Error] Execution halted: ${data.error}`, "error");
                } else {
                    appendLogLine(`[System] Execution finished. Launching dashboard...`, "system");
                    progressBar.style.background = "var(--success)";
                    
                    // Showing  report button
                    viewReportBtn.style.display = "flex";
                    viewReportBtn.onclick = () => {
                        window.location.href = `report.html?id=${data.report_id}`;
                    };
                }
            }
        };
        
        // Event handler for SSE errors
        eventSource.onerror = (err) => {
            console.error("SSE stream error:", err);
            appendLogLine("[Error] Connection lost to analysis process. Trying to reconnect...", "error");
        };
    }
    

    // updateStepperUI is a helper function that updates the UI
    // of the stepper based on the current agent name.
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
