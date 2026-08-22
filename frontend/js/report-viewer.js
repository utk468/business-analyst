import { fetchReport } from './api.js';
import {
    escapeHtml,
    formatNumber,
    formatTextHtml,
    renderBulletList,
    renderRoadmapMilestones
} from './utils.js';




document.addEventListener("DOMContentLoaded", () => {
    // 1. Extract report ID from URL
    const urlParams = new URLSearchParams(window.location.search);
    const reportId = urlParams.get("id");

    if (!reportId) {
        displayError("No Report ID provided. Please visit the Vault to open a strategy.");
        return;
    }

    // 2. Fetch and render report details
    fetchReportDetails(reportId);
});




// displayError function displays an error message to the user
// and provides a link to return to the vault.
function displayError(msg) {
    document.getElementById("report-loading").style.display = "none";
    const container = document.querySelector(".container");
    container.innerHTML = `
        <div class="glass-card" style="border-color: var(--error); text-align: center; padding: 4rem 1.5rem; margin-top: 4rem;">
            <h3 style="color: var(--error); margin-bottom: 1rem;">Report Access Error</h3>
            <p style="color: var(--text-secondary); margin-bottom: 2rem;">${msg}</p>
            <a href="history.html" class="nav-btn primary">Return to Vault</a>
        </div>
    `;
}



function fetchReportDetails(id) {
    fetchReport(id)
        .then(report => {
            document.getElementById("report-loading").style.display = "none";
            document.getElementById("report-main-layout").style.display = "grid";

            document.title = `Business Strategy | Blueprint - ${report.metadata?.startup_idea?.substring(0, 25) || "Strategy"}`;

            renderReport(report);
            setupScrollSpy();
        })
        .catch(err => {
            console.error("Failed to retrieve strategy details:", err);
            displayError(err.message);
        });
}



function renderReport(r) {
    const meta = r.metadata || {};
    const market = r.market_research || {};
    const comp = r.competitor_analysis || {};
    const prod = r.product_strategy || {};
    const brand = r.branding || {};
    const mkt = r.marketing || {};
    const sales = r.sales_strategy || {};
    const ops = r.operations || {};
    const fin = r.financial_planning || {};
    const inv = r.investor_readiness || {};

    // 1. Executive Summary
    document.getElementById("content-summary").innerHTML = formatTextHtml(r.executive_summary);

    // 2. Business Overview
    document.getElementById("content-overview").textContent = r.business_overview;

    const overviewGrid = document.getElementById("overview-metadata");
    overviewGrid.innerHTML = `
        <div class="metric-card">
            <div style="font-size: 1.1rem; font-weight:700; margin-bottom:4px;">${escapeHtml(meta.industry)}</div>
            <div class="metric-label">Industry Vertical</div>
        </div>
        <div class="metric-card">
            <div style="font-size: 1.1rem; font-weight:700; margin-bottom:4px;">${escapeHtml(meta.country)}</div>
            <div class="metric-label">Target Region</div>
        </div>
        <div class="metric-card">
            <div style="font-size: 1.1rem; font-weight:700; margin-bottom:4px;">${escapeHtml(meta.business_stage)}</div>
            <div class="metric-label">Current Stage</div>
        </div>
        <div class="metric-card">
            <div style="font-size: 1.1rem; font-weight:700; margin-bottom:4px;">${escapeHtml(meta.budget)}</div>
            <div class="metric-label">Committed Capital</div>
        </div>
    `;

    // 3. Market Analysis
    document.getElementById("market-tam").textContent = market.market_size || "Calculated TAM";
    document.getElementById("market-cagr").textContent = market.estimated_growth || "N/A";
    document.getElementById("market-overview-txt").textContent = market.industry_overview || "";

    renderBulletList(document.getElementById("market-opportunities-list"), market.emerging_opportunities);
    renderBulletList(document.getElementById("market-gaps-list"), market.market_gaps);

    // 4. Industry Trends
    renderBulletList(document.getElementById("trends-tech-list"), market.technology_trends);
    renderBulletList(document.getElementById("trends-consumer-list"), market.consumer_behavior);
    document.getElementById("trends-outlook").textContent = market.future_outlook || "";

    // 5. Customer Personas
    const personasContainer = document.getElementById("personas-container");
    personasContainer.innerHTML = "";
    const personas = r.customer_research || [];
    personas.forEach(p => {
        const div = document.createElement("div");
        div.className = "persona-profile";

        const goalsHtml = p.goals ? p.goals.map(g => `<li>${escapeHtml(g)}</li>`).join("") : "";
        const painsHtml = p.pain_points ? p.pain_points.map(g => `<li>${escapeHtml(g)}</li>`).join("") : "";

        div.innerHTML = `
            <div class="persona-avatar-box">
                <div class="persona-avatar">👤</div>
                <div class="persona-name">${escapeHtml(p.name)}</div>
                <div class="persona-stat">Age: <span>${p.age || "N/A"}</span></div>
                <div class="persona-stat">Income: <span>${escapeHtml(p.income || "N/A")}</span></div>
                <div class="persona-stat">Profession: <span>${escapeHtml(p.profession || "N/A")}</span></div>
                <div class="persona-stat">Location: <span>${escapeHtml(p.location || "N/A")}</span></div>
            </div>
            <div class="persona-details">
                <h4>Goals & Needs</h4>
                <ul style="padding-left:20px; font-size:0.9rem; color:var(--text-secondary);">${goalsHtml}</ul>
                
                <h4>Pain Points & Friction</h4>
                <ul style="padding-left:20px; font-size:0.9rem; color:var(--text-secondary);">${painsHtml}</ul>
                
                <h4>Buying Behaviour & Habits</h4>
                <p style="font-size:0.9rem; color:var(--text-secondary); margin-bottom:8px;">${escapeHtml(p.buying_behavior)}</p>
                <div style="display:flex; flex-wrap:wrap; gap:6px;">
                    ${p.digital_habits ? p.digital_habits.map(h => `<span style="font-size:0.75rem; background:rgba(255,255,255,0.05); padding:2px 8px; border-radius:10px;">${escapeHtml(h)}</span>`).join("") : ""}
                </div>
            </div>
        `;
        personasContainer.appendChild(div);
    });

    // 6. Competitor Landscape
    document.getElementById("competitor-intro").textContent = comp.gap_analysis || "Comparison matrix mapping competitors.";
    document.getElementById("competitor-gap-txt").textContent = comp.gap_analysis || "";
    renderBulletList(document.getElementById("competitor-diff-list"), comp.differentiation_opportunities);

    const competitorList = document.getElementById("competitor-list-container");
    competitorList.innerHTML = "";
    const competitors = comp.competitors || [];
    competitors.forEach(c => {
        const div = document.createElement("div");
        div.className = "glass-card";
        div.innerHTML = `
            <div style="display:flex; justify-content:space-between; align-items:center; border-bottom:1px solid var(--border-glass); padding-bottom:8px; margin-bottom:12px;">
                <h3 style="font-size:1.15rem; color:var(--secondary);">${escapeHtml(c.name)}</h3>
                <span class="status-badge" style="background:rgba(255,255,255,0.05);">${escapeHtml(c.type)} Competitor</span>
            </div>
            <p style="font-size:0.9rem; font-style:italic; margin-bottom:10px; color:var(--text-primary);">${escapeHtml(c.positioning)}</p>
            <div style="display:grid; grid-template-columns: 1fr 1fr; gap:1.5rem; font-size:0.85rem;">
                <div>
                    <strong style="color:var(--success);">Strengths:</strong>
                    <ul style="padding-left:16px; margin-top:4px;">${c.strengths ? c.strengths.map(s => `<li>${escapeHtml(s)}</li>`).join("") : ""}</ul>
                </div>
                <div>
                    <strong style="color:var(--error);">Weaknesses:</strong>
                    <ul style="padding-left:16px; margin-top:4px;">${c.weaknesses ? c.weaknesses.map(w => `<li>${escapeHtml(w)}</li>`).join("") : ""}</ul>
                </div>
            </div>
            <div style="margin-top:12px; font-size:0.85rem; border-top:1px dashed var(--border-glass); padding-top:8px;">
                <p><strong>Pricing Model:</strong> ${escapeHtml(c.pricing)}</p>
                <p><strong>Core Differentiators:</strong> ${c.differentiators ? c.differentiators.join(", ") : "N/A"}</p>
            </div>
        `;
        competitorList.appendChild(div);
    });

    // 7. Product Strategy
    renderBulletList(document.getElementById("prod-core-list"), prod.core_products);
    renderBulletList(document.getElementById("prod-premium-list"), prod.premium_products);
    document.getElementById("prod-usp").textContent = prod.usp || "";
    document.getElementById("prod-diff-txt").textContent = prod.product_differentiation || "";

    const road = prod.roadmap || {};
    renderRoadmapMilestones(document.getElementById("road-6mo"), road.six_month);
    renderRoadmapMilestones(document.getElementById("road-12mo"), road.twelve_month);
    renderRoadmapMilestones(document.getElementById("road-24mo"), road.twenty_four_month);

    // 8. Branding Strategy
    renderBulletList(document.getElementById("brand-names"), brand.brand_names);
    renderBulletList(document.getElementById("brand-taglines"), brand.taglines);
    document.getElementById("brand-story").innerHTML = formatTextHtml(brand.story);
    document.getElementById("brand-personality").textContent = brand.personality || "N/A";
    document.getElementById("brand-archetype").textContent = brand.archetype || "N/A";

    const guidelines = brand.design_guidelines || {};
    document.getElementById("brand-tone").textContent = guidelines.tone || "N/A";
    document.getElementById("brand-design-lang").textContent = guidelines.language || "";

    const colorsContainer = document.getElementById("brand-colors-container");
    colorsContainer.innerHTML = "";
    const colors = guidelines.colors || [];
    colors.forEach(col => {
        const hexMatch = col.match(/#[0-9A-Fa-f]{6}/);
        const hex = hexMatch ? hexMatch[0] : "#ffffff";

        const card = document.createElement("div");
        card.style.display = "flex";
        card.style.alignItems = "center";
        card.style.gap = "8px";
        card.style.padding = "6px 12px";
        card.style.border = "1px solid var(--border-glass)";
        card.style.borderRadius = "var(--radius-sm)";
        card.style.background = "rgba(255,255,255,0.02)";
        card.innerHTML = `
            <div style="width:24px; height:24px; border-radius:50%; background-color:${hex}; border:1px solid rgba(255,255,255,0.2);"></div>
            <span style="font-size:0.85rem; color:var(--text-secondary);">${escapeHtml(col)}</span>
        `;
        colorsContainer.appendChild(card);
    });

    // 9. Marketing Channels
    const marketingContainer = document.getElementById("marketing-channels-container");
    marketingContainer.innerHTML = "";

    const mktKeys = ["organic", "content", "seo", "email", "influencer", "community", "referral", "pr"];
    mktKeys.forEach(k => {
        if (mkt[k]) {
            const val = mkt[k];
            const div = document.createElement("div");
            div.className = "glass-card";
            div.innerHTML = `
                <h3 style="font-size:1.1rem; color:var(--primary); margin-bottom:8px; text-transform:capitalize;">${k === "pr" ? "Public Relations (PR)" : k + " Marketing"}</h3>
                <p style="font-size:0.9rem; margin-bottom:10px;"><strong>Objective:</strong> ${escapeHtml(val.objectives)}</p>
                <div style="font-size:0.85rem; color:var(--text-secondary); margin-bottom:8px;">
                    <strong>Execution Plan:</strong>
                    <ul style="padding-left:16px; margin-top:4px;">${val.execution ? val.execution.map(e => `<li>${escapeHtml(e)}</li>`).join("") : ""}</ul>
                </div>
                <p style="font-size:0.85rem; font-style:italic;"><strong>Expected Results:</strong> ${escapeHtml(val.results)}</p>
            `;
            marketingContainer.appendChild(div);
        }
    });

    if (mkt.social_media) {
        const sm = mkt.social_media;
        const div = document.createElement("div");
        div.className = "glass-card";
        div.innerHTML = `<h3 style="font-size:1.1rem; color:var(--secondary); margin-bottom:12px;">Social Media Campaigns</h3>`;

        const socialGrid = document.createElement("div");
        socialGrid.style.display = "grid";
        socialGrid.style.gridTemplateColumns = "repeat(auto-fit, minmax(200px, 1fr))";
        socialGrid.style.gap = "1.25rem";

        ["instagram", "linkedin", "youtube"].forEach(plat => {
            if (sm[plat]) {
                const val = sm[plat];
                const box = document.createElement("div");
                box.style.border = "1px solid var(--border-glass)";
                box.style.padding = "1rem";
                box.style.borderRadius = "var(--radius-sm)";
                box.style.background = "rgba(0,0,0,0.15)";
                box.innerHTML = `
                    <h4 style="color:var(--text-primary); text-transform:capitalize; margin-bottom:6px;">${plat}</h4>
                    <p style="font-size:0.8rem; margin-bottom:6px;"><strong>KPI:</strong> ${escapeHtml(val.objectives)}</p>
                    <ul style="font-size:0.8rem; color:var(--text-secondary); padding-left:14px; margin-bottom:6px;">
                        ${val.execution ? val.execution.map(e => `<li>${escapeHtml(e)}</li>`).join("") : ""}
                    </ul>
                    <p style="font-size:0.8rem; font-style:italic; color:var(--text-muted);">${escapeHtml(val.results)}</p>
                `;
                socialGrid.appendChild(box);
            }
        });

        div.appendChild(socialGrid);
        marketingContainer.appendChild(div);
    }

    // 10. Sales Strategy
    document.getElementById("sales-leadgen").textContent = sales.lead_generation || "";
    document.getElementById("sales-conversion").textContent = sales.conversion_strategy || "";
    document.getElementById("sales-retention").textContent = `Retention: ${sales.customer_acquisition_plan || ""}`;
    document.getElementById("sales-success").textContent = `Customer Success: ${sales.customer_success || ""}`;
    renderBulletList(document.getElementById("sales-kpis"), sales.kpis);

    const funnelContainer = document.getElementById("sales-funnel-container");
    funnelContainer.innerHTML = "";
    const funnel = sales.funnel || {};
    const funnelSteps = [
        { key: "awareness", label: "Awareness", color: "#6366f1", width: "100%" },
        { key: "interest", label: "Interest / Evaluation", color: "#4f46e5", width: "80%" },
        { key: "decision", label: "Decision / Intent", color: "#06b6d4", width: "60%" },
        { key: "action", label: "Action / Onboarding", color: "#0891b2", width: "40%" }
    ];

    funnelSteps.forEach(s => {
        const stepVal = funnel[s.key] || "Operational setup steps";
        const row = document.createElement("div");
        row.style.display = "flex";
        row.style.flexDirection = "column";
        row.style.alignItems = "center";
        row.style.marginBottom = "8px";
        row.innerHTML = `
            <div style="width:${s.width}; background:${s.color}; color:white; padding:0.5rem 1rem; border-radius:4px; text-align:center; font-weight:700; font-size:0.85rem; box-shadow:0 2px 8px rgba(0,0,0,0.3);">
                ${s.label}
            </div>
            <div style="font-size:0.8rem; color:var(--text-secondary); text-align:center; padding:4px 10px; max-width:500px;">
                ${escapeHtml(stepVal)}
            </div>
        `;
        funnelContainer.appendChild(row);
    });

    // 11. Operational Strategy
    document.getElementById("ops-structure").textContent = ops.operational_structure || "";
    document.getElementById("ops-vendors").textContent = ops.supply_chain_strategy || "";
    renderBulletList(document.getElementById("ops-hiring"), ops.hiring_plan);
    renderBulletList(document.getElementById("ops-automations"), ops.automation_opportunities);

    const techContainer = document.getElementById("ops-techstack");
    techContainer.innerHTML = "";
    const techStack = ops.technology_stack || [];
    techStack.forEach(t => {
        const badge = document.createElement("span");
        badge.style.fontSize = "0.8rem";
        badge.style.background = "var(--primary-glow)";
        badge.style.color = "#a5b4fc";
        badge.style.border = "1px solid rgba(99,102,241,0.3)";
        badge.style.padding = "3px 10px";
        badge.style.borderRadius = "4px";
        badge.textContent = t;
        techContainer.appendChild(badge);
    });

    // 12. Financial Planning
    const costTable = document.getElementById("table-startup-costs").querySelector("tbody");
    costTable.innerHTML = "";
    const startCosts = fin.startup_costs || {};

    let totalStartup = 0;
    Object.values(startCosts).forEach(v => totalStartup += Number(v));

    Object.entries(startCosts).forEach(([k, val]) => {
        const row = document.createElement("tr");
        const pct = totalStartup > 0 ? ((val / totalStartup) * 100).toFixed(1) : 0;
        row.innerHTML = `
            <td style="text-transform:capitalize;">${escapeHtml(k.replace("_", " "))}</td>
            <td><strong>$${formatNumber(val)}</strong></td>
            <td style="color:var(--text-muted); font-size:0.85rem;">${pct}%</td>
        `;
        costTable.appendChild(row);
    });

    const totalRow = document.createElement("tr");
    totalRow.style.borderTop = "2px solid var(--border-glass)";
    totalRow.style.background = "rgba(255,255,255,0.03)";
    totalRow.innerHTML = `
        <td><strong>Total Initial Capital required</strong></td>
        <td colspan="2"><strong style="color:var(--secondary); font-size:1.1rem;">$${formatNumber(totalStartup)}</strong></td>
    `;
    costTable.appendChild(totalRow);

    const rec = fin.recurring_expenses || {};
    document.getElementById("cost-monthly").textContent = `$${formatNumber(rec.monthly)} / mo`;
    document.getElementById("cost-quarterly").textContent = `$${formatNumber(rec.quarterly)} / qtr`;
    document.getElementById("cost-yearly").textContent = `$${formatNumber(rec.yearly)} / yr`;

    const be = fin.break_even || {};
    document.getElementById("break-even-explanation").textContent = be.explanation || "";
    document.getElementById("break-even-val").textContent = typeof be.units_or_revenue === "number" ? `$${formatNumber(be.units_or_revenue)}` : be.units_or_revenue;

    // 13. Projections & Charts
    const forecastTable = document.getElementById("table-forecasts").querySelector("tbody");
    forecastTable.innerHTML = "";

    const rev = fin.revenue_forecast || {};
    const prof = fin.profit_forecast || {};
    const cf = fin.cash_flow || {};

    const years = ["year_1", "year_2", "year_3"];
    years.forEach((yr, idx) => {
        const row = document.createElement("tr");
        const revenue = rev[yr] || 0;
        const profit = prof[yr] || 0;
        const cash = cf[yr] || 0;
        const expenses = revenue - profit;

        row.innerHTML = `
            <td>Year ${idx + 1} Projections</td>
            <td style="color:var(--secondary);"><strong>$${formatNumber(revenue)}</strong></td>
            <td style="color:var(--text-secondary);">$${formatNumber(expenses)}</td>
            <td style="color:var(--success); font-weight:700;">$${formatNumber(profit)}</td>
            <td>$${formatNumber(cash)}</td>
        `;
        forecastTable.appendChild(row);
    });
    renderForecastChart(rev, prof);
    renderMarketGrowthChart(market.market_size, market.estimated_growth);
    renderMarketSegmentsChart(market.tam_sam_som);
    renderStartupCostsChart(fin.startup_costs);
    renderCompetitorPositioningChart(comp.competitors);
    renderMarketingBudgetChart(mkt);
    renderRisksMatrixChart(r.risk_assessment);
    renderInvestorReadinessChart(inv.readiness_score, inv.attractiveness_score);

    // 14. Risk Assessment
    const risksContainer = document.getElementById("risks-matrix-container");
    risksContainer.innerHTML = "";
    const risks = r.risk_assessment || [];
    risks.forEach(risk => {
        const div = document.createElement("div");
        div.className = "risk-item";

        const lvlClass = String(risk.level).toLowerCase();

        div.innerHTML = `
            <div class="risk-type">${escapeHtml(risk.type)} Risk</div>
            <div>
                <span class="risk-indicator ${lvlClass}">${lvlClass} Risk</span>
            </div>
            <div style="font-size:0.8rem; color:var(--text-secondary); text-align:center;">
                Impact: <strong>${escapeHtml(risk.impact_level || "High")}</strong>
            </div>
            <div style="font-size:0.85rem;">
                <p style="margin-bottom:4px; font-style:italic;">"${escapeHtml(risk.impact)}"</p>
                <p><strong style="color:var(--primary);">Mitigation:</strong> ${escapeHtml(risk.mitigation)}</p>
            </div>
        `;
        risksContainer.appendChild(div);
    });

    // 15. SWOT Analysis
    const swot = r.swot_analysis || {};
    renderBulletList(document.getElementById("swot-s"), swot.strengths);
    renderBulletList(document.getElementById("swot-w"), swot.weaknesses);
    renderBulletList(document.getElementById("swot-o"), swot.opportunities);
    renderBulletList(document.getElementById("swot-t"), swot.threats);
    renderBulletList(document.getElementById("swot-recommendations-list"), swot.strategic_recommendations);

    // 16. Growth Strategy
    const growth = r.growth_strategy || {};
    const groad = growth.roadmap || {};
    renderRoadmapMilestones(document.getElementById("growth-90d"), groad.ninety_days);
    renderRoadmapMilestones(document.getElementById("growth-6mo"), groad.six_months);
    renderRoadmapMilestones(document.getElementById("growth-1yr"), groad.one_year);
    renderRoadmapMilestones(document.getElementById("growth-3yr"), groad.three_years);

    document.getElementById("growth-scaling-strategy").textContent = growth.scaling_strategy || "";
    document.getElementById("growth-partnerships").textContent = `Partnership Opportunities: ${growth.partnership_opportunities ? growth.partnership_opportunities.join(", ") : "N/A"}`;
    document.getElementById("growth-acquisitions").textContent = `Acquisitions & Consolidation: ${growth.acquisition_opportunities ? growth.acquisition_opportunities.join(", ") : "N/A"}`;

    // 17. Investor Readiness
    document.getElementById("score-readiness").textContent = inv.readiness_score || "0";
    document.getElementById("score-attractiveness").textContent = inv.attractiveness_score || "0";
    document.getElementById("investor-stages").innerHTML = inv.funding_stages ? inv.funding_stages.join("<br>") : "Seed";
    document.getElementById("investor-types").innerHTML = inv.investor_types ? inv.investor_types.join("<br>") : "Venture Capital";

    const evals = inv.evaluations || {};
    const evalsContainer = document.getElementById("investor-evals");
    evalsContainer.innerHTML = "";
    Object.entries(evals).forEach(([k, val]) => {
        const box = document.createElement("div");
        box.style.marginBottom = "8px";
        box.innerHTML = `
            <strong style="text-transform:capitalize; color:var(--text-primary);">${k.replace("_", " ")}:</strong> 
            <span>${escapeHtml(val)}</span>
        `;
        evalsContainer.appendChild(box);
    });

    // 18. Recommendations
    renderBulletList(document.getElementById("recs-list"), r.final_recommendations);

    // 19. Action Plan
    const actionContainer = document.getElementById("action-plan-container");
    actionContainer.innerHTML = "";
    const actPlan = r.action_plan || [];
    const columns = [
        { title: "Day 1 - 30", subtitle: "MVP & Setup Phase", color: "var(--primary)" },
        { title: "Day 31 - 90", subtitle: "Beta & Validation Phase", color: "var(--secondary)" },
        { title: "Day 91+", subtitle: "Public Scale Phase", color: "var(--accent)" }
    ];
    columns.forEach((col, idx) => {
        const itemText = actPlan[idx] || "Operations setup procedures.";
        const box = document.createElement("div");
        box.className = "glass-card";
        box.style.borderTop = `4px solid ${col.color}`;
        box.innerHTML = `
            <div style="font-size:0.8rem; font-weight:700; color:var(--text-muted); text-transform:uppercase;">Timeline</div>
            <h3 style="font-size:1.15rem; margin-bottom:4px;">${col.title}</h3>
            <p style="font-size:0.75rem; color:var(--text-muted); margin-bottom:12px;">${col.subtitle}</p>
            <p style="font-size:0.85rem; color:var(--text-secondary); line-height:1.5;">${escapeHtml(itemText)}</p>
        `;
        actionContainer.appendChild(box);
    });

    // 20. Strategic Conclusion
    document.getElementById("content-conclusion").innerHTML = formatTextHtml(r.conclusion);
}

function renderForecastChart(revenue, profit) {
    const ctx = document.getElementById("financial-projection-chart").getContext("2d");

    const y1Rev = revenue.year_1 || 0;
    const y2Rev = revenue.year_2 || 0;
    const y3Rev = revenue.year_3 || 0;

    const y1Prof = profit.year_1 || 0;
    const y2Prof = profit.year_2 || 0;
    const y3Prof = profit.year_3 || 0;

    const expenses = [
        y1Rev - y1Prof,
        y2Rev - y2Prof,
        y3Rev - y3Prof
    ];

    new Chart(ctx, {
        type: 'line',
        data: {
            labels: ['Year 1', 'Year 2', 'Year 3'],
            datasets: [
                {
                    label: 'Gross Revenue',
                    data: [y1Rev, y2Rev, y3Rev],
                    borderColor: '#06b6d4',
                    backgroundColor: 'rgba(6, 182, 212, 0.1)',
                    fill: true,
                    tension: 0.2,
                    borderWidth: 3
                },
                {
                    label: 'Net Profits',
                    data: [y1Prof, y2Prof, y3Prof],
                    borderColor: '#10b981',
                    backgroundColor: 'rgba(16, 185, 129, 0.05)',
                    fill: true,
                    tension: 0.2,
                    borderWidth: 3
                },
                {
                    label: 'Calculated Expenses',
                    data: expenses,
                    borderColor: '#6366f1',
                    borderDash: [5, 5],
                    fill: false,
                    tension: 0.2,
                    borderWidth: 2
                }
            ]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            plugins: {
                legend: {
                    labels: { color: '#f8fafc', font: { family: 'Plus Jakarta Sans' } }
                }
            },
            scales: {
                x: {
                    grid: { color: 'rgba(255,255,255,0.05)' },
                    ticks: { color: '#94a3b8' }
                },
                y: {
                    grid: { color: 'rgba(255,255,255,0.05)' },
                    ticks: {
                        color: '#94a3b8',
                        callback: function (value) {
                            return '$' + value.toLocaleString();
                        }
                    }
                }
            }
        }
    });
}

function renderMarketGrowthChart(marketSizeStr, cagrStr) {
    const ctx = document.getElementById("market-growth-chart").getContext("2d");

    // Parse TAM String values
    function parseAmount(str) {
        if (!str) return 100000000;
        const clean = str.replace(/[^0-9.]/g, '');
        let num = parseFloat(clean);
        if (isNaN(num)) num = 100;
        const lower = str.toLowerCase();
        if (lower.includes("billion") || lower.includes("b")) {
            return num * 1000000000;
        } else if (lower.includes("million") || lower.includes("m")) {
            return num * 1000000;
        }
        return num;
    }

    function parsePct(str) {
        if (!str) return 0.10;
        const clean = str.replace(/[^0-9.]/g, '');
        let num = parseFloat(clean);
        if (isNaN(num)) return 0.10;
        return num / 100;
    }

    const baseAmount = parseAmount(marketSizeStr);
    const growthRate = parsePct(cagrStr);

    const years = ['Year 1', 'Year 2', 'Year 3', 'Year 4', 'Year 5'];
    const projectionData = [baseAmount];
    for (let i = 1; i < 5; i++) {
        projectionData.push(Math.round(projectionData[i - 1] * (1 + growthRate)));
    }

    new Chart(ctx, {
        type: 'bar',
        data: {
            labels: years,
            datasets: [{
                label: 'Projected Addressable Market (TAM)',
                data: projectionData,
                backgroundColor: 'rgba(6, 182, 212, 0.4)',
                borderColor: '#06b6d4',
                borderWidth: 2,
                borderRadius: 4
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            plugins: {
                legend: { labels: { color: '#f8fafc', font: { family: 'Plus Jakarta Sans' } } }
            },
            scales: {
                x: { grid: { color: 'rgba(255,255,255,0.05)' }, ticks: { color: '#94a3b8' } },
                y: {
                    grid: { color: 'rgba(255,255,255,0.05)' },
                    ticks: {
                        color: '#94a3b8',
                        callback: function (value) {
                            if (value >= 1000000000) return '$' + (value / 1000000000).toFixed(1) + 'B';
                            if (value >= 1000000) return '$' + (value / 1000000).toFixed(1) + 'M';
                            return '$' + value.toLocaleString();
                        }
                    }
                }
            }
        }
    });
}

function renderStartupCostsChart(costsObj) {
    const ctx = document.getElementById("startup-costs-chart").getContext("2d");
    if (!costsObj) costsObj = {};

    const labels = Object.keys(costsObj).map(k => k.replace("_", " ").toUpperCase());
    const data = Object.values(costsObj);

    new Chart(ctx, {
        type: 'doughnut',
        data: {
            labels: labels,
            datasets: [{
                data: data,
                backgroundColor: [
                    '#6366f1', // Indigo
                    '#06b6d4', // Teal
                    '#d946ef', // Fuchsia
                    '#f59e0b', // Warning/Amber
                    '#10b981', // Success/Green
                    '#fb7185', // Rose
                    '#64748b'  // Muted Gray
                ],
                borderWidth: 1,
                borderColor: 'rgba(255,255,255,0.1)'
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            plugins: {
                legend: {
                    position: 'right',
                    labels: { color: '#f8fafc', font: { family: 'Plus Jakarta Sans', size: 10 } }
                }
            }
        }
    });
}

function renderInvestorReadinessChart(readinessScore, attractivenessScore) {
    const ctx = document.getElementById("investor-readiness-chart").getContext("2d");

    const readVal = readinessScore || 75;
    const attrVal = attractivenessScore || 80;

    // Generate programmatic scores for radar axes based on calculated scores
    const labels = ['MarketTAM Capacity', 'Moat Moat Moat', 'Scalability', 'Revenue Track', 'Team Capability', 'Funding Appeal'];
    const scoreData = [
        Math.min(100, Math.round(attrVal * 1.08)), // Market TAM Capacity
        Math.min(100, Math.round(readVal * 0.95)), // Moat strength
        Math.min(100, Math.round(readVal * 1.05)), // Scalability
        Math.min(100, Math.round(attrVal * 0.98)), // Revenue predictability
        Math.min(100, Math.round(readVal * 0.92)), // Team structure
        Math.min(100, attrVal)                     // Overall Funding Appeal
    ];

    new Chart(ctx, {
        type: 'radar',
        data: {
            labels: labels,
            datasets: [{
                label: 'Startup Audit Vectors',
                data: scoreData,
                backgroundColor: 'rgba(217, 70, 239, 0.1)',
                borderColor: '#d946ef',
                borderWidth: 2,
                pointBackgroundColor: '#d946ef'
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            plugins: {
                legend: { labels: { color: '#f8fafc', font: { family: 'Plus Jakarta Sans' } } }
            },
            scales: {
                r: {
                    angleLines: { color: 'rgba(255,255,255,0.08)' },
                    gridLines: { color: 'rgba(255,255,255,0.08)' },
                    pointLabels: { color: '#94a3b8', font: { family: 'Plus Jakarta Sans', size: 10 } },
                    ticks: { backdropColor: 'transparent', color: '#64748b', showLabelBackdrop: false },
                    suggestedMin: 0,
                    suggestedMax: 100
                }
            }
        }
    });
}

function renderMarketSegmentsChart(tamSamSomObj) {
    const ctx = document.getElementById("market-segments-chart").getContext("2d");
    if (!tamSamSomObj) tamSamSomObj = { tam: 1000000000, sam: 100000000, som: 10000000 };

    new Chart(ctx, {
        type: 'bar',
        data: {
            labels: ['TAM', 'SAM', 'SOM'],
            datasets: [{
                label: 'Market Size ($)',
                data: [tamSamSomObj.tam || 0, tamSamSomObj.sam || 0, tamSamSomObj.som || 0],
                backgroundColor: [
                    'rgba(99, 102, 241, 0.5)',  // Indigo
                    'rgba(6, 182, 212, 0.5)',   // Teal
                    'rgba(16, 185, 129, 0.5)'   // Emerald
                ],
                borderColor: [
                    '#6366f1',
                    '#06b6d4',
                    '#10b981'
                ],
                borderWidth: 2,
                borderRadius: 4
            }]
        },
        options: {
            indexAxis: 'y',
            responsive: true,
            maintainAspectRatio: false,
            plugins: {
                legend: { display: false }
            },
            scales: {
                x: {
                    grid: { color: 'rgba(255,255,255,0.05)' },
                    ticks: {
                        color: '#94a3b8',
                        callback: function (value) {
                            if (value >= 1000000000) return '$' + (value / 1000000000).toFixed(1) + 'B';
                            if (value >= 1000000) return '$' + (value / 1000000).toFixed(1) + 'M';
                            return '$' + value.toLocaleString();
                        }
                    }
                },
                y: {
                    grid: { display: false },
                    ticks: { color: '#94a3b8' }
                }
            }
        }
    });
}

function renderCompetitorPositioningChart(competitorsList) {
    const ctx = document.getElementById("competitor-positioning-chart").getContext("2d");
    if (!competitorsList || competitorsList.length === 0) return;

    const datasets = competitorsList.map((c, i) => {
        const colors = ['#6366f1', '#06b6d4', '#d946ef', '#10b981', '#f59e0b', '#fb7185'];
        const color = colors[i % colors.length];
        return {
            label: c.name,
            data: [{
                x: c.pricing_level || 5,
                y: c.quality_score || 5,
                r: Math.max(6, Math.min(25, (c.market_share_percent || 10) * 0.4))
            }],
            backgroundColor: color + '80',
            borderColor: color,
            borderWidth: 2,
            hoverRadius: 10
        };
    });

    new Chart(ctx, {
        type: 'bubble',
        data: { datasets: datasets },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            plugins: {
                legend: {
                    position: 'right',
                    labels: { color: '#f8fafc', font: { family: 'Plus Jakarta Sans', size: 9 } }
                },
                tooltip: {
                    callbacks: {
                        label: function (context) {
                            const dataset = context.dataset;
                            const dataPoint = dataset.data[context.dataIndex];
                            return `${dataset.label} (Pricing: ${dataPoint.x}/10, Quality: ${dataPoint.y}/10, Share: ${Math.round(dataPoint.r / 0.4)}%)`;
                        }
                    }
                }
            },
            scales: {
                x: {
                    title: { display: true, text: 'Pricing Level (1=Low, 10=High)', color: '#94a3b8' },
                    grid: { color: 'rgba(255,255,255,0.05)' },
                    ticks: { color: '#94a3b8' },
                    min: 0,
                    max: 11
                },
                y: {
                    title: { display: true, text: 'Product Quality / Value (1=Low, 10=High)', color: '#94a3b8' },
                    grid: { color: 'rgba(255,255,255,0.05)' },
                    ticks: { color: '#94a3b8' },
                    min: 0,
                    max: 11
                }
            }
        }
    });
}

function renderMarketingBudgetChart(marketingObj) {
    const ctx = document.getElementById("marketing-budget-chart").getContext("2d");
    if (!marketingObj) return;

    const labels = [];
    const data = [];

    const mktKeys = ["organic", "content", "seo", "email", "influencer", "community", "referral", "pr"];
    mktKeys.forEach(k => {
        if (marketingObj[k] && typeof marketingObj[k].budget_share_percent === 'number') {
            labels.push(k.toUpperCase());
            data.push(marketingObj[k].budget_share_percent);
        }
    });

    if (marketingObj.social_media) {
        ["instagram", "linkedin", "youtube"].forEach(plat => {
            if (marketingObj.social_media[plat] && typeof marketingObj.social_media[plat].budget_share_percent === 'number') {
                labels.push(`SOCIAL: ${plat.toUpperCase()}`);
                data.push(marketingObj.social_media[plat].budget_share_percent);
            }
        });
    }

    if (data.length === 0) return;

    new Chart(ctx, {
        type: 'doughnut',
        data: {
            labels: labels,
            datasets: [{
                data: data,
                backgroundColor: [
                    '#6366f1', '#06b6d4', '#d946ef', '#f59e0b',
                    '#10b981', '#fb7185', '#64748b', '#818cf8',
                    '#22c55e', '#a855f7', '#ec4899'
                ],
                borderWidth: 1,
                borderColor: 'rgba(255,255,255,0.1)'
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            plugins: {
                legend: {
                    position: 'right',
                    labels: { color: '#f8fafc', font: { family: 'Plus Jakarta Sans', size: 8 } }
                }
            }
        }
    });
}

function renderRisksMatrixChart(risksList) {
    const ctx = document.getElementById("risks-matrix-chart").getContext("2d");
    if (!risksList || risksList.length === 0) return;

    const labels = risksList.map(r => r.type);
    const mapScore = (lvl) => {
        if (!lvl) return 2;
        const l = String(lvl).toLowerCase();
        if (l.includes("high")) return 3;
        if (l.includes("med")) return 2;
        return 1;
    };

    const impactData = risksList.map(r => mapScore(r.impact_level || r.level));
    const likelihoodData = risksList.map(r => mapScore(r.likelihood));

    new Chart(ctx, {
        type: 'bar',
        data: {
            labels: labels,
            datasets: [
                {
                    label: 'Impact Severity',
                    data: impactData,
                    backgroundColor: 'rgba(239, 68, 68, 0.6)',
                    borderColor: '#ef4444',
                    borderWidth: 1.5,
                    borderRadius: 3
                },
                {
                    label: 'Likelihood',
                    data: likelihoodData,
                    backgroundColor: 'rgba(245, 158, 11, 0.6)',
                    borderColor: '#f59e0b',
                    borderWidth: 1.5,
                    borderRadius: 3
                }
            ]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            plugins: {
                legend: {
                    labels: { color: '#f8fafc', font: { family: 'Plus Jakarta Sans' } }
                }
            },
            scales: {
                x: {
                    grid: { color: 'rgba(255,255,255,0.05)' },
                    ticks: { color: '#94a3b8' }
                },
                y: {
                    grid: { color: 'rgba(255,255,255,0.05)' },
                    ticks: {
                        color: '#94a3b8',
                        stepSize: 1,
                        callback: function (value) {
                            if (value === 1) return 'Low';
                            if (value === 2) return 'Medium';
                            if (value === 3) return 'High';
                            return '';
                        }
                    },
                    min: 0,
                    max: 4
                }
            }
        }
    });
}

function setupScrollSpy() {
    const sections = document.querySelectorAll(".report-section");
    const navLinks = document.querySelectorAll(".toc-link");

    const observerOptions = {
        root: null,
        rootMargin: "-20% 0px -60% 0px",
        threshold: 0
    };

    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                const activeId = entry.target.getAttribute("id");

                navLinks.forEach(link => {
                    if (link.getAttribute("href") === `#${activeId}`) {
                        link.classList.add("active");
                    } else {
                        link.classList.remove("active");
                    }
                });
            }
        });
    }, observerOptions);

    sections.forEach(sec => observer.observe(sec));

    navLinks.forEach(link => {
        link.addEventListener("click", (e) => {
            e.preventDefault();
            const targetId = link.getAttribute("href");
            const targetEl = document.querySelector(targetId);

            targetEl.scrollIntoView({ behavior: "smooth" });

            navLinks.forEach(l => l.classList.remove("active"));
            link.classList.add("active");
        });
    });
}
