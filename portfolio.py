import streamlit as st
import plotly.graph_objects as go
from pathlib import Path

# --- PAGE SETUP ---
st.set_page_config(
    page_title="Nayabb Fatima | Principal AI Engineer",
    page_icon="👩‍💻",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# --- INJECT CUSTOM CSS ---
def local_css(file_name):
    try:
        with open(file_name) as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
    except FileNotFoundError:
        css_path = Path(file_name)
        css_path.touch()
        st.markdown(f"<style>{css_path.read_text()}</style>", unsafe_allow_html=True)

css_file = "style.css"
css_content = """
:root {
    --primary-bg: #F8F9FA;
    --secondary-bg: #FFFFFF;
    --text-color: #495057;
    --header-text-color: #212529;
    --accent-color: #4C6EF5;
    --border-color: #DEE2E6;
}

/* Base Styles */
body, .stApp {
    color: var(--text-color);
    background-color: var(--primary-bg);
}

h1, h2, h3, h4, h5, h6 {
    color: var(--header-text-color) !important;
    font-weight: 700 !important;
}

h1 {
    font-size: 3.5rem !important;
    text-align: center;
    padding-top: 2rem;
}

h2 {
    font-size: 2.25rem !important;
    padding-bottom: 1rem;
    border-bottom: 3px solid var(--border-color);
    margin-top: 3rem;
    margin-bottom: 2rem;
}

h3 {
    font-size: 1.5rem !important;
    color: var(--header-text-color) !important;
    font-weight: 600 !important;
}

/* Main Content Layout */
.main-container {
    max-width: 1100px;
    margin: auto;
    padding: 0 2rem;
}

/* Custom Navigation */
.nav-container {
    display: flex;
    justify-content: center;
    align-items: center;
    padding: 1rem 0;
    border-bottom: 1px solid var(--border-color);
    background-color: var(--primary-bg);
    margin-bottom: 2rem;
}

.nav-button {
    background-color: transparent;
    border: none;
    color: var(--text-color);
    padding: 0.75rem 1.5rem;
    text-align: center;
    text-decoration: none;
    display: inline-block;
    font-size: 1rem;
    font-weight: 600;
    margin: 0 0.5rem;
    cursor: pointer;
    border-radius: 0.5rem;
    transition: all 0.3s ease;
}

.nav-button:hover {
    background-color: #E9ECEF;
    color: var(--header-text-color);
}

.nav-button.active {
    background-color: var(--accent-color);
    color: white;
}


/* Skills Section */
.skill-card {
    background-color: var(--secondary-bg);
    padding: 2rem;
    border-radius: 0.75rem;
    border: 1px solid var(--border-color);
    height: 100%;
}
.skill-card h3 {
    margin-bottom: 1.5rem;
    color: var(--accent-color);
}
.skill-list {
    display: flex;
    flex-wrap: wrap;
    gap: 0.75rem;
}
.skill-tag {
    background-color: #E9ECEF;
    color: var(--text-color);
    padding: 0.5rem 1rem;
    border-radius: 0.5rem;
    font-size: 0.9rem;
    font-weight: 500;
}

/* Experience Timeline */
.timeline-item {
    padding: 0 0 3rem 2rem;
    border-left: 2px solid var(--border-color);
    position: relative;
}
.timeline-item:last-child {
    padding-bottom: 0.5rem;
}
.timeline-item::before {
    content: '';
    position: absolute;
    left: -11px;
    top: 5px;
    width: 20px;
    height: 20px;
    border-radius: 50%;
    background-color: var(--secondary-bg);
    border: 4px solid var(--accent-color);
}
.timeline-item p i {
    color: #6C757D;
}
.timeline-item ul {
    margin-left: 1.25rem;
    list-style-type: disc;
    padding-top: 0.5rem;
}

/* Project Cards */
.project-card {
    background-color: var(--secondary-bg);
    border: 1px solid var(--border-color);
    border-radius: 0.75rem;
    padding: 1.5rem;
    height: 100%;
    display: flex;
    flex-direction: column;
    transition: all 0.3s ease;
    box-shadow: 0 4px 6px rgba(0,0,0,0.04);
}
.project-card:hover {
    transform: translateY(-5px);
    box-shadow: 0 10px 20px rgba(0,0,0,0.07);
    border-color: var(--accent-color);
}
.project-card a { text-decoration: none; }
.project-card h3 {
    transition: color 0.3s ease;
}
.project-card:hover h3 { color: var(--accent-color); }
.project-card .tag-container {
    margin-top: auto;
    padding-top: 1rem;
    display: flex;
    flex-wrap: wrap;
    gap: 0.5rem;
}
.project-card .tag {
    background-color: #E9ECEF;
    color: #495057;
    font-weight: 500;
    padding: 4px 10px;
    border-radius: 15px;
    font-size: 0.75rem;
}
"""
try:
    with open(css_file, "w") as f:
        f.write(css_content)
except Exception as e:
    st.error(f"Error writing CSS file: {e}")

local_css(css_file)

# --- DATA ---
SKILLS = {
    "Generative AI & LLMs": [
        'LLM Fine-Tuning (PEFT, TRL)', 'RAG Systems', 'Multi-Agent Systems', 'Prompt Engineering', 'LangChain', 'Hugging Face'
    ],
    "Computer Vision & Medical AI": [
        'Deep Learning (CNNs, Transformers)', 'Image Segmentation', 'Object Detection', 'Medical Image Analysis', 'PyTorch', 'TensorFlow'
    ],
    "MLOps & Systems": [
        'ML Pipelines', 'Model Deployment', 'API Development (FastAPI)', 'Docker', 'PostgreSQL', 'AWS Basics'
    ],
    "Core Programming & Data Science": [
        'Python', 'SQL', 'Data Modeling', 'Predictive Modeling', 'Scikit-learn', 'Algorithm Design'
    ]
}

PROJECTS = {
    "Email Agent System": {
        "desc": "Architected a multi-agent RAG system capable of parsing, understanding, and automating actions based on incoming email content, significantly reducing manual processing time.",
        "tags": ["LLM / RAG", "Python", "LangChain", "Automation"],
        "url": "https://github.com/Nayab-zak/email_agent_system"
    },
    "Qwen2.5 VLM Fine-tuning": {
        "desc": "Developed a modular and reusable pipeline for fine-tuning Vision-Language Models on domain-specific datasets, enabling nuanced multimodal understanding for specialized tasks.",
        "tags": ["Multimodal AI", "Fine-Tuning", "PyTorch", "Pipelines"],
        "url": "https://github.com/Nayab-zak/VLM_fine_tuning"
    },
    "On-Prem RAG Chatbot": {
        "desc": "Built and deployed a secure, on-premise RAG system integrating web search and image generation to provide comprehensive, context-aware answers from internal knowledge bases.",
        "tags": ["LLM / RAG", "Docker", "FastAPI", "Enterprise AI"],
        "url": "https://github.com/Nayab-zak/onprem_rag_chatbot"
    },
    "Predictive Modeling & API": {
        "desc": "Engineered a predictive model for cryptocurrency token pricing and exposed it via a high-performance FastAPI endpoint for real-time inference.",
        "tags": ["Predictive Modeling", "Backend", "API", "FastAPI"],
        "url": "https://github.com/Nayab-zak/gate_token_prediction"
    },
    "MCP Postgres Server": {
        "desc": "Designed and implemented a robust PostgreSQL server architecture optimized for high-availability and performance for mission-critical applications.",
        "tags": ["Backend", "Database", "SQL", "Systems Design"],
        "url": "https://github.com/Nayab-zak/mcp-postgres-server"
    },
    "Retinal Blood Leakage Detection": {
        "desc": "Created a novel hybrid machine learning model for the automated detection and classification of microaneurysms in retinal fundus images, aiding in early diabetic retinopathy diagnosis.",
        "tags": ["Medical AI", "Computer Vision", "Scikit-learn"],
        "url": None
    },
    "Brain Tumor Segmentation": {
        "desc": "Applied state-of-the-art deep learning segmentation models to precisely delineate tumor boundaries in medical scans, improving the accuracy of treatment planning.",
        "tags": ["Medical AI", "Deep Learning", "TensorFlow"],
        "url": None
    },
}

# --- HEADER & NAVIGATION ---
st.markdown('<div class="main-container">', unsafe_allow_html=True)

st.markdown("<h1>Nayabb Fatima</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center; color: #6C757D; font-weight: 500;'>Principal AI Engineer & Researcher</h3>", unsafe_allow_html=True)

# Initialize session state for navigation
if 'page' not in st.session_state:
    st.session_state.page = "Overview"

# Create Navigation Buttons
nav_cols = st.columns(5)
pages = ["Overview", "Competencies", "Trajectory", "Projects", "Education"]
for i, page_name in enumerate(pages):
    with nav_cols[i]:
        if st.button(page_name, use_container_width=True):
            st.session_state.page = page_name

# --- PAGE CONTENT ---
if st.session_state.page == "Overview":
    st.markdown("<h2>Mission</h2>", unsafe_allow_html=True)
    st.markdown("""
    <div style="text-align: justify; font-size: 1.1rem; line-height: 1.8;">
    I am a Principal AI Engineer with over five years of experience leading the design, development, and deployment of intelligent systems that solve tangible, real-world problems. My work operates at the intersection of generative AI, computer vision, and MLOps, with a focus on creating robust, scalable, and impactful solutions in sectors like logistics, healthcare, and enterprise automation.

    My mission is to translate state-of-the-art research into production-grade applications. I have a proven history of architecting systems that deliver significant efficiency gains, from fine-tuning Large Language Models for specialized enterprise tasks to building high-precision computer vision models for medical diagnostics. I thrive on complex challenges and am passionate about building the next generation of AI-driven tools.
    </div>
    """, unsafe_allow_html=True)

if st.session_state.page == "Competencies":
    st.markdown("<h2>Core Competencies</h2>", unsafe_allow_html=True)
    
    cols = st.columns(2)
    skills_items = list(SKILLS.items())
    
    with cols[0]:
        for category, skills_list in skills_items[:2]:
            st.markdown(f"""
            <div class="skill-card">
                <h3>{category}</h3>
                <div class="skill-list">
                    {''.join([f'<span class="skill-tag">{skill}</span>' for skill in skills_list])}
                </div>
            </div>
            """, unsafe_allow_html=True)
            st.write("") # Spacer

    with cols[1]:
        for category, skills_list in skills_items[2:]:
            st.markdown(f"""
            <div class="skill-card">
                <h3>{category}</h3>
                <div class="skill-list">
                    {''.join([f'<span class="skill-tag">{skill}</span>' for skill in skills_list])}
                </div>
            </div>
            """, unsafe_allow_html=True)
            st.write("") # Spacer


if st.session_state.page == "Trajectory":
    st.markdown("<h2>Career Trajectory</h2>", unsafe_allow_html=True)
    st.markdown("""
    <div class="timeline-container">
        <div class="timeline-item">
            <p><i>Jan 2024 - Present</i></p>
            <h3>AI and Data Specialist</h3>
            <p><i>DP World, JAFZA, Dubai, UAE</i></p>
            <ul>
                <li>Led the architectural design and implementation of AI-powered automation for vessel/yard planning, resulting in a 40% reduction in planning time and a 25% improvement in space utilization.</li>
                <li>Engineered and deployed end-to-end data pipelines using Python, PostgreSQL, and FastAPI to support real-time AI inference.</li>
            </ul>
        </div>
        <div class="timeline-item">
            <p><i>Sep 2023 - Jan 2024</i></p>
            <h3>LLM Engineer (Remote)</h3>
            <p><i>Gasame</i></p>
            <ul>
                <li>Created and fine-tuned domain-specific LLMs for specialized enterprise applications, improving task-specific accuracy by over 40%.</li>
                <li>Implemented advanced fine-tuning and prompt engineering strategies to enhance model performance for complex, industry-specific use cases.</li>
            </ul>
        </div>
        <div class="timeline-item">
            <p><i>Aug 2022 - Jul 2023</i></p>
            <h3>Senior AI Engineer (Remote)</h3>
            <p><i>iEKOMEDIA</i></p>
            <ul>
                <li>Designed and deployed a computer vision system for retail analytics, achieving 92% accuracy in customer behavior prediction and providing actionable business insights.</li>
                <li>Mentored a team of 4 junior AI engineers, fostering technical growth and improving overall team productivity by 30%.</li>
            </ul>
        </div>
        <div class="timeline-item">
            <p><i>May 2021 - Jul 2022</i></p>
            <h3>Artificial Intelligence Engineer (Remote)</h3>
            <p><i>Quantsys</i></p>
            <ul>
                <li>Automated critical infrastructure for the data science team, increasing team productivity and experiment throughput by 40%.</li>
                <li>Developed robust, scalable infrastructures for data transformation and ingestion capable of processing terabytes of data daily.</li>
            </ul>
        </div>
    </div>
    """, unsafe_allow_html=True)

if st.session_state.page == "Projects":
    st.markdown("<h2>Featured Projects</h2>", unsafe_allow_html=True)
    
    project_items = list(PROJECTS.items())
    num_cols = 2
    for i in range(0, len(project_items), num_cols):
        cols = st.columns(num_cols)
        for j in range(num_cols):
            if i + j < len(project_items):
                with cols[j]:
                    title, data = project_items[i+j]
                    if data["url"]:
                        title_html = f'<a href="{data["url"]}" target="_blank"><h3>{title}</h3></a>'
                    else:
                        title_html = f'<h3>{title}</h3>'
                    
                    st.markdown(f"""
                    <div class="project-card">
                        {title_html}
                        <p>{data['desc']}</p>
                        <div class="tag-container">
                            {''.join([f'<span class="tag">{tag}</span>' for tag in data['tags']])}
                        </div>
                    </div>
                    """, unsafe_allow_html=True)

if st.session_state.page == "Education":
    st.markdown("<h2>Academic Foundations</h2>", unsafe_allow_html=True)
    
    st.markdown("<h3>Education</h3>", unsafe_allow_html=True)
    st.markdown("""
    - **Ph.D. in Computer Science** (2021 - Present)
      - *Pakistan Institute of Engineering and Applied Sciences (PIEAS), Islamabad*
    - **M.S. in Electrical and Computer Engineering** (2015 - 2018)
      - *Comsats University of Information Technology, Islamabad*
    - **B.S. in Electrical and Computer Engineering** (2009 - 2013)
      - *Comsats University of Information Technology, Lahore*
    """)

    st.markdown("<h3>Selected Publications</h3>", unsafe_allow_html=True)
    st.markdown("""
    - "Automatic optic disk detection and segmentation by variational active contour estimation in retinal fundus images"
    - "Gunshots Localization and Classification Model Based on Wind Noise Sensitivity Analysis Using Extreme Learning Machine"
    """)

st.markdown('</div>', unsafe_allow_html=True)

