const API_CHAT_ENDPOINT = "/api/chat";
const ICONS = {
    expand: `<svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M15 3h6v6M9 21H3v-6M21 3l-7 7M3 21l7-7"/></svg>`,
    minimize: `<svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M4 14h6v6M20 10h-6V4M14 10l7-7M3 21l7-7"/></svg>`,
    trash: `<svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><polyline points="3 6 5 6 21 6"></polyline><path d="M19 6v14a2 2 0 0 1-2 2H7a2 2 0 0 1-2-2V6m3 0V4a2 2 0 0 1 2-2h4a2 2 0 0 1 2 2v2"></path><line x1="10" y1="11" x2="10" y2="17"></line><line x1="14" y1="11" x2="14" y2="17"></line></svg>`,
    send: `<svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"><line x1="22" y1="2" x2="11" y2="13"></line><polygon points="22 2 15 22 11 13 2 9 22 2"></polygon></svg>`
};
class StrategyChatbot {
    constructor(containerId = "chatbot-widget", options = {}) {
        this.container = document.getElementById(containerId);
        this.options = options;
        this.history = [];
        this.isProcessing = false;
        if (this.container) {
            this.render();
            this.bindEvents();
            this.loadInitialGreeting();
        }
    }
    render() {
        const isFullPage = this.options.fullPage || false;
        this.container.innerHTML = `
            <div class="chatbot-card ${isFullPage ? 'full-page-card' : ''}" id="${this.container.id}-card">
                <div class="chat-card-header">
                    <div class="chat-header-title">
                        <span style="font-weight: 700; font-size: 0.85rem; color: var(--primary-dark);">AI Strategy Consultant</span>
                    </div>
                    <div class="chat-header-actions">
                        <button type="button" class="chat-action-btn" id="${this.container.id}-expand-toggle" title="Toggle Fullscreen View">
                            <span id="${this.container.id}-expand-icon">${ICONS.expand}</span>
                        </button>
                        <button type="button" class="chat-action-btn" id="${this.container.id}-clear-btn" title="Clear Chat History">
                            ${ICONS.trash}
                        </button>
                    </div>
                </div>
                <div class="chat-messages ${isFullPage ? 'full-page' : ''}" id="${this.container.id}-messages"></div>
                <form class="chat-input-bar" id="${this.container.id}-form">
                    <input 
                        type="text" 
                        class="chat-input" 
                        id="${this.container.id}-input" 
                        placeholder="Ask anything (e.g. market sizing, pricing model)..." 
                        autocomplete="off"
                    />
                    <button type="submit" class="chat-send-btn" id="${this.container.id}-send-btn" title="Send message">
                        ${ICONS.send}
                    </button>
                </form>
            </div>
        `;
    }
    bindEvents() {
        const form = document.getElementById(`${this.container.id}-form`);
        const clearBtn = document.getElementById(`${this.container.id}-clear-btn`);
        const input = document.getElementById(`${this.container.id}-input`);
        const headerExpandBtn = document.getElementById(`${this.container.id}-expand-toggle`);
        if (form) {
            form.addEventListener("submit", (e) => {
                e.preventDefault();
                this.handleSendMessage();
            });
        }
        if (clearBtn) {
            clearBtn.addEventListener("click", () => {
                this.clearChat();
            });
        }
        if (headerExpandBtn) {
            headerExpandBtn.addEventListener("click", () => {
                this.toggleFullscreen();
            });
        }
        if (input) {
            input.addEventListener("keydown", (e) => {
                if (e.key === "Enter" && !e.shiftKey) {
                    e.preventDefault();
                    this.handleSendMessage();
                }
            });
        }
        document.addEventListener("keydown", (e) => {
            if (e.key === "Escape") {
                const card = document.getElementById(`${this.container.id}-card`);
                if (card && card.classList.contains("is-fullscreen")) {
                    this.toggleFullscreen();
                }
            }
        });
    }
    toggleFullscreen() {
        const card = document.getElementById(`${this.container.id}-card`);
        if (!card) return;
        let backdrop = document.getElementById("chat-fullscreen-backdrop");
        if (!backdrop) {
            backdrop = document.createElement("div");
            backdrop.id = "chat-fullscreen-backdrop";
            backdrop.className = "chat-fullscreen-backdrop";
            document.body.appendChild(backdrop);
            backdrop.addEventListener("click", () => this.toggleFullscreen());
        }
        const isFullscreen = card.classList.toggle("is-fullscreen");
        backdrop.classList.toggle("active", isFullscreen);
        document.body.classList.toggle("chat-modal-open", isFullscreen);
        const iconEl = document.getElementById(`${this.container.id}-expand-icon`);
        if (iconEl) {
            iconEl.innerHTML = isFullscreen ? ICONS.minimize : ICONS.expand;
        }
        const messages = document.getElementById(`${this.container.id}-messages`);
        if (messages) {
            setTimeout(() => {
                messages.scrollTop = messages.scrollHeight;
            }, 100);
        }
    }
    loadInitialGreeting() {
        const greeting = "How can I assist with your startup positioning, unit economics, competitor intelligence, or market strategy today?";
        this.appendMessage("assistant", greeting);
    }
    async loadSuggestions() {
        const suggestionsContainer = document.getElementById(`${this.container.id}-suggestions`);
        if (!suggestionsContainer) return;
        let suggestions = [
            "Evaluate my SaaS idea",
            "Calculate CAC vs LTV",
            "Zero-budget GTM hacks",
            "Angel investor checklist",
            "Defensible market moat"
        ];
        try {
            const res = await fetch(`${API_CHAT_ENDPOINT}/suggestions`);
            if (res.ok) {
                const data = await res.json();
                if (data.suggestions && data.suggestions.length) {
                    suggestions = data.suggestions;
                }
            }
        } catch (e) {
        }
        suggestionsContainer.innerHTML = "";
        suggestions.forEach(text => {
            const chip = document.createElement("button");
            chip.type = "button";
            chip.className = "suggestion-chip";
            chip.textContent = text;
            chip.addEventListener("click", () => {
                const input = document.getElementById(`${this.container.id}-input`);
                if (input) {
                    input.value = text;
                    input.focus();
                }
            });
            suggestionsContainer.appendChild(chip);
        });
    }
    getFormContext() {
        const idea = document.getElementById("startup_idea")?.value;
        const industry = document.getElementById("industry")?.value;
        const country = document.getElementById("country")?.value;
        const audience = document.getElementById("target_audience")?.value;
        const budget = document.getElementById("budget")?.value;
        const stage = document.getElementById("business_stage")?.value;
        if (idea || industry || country) {
            return {
                startup_idea: idea || "",
                industry: industry || "",
                country: country || "",
                target_audience: audience || "",
                budget: budget || "",
                business_stage: stage || ""
            };
        }
        return null;
    }
    async handleSendMessage() {
        if (this.isProcessing) return;
        const input = document.getElementById(`${this.container.id}-input`);
        const sendBtn = document.getElementById(`${this.container.id}-send-btn`);
        const messageText = input?.value?.trim();
        if (!messageText) return;
        this.appendMessage("user", messageText);
        input.value = "";
        this.history.push({ role: "user", content: messageText });
        this.isProcessing = true;
        if (sendBtn) sendBtn.disabled = true;
        const typingIndicator = this.showTypingIndicator();
        try {
            const context = this.getFormContext();
            const response = await fetch(API_CHAT_ENDPOINT, {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify({
                    message: messageText,
                    history: this.history.slice(-8),
                    context: context
                })
            });
            typingIndicator.remove();
            if (!response.ok) {
                const errData = await response.json().catch(() => ({}));
                throw new Error(errData.detail || `Server error (${response.status})`);
            }
            const data = await response.json();
            const reply = data.reply || "I apologize, but I could not generate a response. Please try again.";
            this.appendMessage("assistant", reply);
            this.history.push({ role: "assistant", content: reply });
        } catch (err) {
            typingIndicator.remove();
            this.appendMessage("assistant", `⚠️ **Error:** ${err.message || 'Unable to connect to AI consultant.'}`);
        } finally {
            this.isProcessing = false;
            if (sendBtn) sendBtn.disabled = false;
            input?.focus();
        }
    }
    showTypingIndicator() {
        const messagesContainer = document.getElementById(`${this.container.id}-messages`);
        const row = document.createElement("div");
        row.className = "chat-msg-row assistant";
        row.innerHTML = `
            <div class="chat-msg-avatar bot-av">✦</div>
            <div class="chat-bubble">
                <div class="typing-indicator">
                    <span class="typing-dot"></span>
                    <span class="typing-dot"></span>
                    <span class="typing-dot"></span>
                </div>
            </div>
        `;
        messagesContainer.appendChild(row);
        messagesContainer.scrollTop = messagesContainer.scrollHeight;
        return row;
    }
    appendMessage(role, text) {
        const messagesContainer = document.getElementById(`${this.container.id}-messages`);
        if (!messagesContainer) return;
        const row = document.createElement("div");
        row.className = `chat-msg-row ${role}`;
        const avatar = role === "user" ? `<div class="chat-msg-avatar user-av">👤</div>` : `<div class="chat-msg-avatar bot-av">✦</div>`;
        const formattedHtml = this.formatMarkdown(text);
        const timeStr = new Date().toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' });
        row.innerHTML = `
            ${avatar}
            <div>
                <div class="chat-bubble">${formattedHtml}</div>
                <div class="chat-msg-time">${timeStr}</div>
            </div>
        `;
        messagesContainer.appendChild(row);
        messagesContainer.scrollTop = messagesContainer.scrollHeight;
    }
    formatMarkdown(text) {
        if (!text) return "";
        if (typeof window !== "undefined" && window.marked && typeof window.marked.parse === "function") {
            try {
                return window.marked.parse(text);
            } catch (e) {
            }
        }
        let content = text.replace(/\r\n/g, "\n");
        const codeBlocks = [];
        content = content.replace(/(?:```|``)(\w*)\n([\s\S]*?)(?:```|``)/g, (match, lang, code) => {
            const index = codeBlocks.length;
            const escapedCode = code
                .replace(/&/g, "&amp;")
                .replace(/</g, "&lt;")
                .replace(/>/g, "&gt;");
            codeBlocks.push(`<pre><code class="language-${lang || 'plaintext'}">${escapedCode.trim()}</code></pre>`);
            return `__CODE_BLOCK_${index}__`;
        });
        content = content.replace(/((?:\|[^\n]+\|\n?)+)/g, (match) => {
            const lines = match.trim().split("\n").filter(l => l.includes("|"));
            if (lines.length < 2) return match;
            const parseRow = (line) => {
                return line
                    .replace(/^\||\|$/g, "")
                    .split("|")
                    .map(cell => cell.trim());
            };
            let tableHtml = "<div class='chat-table-wrapper'><table>";
            let hasHeader = false;
            let startRow = 0;
            if (lines.length >= 2 && /^[\s|:-]+$/.test(lines[1])) {
                hasHeader = true;
                const headers = parseRow(lines[0]);
                tableHtml += "<thead><tr>";
                headers.forEach(h => {
                    tableHtml += `<th>${h}</th>`;
                });
                tableHtml += "</tr></thead>";
                startRow = 2;
            }
            tableHtml += "<tbody>";
            for (let i = startRow; i < lines.length; i++) {
                if (/^[\s|:-]+$/.test(lines[i])) continue;
                const cells = parseRow(lines[i]);
                tableHtml += "<tr>";
                cells.forEach(c => {
                    tableHtml += `<td>${c}</td>`;
                });
                tableHtml += "</tr>";
            }
            tableHtml += "</tbody></table></div>";
            return tableHtml;
        });
        content = content
            .replace(/^#### (.*$)/gim, "<h5 style='margin: 0.5rem 0 0.2rem 0; color: var(--primary-dark); font-size: 0.9rem;'>$1</h5>")
            .replace(/^### (.*$)/gim, "<h4 style='margin: 0.6rem 0 0.25rem 0; color: var(--primary-dark); font-size: 0.98rem; font-weight: 700;'>$1</h4>")
            .replace(/^## (.*$)/gim, "<h3 style='margin: 0.75rem 0 0.35rem 0; color: var(--primary-dark); font-size: 1.08rem; font-weight: 800;'>$1</h3>")
            .replace(/^# (.*$)/gim, "<h2 style='margin: 0.85rem 0 0.4rem 0; color: var(--primary-dark); font-size: 1.18rem; font-weight: 800;'>$1</h2>");
        content = content.replace(/^---$/gim, "<hr style='border:none; border-top:1px solid var(--border-default); margin:0.8rem 0;'>");
        content = content
            .replace(/\*\*\*(.*?)\*\*\*/g, "<strong><em>$1</em></strong>")
            .replace(/\*\*(.*?)\*\*/g, "<strong>$1</strong>")
            .replace(/\*(.*?)\*/g, "<em>$1</em>")
            .replace(/`([^`]+)`/g, "<code>$1</code>");
        // Lists
        content = content
            .replace(/^\s*[-*•]\s+(.*$)/gim, "<li style='margin-bottom: 3px;'>$1</li>")
            .replace(/^\s*(\d+)\.\s+(.*$)/gim, "<li style='margin-bottom: 3px;'>$2</li>");
        // Line breaks & paragraphs
        content = content
            .replace(/\n\n+/g, "</p><p style='margin: 0 0 0.5rem 0;'>")
            .replace(/\n/g, "<br>");
        // Restore code blocks
        codeBlocks.forEach((block, i) => {
            content = content.replace(`__CODE_BLOCK_${i}__`, block);
        });
        return `<div class='chat-rendered-body'>${content}</div>`;
    }
    clearChat() {
        this.history = [];
        const messagesContainer = document.getElementById(`${this.container.id}-messages`);
        if (messagesContainer) {
            messagesContainer.innerHTML = "";
            this.loadInitialGreeting();
        }
    }
}
document.addEventListener("DOMContentLoaded", () => {
    if (document.getElementById("chatbot-widget")) {
        window.activeChatbot = new StrategyChatbot("chatbot-widget", { fullPage: false });
    }
    if (document.getElementById("chatbot-container")) {
        window.activeChatbotPage = new StrategyChatbot("chatbot-container", { fullPage: true });
    }
});
export { StrategyChatbot };
