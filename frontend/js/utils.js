// Shared UI Utility & Country Currency Localization Functions

export const COUNTRY_CURRENCY_MAP = {
    "india": { symbol: "₹", code: "INR", name: "Indian Rupee", locale: "en-IN", rate: 85, exampleBudgets: ["₹1,00,000 - ₹5,00,000", "₹5,00,000 - ₹25,00,000", "₹25,00,000 - ₹1,00,00,000", "₹1,00,00,000 - ₹5,00,00,000+"] },
    "bharat": { symbol: "₹", code: "INR", name: "Indian Rupee", locale: "en-IN", rate: 85, exampleBudgets: ["₹1,00,000 - ₹5,00,000", "₹5,00,000 - ₹25,00,000", "₹25,00,000 - ₹1,00,00,000", "₹1,00,00,000 - ₹5,00,00,000+"] },
    "united states": { symbol: "$", code: "USD", name: "US Dollar", locale: "en-US", rate: 1, exampleBudgets: ["$10,000 - $25,000", "$25,000 - $100,000", "$100,000 - $500,000", "$500,000 - $2M+"] },
    "usa": { symbol: "$", code: "USD", name: "US Dollar", locale: "en-US", rate: 1, exampleBudgets: ["$10,000 - $25,000", "$25,000 - $100,000", "$100,000 - $500,000", "$500,000 - $2M+"] },
    "us": { symbol: "$", code: "USD", name: "US Dollar", locale: "en-US", rate: 1, exampleBudgets: ["$10,000 - $25,000", "$25,000 - $100,000", "$100,000 - $500,000", "$500,000 - $2M+"] },
    "global": { symbol: "$", code: "USD", name: "US Dollar", locale: "en-US", rate: 1, exampleBudgets: ["$10,000 - $25,000", "$25,000 - $100,000", "$100,000 - $500,000", "$500,000 - $2M+"] },
    "united kingdom": { symbol: "£", code: "GBP", name: "British Pound", locale: "en-GB", rate: 0.78, exampleBudgets: ["£10,000 - £25,000", "£25,000 - £100,000", "£100,000 - £500,000", "£500,000 - £2M+"] },
    "uk": { symbol: "£", code: "GBP", name: "British Pound", locale: "en-GB", rate: 0.78, exampleBudgets: ["£10,000 - £25,000", "£25,000 - £100,000", "£100,000 - £500,000", "£500,000 - £2M+"] },
    "great britain": { symbol: "£", code: "GBP", name: "British Pound", locale: "en-GB", rate: 0.78, exampleBudgets: ["£10,000 - £25,000", "£25,000 - £100,000", "£100,000 - £500,000", "£500,000 - £2M+"] },
    "england": { symbol: "£", code: "GBP", name: "British Pound", locale: "en-GB", rate: 0.78, exampleBudgets: ["£10,000 - £25,000", "£25,000 - £100,000", "£100,000 - £500,000", "£500,000 - £2M+"] },
    "germany": { symbol: "€", code: "EUR", name: "Euro", locale: "de-DE", rate: 0.92, exampleBudgets: ["€10.000 - €25.000", "€25.000 - €100.000", "€100.000 - €500.000", "€500.000 - €2M+"] },
    "france": { symbol: "€", code: "EUR", name: "Euro", locale: "fr-FR", rate: 0.92, exampleBudgets: ["€10 000 - €25 000", "€25 000 - €100 000", "€100 000 - €500 000", "€500 000 - €2M+"] },
    "italy": { symbol: "€", code: "EUR", name: "Euro", locale: "it-IT", rate: 0.92, exampleBudgets: ["€10.000 - €25.000", "€25.000 - €100.000", "€100.000 - €500.000", "€500.000 - €2M+"] },
    "spain": { symbol: "€", code: "EUR", name: "Euro", locale: "es-ES", rate: 0.92, exampleBudgets: ["€10.000 - €25.000", "€25.000 - €100.000", "€100.000 - €500.000", "€500.000 - €2M+"] },
    "netherlands": { symbol: "€", code: "EUR", name: "Euro", locale: "nl-NL", rate: 0.92, exampleBudgets: ["€10.000 - €25.000", "€25.000 - €100.000", "€100.000 - €500.000", "€500.000 - €2M+"] },
    "europe": { symbol: "€", code: "EUR", name: "Euro", locale: "de-DE", rate: 0.92, exampleBudgets: ["€10.000 - €25.000", "€25.000 - €100.000", "€100.000 - €500.000", "€500.000 - €2M+"] },
    "eu": { symbol: "€", code: "EUR", name: "Euro", locale: "de-DE", rate: 0.92, exampleBudgets: ["€10.000 - €25.000", "€25.000 - €100.000", "€100.000 - €500.000", "€500.000 - €2M+"] },
    "canada": { symbol: "CA$", code: "CAD", name: "Canadian Dollar", locale: "en-CA", rate: 1.35, exampleBudgets: ["CA$10,000 - CA$25,000", "CA$25,000 - CA$100,000", "CA$100,000 - CA$500,000", "CA$500,000 - CA$2M+"] },
    "australia": { symbol: "AU$", code: "AUD", name: "Australian Dollar", locale: "en-AU", rate: 1.52, exampleBudgets: ["AU$15,000 - AU$35,000", "AU$35,000 - AU$150,000", "AU$150,000 - AU$750,000", "AU$750,000 - AU$3M+"] },
    "japan": { symbol: "¥", code: "JPY", name: "Japanese Yen", locale: "ja-JP", rate: 155, exampleBudgets: ["¥1,500,000 - ¥3,500,000", "¥3,500,000 - ¥15,000,000", "¥15,000,000 - ¥75,000,000", "¥75,000,000+"] },
    "china": { symbol: "¥", code: "CNY", name: "Chinese Yuan", locale: "zh-CN", rate: 7.2, exampleBudgets: ["¥70,000 - ¥180,000", "¥180,000 - ¥700,000", "¥700,000 - ¥3,500,000", "¥3,500,000+"] },
    "united arab emirates": { symbol: "AED ", code: "AED", name: "UAE Dirham", locale: "en-AE", rate: 3.67, exampleBudgets: ["AED 35,000 - AED 90,000", "AED 90,000 - AED 350,000", "AED 350,000 - AED 1.8M", "AED 1.8M+"] },
    "uae": { symbol: "AED ", code: "AED", name: "UAE Dirham", locale: "en-AE", rate: 3.67, exampleBudgets: ["AED 35,000 - AED 90,000", "AED 90,000 - AED 350,000", "AED 350,000 - AED 1.8M", "AED 1.8M+"] },
    "dubai": { symbol: "AED ", code: "AED", name: "UAE Dirham", locale: "en-AE", rate: 3.67, exampleBudgets: ["AED 35,000 - AED 90,000", "AED 90,000 - AED 350,000", "AED 350,000 - AED 1.8M", "AED 1.8M+"] },
    "singapore": { symbol: "S$", code: "SGD", name: "Singapore Dollar", locale: "en-SG", rate: 1.34, exampleBudgets: ["S$15,000 - S$35,000", "S$35,000 - S$135,000", "S$135,000 - S$700,000", "S$700,000+"] },
    "switzerland": { symbol: "CHF ", code: "CHF", name: "Swiss Franc", locale: "de-CH", rate: 0.88, exampleBudgets: ["CHF 10,000 - CHF 25,000", "CHF 25,000 - CHF 100,000", "CHF 100,000 - CHF 500,000", "CHF 500,000+"] },
    "saudi arabia": { symbol: "SAR ", code: "SAR", name: "Saudi Riyal", locale: "en-SA", rate: 3.75, exampleBudgets: ["SAR 35,000 - SAR 90,000", "SAR 90,000 - SAR 375,000", "SAR 375,000 - SAR 1.8M", "SAR 1.8M+"] },
    "brazil": { symbol: "R$", code: "BRL", name: "Brazilian Real", locale: "pt-BR", rate: 5.5, exampleBudgets: ["R$ 50.000 - R$ 130.000", "R$ 130.000 - R$ 550.000", "R$ 550.000 - R$ 2.7M", "R$ 2.7M+"] },
    "mexico": { symbol: "MX$", code: "MXN", name: "Mexican Peso", locale: "es-MX", rate: 19.5, exampleBudgets: ["MX$200,000 - MX$500,000", "MX$500,000 - MX$2M", "MX$2M - MX$10M", "MX$10M+"] },
    "south africa": { symbol: "R ", code: "ZAR", name: "South African Rand", locale: "en-ZA", rate: 18.2, exampleBudgets: ["R 180,000 - R 450,000", "R 450,000 - R 1.8M", "R 1.8M - R 9M", "R 9M+"] },
    "nigeria": { symbol: "₦", code: "NGN", name: "Nigerian Naira", locale: "en-NG", rate: 1500, exampleBudgets: ["₦15,000,000 - ₦35,000,000", "₦35,000,000 - ₦150,000,000", "₦150,000,000 - ₦750,000,000", "₦750,000,000+"] },
    "indonesia": { symbol: "Rp ", code: "IDR", name: "Indonesian Rupiah", locale: "id-ID", rate: 15800, exampleBudgets: ["Rp 150 Jt - Rp 400 Jt", "Rp 400 Jt - Rp 1.5 M", "Rp 1.5 M - Rp 8 M", "Rp 8 M+"] },
    "malaysia": { symbol: "RM ", code: "MYR", name: "Malaysian Ringgit", locale: "ms-MY", rate: 4.4, exampleBudgets: ["RM 45,000 - RM 110,000", "RM 110,000 - RM 440,000", "RM 440,000 - RM 2.2M", "RM 2.2M+"] },
    "philippines": { symbol: "₱", code: "PHP", name: "Philippine Peso", locale: "en-PH", rate: 58, exampleBudgets: ["₱500,000 - ₱1,500,000", "₱1,500,000 - ₱5,800,000", "₱5,800,000 - ₱29,000,000", "₱29,000,000+"] },
    "vietnam": { symbol: "₫", code: "VND", name: "Vietnamese Dong", locale: "vi-VN", rate: 25000, exampleBudgets: ["250 Triệu - 600 Triệu ₫", "600 Triệu - 2.5 Tỷ ₫", "2.5 Tỷ - 12.5 Tỷ ₫", "12.5 Tỷ ₫+"] },
    "south korea": { symbol: "₩", code: "KRW", name: "South Korean Won", locale: "ko-KR", rate: 1350, exampleBudgets: ["₩13,500,000 - ₩35,000,000", "₩35,000,000 - ₩135,000,000", "₩135,000,000 - ₩675,000,000", "₩675,000,000+"] },
    "korea": { symbol: "₩", code: "KRW", name: "South Korean Won", locale: "ko-KR", rate: 1350, exampleBudgets: ["₩13,500,000 - ₩35,000,000", "₩35,000,000 - ₩135,000,000", "₩135,000,000 - ₩675,000,000", "₩675,000,000+"] },
    "sweden": { symbol: "kr ", code: "SEK", name: "Swedish Krona", locale: "sv-SE", rate: 10.5, exampleBudgets: ["100 000 kr - 250 000 kr", "250 000 kr - 1 000 000 kr", "1 000 000 kr - 5 000 000 kr", "5 000 000 kr+"] },
    "norway": { symbol: "kr ", code: "NOK", name: "Norwegian Krone", locale: "no-NO", rate: 10.8, exampleBudgets: ["100 000 kr - 250 000 kr", "250 000 kr - 1 000 000 kr", "1 000 000 kr - 5 000 000 kr", "5 000 000 kr+"] },
    "denmark": { symbol: "kr ", code: "DKK", name: "Danish Krone", locale: "da-DK", rate: 6.85, exampleBudgets: ["70.000 kr - 170.000 kr", "170.000 kr - 700.000 kr", "700.000 kr - 3.5M kr", "3.5M kr+"] },
    "poland": { symbol: "zł ", code: "PLN", name: "Polish Zloty", locale: "pl-PL", rate: 3.95, exampleBudgets: ["40 000 zł - 100 000 zł", "100 000 zł - 400 000 zł", "400 000 zł - 2 000 000 zł", "2 000 000 zł+"] },
    "new zealand": { symbol: "NZ$", code: "NZD", name: "New Zealand Dollar", locale: "en-NZ", rate: 1.65, exampleBudgets: ["NZ$15,000 - NZ$40,000", "NZ$40,000 - NZ$165,000", "NZ$165,000 - NZ$800,000", "NZ$800,000+"] },
    "pakistan": { symbol: "₨ ", code: "PKR", name: "Pakistani Rupee", locale: "ur-PK", rate: 278, exampleBudgets: ["₨ 2,800,000 - ₨ 7,000,000", "₨ 7,000,000 - ₨ 28,000,000", "₨ 28,000,000 - ₨ 140,000,000", "₨ 140,000,000+"] },
    "bangladesh": { symbol: "৳", code: "BDT", name: "Bangladeshi Taka", locale: "bn-BD", rate: 120, exampleBudgets: ["৳1,200,000 - ৳3,000,000", "৳3,000,000 - ৳12,000,000", "৳12,000,000 - ৳60,000,000", "৳60,000,000+"] },
    "egypt": { symbol: "E£ ", code: "EGP", name: "Egyptian Pound", locale: "ar-EG", rate: 48, exampleBudgets: ["E£ 480,000 - E£ 1,200,000", "E£ 1,200,000 - E£ 4,800,000", "E£ 4,800,000 - E£ 24,000,000", "E£ 24,000,000+"] },
    "turkey": { symbol: "₺", code: "TRY", name: "Turkish Lira", locale: "tr-TR", rate: 34, exampleBudgets: ["350.000 ₺ - 850.000 ₺", "850.000 ₺ - 3.400.000 ₺", "3.400.000 ₺ - 17.000.000 ₺", "17.000.000 ₺+"] }
};

export function getCountryCurrency(countryName) {
    if (!countryName || typeof countryName !== "string") {
        return COUNTRY_CURRENCY_MAP["global"];
    }

    const clean = countryName.trim().toLowerCase();

    // Direct match
    if (COUNTRY_CURRENCY_MAP[clean]) {
        return COUNTRY_CURRENCY_MAP[clean];
    }

    // Substring match
    for (const [k, v] of Object.entries(COUNTRY_CURRENCY_MAP)) {
        if (clean.includes(k) || k.includes(clean)) {
            return v;
        }
    }

    // Default USD if unrecognized
    return { symbol: "$", code: "USD", name: "US Dollar", locale: "en-US", rate: 1, exampleBudgets: ["$10,000 - $25,000", "$25,000 - $100,000", "$100,000 - $500,000", "$500,000 - $2M+"] };
}

export function formatCurrency(amount, countryName) {
    const num = Number(amount);
    if (isNaN(num)) return amount || "0";

    const curr = getCountryCurrency(countryName);
    try {
        const formatted = Math.round(num).toLocaleString(curr.locale);
        return `${curr.symbol}${formatted}`;
    } catch {
        return `${curr.symbol}${Math.round(num).toLocaleString()}`;
    }
}

export function formatCompactCurrency(amount, countryName) {
    const num = Number(amount);
    if (isNaN(num)) return amount || "0";

    const curr = getCountryCurrency(countryName);

    // Special Indian numbering format (Crore / Lakh) if India
    if (curr.code === "INR") {
        if (num >= 10000000) {
            return `${curr.symbol}${(num / 10000000).toFixed(1)} Cr`;
        } else if (num >= 100000) {
            return `${curr.symbol}${(num / 100000).toFixed(1)} L`;
        } else if (num >= 1000) {
            return `${curr.symbol}${(num / 1000).toFixed(1)} K`;
        }
        return `${curr.symbol}${num.toLocaleString(curr.locale)}`;
    }

    if (num >= 1000000000) {
        return `${curr.symbol}${(num / 1000000000).toFixed(1)}B`;
    } else if (num >= 1000000) {
        return `${curr.symbol}${(num / 1000000).toFixed(1)}M`;
    } else if (num >= 1000) {
        return `${curr.symbol}${(num / 1000).toFixed(1)}K`;
    }
    return `${curr.symbol}${num.toLocaleString(curr.locale)}`;
}

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
