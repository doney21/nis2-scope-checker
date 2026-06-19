"""
NIS2 Scope Checker
A step-by-step tool to determine NIS2 Essential / Important Entity status.
"""

import streamlit as st
from nis2_data import (
    EU_MEMBER_STATES,
    NIS2_SECTORS,
    SIZE_THRESHOLDS,
    OBLIGATIONS,
    AUTO_IN_SCOPE_TRIGGERS,
)
from report_generator import generate_report

# ---------------------------------------------------------------------------
# Page config
# ---------------------------------------------------------------------------

st.set_page_config(
    page_title="NIS2 Scope Checker",
    page_icon="🔒",
    layout="centered",
    initial_sidebar_state="collapsed",
)

st.markdown(
    """
    <style>
    /* Constrain width for readability */
    .block-container { max-width: 760px; padding-top: 2rem; }

    /* Step header */
    .step-header {
        font-size: 0.8rem;
        font-weight: 600;
        text-transform: uppercase;
        letter-spacing: 0.08em;
        color: #6b7280;
        margin-bottom: 0.25rem;
    }

    /* Verdict boxes */
    .verdict-essential {
        background: #fef2f2;
        border-left: 5px solid #dc2626;
        padding: 1.25rem 1.5rem;
        border-radius: 6px;
        margin-bottom: 1rem;
    }
    .verdict-important {
        background: #fffbeb;
        border-left: 5px solid #d97706;
        padding: 1.25rem 1.5rem;
        border-radius: 6px;
        margin-bottom: 1rem;
    }
    .verdict-out {
        background: #f0fdf4;
        border-left: 5px solid #16a34a;
        padding: 1.25rem 1.5rem;
        border-radius: 6px;
        margin-bottom: 1rem;
    }

    /* Article citation card */
    .article-card {
        background: #f8fafc;
        border: 1px solid #e2e8f0;
        border-radius: 6px;
        padding: 0.75rem 1rem;
        margin-bottom: 0.5rem;
    }
    .article-label {
        font-weight: 700;
        color: #1e293b;
        font-size: 0.85rem;
    }
    .article-text {
        color: #475569;
        font-size: 0.85rem;
        margin-top: 0.2rem;
    }

    /* Auto-in-scope banner */
    .auto-banner {
        background: #eff6ff;
        border: 1px solid #3b82f6;
        border-radius: 6px;
        padding: 0.75rem 1rem;
        margin-bottom: 1rem;
        font-size: 0.875rem;
        color: #1d4ed8;
    }

    /* Disclaimer */
    .disclaimer {
        font-size: 0.78rem;
        color: #9ca3af;
        margin-top: 1.5rem;
        border-top: 1px solid #e5e7eb;
        padding-top: 0.75rem;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# ---------------------------------------------------------------------------
# Session state initialisation
# ---------------------------------------------------------------------------

STEPS = [
    "welcome",
    "member_state",
    "auto_check",
    "sector_annex",
    "sector",
    "subsector",
    "size",
    "result",
]


def init():
    if "step" not in st.session_state:
        st.session_state.step = "welcome"
    if "answers" not in st.session_state:
        st.session_state.answers = {}


def go(step: str):
    st.session_state.step = step
    st.rerun()


def back(current: str):
    idx = STEPS.index(current)
    if idx > 0:
        st.session_state.step = STEPS[idx - 1]
        st.rerun()


def progress_pct(step: str) -> float:
    idx = STEPS.index(step) if step in STEPS else 0
    return idx / (len(STEPS) - 1)


init()
step = st.session_state.step
answers = st.session_state.answers

# ---------------------------------------------------------------------------
# Progress bar (hidden on welcome)
# ---------------------------------------------------------------------------

if step != "welcome":
    st.progress(progress_pct(step))
    step_n = STEPS.index(step)
    st.markdown(
        f'<div class="step-header">Step {step_n} of {len(STEPS) - 1}</div>',
        unsafe_allow_html=True,
    )

# ---------------------------------------------------------------------------
# STEP: Welcome
# ---------------------------------------------------------------------------

if step == "welcome":
    st.title("🔒 NIS2 Scope Checker")
    st.markdown(
        """
        Determine your organisation's status under the **EU NIS2 Directive (2022/2555)** —
        whether you are an **Essential Entity**, an **Important Entity**, or out of scope.

        The tool covers:
        - All **Annex I** (high criticality) and **Annex II** (other critical) sectors
        - Subsector-level classification with entity type guidance
        - Size thresholds and automatic in-scope triggers
        - Applicable article citations and key obligations
        - Downloadable scoping report in Markdown format

        **Takes approximately 2 minutes.**
        """
    )
    st.markdown(
        '<div class="disclaimer">⚠️ This tool provides indicative scoping guidance only and '
        "does not constitute legal advice. For a definitive determination, consult your national "
        "competent authority (NCA) or qualified legal counsel.</div>",
        unsafe_allow_html=True,
    )
    st.markdown("")
    if st.button("Start →", type="primary", use_container_width=True):
        go("member_state")

# ---------------------------------------------------------------------------
# STEP: Member State
# ---------------------------------------------------------------------------

elif step == "member_state":
    st.subheader("Where is your organisation established?")
    st.markdown(
        "NIS2 applies to entities **established in the EU**, or entities established outside the EU "
        "that provide services to recipients in the EU (Art. 2(3))."
    )

    ms_options = ["— select —"] + EU_MEMBER_STATES + ["Other EU / EEA", "Outside EU"]
    ms = st.selectbox("Member State of establishment", ms_options)

    col1, col2 = st.columns([1, 3])
    with col1:
        if st.button("← Back"):
            go("welcome")
    with col2:
        if st.button("Next →", type="primary", use_container_width=True):
            if ms == "— select —":
                st.warning("Please select a member state.")
            elif ms == "Outside EU":
                answers["member_state"] = ms
                answers["verdict"] = "out_of_scope"
                answers["out_of_scope_reason"] = (
                    "Your organisation is not established in the EU. Unless you provide services "
                    "to EU recipients and have designated an EU representative (Art. 2(3)), NIS2 "
                    "does not apply."
                )
                go("result")
            else:
                answers["member_state"] = ms
                go("auto_check")

# ---------------------------------------------------------------------------
# STEP: Auto-in-scope check
# ---------------------------------------------------------------------------

elif step == "auto_check":
    st.subheader("Automatic in-scope triggers")
    st.markdown(
        "Certain entities are in scope **regardless of their size**. "
        "Select any that apply to your organisation (Art. 2(2))."
    )

    trigger_labels = {t["id"]: t["label"] for t in AUTO_IN_SCOPE_TRIGGERS}
    selected_ids = []
    for t in AUTO_IN_SCOPE_TRIGGERS:
        if st.checkbox(f"{t['label']}  \n*{t['article']} — {t['note']}*", key=t["id"]):
            selected_ids.append(t["id"])

    col1, col2 = st.columns([1, 3])
    with col1:
        if st.button("← Back"):
            back("auto_check")
    with col2:
        if st.button("Next →", type="primary", use_container_width=True):
            if selected_ids:
                trigger = next(t for t in AUTO_IN_SCOPE_TRIGGERS if t["id"] == selected_ids[0])
                answers["auto_in_scope_trigger"] = trigger
                answers["verdict"] = trigger["verdict"]
                # Still collect sector for the report, but skip size
                go("sector_annex")
            else:
                answers.pop("auto_in_scope_trigger", None)
                go("sector_annex")

# ---------------------------------------------------------------------------
# STEP: Annex selection
# ---------------------------------------------------------------------------

elif step == "sector_annex":
    st.subheader("Which sector best describes your organisation?")
    st.markdown(
        "NIS2 covers entities in **Annex I** (high criticality) and **Annex II** (other critical) sectors. "
        "If your sector appears in both, choose Annex I."
    )

    annex_choice = st.radio(
        "Select the applicable annex:",
        options=[
            "Annex I — High Criticality Sectors (energy, transport, banking, health, digital infrastructure…)",
            "Annex II — Other Critical Sectors (postal, waste, chemicals, food, manufacturing, digital providers…)",
            "My sector is not listed in either annex",
        ],
        index=0,
    )

    col1, col2 = st.columns([1, 3])
    with col1:
        if st.button("← Back"):
            back("sector_annex")
    with col2:
        if st.button("Next →", type="primary", use_container_width=True):
            if "not listed" in annex_choice:
                answers["sector_annex"] = None
                answers["verdict"] = "out_of_scope"
                answers["out_of_scope_reason"] = (
                    "Your organisation's sector does not appear in Annex I or Annex II of NIS2. "
                    "Unless your Member State has extended scope via national transposition, "
                    "NIS2 obligations do not apply."
                )
                go("result")
            elif "Annex I" in annex_choice:
                answers["sector_annex"] = "annex_i"
                go("sector")
            else:
                answers["sector_annex"] = "annex_ii"
                go("sector")

# ---------------------------------------------------------------------------
# STEP: Sector
# ---------------------------------------------------------------------------

elif step == "sector":
    annex_key = answers.get("sector_annex", "annex_i")
    annex_data = NIS2_SECTORS[annex_key]

    st.subheader(f"Select your sector — {annex_data['label']}")

    sector_options = {k: v["name"] for k, v in annex_data["sectors"].items()}
    sector_display = ["— select —"] + list(sector_options.values())
    sector_keys = [None] + list(sector_options.keys())

    choice = st.selectbox("Sector", sector_display)

    col1, col2 = st.columns([1, 3])
    with col1:
        if st.button("← Back"):
            back("sector")
    with col2:
        if st.button("Next →", type="primary", use_container_width=True):
            if choice == "— select —":
                st.warning("Please select a sector.")
            else:
                idx = sector_display.index(choice)
                answers["sector_key"] = sector_keys[idx]
                go("subsector")

# ---------------------------------------------------------------------------
# STEP: Subsector
# ---------------------------------------------------------------------------

elif step == "subsector":
    annex_key = answers.get("sector_annex", "annex_i")
    sector_key = answers.get("sector_key", "")
    annex_data = NIS2_SECTORS[annex_key]
    sector_data = annex_data["sectors"].get(sector_key, {})
    subsectors = sector_data.get("subsectors", {})

    st.subheader(f"Select your subsector — {sector_data.get('name', '')}")

    sub_options = {k: v["name"] for k, v in subsectors.items()}
    sub_display = ["— select —"] + list(sub_options.values())
    sub_keys = [None] + list(sub_options.keys())
    sub_descs = {k: v.get("description", "") for k, v in subsectors.items()}

    choice = st.selectbox("Subsector", sub_display)

    # Show description for selected subsector
    if choice and choice != "— select —":
        chosen_key = sub_keys[sub_display.index(choice)]
        desc = sub_descs.get(chosen_key, "")
        if desc:
            st.caption(f"📋 {desc}")

    col1, col2 = st.columns([1, 3])
    with col1:
        if st.button("← Back"):
            back("subsector")
    with col2:
        if st.button("Next →", type="primary", use_container_width=True):
            if choice == "— select —":
                st.warning("Please select a subsector.")
            else:
                idx = sub_display.index(choice)
                answers["subsector_key"] = sub_keys[idx]
                # If auto-in-scope already triggered, skip size
                if answers.get("auto_in_scope_trigger"):
                    go("result")
                else:
                    go("size")

# ---------------------------------------------------------------------------
# STEP: Size
# ---------------------------------------------------------------------------

elif step == "size":
    st.subheader("What is the size of your organisation?")
    st.markdown(
        "NIS2 generally applies to **medium and large enterprises** only. "
        "Size is assessed using the EU Commission Recommendation 2003/361/EC thresholds."
    )

    st.markdown(
        """
        | Size | Employees | Annual Turnover | Balance Sheet |
        |------|-----------|----------------|---------------|
        | **Large** | ≥ 250 | > €50M | > €43M |
        | **Medium** | 50–249 | ≤ €50M | ≤ €43M |
        | **Small** | 10–49 | ≤ €10M | ≤ €10M |
        | **Micro** | < 10 | ≤ €2M | ≤ €2M |
        """
    )
    st.caption("For Annex I entities: Large → Essential Entity, Medium → Important Entity (unless otherwise designated). For Annex II entities: Medium or Large → Important Entity.")

    size_choice = st.radio(
        "Your organisation's size:",
        options=["Large (≥250 employees or >€50M turnover)", "Medium (50–249 employees)", "Small (10–49 employees)", "Micro (<10 employees)"],
    )

    col1, col2 = st.columns([1, 3])
    with col1:
        if st.button("← Back"):
            back("size")
    with col2:
        if st.button("Calculate scope →", type="primary", use_container_width=True):
            annex_key = answers.get("sector_annex", "annex_i")
            answers["size"] = size_choice

            if "Small" in size_choice or "Micro" in size_choice:
                answers["verdict"] = "out_of_scope"
                answers["out_of_scope_reason"] = (
                    "Small and micro enterprises are generally outside NIS2 scope (Art. 2(1)), "
                    "unless they qualify as an automatic in-scope entity under Art. 2(2). "
                    "Check the auto-in-scope triggers and your Member State's national transposition "
                    "for any extended scope provisions."
                )
            elif annex_key == "annex_i":
                if "Large" in size_choice:
                    answers["verdict"] = "essential"
                else:  # Medium
                    answers["verdict"] = "important"
            else:  # Annex II
                answers["verdict"] = "important"

            go("result")

# ---------------------------------------------------------------------------
# STEP: Result
# ---------------------------------------------------------------------------

elif step == "result":
    verdict = answers.get("verdict", "out_of_scope")
    obs = OBLIGATIONS[verdict]
    auto_trigger = answers.get("auto_in_scope_trigger")

    # Verdict banner
    css_class = {
        "essential": "verdict-essential",
        "important": "verdict-important",
        "out_of_scope": "verdict-out",
    }[verdict]

    st.markdown(
        f'<div class="{css_class}"><h3>{obs["colour"]} {obs["label"]}</h3>'
        f"<p>{obs['summary']}</p></div>",
        unsafe_allow_html=True,
    )

    # Auto-in-scope callout
    if auto_trigger:
        st.markdown(
            f'<div class="auto-banner">🔵 <strong>Auto-in-scope trigger — {auto_trigger["article"]}:</strong> '
            f'{auto_trigger["label"]}<br><em>{auto_trigger["note"]}</em></div>',
            unsafe_allow_html=True,
        )

    # Out-of-scope reason
    out_reason = answers.get("out_of_scope_reason", "")
    if out_reason:
        st.info(out_reason)

    # Summary table
    st.markdown("### Entity Summary")
    annex_key = answers.get("sector_annex", "")
    sector_key = answers.get("sector_key", "")
    subsector_key = answers.get("subsector_key", "")
    annex_label = NIS2_SECTORS.get(annex_key, {}).get("label", "—") if annex_key else "—"
    sector_name = NIS2_SECTORS.get(annex_key, {}).get("sectors", {}).get(sector_key, {}).get("name", "—") if annex_key and sector_key else "—"
    subsector_name = (
        NIS2_SECTORS.get(annex_key, {}).get("sectors", {}).get(sector_key, {}).get("subsectors", {}).get(subsector_key, {}).get("name", "—")
        if annex_key and sector_key and subsector_key
        else "—"
    )

    col_a, col_b = st.columns(2)
    with col_a:
        st.metric("Member State", answers.get("member_state", "—"))
        st.metric("Sector", sector_name)
        st.metric("Subsector", subsector_name)
    with col_b:
        st.metric("Classification Basis", annex_label)
        st.metric("Organisation Size", answers.get("size", "—"))
        st.metric("NIS2 Status", obs["label"])

    # Article citations
    if obs["articles"]:
        st.markdown("### Applicable Articles & Obligations")
        for article, desc in obs["articles"].items():
            st.markdown(
                f'<div class="article-card">'
                f'<div class="article-label">{article}</div>'
                f'<div class="article-text">{desc}</div>'
                f"</div>",
                unsafe_allow_html=True,
            )

    # Download report
    st.markdown("### Download Scoping Report")
    report_md = generate_report(answers)
    st.download_button(
        label="⬇️ Download Markdown Report",
        data=report_md,
        file_name="nis2_scoping_report.md",
        mime="text/markdown",
        use_container_width=True,
        type="primary",
    )

    st.markdown("")

    # Restart
    if st.button("🔄 Start over", use_container_width=True):
        st.session_state.answers = {}
        go("welcome")

    # Disclaimer
    st.markdown(
        '<div class="disclaimer">⚠️ This report provides indicative scoping guidance only and does not '
        "constitute legal advice. For a definitive determination, consult your national competent "
        "authority (NCA) or qualified legal counsel. "
        "NIS2 was required to be transposed by Member States by 17 October 2024 — national "
        "transpositions may extend or modify the baseline scope.</div>",
        unsafe_allow_html=True,
    )
