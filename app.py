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
# CUSTOM CSS
# =========================================================

st.markdown("""
<style>

    /* ============================================================
   THEME VARIABLES
   ============================================================ */

:root {
    --bg: #0b0d0f;
    --surface: #111318;
    --surface-2: #171a20;
    --text: #ffffff;
    --muted: #8f96a3;
    --border: #292d35;
    --accent: #8b5cf6;
}


/* LIGHT MODE */

[data-theme="light"] {
    --bg: #f7f7f8;
    --surface: #ffffff;
    --surface-2: #f0f1f3;
    --text: #171717;
    --muted: #626873;
    --border: #dedfe3;
    --accent: #7c3aed;
}

    /* =====================================================
       GLOBAL
       ===================================================== */

    .stApp {
    background: var(--bg) !important;
    color: var(--text) !important;
}

    .block-container {
        max-width: 1120px;
        padding-top: 1rem;
        padding-bottom: 4rem;
    }

    #MainMenu {
        visibility: hidden;
    }

    header {
        visibility: hidden;
    }

    footer {
        visibility: hidden;
    }

    /* Remove default Streamlit spacing */
    [data-testid="stVerticalBlock"] {
        gap: 0.5rem;
    }


    /* =====================================================
       HERO
       ===================================================== */

    .hero {
        text-align: center;
        padding: 70px 20px 55px 20px;
    }

    .hero-label {
        color: #8b5cf6;
        font-size: 12px;
        font-weight: 600;
        letter-spacing: 3px;
        text-transform: uppercase;
        margin-bottom: 18px;
    }

    .hero-title {
        font-size: 64px;
        font-weight: 700;
        letter-spacing: -3px;
        line-height: 1.05;
        margin: 0;
    }

    .hero-title span {
        color: #8b5cf6;
    }

    .hero-subtitle {
        color: #c5cad3;
        font-size: 21px;
        margin-top: 20px;
        line-height: 1.5;
    }

    .hero-description {
        max-width: 680px;
        margin: 18px auto 0 auto;
        color: #8b949e;
        font-size: 15px;
        line-height: 1.7;
    }


    /* =====================================================
       SECTION
       ===================================================== */

    .section {
        margin-top: 72px;
        margin-bottom: 28px;
        scroll-margin-top: 90px;
    }

    .section-label {
        color: #8b5cf6;
        font-size: 11px;
        font-weight: 600;
        letter-spacing: 2px;
        text-transform: uppercase;
        margin-bottom: 7px;
    }

    .section-title {
        font-size: 30px;
        font-weight: 650;
        margin-bottom: 10px;
    }

    .section-description {
        color: #8b949e;
        font-size: 15px;
        line-height: 1.6;
        max-width: 760px;
    }


    /* =====================================================
       QUICK METRICS
       ===================================================== */

    .metric-box {
        text-align: center;
        padding: 18px 10px;
        min-height: 80px;
        box-sizing: border-box;
    }

    .metric-value {
        font-size: 25px;
        font-weight: 650;
    }

    .metric-label {
        color: #8b949e;
        font-size: 12px;
        margin-top: 5px;
    }


    /* =====================================================
       GENERAL CARD
       ===================================================== */

    .card {
        background: #111418;
        border: 1px solid #252a31;
        border-radius: 14px;
        padding: 26px;
        min-height: 235px;
        height: 235px;
        box-sizing: border-box;

        display: flex;
        flex-direction: column;

        transition:
            border-color 0.2s ease,
            transform 0.2s ease;
    }

    .card:hover {
        border-color: #8b5cf6;
        transform: translateY(-3px);
    }

    .card-number {
        color: #8b5cf6;
        font-size: 11px;
        font-weight: 600;
        letter-spacing: 1.5px;
    }

    .card-title {
        font-size: 20px;
        font-weight: 600;
        margin-top: 12px;
        margin-bottom: 10px;
    }

    .card-description {
        color: #8b949e;
        font-size: 14px;
        line-height: 1.65;
        flex-grow: 1;
    }

    .card-tools {
        color: #d1d5db;
        font-size: 12px;
        margin-top: auto;
        padding-top: 15px;
    }


    /* =====================================================
   PREMIUM INTERACTIVE FUNNEL
   ===================================================== */

.funnel-container {
    position: relative;

    max-width: 850px;

    margin: 32px auto 0 auto;

    padding: 10px 0 20px 0;
}


/* =====================================================
   FUNNEL CONNECTOR
   ===================================================== */

.funnel-arrow {
    position: relative;

    display: flex;
    justify-content: center;
    align-items: center;

    height: 24px;

    margin: 2px 0;

    color: #6d4bc1;

    font-size: 15px;

    line-height: 1;

    opacity: 0.8;
}

.funnel-arrow::before {
    content: "";

    position: absolute;

    top: 0;
    bottom: 0;

    left: 50%;

    width: 1px;

    background:
        linear-gradient(
            to bottom,
            transparent,
            #6d4bc1,
            transparent
        );

    transform: translateX(-50%);
}


/* =====================================================
   FUNNEL BUTTON
   ===================================================== */

.funnel-container div[data-testid="stButton"] {
    position: relative;

    z-index: 2;

    margin: 0;
}

.funnel-container div[data-testid="stButton"] > button {
    width: 100%;

    min-height: 58px;

    background: #111418;

    border: 1px solid #252a31;

    border-radius: 12px;

    color: #e5e7eb;

    font-size: 13px;

    font-weight: 600;

    letter-spacing: 0.2px;

    transition:
        border-color 0.2s ease,
        background 0.2s ease,
        transform 0.2s ease,
        box-shadow 0.2s ease;
}

.funnel-container div[data-testid="stButton"] > button:hover {
    border-color: #8b5cf6;

    background:
        linear-gradient(
            90deg,
            #111418,
            #171520,
            #111418
        );

    color: #ffffff;

    transform: translateY(-2px);

    box-shadow:
        0 8px 25px rgba(0, 0, 0, 0.20);
}

.funnel-container div[data-testid="stButton"] > button:focus {
    border-color: #8b5cf6;

    color: #ffffff;

    box-shadow:
        0 0 0 1px #8b5cf6,
        0 0 22px rgba(139, 92, 246, 0.12);
}


/* =====================================================
   DETAIL PANEL
   ===================================================== */

.funnel-detail {
    position: relative;

    max-width: 720px;

    margin: 28px auto 0 auto;

    background:
        linear-gradient(
            145deg,
            #111418,
            #13151b
        );

    border: 1px solid rgba(139, 92, 246, 0.42);

    border-radius: 15px;

    padding: 26px 30px;

    box-sizing: border-box;

    box-shadow:
        0 15px 40px rgba(0, 0, 0, 0.18);

    animation: funnelFade 0.25s ease;
}


/* Accent line */

.funnel-detail::before {
    content: "";

    position: absolute;

    top: 18px;
    bottom: 18px;

    left: 0;

    width: 2px;

    background: #8b5cf6;

    border-radius: 2px;
}


.funnel-detail-label {
    color: #8b5cf6;

    font-size: 10px;

    font-weight: 650;

    letter-spacing: 2px;

    text-transform: uppercase;

    margin-bottom: 7px;
}


.funnel-detail-title {
    color: #f5f5f5;

    font-size: 23px;

    font-weight: 650;

    letter-spacing: -0.3px;

    margin-bottom: 8px;
}


.funnel-detail-description {
    color: #9ca3af;

    font-size: 13px;

    line-height: 1.75;

    max-width: 650px;
}


/* =====================================================
   TOOL TAGS
   ===================================================== */

.funnel-tools {
    display: flex;

    flex-wrap: wrap;

    gap: 7px;

    margin-top: 17px;
}

.funnel-tool {
    background: #181b21;

    border: 1px solid #292e36;

    border-radius: 7px;

    padding: 6px 9px;

    color: #d1d5db;

    font-size: 10px;

    transition:
        border-color 0.2s ease,
        color 0.2s ease;
}

.funnel-tool:hover {
    border-color: #8b5cf6;

    color: #ffffff;
}


/* =====================================================
   BUSINESS OUTCOME
   ===================================================== */

.funnel-outcome {
    max-width: 560px;

    margin: 22px auto 0 auto;

    padding: 18px 22px;

    text-align: center;

    background: #0f1115;

    border: 1px dashed #30353d;

    border-radius: 12px;
}

.funnel-outcome-label {
    color: #8b5cf6;

    font-size: 9px;

    font-weight: 650;

    letter-spacing: 2px;

    text-transform: uppercase;

    margin-bottom: 7px;
}

.funnel-outcome-title {
    color: #e5e7eb;

    font-size: 14px;

    font-weight: 600;

    margin-bottom: 5px;
}

.funnel-outcome-text {
    color: #7f8792;

    font-size: 11px;

    line-height: 1.6;
}


/* =====================================================
   ANIMATION
   ===================================================== */

@keyframes funnelFade {

    from {
        opacity: 0;

        transform:
            translateY(6px);
    }

    to {
        opacity: 1;

        transform:
            translateY(0);
    }

}


/* =====================================================
   MOBILE
   ===================================================== */

@media (max-width: 700px) {

    .funnel-container {
        padding-left: 4px;
        padding-right: 4px;
    }

    .funnel-detail {
        padding: 23px 22px;
    }

    .funnel-detail-title {
        font-size: 21px;
    }

}


    /* =====================================================
       PROJECT CARDS
       ===================================================== */

    .project {
        background: #111418;
        border: 1px solid #252a31;
        border-radius: 14px;
        padding: 28px;

        height: 285px;
        min-height: 285px;

        box-sizing: border-box;

        display: flex;
        flex-direction: column;

        transition:
            border-color 0.2s ease,
            transform 0.2s ease;
    }

    .project:hover {
        border-color: #8b5cf6;
        transform: translateY(-3px);
    }

    .project-category {
        color: #8b5cf6;
        font-size: 11px;
        font-weight: 600;
        letter-spacing: 1.5px;
    }

    .project-title {
        font-size: 21px;
        font-weight: 600;
        margin-top: 10px;
        margin-bottom: 10px;
    }

    .project-description {
        color: #8b949e;
        font-size: 14px;
        line-height: 1.65;

        flex-grow: 1;
    }

    .project-stack {
        color: #d1d5db;
        font-size: 12px;

        margin-top: auto;
        padding-top: 15px;
    }
    
    /* =====================================================
   INTERACTIVE PROJECT SHOWCASE
   ===================================================== */

.project-selector {
    height: 230px;
    min-height: 230px;

    background: #111418;
    border: 1px solid #252a31;
    border-radius: 14px;

    padding: 25px;
    box-sizing: border-box;

    display: flex;
    flex-direction: column;

    transition:
        border-color 0.2s ease,
        transform 0.2s ease,
        background 0.2s ease;
}

.project-selector:hover {
    border-color: #8b5cf6;
    background: #151821;
    transform: translateY(-3px);
}

.project-selector.active {
    border-color: #8b5cf6;
    box-shadow: 0 0 0 1px #8b5cf6;
}

.project-selector-category {
    color: #8b5cf6;
    font-size: 11px;
    font-weight: 600;
    letter-spacing: 1.5px;
}

.project-selector-title {
    font-size: 20px;
    font-weight: 600;
    margin-top: 10px;
    margin-bottom: 10px;
}

.project-selector-description {
    color: #8b949e;
    font-size: 13px;
    line-height: 1.6;
    flex-grow: 1;
}

.project-selector-tools {
    color: #d1d5db;
    font-size: 11px;
    margin-top: auto;
    padding-top: 12px;
}


/* Project selector buttons */

.project-selector-button div[data-testid="stButton"] > button {
    width: 100%;
    height: 230px;

    background: transparent;
    border: none;

    padding: 0;

    color: transparent;

    position: absolute;
    top: 0;
    left: 0;

    z-index: 5;
}

.project-selector-button div[data-testid="stButton"] > button:hover {
    background: transparent;
    border: none;
}

.project-selector-button div[data-testid="stButton"] > button:focus {
    background: transparent;
    border: none;
    box-shadow: none;
}


/* =====================================================
   PROJECT CASE STUDY
   ===================================================== */

.project-detail {
    position: relative;

    margin-top: 24px;

    background:
        linear-gradient(
            145deg,
            #111418,
            #13151b
        );

    border: 1px solid rgba(139, 92, 246, 0.42);

    border-radius: 15px;

    padding: 30px;

    box-sizing: border-box;

    box-shadow:
        0 15px 40px rgba(0, 0, 0, 0.18);

    animation: projectFade 0.25s ease;
}


/* Purple accent */

.project-detail::before {
    content: "";

    position: absolute;

    top: 20px;
    bottom: 20px;
    left: 0;

    width: 2px;

    background: #8b5cf6;

    border-radius: 2px;
}


.project-detail-category {
    color: #8b5cf6;

    font-size: 10px;
    font-weight: 650;

    letter-spacing: 2px;

    text-transform: uppercase;
}


.project-detail-title {
    color: #f5f5f5;

    font-size: 28px;
    font-weight: 650;

    letter-spacing: -0.5px;

    margin-top: 8px;
    margin-bottom: 10px;
}


.project-detail-description {
    color: #9ca3af;

    font-size: 14px;
    line-height: 1.7;

    max-width: 780px;
}


/* =====================================================
   CHALLENGE / SOLUTION
   ===================================================== */

.project-case-grid {
    display: grid;

    grid-template-columns: 1fr 1fr;

    gap: 12px;

    margin-top: 24px;
}


.project-case-card {
    background: #0f1115;

    border: 1px solid #252a31;

    border-radius: 10px;

    padding: 18px;

    box-sizing: border-box;

    min-height: 145px;
}


.project-case-label {
    color: #8b5cf6;

    font-size: 9px;
    font-weight: 650;

    letter-spacing: 1.8px;

    text-transform: uppercase;

    margin-bottom: 9px;
}


.project-case-text {
    color: #8b949e;

    font-size: 12px;

    line-height: 1.7;
}


/* =====================================================
   WORKFLOW
   ===================================================== */

.project-detail-section {
    margin-top: 24px;
}


.project-detail-label {
    color: #f5f5f5;

    font-size: 10px;
    font-weight: 650;

    letter-spacing: 1.5px;

    text-transform: uppercase;

    margin-bottom: 10px;
}


.project-flow {
    display: flex;

    flex-wrap: wrap;

    align-items: center;

    gap: 7px;
}


.project-flow-step {
    background: #181b21;

    border: 1px solid #292e36;

    border-radius: 7px;

    padding: 7px 10px;

    color: #d1d5db;

    font-size: 11px;

    transition:
        border-color 0.2s ease,
        transform 0.2s ease;
}


.project-flow-step:hover {
    border-color: #8b5cf6;

    transform: translateY(-2px);
}


.project-flow-arrow {
    color: #6d4bc1;

    font-size: 12px;
}


/* =====================================================
   TECHNOLOGY
   ===================================================== */

.project-tools {
    display: flex;

    flex-wrap: wrap;

    gap: 7px;
}


.project-tool {
    background: #181b21;

    border: 1px solid #292e36;

    border-radius: 7px;

    padding: 6px 9px;

    color: #d1d5db;

    font-size: 10px;
}


/* =====================================================
   PROJECT IMPACT
   ===================================================== */

.project-impact {
    margin-top: 24px;

    padding: 17px 18px;

    background:
        linear-gradient(
            90deg,
            rgba(139, 92, 246, 0.07),
            transparent
        );

    border: 1px solid #252a31;

    border-radius: 10px;
}


.project-impact-label {
    color: #8b5cf6;

    font-size: 9px;
    font-weight: 650;

    letter-spacing: 1.8px;

    text-transform: uppercase;

    margin-bottom: 7px;
}


.project-impact-text {
    color: #d1d5db;

    font-size: 12px;

    line-height: 1.65;
}


/* =====================================================
   MOBILE
   ===================================================== */

@media (max-width: 700px) {

    .project-case-grid {
        grid-template-columns: 1fr;
    }

    .project-detail {
        padding: 24px 22px;
    }

    .project-detail-title {
        font-size: 24px;
    }

    .project-flow {
        gap: 6px;
    }

}


/* =====================================================
ABOUT + EXPERIENCE
===================================================== */

.about-profile {
    background: #111418;
    border: 1px solid #252a31;
    border-radius: 14px;

    height: 430px;
    min-height: 430px;

    padding: 30px;
    box-sizing: border-box;

    display: flex;
    flex-direction: column;

    transition:
        border-color 0.2s ease,
        transform 0.2s ease;
}

.about-profile:hover {
    border-color: #8b5cf6;
    transform: translateY(-3px);
}

.about-profile-label {
    color: #8b5cf6;
    font-size: 11px;
    font-weight: 600;
    letter-spacing: 2px;
    text-transform: uppercase;
}

.about-profile-title {
    font-size: 26px;
    font-weight: 650;

    margin-top: 12px;
    margin-bottom: 15px;

    line-height: 1.2;
}

.about-profile-text {
    color: #9ca3af;

    font-size: 14px;
    line-height: 1.75;

    /* Don't force this area to stretch */
    flex-grow: 0;
}

.about-highlight {
    border-left: 2px solid #8b5cf6;

    padding-left: 14px;
    margin-top: auto;

    color: #d1d5db;

    font-size: 13px;
    line-height: 1.6;
}


/* =====================================================
   EXPERIENCE
   ===================================================== */

.experience-container {
    background: #111418;
    border: 1px solid #252a31;
    border-radius: 14px;

    height: 430px;
    min-height: 430px;

    padding: 30px;
    box-sizing: border-box;

    display: flex;
    flex-direction: column;

    transition:
        border-color 0.2s ease,
        transform 0.2s ease;
}

.experience-container:hover {
    border-color: #8b5cf6;
    transform: translateY(-3px);
}

.experience-label {
    color: #8b5cf6;
    font-size: 11px;
    font-weight: 600;
    letter-spacing: 2px;
    text-transform: uppercase;
    margin-bottom: 20px;
}

.experience-item {
    position: relative;
    padding-left: 22px;
    padding-bottom: 22px;
    border-left: 1px solid #30353d;
}

.experience-item:last-of-type {
    padding-bottom: 0;
}

.experience-dot {
    position: absolute;

    width: 8px;
    height: 8px;

    background: #8b5cf6;
    border-radius: 50%;

    left: -4px;
    top: 5px;

    box-shadow: 0 0 0 4px #111418;
}

.experience-role {
    font-size: 16px;
    font-weight: 600;
    margin-bottom: 3px;
}

.experience-company {
    color: #8b5cf6;
    font-size: 12px;
    font-weight: 600;
    margin-bottom: 5px;
}

.experience-period {
    color: #6b7280;
    font-size: 11px;
    margin-bottom: 9px;
}

.experience-description {
    color: #8b949e;
    font-size: 13px;
    line-height: 1.6;
}

.experience-content {
    padding-top: 2px;
}

.resume-caption {
    color: #8b949e;
    font-size: 12px;
    padding-top: 8px;
}

.resume-area {
    margin-top: auto;
    padding-top: 16px;

    border-top: 1px solid #252a31;
}

/* =====================================================
   RESUME
   ===================================================== */

.resume-row {
    margin-top: auto;
    padding-top: 16px;

    border-top: 1px solid #252a31;

    display: flex;
    align-items: center;
    justify-content: space-between;
    gap: 15px;
}

.resume-text {
    color: #8b949e;
    font-size: 12px;
}

/* Mobile */

@media (max-width: 700px) {

    .about-profile,
    .experience-container {
        height: auto;
        min-height: 0;
    }

    .about-profile {
        margin-bottom: 15px;
    }

}


    /* =====================================================
       TOOL / STACK BOXES
       ===================================================== */

    .tool-box {
        background: #111418;
        border: 1px solid #252a31;
        border-radius: 12px;

        height: 95px;
        min-height: 95px;

        padding: 18px;
        box-sizing: border-box;

        display: flex;
        align-items: center;
        justify-content: center;

        text-align: center;

        transition:
            border-color 0.2s ease,
            transform 0.2s ease;
    }

    .tool-box:hover {
        border-color: #8b5cf6;
        transform: translateY(-2px);
    }

    .tool-name {
        font-size: 15px;
        font-weight: 550;
    }


    /* =====================================================
       CTA
       ===================================================== */

    .cta {
        background: #111418;
        border: 1px solid #252a31;
        border-radius: 16px;

        text-align: center;

        padding: 45px 25px;

        margin-top: 60px;

        transition:
            border-color 0.2s ease;
    }

    .cta:hover {
        border-color: #8b5cf6;
    }

    .cta-title {
        font-size: 28px;
        font-weight: 650;
        margin-bottom: 10px;
    }

    .cta-description {
        color: #8b949e;
        font-size: 15px;
    }


    /* =====================================================
       FOOTER
       ===================================================== */

    .footer {
        text-align: center;
        color: #6b7280;
        font-size: 12px;

        border-top: 1px solid #252a31;

        margin-top: 60px;
        padding-top: 25px;
    }
    
    /* =====================================================
   INTERACTIVE FUNNEL
   ===================================================== */

.funnel-container {
    max-width: 820px;
    margin: 30px auto 0 auto;
}

.funnel-row {
    margin-bottom: 0.15rem;
}

.funnel-arrow {
    text-align: center;
    color: #8b5cf6;
    font-size: 18px;
    line-height: 1;
    margin: 3px 0;
}

.funnel-detail {
    max-width: 720px;
    margin: 25px auto 0 auto;

    background: #111418;
    border: 1px solid #8b5cf6;
    border-radius: 14px;

    padding: 24px 28px;

    box-sizing: border-box;

    animation: funnelFade 0.25s ease;
}

.funnel-detail-label {
    color: #8b5cf6;
    font-size: 11px;
    font-weight: 600;
    letter-spacing: 2px;
    text-transform: uppercase;
    margin-bottom: 8px;
}

.funnel-detail-title {
    font-size: 22px;
    font-weight: 650;
    margin-bottom: 8px;
}

.funnel-detail-description {
    color: #9ca3af;
    font-size: 14px;
    line-height: 1.7;
}

.funnel-tools {
    display: flex;
    flex-wrap: wrap;
    gap: 8px;
    margin-top: 17px;
}

.funnel-tool {
    background: #181b21;
    border: 1px solid #252a31;
    border-radius: 7px;

    padding: 7px 11px;

    color: #d1d5db;
    font-size: 12px;
}

@keyframes funnelFade {
    from {
        opacity: 0;
        transform: translateY(5px);
    }

    to {
        opacity: 1;
        transform: translateY(0);
    }
}


/* Funnel buttons */

.funnel-container div[data-testid="stButton"] > button {
    width: 100%;
    min-height: 58px;

    background: #111418;
    border: 1px solid #252a31;
    border-radius: 12px;

    color: #f5f5f5;

    font-size: 15px;
    font-weight: 600;

    transition:
        border-color 0.2s ease,
        background 0.2s ease,
        transform 0.2s ease;
}

.funnel-container div[data-testid="stButton"] > button:hover {
    border-color: #8b5cf6;
    background: #151821;
    color: #ffffff;

    transform: translateY(-2px);
}

.funnel-container div[data-testid="stButton"] > button:focus {
    border-color: #8b5cf6;
    box-shadow: 0 0 0 1px #8b5cf6;
}


    /* =====================================================
       MOBILE
       ===================================================== */

    @media (max-width: 700px) {

        .hero {
            padding-top: 45px;
        }

        .hero-title {
            font-size: 42px;
            letter-spacing: -2px;
        }

        .hero-subtitle {
            font-size: 18px;
        }

        .section-title {
            font-size: 26px;
        }

        .card {
            height: auto;
            min-height: 235px;
        }

        .project {
            height: auto;
            min-height: 270px;
        }

        .about-box {
            height: auto;
            min-height: 280px;
        }

        .funnel-1,
        .funnel-2,
        .funnel-3,
        .funnel-4,
        .funnel-5 {
            width: 100%;
        }

    }
    
/* =====================================================
   TOOLKIT / SKILLS
   ===================================================== */

.toolkit-grid {
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    gap: 14px;
    margin-top: 28px;
}

.toolkit-card {
    background: #111418;
    border: 1px solid #252a31;
    border-radius: 14px;

    height: 175px;
    min-height: 175px;

    padding: 24px;
    box-sizing: border-box;

    display: flex;
    flex-direction: column;

    transition:
        border-color 0.2s ease,
        transform 0.2s ease,
        background 0.2s ease;
}

.toolkit-card:hover {
    border-color: #8b5cf6;
    background: #151821;
    transform: translateY(-3px);
}

.toolkit-number {
    color: #8b5cf6;

    font-size: 10px;
    font-weight: 600;

    letter-spacing: 1.8px;
    text-transform: uppercase;
}

.toolkit-title {
    font-size: 18px;
    font-weight: 600;

    margin-top: 9px;
    margin-bottom: 7px;
}

.toolkit-description {
    color: #8b949e;

    font-size: 12px;
    line-height: 1.55;

    flex-grow: 1;
}

.toolkit-tools {
    display: flex;
    flex-wrap: wrap;
    gap: 6px;

    margin-top: 12px;
}

.toolkit-tag {
    background: #181b21;
    border: 1px solid #252a31;
    border-radius: 6px;

    padding: 5px 8px;

    color: #d1d5db;

    font-size: 10px;
}


/* Full-width final card */

.toolkit-card-wide {
    grid-column: 1 / -1;
}


/* Mobile */

@media (max-width: 700px) {

    .toolkit-grid {
        grid-template-columns: 1fr;
    }

    .toolkit-card-wide {
        grid-column: auto;
    }

    .toolkit-card {
        height: auto;
        min-height: 175px;
    }

}

/* =====================================================
   FINAL CTA / CONTACT
   ===================================================== */

.final-cta {
    position: relative;

    background: #111418;
    border: 1px solid #252a31;
    border-radius: 18px;

    padding: 55px 45px;

    margin-top: 70px;

    text-align: center;

    overflow: hidden;

    transition:
        border-color 0.25s ease,
        transform 0.25s ease;
}

.final-cta:hover {
    border-color: #8b5cf6;
    transform: translateY(-2px);
}


/* Subtle glow */

.final-cta::before {
    content: "";

    position: absolute;

    width: 260px;
    height: 260px;

    background: #8b5cf6;

    opacity: 0.055;

    border-radius: 50%;

    top: -150px;
    left: 50%;

    transform: translateX(-50%);

    filter: blur(40px);

    pointer-events: none;
}


.final-cta-label {
    position: relative;

    color: #8b5cf6;

    font-size: 11px;
    font-weight: 600;

    letter-spacing: 2.5px;
    text-transform: uppercase;
}


.final-cta-title {
    position: relative;

    font-size: 34px;
    font-weight: 650;

    letter-spacing: -1px;

    margin-top: 12px;
    margin-bottom: 12px;
}


.final-cta-description {
    position: relative;

    max-width: 600px;

    margin: 0 auto;

    color: #8b949e;

    font-size: 15px;
    line-height: 1.7;
}


/* Contact buttons */

.contact-buttons {
    position: relative;

    display: flex;

    justify-content: center;
    align-items: center;

    flex-wrap: wrap;

    gap: 10px;

    margin-top: 25px;
}


.contact-button {
    display: inline-flex;

    align-items: center;
    justify-content: center;

    min-width: 130px;

    padding: 10px 17px;

    border-radius: 8px;

    border: 1px solid #30353d;

    background: #181b21;

    color: #d1d5db;

    font-size: 12px;
    font-weight: 500;

    text-decoration: none;

    transition:
        border-color 0.2s ease,
        background 0.2s ease,
        color 0.2s ease,
        transform 0.2s ease;
}


.contact-button:hover {
    border-color: #8b5cf6;

    background: #1b1d25;

    color: #ffffff;

    transform: translateY(-2px);
}


.contact-button.primary {
    background: #8b5cf6;

    border-color: #8b5cf6;

    color: #ffffff;
}


.contact-button.primary:hover {
    background: #7c4fe0;

    border-color: #7c4fe0;
}


/* Footer */

.final-footer {
    text-align: center;

    color: #6b7280;

    font-size: 11px;

    margin-top: 35px;
    padding-bottom: 20px;
}


/* Mobile */

@media (max-width: 700px) {

    .final-cta {
        padding: 40px 22px;
    }

    .final-cta-title {
        font-size: 28px;
    }

    .contact-buttons {
        flex-direction: column;
    }

    .contact-button {
        width: 100%;
        max-width: 220px;
    }

}

/* =====================================================
   PREMIUM NAVIGATION
   ===================================================== */

/* =====================================================
   FIXED NAVIGATION
   ===================================================== */

.top-nav {
    position: fixed;

    top: 14px;
    left: 50%;

    transform: translateX(-50%);

    z-index: 999999;

    width: min(1080px, calc(100% - 32px));

    display: flex;
    align-items: center;
    justify-content: space-between;

    padding: 10px 14px;

    box-sizing: border-box;

    background: rgba(11, 13, 16, 0.88);

    border: 1px solid rgba(139, 92, 246, 0.20);

    border-radius: 13px;

    backdrop-filter: blur(16px);
    -webkit-backdrop-filter: blur(16px);

    box-shadow:
        0 10px 35px rgba(0, 0, 0, 0.30);
}


/* Brand */

.nav-brand {
    color: #f5f5f5;

    font-size: 12px;
    font-weight: 650;

    letter-spacing: 1.2px;

    text-decoration: none;

    white-space: nowrap;
}

.nav-brand span {
    color: #8b5cf6;
}


/* Navigation links */

.nav-links {
    display: flex;

    align-items: center;

    gap: 4px;
}

.nav-link {
    color: #8b949e;

    font-size: 11px;
    font-weight: 500;

    text-decoration: none;

    padding: 7px 11px;

    border-radius: 7px;

    transition:
        color 0.2s ease,
        background 0.2s ease;
}

.nav-link:hover {
    color: #ffffff;

    background: #181b21;
}

.nav-link.contact {
    color: #ffffff;

    background: #8b5cf6;
}

.nav-link.contact:hover {
    background: #7c4fe0;
}


/* =====================================================
   MOBILE
   ===================================================== */

@media (max-width: 700px) {

    .top-nav {

        top: 8px;

        width: calc(100% - 16px);

        padding: 9px 10px;

    }

    .nav-brand {
        font-size: 10px;
    }

    .nav-links {
        gap: 1px;
    }

    .nav-link {
        font-size: 9px;
        padding: 6px 6px;
    }

    .nav-link:nth-child(1),
    .nav-link:nth-child(2) {
        display: none;
    }

}

/* =====================================================
   MOBILE NAV
   ===================================================== */

@media (max-width: 700px) {

    .top-nav {
        padding: 10px 12px;
    }

    .nav-brand {
        font-size: 10px;
    }

    .nav-links {
        gap: 2px;
    }

    .nav-link {
        font-size: 10px;
        padding: 6px 7px;
    }

    .nav-link:nth-child(1),
    .nav-link:nth-child(2) {
        display: none;
    }

}

/* =====================================================
   PREMIUM HERO
   ===================================================== */

.hero {
    position: relative;

    text-align: center;

    padding: 115px 20px 65px 20px;

    overflow: hidden;
}


/* Ambient glow */

.hero::before {
    content: "";

    position: absolute;

    width: 420px;
    height: 420px;

    top: -250px;
    left: 50%;

    transform: translateX(-50%);

    background: #8b5cf6;

    opacity: 0.055;

    border-radius: 50%;

    filter: blur(70px);

    pointer-events: none;
}


/* Status */

.hero-status {
    position: relative;

    display: inline-flex;

    align-items: center;

    gap: 7px;

    padding: 6px 11px;

    margin-bottom: 20px;

    background: #111418;

    border: 1px solid #252a31;

    border-radius: 999px;

    color: #9ca3af;

    font-size: 10px;
    font-weight: 500;

    letter-spacing: 0.4px;
}

.hero-status-dot {
    width: 6px;
    height: 6px;

    border-radius: 50%;

    background: #8b5cf6;

    box-shadow: 0 0 8px rgba(139, 92, 246, 0.7);
}


/* Label */

.hero-label {
    position: relative;

    color: #8b5cf6;

    font-size: 11px;
    font-weight: 600;

    letter-spacing: 3px;

    text-transform: uppercase;

    margin-bottom: 15px;
}


/* Main title */

.hero-title {
    position: relative;

    font-size: clamp(48px, 7vw, 78px);

    font-weight: 750;

    letter-spacing: -4px;

    line-height: 0.98;

    margin: 0;

    color: #f5f5f5;
}

.hero-title span {
    color: #8b5cf6;
}


/* Subtitle */

.hero-subtitle {
    position: relative;

    max-width: 680px;

    margin: 22px auto 0 auto;

    color: #c5cad3;

    font-size: 22px;

    line-height: 1.45;

    font-weight: 450;
}


/* Description */

.hero-description {
    position: relative;

    max-width: 620px;

    margin: 15px auto 0 auto;

    color: #8b949e;

    font-size: 14px;

    line-height: 1.7;
}


/* Skill tags */

.hero-tags {
    position: relative;

    display: flex;

    justify-content: center;

    align-items: center;

    flex-wrap: wrap;

    gap: 7px;

    margin-top: 22px;
}

.hero-tag {
    padding: 6px 10px;

    background: #111418;

    border: 1px solid #252a31;

    border-radius: 7px;

    color: #b8bec8;

    font-size: 10px;

    transition:
        border-color 0.2s ease,
        color 0.2s ease,
        transform 0.2s ease;
}

.hero-tag:hover {
    border-color: #8b5cf6;

    color: #ffffff;

    transform: translateY(-2px);
}


/* Hero buttons */

.hero-actions {
    position: relative;

    display: flex;

    justify-content: center;

    align-items: center;

    flex-wrap: wrap;

    gap: 10px;

    margin-top: 28px;
}

.hero-button {
    display: inline-flex;

    align-items: center;
    justify-content: center;

    min-width: 135px;

    padding: 10px 17px;

    border-radius: 8px;

    border: 1px solid #30353d;

    background: #111418;

    color: #d1d5db;

    font-size: 12px;
    font-weight: 550;

    text-decoration: none;

    transition:
        border-color 0.2s ease,
        background 0.2s ease,
        color 0.2s ease,
        transform 0.2s ease;
}

.hero-button:hover {
    border-color: #8b5cf6;

    background: #181b21;

    color: #ffffff;

    transform: translateY(-2px);
}

.hero-button.primary {
    background: #8b5cf6;

    border-color: #8b5cf6;

    color: #ffffff;
}

.hero-button.primary:hover {
    background: #7c4fe0;

    border-color: #7c4fe0;
}


/* Hero divider */

.hero-divider {
    position: relative;

    width: 70px;

    height: 1px;

    margin: 38px auto 0 auto;

    background: #252a31;
}


/* Mobile */

@media (max-width: 700px) {

    .hero {
        padding: 105px 15px 50px 15px;
    }

    .hero-title {
        font-size: 47px;

        letter-spacing: -2.5px;
    }

    .hero-subtitle {
        font-size: 18px;
    }

    .hero-description {
        font-size: 13px;
    }

    .hero-actions {
        flex-direction: column;
    }

    .hero-button {
        width: 210px;
    }

}

/* =====================================================
   PRODUCTION RESPONSIVE CLEANUP
   ===================================================== */

* {
    box-sizing: border-box;
}

html {
    scroll-behavior: smooth;
    scroll-padding-top: 110px;
}

body {
    overflow-x: hidden;
}


/* Prevent Streamlit content from becoming too wide */

.block-container {
    max-width: 1180px !important;

    padding-left: 24px !important;
    padding-right: 24px !important;
}


/* Remove excessive Streamlit spacing */

div[data-testid="stVerticalBlock"] {
    gap: 0.4rem;
}


/* =====================================================
   TABLET
   ===================================================== */

@media (max-width: 900px) {

    .block-container {
        padding-left: 18px !important;
        padding-right: 18px !important;
    }

    .project-case-grid {
        grid-template-columns: 1fr;
    }

}


/* =====================================================
   MOBILE
   ===================================================== */

@media (max-width: 700px) {

    .block-container {
        padding-left: 12px !important;
        padding-right: 12px !important;
    }

    .section {
        margin-top: 55px;
    }

    .toolkit-grid {
        grid-template-columns: 1fr;
    }

    .project-case-grid {
        grid-template-columns: 1fr;
    }

    .about-profile,
    .experience-container {
        height: auto;
        min-height: 0;
    }

    .funnel-detail {
        margin-left: 4px;
        margin-right: 4px;
    }

    .project-detail {
        margin-left: 2px;
        margin-right: 2px;
    }

}

/* =====================================================
   STREAMLIT UI CLEANUP
   ===================================================== */

/* Hide default menu */

#MainMenu {
    visibility: hidden;
}


/* Hide footer */

footer {
    visibility: hidden;
}


/* Hide header */

header[data-testid="stHeader"] {
    background: transparent;
}


/* Remove top decoration */

[data-testid="stDecoration"] {
    display: none;
}


/* Make buttons consistent */

button {
    font-family: inherit !important;
}


/* Download button */

div[data-testid="stDownloadButton"] > button {
    border-radius: 8px !important;

    font-size: 11px !important;
    font-weight: 600 !important;

    background: #8b5cf6 !important;

    border: 1px solid #8b5cf6 !important;

    color: white !important;

    transition:
        background 0.2s ease,
        transform 0.2s ease,
        box-shadow 0.2s ease;
}

div[data-testid="stDownloadButton"] > button:hover {
    background: #7c4fe0 !important;

    border-color: #7c4fe0 !important;

    transform: translateY(-2px);

    box-shadow:
        0 7px 20px rgba(139, 92, 246, 0.20);
}

/* =====================================================
   PROJECT INTERACTION
   ===================================================== */

.project-selector {
    cursor: pointer;
}

.project-selector::after {
    content: "VIEW PROJECT →";

    display: block;

    margin-top: 10px;

    color: #6d4bc1;

    font-size: 9px;
    font-weight: 600;

    letter-spacing: 1px;

    opacity: 0;

    transform: translateY(3px);

    transition:
        opacity 0.2s ease,
        transform 0.2s ease;
}

.project-selector:hover::after {
    opacity: 1;

    transform: translateY(0);
}

/* =====================================================
   FUNNEL INTERACTION
   ===================================================== */

.funnel-container
div[data-testid="stButton"] > button {
    cursor: pointer;
}

.funnel-container
div[data-testid="stButton"] > button::after {
    content: "  →";

    color: #6d4bc1;

    transition:
        color 0.2s ease;
}

.funnel-container
div[data-testid="stButton"] > button:hover::after {
    color: #8b5cf6;
}

/* =====================================================
   SUBTLE SECTION ANIMATION
   ===================================================== */

.section {
    animation: sectionReveal 0.55s ease both;
}

@keyframes sectionReveal {

    from {
        opacity: 0;

        transform: translateY(8px);
    }

    to {
        opacity: 1;

        transform: translateY(0);
    }

}

/* =====================================================
   YOUTUBE PROJECT DEMO
   ===================================================== */

.project-demo {
    margin-top: 24px;
}

.project-demo-button {
    display: inline-flex;
    align-items: center;
    justify-content: center;

    gap: 8px;

    padding: 10px 15px;

    background: #181b21;

    border: 1px solid #30353d;

    border-radius: 8px;

    color: #d1d5db;

    font-size: 11px;
    font-weight: 600;

    text-decoration: none;

    transition:
        border-color 0.2s ease,
        background 0.2s ease,
        color 0.2s ease,
        transform 0.2s ease;
}

.project-demo-button:hover {
    border-color: #8b5cf6;

    background: #1b1d25;

    color: #ffffff;

    transform: translateY(-2px);
}

.project-demo-icon {
    color: #8b5cf6;

    font-size: 13px;
}

</style>
""", unsafe_allow_html=True)
#CSS END

# =========================================================
# TOP NAVIGATION
# =========================================================

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

def funnel_button(stage, width):

    total_width = 14
    side_width = (total_width - width) / 2

    cols = st.columns(
        [side_width, width, side_width]
    )

    with cols[1]:

        if st.button(
            f"{funnel_data[stage]['number']}  ·  {stage}",
            key=f"funnel_{stage}",
            use_container_width=True
        ):
            st.session_state.selected_funnel = stage
            
# =========================================================
# FUNNEL
# =========================================================

st.markdown(
    '<div class="funnel-container">',
    unsafe_allow_html=True
)


funnel_button("Understand", 12)

st.html("""
<div class="funnel-arrow">↓</div>
""")

funnel_button("Collect", 10)

st.html("""
<div class="funnel-arrow">↓</div>
""")

funnel_button("Transform", 8)

st.html("""
<div class="funnel-arrow">↓</div>
""")

funnel_button("Automate", 10)

st.html("""
<div class="funnel-arrow">↓</div>
""")

funnel_button("Visualize", 12)


# =========================================================
# FUNNEL DETAILS
# =========================================================

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

st.html("""
<div class="funnel-outcome">

    <div class="funnel-outcome-label">
        BUSINESS OUTCOME
    </div>

    <div class="funnel-outcome-title">
        Better decisions. Less manual work.
    </div>

    <div class="funnel-outcome-text">
        The goal isn't just cleaner data or better dashboards.
        It's creating systems that make the business easier
        to understand, operate, and improve.
    </div>

</div>
""")


st.markdown(
    '</div>',
    unsafe_allow_html=True
)

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

col1, col2, col3 = st.columns(3)


for index, project_name in enumerate(projects):

    data = project_data[project_name]

    if index == 0:
        column = col1

    elif index == 1:
        column = col2

    else:
        column = col3


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