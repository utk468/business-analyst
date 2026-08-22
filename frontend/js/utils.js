// Shared UI Utility Functions

export function escapeHtml(unsafe) {
    if (unsafe === undefined || unsafe === null) return "";
    return String(unsafe)
         .replace(/&/g, "&amp;")
         .replace(/</g, "&lt;")
         .replace(/>/g, "&gt;")
         .replace(/"/g, "&quot;")
         .replace(/'/g, "&#039;");
}

export function formatNumber(val) {
    const num = Number(val);
    if (isNaN(num)) return val;
    return num.toLocaleString();
}

export function formatTextHtml(text) {
    if (!text) return "";
    return escapeHtml(text)
        .replace(/\n\n/g, "</p><p>")
        .replace(/\n/g, "<br>")
        .split("</p><p>").map(p => `<p style="margin-bottom: 1rem;">${p}</p>`).join("");
}

export function renderBulletList(element, list) {
    if (!element) return;
    element.innerHTML = "";
    if (!list || list.length === 0) {
        element.innerHTML = "<li style='color:var(--text-muted);'>No details compiled.</li>";
        return;
    }
    list.forEach(item => {
        const li = document.createElement("li");
        li.style.marginBottom = "6px";
        li.innerHTML = escapeHtml(item);
        element.appendChild(li);
    });
}

export function renderRoadmapMilestones(element, milestones) {
    if (!element) return;
    element.innerHTML = "";
    if (!milestones || milestones.length === 0) {
        element.textContent = "Milestones undefined.";
        return;
    }
    const ul = document.createElement("ul");
    ul.style.paddingLeft = "20px";
    milestones.forEach(m => {
        const li = document.createElement("li");
        li.style.marginBottom = "4px";
        li.textContent = m;
        ul.appendChild(li);
    });
    element.appendChild(ul);
}
