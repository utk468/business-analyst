import { getSystemStatus, fetchReports, deleteReport } from './api.js';
import { escapeHtml } from './utils.js';




document.addEventListener("DOMContentLoaded", () => {
    // Check system status
    fetchSystemStatus();
    
    // Check if history dashboard elements exist
    if (document.getElementById("history-container")) {
        initHistoryHandler();
    }
});





// fetchSystemStatus function fetches the status of the backend API
// and updates the status badges on the frontend.
function fetchSystemStatus() {
    getSystemStatus()
        .then(data => {
            const dbBadge = document.getElementById("badge-db");
            if (dbBadge) {
                dbBadge.textContent = data.storage;
                dbBadge.className = "status-badge " + (data.database_connected ? "mongo" : "local");
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



// initHistoryHandler function initializes the history dashboard
// by fetching and rendering the reports.
function initHistoryHandler() {
    const container = document.getElementById("history-container");
    
    function fetchAndRenderHistory() {
        container.innerHTML = `
            <div style="grid-column: 1/-1; text-align: center; padding: 4rem 0;" id="loading-state">
                <div class="spinner" style="margin: 0 auto 1rem auto; width: 40px; height: 40px; border-width: 4px; border-top-color: var(--primary);"></div>
                <p style="color: var(--text-muted);">Retrieving compiled profiles...</p>
            </div>
        `;
        
        fetchReports()
            .then(reports => {
                container.innerHTML = "";
                
                if (reports.length === 0) {
                    container.innerHTML = `
                        <div style="grid-column: 1/-1; text-align: center; padding: 4rem 1.5rem;" class="glass-card">
                            <h3 style="margin-bottom: 0.5rem; color: var(--text-secondary);">Vault is Empty</h3>
                            <p style="color: var(--text-muted); margin-bottom: 1.5rem; font-size: 0.95rem;">You haven't generated any startup strategies yet.</p>
                            <a href="index.html" class="nav-btn primary" style="display: inline-block;">Consult New Venture</a>
                        </div>
                    `;
                    return;
                }
                
                reports.forEach(report => {
                    const card = document.createElement("div");
                    card.className = "glass-card report-card";
                    
                    const date = new Date(report.created_at).toLocaleDateString(undefined, {
                        year: 'numeric', month: 'short', day: 'numeric', hour: '2-digit', minute: '2-digit'
                    });
                    
                    const meta = report.metadata || {};
                    
                    card.innerHTML = `
                        <div class="report-card-header">
                            <div class="report-card-title">${escapeHtml(meta.startup_idea)}</div>
                            <div class="report-card-meta">
                                <span>${escapeHtml(meta.industry)} | ${escapeHtml(meta.country)}</span>
                            </div>
                        </div>
                        <div class="report-card-body">
                            <p style="font-size:0.8rem; color:var(--text-muted); margin-bottom:8px;">${date}</p>
                            <p style="line-height:1.4;">${escapeHtml(report.executive_summary || "No executive summary available.")}</p>
                        </div>
                        <div class="report-card-footer">
                            <a href="report.html?id=${report.id}" class="card-btn view">Open Report</a>
                            <button class="card-btn delete" data-id="${report.id}" title="Delete Strategy">
                                <span style="font-size: 1.1rem;">🗑</span>
                            </button>
                        </div>
                    `;
                    
                    container.appendChild(card);
                });
                
                // Bind delete event listeners
                container.querySelectorAll(".delete").forEach(btn => {
                    btn.addEventListener("click", () => {
                        const reportId = btn.getAttribute("data-id");
                        if (confirm("Are you sure you want to permanently delete this strategy?")) {
                            executeDeleteReport(reportId);
                        }
                    });
                });
            })
            .catch(err => {
                console.error("Failed to load report history:", err);
                container.innerHTML = `
                    <div style="grid-column: 1/-1; text-align: center; padding: 4rem 1.5rem; border-color: var(--error);" class="glass-card">
                        <h3 style="margin-bottom: 0.5rem; color: var(--error);">Failed to Retrieve Vault</h3>
                        <p style="color: var(--text-muted);">${err.message}</p>
                    </div>
                `;
            });
    }
    
    function executeDeleteReport(reportId) {
        deleteReport(reportId)
            .then(() => {
                fetchAndRenderHistory();
            })
            .catch(err => {
                alert(`Error deleting report: ${err.message}`);
            });
    }
    
    fetchAndRenderHistory();
}
