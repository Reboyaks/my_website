import os

import streamlit as st
import streamlit.components.v1 as components

from pathlib import Path
import streamlit as st

BASE_DIR = Path(__file__).resolve().parent
ASSETS_DIR = BASE_DIR / "assets"

# =========================================================
# PAGE CONFIG
# =========================================================

st.set_page_config(
    page_title="Reynaldo Lorenzo | Data Analyst",
    page_icon="◆",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# =========================================================
# THEME STATE
# =========================================================

BASE_DIR = Path(__file__).resolve().parent

if "theme" not in st.session_state:
    st.session_state.theme = "light"

def toggle_theme():
    st.session_state.theme = (
        "light"
        if st.session_state.theme == "dark"
        else "dark"
    )

def load_theme_css():
    css_file = (
        BASE_DIR / "light_style.css"
        if st.session_state.theme == "light"
        else BASE_DIR / "dark_style.css"
    )

    css = css_file.read_text(encoding="utf-8")

    st.markdown(
        f"<style>{css}</style>",
        unsafe_allow_html=True
    )

load_theme_css()

st.html("""
<nav class="top-nav">

    <a href="#top" class="nav-brand">
        REYNALDO<span>.</span>
    </a>

    <div class="nav-links">

        <a href="#process" class="nav-link">
            Process
        </a>

        <a href="#work" class="nav-link">
            Work
        </a>

        <a href="#about" class="nav-link">
            About
        </a>

        <a href="#toolkit" class="nav-link">
            Toolkit
        </a>

        <a href="#contact" class="nav-link contact">
            Contact
        </a>

    </div>

</nav>
""")

# =========================================================
# THEME TOGGLE
# =========================================================

theme_icon = "☀" if st.session_state.theme == "dark" else "☾"

st.button(
    theme_icon,
    key="theme_button",
    on_click=toggle_theme,
    help="Toggle light / dark mode",
)

# =========================================================
# HERO
# =========================================================

st.html("""
<div id="top" class="hero">

    <div class="hero-status">

        <div class="hero-status-dot"></div>

        Open to opportunities & projects

    </div>


    <div class="hero-label">
        DATA · AUTOMATION · BUSINESS INTELLIGENCE
    </div>


    <h1 class="hero-title">
        Reynaldo <span>Lorenzo.</span>
    </h1>


    <div class="hero-subtitle">
        I turn business problems into practical systems.
    </div>


    <div class="hero-description">
        Data Analyst focused on Python, automation,
        business intelligence, ETL, dashboards, and
        practical technology solutions.
    </div>


    <div class="hero-tags">

        <div class="hero-tag">
            Python
        </div>

        <div class="hero-tag">
            SQL
        </div>

        <div class="hero-tag">
            Automation
        </div>

        <div class="hero-tag">
            Business Intelligence
        </div>

        <div class="hero-tag">
            ETL
        </div>

    </div>


    <div class="hero-actions">

        <a
            href="#work"
            class="hero-button primary"
        >
            View My Work ↓
        </a>

        <a
            href="#process"
            class="hero-button"
        >
            See My Process
        </a>

    </div>


    <div class="hero-divider"></div>

</div>
""")

# =========================================================
# INTERACTIVE FUNNEL DATA
# =========================================================

funnel_data = {
    "Understand": {
        "number": "01",
        "description": (
            "Start with the business problem. "
            "Understand what needs to be improved, measured, "
            "automated, or explained."
        ),
        "tools": [
            "Business Requirements",
            "KPI Definition",
            "Process Analysis"
        ]
    },

    "Collect": {
        "number": "02",
        "description": (
            "Identify and collect the right information from "
            "business systems, spreadsheets, APIs, and other sources."
        ),
        "tools": [
            "REST APIs",
            "Google Sheets",
            "SQL",
            "CRM Data"
        ]
    },

    "Transform": {
        "number": "03",
        "description": (
            "Turn raw information into structured, reliable "
            "data that can actually be analyzed and used."
        ),
        "tools": [
            "Python",
            "pandas",
            "SQL",
            "ETL"
        ]
    },

    "Automate": {
        "number": "04",
        "description": (
            "Remove repetitive manual processes by connecting "
            "systems and building repeatable workflows."
        ),
        "tools": [
            "Python",
            "REST APIs",
            "n8n",
            "Zapier"
        ]
    },

    "Visualize": {
        "number": "05",
        "description": (
            "Turn processed data into dashboards, KPIs, reports, "
            "and useful business insights."
        ),
        "tools": [
            "Power BI",
            "Looker Studio",
            "Plotly",
            "Dashboards"
        ]
    }
}

# =========================================================
# INTERACTIVE FUNNEL
# =========================================================

st.html("""
<div id="process" class="section">

    <div class="section-label">
        My Process
    </div>

    <div class="section-title">
        From Problem to Solution
    </div>

    <div class="section-description">
        Click through the process to see how I connect
        business problems, data, automation, and intelligence.
    </div>

</div>
""")


# ---------------------------------------------------------
# Selected funnel stage
# ---------------------------------------------------------

if "selected_funnel" not in st.session_state:
    st.session_state.selected_funnel = "Transform"


# ---------------------------------------------------------
# Funnel helper
# ---------------------------------------------------------

def funnel_button(stage):

    if st.button(
        f"{funnel_data[stage]['number']}  ·  {stage}",
        key=f"funnel_{stage}",
        use_container_width=True
    ):
        st.session_state.selected_funnel = stage
            
# =========================================================
# PROCESS + DETAIL — TWO COLUMN LAYOUT
# =========================================================

with st.container(key="process-layout"):

    process_col, detail_col = st.columns(
        [0.9, 1.1],
        gap="large"
    )

    # -----------------------------------------------------
    # LEFT — PROCESS FLOW
    # -----------------------------------------------------

    with process_col:

        funnel_button("Understand")

        st.html("""
        <div class="funnel-arrow">↓</div>
        """)

        funnel_button("Collect")

        st.html("""
        <div class="funnel-arrow">↓</div>
        """)

        funnel_button("Transform")

        st.html("""
        <div class="funnel-arrow">↓</div>
        """)

        funnel_button("Automate")

        st.html("""
        <div class="funnel-arrow">↓</div>
        """)

        funnel_button("Visualize")


    # -----------------------------------------------------
    # RIGHT — SELECTED DETAIL
    # -----------------------------------------------------

    with detail_col:

        selected = st.session_state.selected_funnel
        data = funnel_data[selected]

        tools_html = "".join(
            f'<div class="funnel-tool">{tool}</div>'
            for tool in data["tools"]
        )

        st.html(f"""
        <div class="funnel-detail">

            <div class="funnel-detail-label">
                STEP {data["number"]}
            </div>

            <div class="funnel-detail-title">
                {selected}
            </div>

            <div class="funnel-detail-description">
                {data["description"]}
            </div>

            <div class="funnel-tools">
                {tools_html}
            </div>

        </div>
        """)

# =========================================================
# WHAT I BUILD
# =========================================================

st.html("""
<div class="section">

    <div class="section-label">
        Expertise
    </div>

    <div class="section-title">
        What I Build
    </div>

    <div class="section-description">
        A combination of analytics, automation, and
        business intelligence to solve practical problems.
    </div>

</div>
""")


col1, col2, col3 = st.columns(3)

with col1:
    st.html("""
    <div class="card">

        <div class="card-number">
            01 · ANALYTICS
        </div>

        <div class="card-title">
            Data Analytics
        </div>

        <div class="card-description">
            Clean, transform, analyze, and structure
            business data to uncover useful insights.
        </div>

        <div class="card-tools">
            Python · pandas · SQL · Excel
        </div>

    </div>
    """)

with col2:
    st.html("""
    <div class="card">

        <div class="card-number">
            02 · INTELLIGENCE
        </div>

        <div class="card-title">
            Business Intelligence
        </div>

        <div class="card-description">
            Turn processed data into dashboards,
            KPIs, reports, and decision-support tools.
        </div>

        <div class="card-tools">
            Power BI · Looker Studio · Plotly
        </div>

    </div>
    """)

with col3:
    st.html("""
    <div class="card">

        <div class="card-number">
            03 · AUTOMATION
        </div>

        <div class="card-title">
            Automation & APIs
        </div>

        <div class="card-description">
            Connect systems and eliminate repetitive
            processes using code, APIs, and automation tools.
        </div>

        <div class="card-tools">
            Python · APIs · n8n · Zapier
        </div>

    </div>
    """)
    
# =========================================================
# PROJECT DATA
# =========================================================

project_data = {

    "Roofing Analytics": {

    "category": "DATA + AUTOMATION",

    "description": (
        "An end-to-end data workflow designed to transform "
        "operational CRM information into structured data "
        "for reporting and business intelligence."
    ),

    "challenge": (
        "Operational data needed to be collected from a CRM, "
        "processed consistently, and prepared for analysis "
        "without relying on repetitive manual preparation."
    ),

    "solution": (
        "Built a Python-based workflow for API extraction, "
        "pagination, data cleaning, transformation, and "
        "incremental data processing."
    ),

    "flow": [
        "CRM",
        "REST API",
        "Python",
        "ETL",
        "Google Sheets",
        "Looker Studio"
    ],

    "tools": [
        "Python",
        "pandas",
        "REST API",
        "Google Sheets",
        "ETL",
        "Looker Studio"
    ],

    "impact": (
        "Created a repeatable pipeline for turning operational "
        "CRM data into structured information ready for "
        "reporting, KPI analysis, and business intelligence."
    ),
    
    "YouTube": "https://youtu.be/VF-GGJQERTM"
    
},


    "Payroll Automation": {

    "category": "PYTHON AUTOMATION",

    "description": (
        "A Python-based automation workflow for processing "
        "commission calculations and generating payroll-related "
        "documents."
    ),

    "challenge": (
        "Commission and payroll preparation involved repetitive "
        "data processing that could be standardized and automated."
    ),

    "solution": (
        "Used Python and structured data processing to automate "
        "calculations and generate formatted payroll documents."
    ),

    "flow": [
        "Raw Data",
        "Python",
        "Calculations",
        "Validation",
        "HTML",
        "PDF"
    ],

    "tools": [
        "Python",
        "pandas",
        "HTML",
        "PDF Generation"
    ],

    "impact": (
        "Converted a repetitive payroll preparation workflow "
        "into a more structured and repeatable Python-based "
        "process."
    ),
    
    "YouTube": "To be Made"

},


    "Sales & Marketing Analytics": {

    "category": "BUSINESS INTELLIGENCE",

    "description": (
        "A business intelligence workflow focused on sales, "
        "marketing, conversion, revenue, and operational KPIs."
    ),

    "challenge": (
        "Business performance required a clearer view across "
        "sales funnels, marketing efficiency, revenue, and "
        "operational metrics."
    ),

    "solution": (
        "Structured business data into KPI-driven reporting "
        "and dashboard views designed to make performance "
        "easier to understand and monitor."
    ),

    "flow": [
        "Business Data",
        "SQL",
        "Transformation",
        "KPI Layer",
        "Dashboard",
        "Insights"
    ],

    "tools": [
        "SQL",
        "Power BI",
        "Looker Studio",
        "Data Analytics"
    ],

    "impact": (
        "Created a clearer framework for monitoring sales, "
        "marketing, revenue, and operational performance "
        "through KPI-driven reporting."
    ),
    
    "YouTube": "https://youtu.be/NiThRvV7QJo"
},

"Lead Finder Web Application": {

    "category": "WEB APPLICATION + AUTOMATION",

    "description": (
        "A full-stack lead discovery application designed to find, "
        "qualify, enrich, score, and manage roofing company prospects "
        "from live web data."
    ),

    "challenge": (
        "Finding relevant roofing prospects required repetitive "
        "web searching, manual qualification, website research, "
        "and prospect prioritization."
    ),

    "solution": (
        "Built a web application that searches live web data, "
        "qualifies roofing companies, enriches their websites "
        "with business intelligence, scores prospects, and prepares "
        "qualified leads for sales workflows."
    ),

    "flow": [
        "Live Web Search",
        "Lead Qualification",
        "Website Enrichment",
        "Technology Detection",
        "Prospect Scoring",
        "Sales Pipeline"
    ],

    "tools": [
        "React",
        "FastAPI",
        "Python",
        "Brave Search API",
        "SQLite",
        "REST API"
    ],

    "impact": (
        "Turned manual prospect research into a structured lead "
        "discovery and qualification workflow with searchable "
        "prospect data, enrichment, scoring, and sales tracking."
    ),

    "YouTube": "To be Made"
}
    
    
    
}
# =========================================================
# INTERACTIVE PROJECT SHOWCASE
# =========================================================

st.html("""
<div id="work" class="section">

    <div class="section-label">
        Selected Work
    </div>

    <div class="section-title">
        Featured Projects
    </div>

    <div class="section-description">
        Click a project to explore the problem, approach,
        workflow, and technologies behind it.
    </div>

</div>
""")


# ---------------------------------------------------------
# Selected project
# ---------------------------------------------------------

if "selected_project" not in st.session_state:

    st.session_state.selected_project = "Roofing Analytics"


# ---------------------------------------------------------
# Project selector
# ---------------------------------------------------------

projects = list(project_data.keys())

cols = st.columns(4)

for index, project_name in enumerate(projects):

    data = project_data[project_name]

    column = cols[index % 4]

    with column:

        is_active = (
            st.session_state.selected_project == project_name
        )

        active_class = " active" if is_active else ""

        st.html(f"""
        <div class="project-selector{active_class}">

            <div class="project-selector-category">
                {data["category"]}
            </div>

            <div class="project-selector-title">
                {project_name}
            </div>

            <div class="project-selector-description">
                {data["description"]}
            </div>

            <div class="project-selector-tools">
                {" · ".join(data["tools"][:4])}
            </div>

        </div>
        """)

        st.markdown(
            '<div class="project-selector-button">',
            unsafe_allow_html=True
        )

        if st.button(
            f"View {project_name}",
            key=f"project_{index}",
            use_container_width=True
        ):
            st.session_state.selected_project = project_name

        st.markdown(
            '</div>',
            unsafe_allow_html=True
        )


# ---------------------------------------------------------
# Project detail
# ---------------------------------------------------------

selected_project = st.session_state.selected_project

data = project_data[selected_project]


# =========================================================
# WORKFLOW HTML
# =========================================================

flow_html = ""

for index, step in enumerate(data["flow"]):

    flow_html += f"""
    <div class="project-flow-step">
        {step}
    </div>
    """

    if index < len(data["flow"]) - 1:

        flow_html += """
        <div class="project-flow-arrow">
            →
        </div>
        """


# =========================================================
# TECHNOLOGY HTML
# =========================================================

tools_html = "".join(
    f'<div class="project-tool">{tool}</div>'
    for tool in data["tools"]
)


# =========================================================
# CASE STUDY
# =========================================================

st.html(f"""
<div class="project-detail">
    

    <div class="project-detail-category">
        {data["category"]}
    </div>


    <div class="project-detail-title">
        {selected_project}
    </div>


    <div class="project-detail-description">
        {data["description"]}
    </div>


    <!-- ===============================================
         CHALLENGE + SOLUTION
         =============================================== -->

    <div class="project-case-grid">

        <div class="project-case-card">

            <div class="project-case-label">
                THE CHALLENGE
            </div>

            <div class="project-case-text">
                {data["challenge"]}
            </div>

        </div>


        <div class="project-case-card">

            <div class="project-case-label">
                THE SOLUTION
            </div>

            <div class="project-case-text">
                {data["solution"]}
            </div>

        </div>

    </div>


    <!-- ===============================================
         WORKFLOW
         =============================================== -->

    <div class="project-detail-section">

        <div class="project-detail-label">
            Workflow
        </div>

        <div class="project-flow">
            {flow_html}
        </div>

    </div>


    <!-- ===============================================
         TECHNOLOGY
         =============================================== -->

    <div class="project-detail-section">

        <div class="project-detail-label">
            Technology
        </div>

        <div class="project-tools">
            {tools_html}
        </div>

    </div>
    
    <!-- ===============================================
     PROJECT DEMO
     =============================================== -->

    <div class="project-demo">

        <a
            href="{data.get("YouTube", "#")}"
            target="_blank"
            class="project-demo-button"
        >

            <span class="project-demo-icon">
                ▶
            </span>

            Watch Project Demo

        </a>

    </div>

    <!-- ===============================================
         IMPACT
         =============================================== -->

    <div class="project-impact">

        <div class="project-impact-label">
            BUSINESS VALUE
        </div>

        <div class="project-impact-text">
            {data["impact"]}
        </div>

    </div>

</div>
""")

# =========================================================
# ABOUT + EXPERIENCE
# =========================================================

st.html("""
<div id="about" class="section">

    <div class="section-label">
        About Me
    </div>

    <div class="section-title">
        Technical Thinking. Practical Solutions.
    </div>

    <div class="section-description">
        A combination of technical experience, analytical
        thinking, and practical problem solving.
    </div>

</div>
""")


col1, col2 = st.columns([1.05, 1])


# =========================================================
# ABOUT
# =========================================================

with col1:

    st.html("""
    <div class="about-profile">

        <div class="about-profile-label">
            PROFILE
        </div>

        <div class="about-profile-title">
            Data Analyst with a technical mindset.
        </div>

        <div class="about-profile-text">

            I'm a Data Analyst with a background in
            telecommunications engineering and a growing
            focus on data analytics, automation,
            business intelligence, and development.

            <br><br>

            I enjoy working with messy data, repetitive
            processes, and business problems that can be
            improved through better systems.

            <br><br>

            My approach is practical: understand the problem,
            work with the data, automate what makes sense,
            and turn the result into something people can use.

        </div>

        <div class="about-highlight">

            I don't just want to analyze data.
            I want to build systems that make the data useful.

        </div>

    </div>
    """)

# =========================================================
# EXPERIENCE
# =========================================================

with col2:

    with st.container(border=True, height=430):

        st.html("""
        <div class="experience-label">
            EXPERIENCE
        </div>
        """)

        # -------------------------------------------------
        # DATA ANALYST
        # -------------------------------------------------

        st.html("""
        <div class="experience-item">

            <div class="experience-dot"></div>

            <div class="experience-role">
                Data Analyst
            </div>

            <div class="experience-company">
                Knewsales
            </div>

            <div class="experience-period">
                Current
            </div>

            <div class="experience-description">
                Transform sales and operational data into
                structured datasets, automated processes,
                dashboards, and business insights.
            </div>

        </div>
        """)


        # -------------------------------------------------
        # RF ENGINEER
        # -------------------------------------------------

        st.html("""
        <div class="experience-item">

            <div class="experience-dot"></div>

            <div class="experience-role">
                RF Engineer
            </div>

            <div class="experience-company">
                Globe Telecom / FINSI
            </div>

            <div class="experience-period">
                Previous Experience
            </div>

            <div class="experience-description">
                Technical engineering experience involving
                telecommunications, analysis, troubleshooting,
                and technical reporting.
            </div>

        </div>
        """)


        # -------------------------------------------------
        # RESUME CTA
        # -------------------------------------------------

        st.markdown(
            "<div style='height: 10px;'></div>",
            unsafe_allow_html=True
        )

        resume_col1, resume_col2 = st.columns(
            [1.4, 1],
            vertical_alignment="center"
        )

        with resume_col1:

            st.markdown(
                """
                <div class="resume-caption">
                    Want the complete background?
                </div>
                """,
                unsafe_allow_html=True
            )

        with resume_col2:

            resume_path = "assets/resume.pdf"

            if os.path.exists(resume_path):

                with open(resume_path, "rb") as file:

                    st.download_button(
                        label="Download Resume",
                        data=file,
                        file_name="Reynaldo_Lorenzo_Resume.pdf",
                        mime="application/pdf",
                        key="resume_download",
                        use_container_width=True
                    )
                
# =========================================================
# TOOLKIT / SKILLS
# =========================================================

st.html("""
<div class="section", id="toolkit">

    <div class="section-label">
        Technology
    </div>

    <div class="section-title">
        Toolkit & Capabilities
    </div>

    <div class="section-description">
        The tools I use to move from raw data and business
        problems to automated workflows and useful insights.
    </div>

</div>
""")


st.html("""
<div class="toolkit-grid">


    <!-- =================================================
         DATA & ANALYSIS
         ================================================= -->

    <div class="toolkit-card">

        <div class="toolkit-number">
            01 · DATA
        </div>

        <div class="toolkit-title">
            Data & Analysis
        </div>

        <div class="toolkit-description">
            Clean, transform, analyze, and structure
            business data for reliable decision-making.
        </div>

        <div class="toolkit-tools">

            <div class="toolkit-tag">
                Python
            </div>

            <div class="toolkit-tag">
                pandas
            </div>

            <div class="toolkit-tag">
                SQL
            </div>

            <div class="toolkit-tag">
                Excel
            </div>

        </div>

    </div>


    <!-- =================================================
         AUTOMATION
         ================================================= -->

    <div class="toolkit-card">

        <div class="toolkit-number">
            02 · AUTOMATION
        </div>

        <div class="toolkit-title">
            Automation & APIs
        </div>

        <div class="toolkit-description">
            Connect systems and reduce repetitive work
            through code, APIs, and workflow automation.
        </div>

        <div class="toolkit-tools">

            <div class="toolkit-tag">
                Python
            </div>

            <div class="toolkit-tag">
                REST APIs
            </div>

            <div class="toolkit-tag">
                n8n
            </div>

            <div class="toolkit-tag">
                Zapier
            </div>

        </div>

    </div>


    <!-- =================================================
         BUSINESS INTELLIGENCE
         ================================================= -->

    <div class="toolkit-card">

        <div class="toolkit-number">
            03 · BI
        </div>

        <div class="toolkit-title">
            Business Intelligence
        </div>

        <div class="toolkit-description">
            Turn processed data into dashboards, KPIs,
            reports, and business insights.
        </div>

        <div class="toolkit-tools">

            <div class="toolkit-tag">
                Power BI
            </div>

            <div class="toolkit-tag">
                Looker Studio
            </div>

            <div class="toolkit-tag">
                Plotly
            </div>

            <div class="toolkit-tag">
                KPI Reporting
            </div>

        </div>

    </div>


    <!-- =================================================
         DEVELOPMENT
         ================================================= -->

    <div class="toolkit-card">

        <div class="toolkit-number">
            04 · DEVELOPMENT
        </div>

        <div class="toolkit-title">
            Development
        </div>

        <div class="toolkit-description">
            Build lightweight applications and data tools
            that turn analytical workflows into usable systems.
        </div>

        <div class="toolkit-tools">

            <div class="toolkit-tag">
                Streamlit
            </div>

            <div class="toolkit-tag">
                HTML / CSS
            </div>

            <div class="toolkit-tag">
                SQLAlchemy
            </div>

            <div class="toolkit-tag">
                Git
            </div>

        </div>

    </div>


    <!-- =================================================
         DATA ENGINEERING
         ================================================= -->

    <div class="toolkit-card toolkit-card-wide">

        <div class="toolkit-number">
            05 · DATA ENGINEERING
        </div>

        <div class="toolkit-title">
            ETL & Data Pipelines
        </div>

        <div class="toolkit-description">
            Build repeatable data workflows that move,
            clean, transform, and prepare information
            for reporting and analysis.
        </div>

        <div class="toolkit-tools">

            <div class="toolkit-tag">
                ETL
            </div>

            <div class="toolkit-tag">
                REST APIs
            </div>

            <div class="toolkit-tag">
                Google Sheets
            </div>

            <div class="toolkit-tag">
                MySQL
            </div>

            <div class="toolkit-tag">
                pandas
            </div>

        </div>

    </div>


</div>
""")

# =========================================================
# FINAL CTA / CONTACT
# =========================================================

st.html("""
<div id="contact" class="final-cta">

    <div class="final-cta-label">
        LET'S BUILD SOMETHING USEFUL
    </div>

    <div class="final-cta-title">
        Have a data or automation problem?
    </div>

    <div class="final-cta-description">
        Whether it's turning messy data into useful insights,
        automating a repetitive workflow, or building a
        better reporting system, I'd be happy to explore
        what we can build.
    </div>

    <div class="contact-buttons">

        <a
            class="contact-button primary"
            href="mailto:engrlorenzo22@gmail.com"
        >
            Email Me
        </a>

        <a
            class="contact-button"
            href="https://www.linkedin.com/in/reynaldo-lorenzo-62b755247/"
            target="_blank"
        >
            LinkedIn
        </a>

        <a
            class="contact-button"
            href="https://github.com/Reboyaks"
            target="_blank"
        >
            GitHub
        </a>

    </div>

</div>
""")



# =========================================================
# FOOTER
# =========================================================

st.html("""
<div class="final-footer">

    Built with Python & Streamlit · Reynaldo Lorenzo

</div>
""")

import streamlit as st


# ============================================================
# REYNALDO CHATKIT
# ============================================================

REYNALDO_CHATKIT_HTML = """
<div id="reynaldo-chat-root">

    <button id="reynaldo-chat-button" type="button">
        <span>✦</span>
        <span>Ask Reynaldo</span>
    </button>

    <div id="reynaldo-chat-window">

        <button
            id="reynaldo-chat-close"
            type="button"
            aria-label="Close chat"
        >
            ×
        </button>

        <iframe
            id="reynaldo-chat-iframe"
            src="https://reychatkit.netlify.app/?embed=1"
            title="Ask Reynaldo AI Assistant"
            allow="microphone; camera"
        ></iframe>

    </div>

</div>
"""


REYNALDO_CHATKIT_CSS = """

/* Component host */

/* ============================================================
   STREAMLIT COMPONENT BACKGROUND
   ============================================================ */

:host {
    display: block !important;

    background: transparent !important;

    border: none !important;

    box-shadow: none !important;

    margin: 0 !important;
    padding: 0 !important;
}

html,
body,
#root {
    margin: 0 !important;
    padding: 0 !important;

    width: 100% !important;
    height: 100% !important;

    background: transparent !important;

    border: none !important;

    box-shadow: none !important;
}

body {
    overflow: visible !important;
}

/* ============================================================
   CHAT BUTTON
   ============================================================ */

#reynaldo-chat-button {

    position: fixed;

    right: 24px;
    bottom: 24px;

    display: flex;
    align-items: center;
    gap: 9px;

    padding: 13px 18px;

    border: 1px solid rgba(139, 92, 246, 0.55);
    border-radius: 999px;

    background: #111318;

    color: white;

    font-family: Arial, sans-serif;
    font-size: 14px;
    font-weight: 600;

    cursor: pointer;

    z-index: 2147483647;

    box-shadow:
        0 10px 30px rgba(0, 0, 0, 0.35),
        0 0 20px rgba(139, 92, 246, 0.12);
}


/* ============================================================
   CHAT WINDOW
   ============================================================ */

#reynaldo-chat-window {

    display: none;

    position: fixed;

    right: 24px;
    bottom: 24px;

    width: 460px;
    height: 680px;

    margin: 0;
    padding: 0;

    background: transparent;

    border: none;

    box-shadow: none;

    overflow: visible;

    z-index: 2147483646;
}


/* ============================================================
   NETLIFY IFRAME
   ============================================================ */

#reynaldo-chat-iframe {

    position: absolute;

    left: 0;
    top: 0;

    width: 100%;
    height: 100%;

    border: none;

    display: block;

    background: transparent;

    border-radius: 22px;

    overflow: hidden;
}


/* ============================================================
   STREAMLIT CLOSE BUTTON
   ============================================================ */

#reynaldo-chat-close {

    position: absolute;

    top: 12px;
    right: 12px;

    width: 42px;
    height: 42px;

    display: flex;
    align-items: center;
    justify-content: center;

    border: 1px solid #30343d;
    border-radius: 50%;

    background: #171a20;

    color: white;

    font-size: 27px;
    line-height: 1;

    cursor: pointer;

    z-index: 2147483647;
}


/* ============================================================
   MOBILE
   ============================================================ */

@media (max-width: 600px) {

    #reynaldo-chat-window {

        right: 10px;
        bottom: 10px;

        width: calc(100vw - 20px);
        height: calc(100vh - 20px);
    }

}
"""


REYNALDO_CHATKIT_JS = """
export default function(component) {

    const root = component.parentElement;
    
    const wrapper = component.parentElement;

    wrapper.style.width = "0px";
    wrapper.style.height = "0px";
    wrapper.style.minWidth = "0px";
    wrapper.style.minHeight = "0px";
    wrapper.style.margin = "0";
    wrapper.style.padding = "0";
    wrapper.style.border = "none";
    wrapper.style.background = "transparent";
    wrapper.style.boxShadow = "none";
    wrapper.style.overflow = "visible";

    const button =
        root.querySelector("#reynaldo-chat-button");

    const windowBox =
        root.querySelector("#reynaldo-chat-window");

    const closeButton =
        root.querySelector("#reynaldo-chat-close");

    const iframe =
        root.querySelector("#reynaldo-chat-iframe");

    if (!button || !windowBox || !closeButton || !iframe) {
        console.error("Reynaldo ChatKit: elements missing");
        return;
    }

    button.addEventListener("click", () => {

        button.style.display = "none";
        windowBox.style.display = "block";

        iframe.contentWindow.postMessage(
            {
                source: "reynaldo-streamlit",
                type: "OPEN_CHAT"
            },
            "https://reychatkit.netlify.app"
        );
    });

    closeButton.addEventListener("click", () => {

        windowBox.style.display = "none";
        button.style.display = "flex";

        iframe.contentWindow.postMessage(
            {
                source: "reynaldo-streamlit",
                type: "CLOSE_CHAT"
            },
            "https://reychatkit.netlify.app"
        );
    });
}
"""


reynaldo_chatkit = st.components.v2.component(
    "reynaldo_chatkit",
    html=REYNALDO_CHATKIT_HTML,
    css=REYNALDO_CHATKIT_CSS,
    js=REYNALDO_CHATKIT_JS,
    isolate_styles=False,
)

reynaldo_chatkit(
    width=1,
    height=1,
)