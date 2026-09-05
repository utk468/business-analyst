import { API_BASE } from './config.js';
export async function getSystemStatus() {
    const res = await fetch(`${API_BASE}/api/status`);
    if (!res.ok) throw new Error("API status check failed");
    return res.json();
}
export async function submitBrief(payload) {
    const res = await fetch(`${API_BASE}/api/analyze`, {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify(payload)
    });
    if (!res.ok) throw new Error("Form submission failed");
    return res.json();
}
export async function fetchReports() {
    const res = await fetch(`${API_BASE}/api/reports`);
    if (!res.ok) throw new Error("Failed to fetch reports vault");
    return res.json();
}
export async function fetchReport(id) {
    const res = await fetch(`${API_BASE}/api/reports/${id}`);
    if (!res.ok) throw new Error("Failed to fetch report detailed dossier");
    return res.json();
}
export async function deleteReport(id) {
    const res = await fetch(`${API_BASE}/api/reports/${id}`, {
        method: "DELETE"
    });
    if (!res.ok) throw new Error("Failed to delete strategy from vault");
    return res.json();
}
