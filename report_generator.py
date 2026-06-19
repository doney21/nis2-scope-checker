"""
NIS2 Scope Checker — Report Generator
Produces a downloadable Markdown scoping summary from quiz answers.
"""

import datetime
from nis2_data import OBLIGATIONS, NIS2_SECTORS


def generate_report(answers: dict) -> str:
    """Return a Markdown string summarising the scoping result."""

    verdict = answers.get("verdict", "out_of_scope")
    obs = OBLIGATIONS[verdict]

    sector_annex = answers.get("sector_annex", "")
    sector_key = answers.get("sector_key", "")
    subsector_key = answers.get("subsector_key", "")
    member_state = answers.get("member_state", "Not specified")
    size = answers.get("size", "Not specified")
    auto_trigger = answers.get("auto_in_scope_trigger")
    out_reason = answers.get("out_of_scope_reason", "")

    # Resolve human-readable sector / subsector names
    sector_name = ""
    subsector_name = ""
    subsector_desc = ""
    if sector_annex and sector_key:
        annex_data = NIS2_SECTORS.get(sector_annex, {})
        sector_data = annex_data.get("sectors", {}).get(sector_key, {})
        sector_name = sector_data.get("name", sector_key)
        if subsector_key:
            sub = sector_data.get("subsectors", {}).get(subsector_key, {})
            subsector_name = sub.get("name", subsector_key)
            subsector_desc = sub.get("description", "")

    now = datetime.datetime.utcnow().strftime("%d %B %Y, %H:%M UTC")
    annex_label = NIS2_SECTORS.get(sector_annex, {}).get("label", "") if sector_annex else ""

    lines = []

    # Header
    lines += [
        "# NIS2 Scoping Report",
        "",
        f"**Generated:** {now}  ",
        f"**Tool:** NIS2 Scope Checker (github.com/donalkerr/nis2-scope-checker)  ",
        "",
        "> ⚠️ **Disclaimer:** This report provides indicative scoping guidance only and does not constitute "
        "legal advice. For a definitive determination, consult your national competent authority (NCA) "
        "or qualified legal counsel.",
        "",
        "---",
        "",
    ]

    # Verdict banner
    lines += [
        "## Scoping Verdict",
        "",
        f"### {obs['colour']} {obs['label']}",
        "",
    ]

    # Clean summary of plain text (strip markdown bold for body)
    summary_clean = obs["summary"].replace("**", "")
    lines += [f"{obs['summary']}", ""]

    if out_reason:
        lines += [f"> {out_reason}", ""]

    if auto_trigger:
        lines += [
            f"**Auto-in-scope trigger ({auto_trigger['article']}):** {auto_trigger['label']}  ",
            f"_{auto_trigger['note']}_",
            "",
        ]

    lines += ["---", ""]

    # Entity details
    lines += [
        "## Entity Details",
        "",
        f"| Field | Value |",
        f"|-------|-------|",
        f"| Member State | {member_state} |",
    ]
    if sector_name:
        lines += [f"| Sector | {sector_name} |"]
    if annex_label:
        lines += [f"| Classification Basis | {annex_label} |"]
    if subsector_name:
        lines += [f"| Subsector | {subsector_name} |"]
    if subsector_desc:
        lines += [f"| Subsector Description | {subsector_desc} |"]
    if size and size != "Not specified":
        lines += [f"| Organisation Size | {size} |"]
    lines += [""]

    lines += ["---", ""]

    # Applicable obligations
    if obs["articles"]:
        lines += [
            "## Applicable NIS2 Obligations and Article References",
            "",
        ]
        for article, desc in obs["articles"].items():
            lines += [
                f"### {article}",
                f"{desc}",
                "",
            ]

    lines += ["---", ""]

    # Key next steps
    lines += [
        "## Recommended Next Steps",
        "",
    ]

    if verdict == "essential":
        lines += [
            "1. **Register** with your national competent authority (NCA) — Art. 27",
            "2. **Conduct a gap assessment** against Art. 21 security measures",
            "3. **Establish incident detection and reporting workflows** aligned to Art. 23 timelines (24h / 72h / 1 month)",
            "4. **Brief management** on their obligations under Art. 20 and arrange cybersecurity training",
            "5. **Review supply chain contracts** for ICT third-party risk clauses — Art. 21(2)(d)",
            "6. **Assess DORA intersection** if your entity is also a financial entity subject to Regulation (EU) 2022/2554",
        ]
    elif verdict == "important":
        lines += [
            "1. **Register** with your national competent authority (NCA) — Art. 27",
            "2. **Conduct a gap assessment** against Art. 21 security measures (same technical obligations as Essential Entities)",
            "3. **Establish incident detection and reporting workflows** aligned to Art. 23 timelines (24h / 72h / 1 month)",
            "4. **Brief management** on their obligations under Art. 20 and arrange cybersecurity training",
            "5. **Review supply chain contracts** for ICT third-party risk clauses — Art. 21(2)(d)",
        ]
    else:
        lines += [
            "1. **Monitor** for changes in your sector, size, or service portfolio that could bring you in scope",
            "2. **Consider voluntary adoption** of Art. 21 security measures as a baseline cybersecurity standard",
            "3. **Check Member State transposition** — your NCA may have extended scope beyond NIS2 minimum requirements",
        ]

    lines += [
        "",
        "---",
        "",
        "## References",
        "",
        "- [NIS2 Directive (EU) 2022/2555](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX%3A32022L2555)",
        "- [ENISA NIS2 Implementation Guidance](https://www.enisa.europa.eu/topics/cybersecurity-policy/nis-directive-new)",
        "- [EBA DORA resources](https://www.eba.europa.eu/activities/direct-supervision-and-oversight/digital-operational-resilience-act)",
        "",
        "---",
        "",
        "_Report generated by NIS2 Scope Checker. MIT Licensed. Contributions welcome._",
    ]

    return "\n".join(lines)
