import streamlit as st
from pathlib import Path

# --- PAGE SETUP ---
st.set_page_config(
    page_title="Nayabb Fatima | Principal AI Engineer",
    page_icon="👩‍💻",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# --- INJECT CUSTOM CSS & FONTS ---
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
@import url('https://fonts.googleapis.com/css2?family=Lora:ital,wght@0,400;0,600;1,400&family=Source+Sans+3:wght@400;600;700&display=swap');

:root {
    --primary-bg: #FFFFFF;
    --text-color: #333333;
    --header-text-color: #111111;
    --accent-color: #0055A4; /* A professional, deep blue */
    --border-color: #EAEAEA;
    --secondary-text-color: #555555;
    --font-sans: 'Source Sans 3', sans-serif;
    --font-serif: 'Lora', serif;
}

/* Base Styles */
body, .stApp {
    color: var(--text-color);
    background-color: var(--primary-bg);
    font-family: var(--font-serif);
}

h1, h2, h3, h4, h5, h6 {
    color: var(--header-text-color) !important;
    font-family: var(--font-sans) !important;
    font-weight: 700 !important;
}

h1 {
    font-size: 3rem !important;
    text-align: center;
    padding-top: 2rem;
    margin-bottom: 0.5rem;
}

h2 {
    font-size: 2rem !important;
    padding-bottom: 0.75rem;
    border-bottom: 2px solid var(--border-color);
    margin-top: 3.5rem;
    margin-bottom: 1.5rem;
}

h3 {
    font-size: 1.5rem !important;
    color: var(--header-text-color) !important;
    font-weight: 600 !important;
    font-family: var(--font-sans) !important;
}

p, li {
    font-size: 1.1rem;
    line-height: 1.8;
}

/* Main Content Layout */
.main-container {
    max-width: 800px;
    margin: auto;
    padding: 0 2rem 4rem 2rem;
}

/* Custom Navigation */
.stButton>button {
    background-color: transparent;
    border: none;
    color: var(--secondary-text-color);
    padding: 0.5rem 1rem;
    text-align: center;
    text-decoration: none;
    display: inline-block;
    font-size: 1rem;
    font-weight: 600;
    font-family: var(--font-sans);
    margin: 0 0.25rem;
    cursor: pointer;
    border-radius: 0.25rem;
    transition: all 0.3s ease;
    border-bottom: 2px solid transparent;
}

.stButton>button:hover {
    color: var(--accent-color);
}

.stButton>button:focus {
    color: var(--accent-color) !important;
    border-bottom: 2px solid var(--accent-color) !important;
    background-color: transparent !important;
    box-shadow: none !important;
}

/* Skills Section */
.skill-category {
    margin-bottom: 2rem;
}
.skill-list {
    display: flex;
    flex-wrap: wrap;
    gap: 0.75rem;
    margin-top: 1rem;
}
.skill-tag {
    background-color: #F1F3F5;
    color: var(--secondary-text-color);
    padding: 0.5rem 1rem;
    border-radius: 0.25rem;
    font-size: 0.9rem;
    font-family: var(--font-sans);
    font-weight: 500;
}

/* Experience Timeline */
.timeline-item {
    padding: 0 0 2.5rem 1.5rem;
    border-left: 2px solid var(--border-color);
    position: relative;
}
.timeline-item:last-child {
    padding-bottom: 0.5rem;
    border-left: 2px solid transparent;
}
.timeline-item::before {
    content: '';
    position: absolute;
    left: -7px;
    top: 5px;
    width: 12px;
    height: 12px;
    border-radius: 50%;
    background-color: var(--accent-color);
}
.timeline-item p i {
    color: #6C757D;
    font-family: var(--font-sans);
}
.timeline-item ul {
    margin-left: 1.25rem;
    list-style-type: disc;
    padding-top: 0.5rem;
}

/* Project Cards */
.project-card {
    border-bottom: 1px solid var(--border-color);
    padding: 2rem 0;
}
.project-card:last-child {
    border-bottom: none;
}
.project-card a { text-decoration: none; }
.project-card h3 {
    transition: color 0.3s ease;
}
.project-card a:hover h3 { color: var(--accent-color); }
.project-card .tag-container {
    margin-top: 1rem;
    display: flex;
    flex-wrap: wrap;
    gap: 0.5rem;
}
.project-card .tag {
    background-color: #F1F3F5;
    color: #495057;
    font-weight: 500;
    padding: 4px 10px;
    border-radius: 15px;
    font-size: 0.75rem;
    font-family: var(--font-sans);
}

/* Footer */
.footer {
    border-top: 1px solid var(--border-color);
    padding: 2.5rem 0;
    text-align: center;
}
.contact-container {
    display: flex;
    justify-content: center;
    align-items: center;
    gap: 2rem;
}
.contact-info {
    display: flex;
    align-items: center;
    gap: 8px;
    color: var(--secondary-text-color);
    text-decoration: none;
    font-weight: 600;
    font-family: var(--font-sans);
    transition: color 0.3s;
}
.contact-info:hover {
    color: var(--accent-color);
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
st.markdown("<h3 style='text-align: center; color: #6C757D; font-weight: 400; font-family: var(--font-sans); margin-bottom: 2rem;'>Principal AI Engineer & Researcher</h3>", unsafe_allow_html=True)

# Initialize session state for navigation
if 'page' not in st.session_state:
    st.session_state.page = "Overview"

# Create Navigation Buttons
nav_cols = st.columns(5)
pages = ["Overview", "Competencies", "Trajectory", "Projects", "Education"]
for i, page_name in enumerate(pages):
    with nav_cols[i]:
        if st.button(page_name, use_container_width=True, key=f"nav_{page_name}"):
            st.session_state.page = page_name

st.markdown("<hr style='margin: 1rem 0 2rem 0; border-color: var(--border-color);'>", unsafe_allow_html=True)

# --- PAGE CONTENT ---
if st.session_state.page == "Overview":
    st.markdown("<h2>Mission</h2>", unsafe_allow_html=True)
    st.markdown("""
    <div style="text-align: justify;">
    <p>I am a Principal AI Engineer with over five years of experience leading the design, development, and deployment of intelligent systems that solve tangible, real-world problems. My work operates at the intersection of generative AI, computer vision, and MLOps, with a focus on creating robust, scalable, and impactful solutions in sectors like logistics, healthcare, and enterprise automation.</p>
    <p>My mission is to translate state-of-the-art research into production-grade applications. I have a proven history of architecting systems that deliver significant efficiency gains, from fine-tuning Large Language Models for specialized enterprise tasks to building high-precision computer vision models for medical diagnostics. I thrive on complex challenges and am passionate about building the next generation of AI-driven tools.</p>
    </div>
    """, unsafe_allow_html=True)

if st.session_state.page == "Competencies":
    st.markdown("<h2>Core Competencies</h2>", unsafe_allow_html=True)
    
    for category, skills_list in SKILLS.items():
        st.markdown(f"""
        <div class="skill-category">
            <h3>{category}</h3>
            <div class="skill-list">
                {''.join([f'<span class="skill-tag">{skill}</span>' for skill in skills_list])}
            </div>
        </div>
        """, unsafe_allow_html=True)

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
    
    for title, data in PROJECTS.items():
        st.markdown('<div class="project-card">', unsafe_allow_html=True)
        if data["url"]:
            title_html = f'<a href="{data["url"]}" target="_blank"><h3>{title}</h3></a>'
        else:
            title_html = f'<h3>{title}</h3>'
        
        st.markdown(title_html, unsafe_allow_html=True)
        st.markdown(f"<p>{data['desc']}</p>", unsafe_allow_html=True)
        st.markdown(f"""
            <div class="tag-container">
                {''.join([f'<span class="tag">{tag}</span>' for tag in data['tags']])}
            </div>
        """, unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)


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
    <p>- "Automatic optic disk detection and segmentation by variational active contour estimation in retinal fundus images"</p>
    <p>- "Gunshots Localization and Classification Model Based on Wind Noise Sensitivity Analysis Using Extreme Learning Machine"</p>
    """, unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

# --- FOOTER ---
st.markdown("""
<div class="footer">
    <div class="contact-container">
        <a href="mailto:nayabfatima97@gmail.com" target="_blank" class="contact-info">📧 Email</a>
        <a href="https://wa.me/971522429814" target="_blank" class="contact-info">📱 WhatsApp</a>
        <a href="https://linkedin.com/in/nayabb-fatima-9b177a55/" target="_blank" class="contact-info">💼 LinkedIn</a>
        <a href="https://github.com/Nayab-zak" target="_blank" class="contact-info">💻 GitHub</a>
    </div>
</div>
""", unsafe_allow_html=True)

