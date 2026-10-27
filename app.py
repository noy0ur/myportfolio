import streamlit as st

st.set_page_config(
    page_title="Sameer Shaik | Python Developer",
    page_icon="🐍",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# Update these placeholders before publishing.
NAME = "Sameer Shaik"
GITHUB_USERNAME = "https://github.com/noy0ur"
EMAIL = "shameershaik1499@gmail.com"

st.markdown("""
<style>
:root { color-scheme: dark; }
.stApp {
  background: linear-gradient(180deg, #0b1020 0%, #10172a 48%, #0b1020 100%);
  color: #f3f4f6;
}
.block-container {
  max-width: 1120px;
  padding: 1.5rem clamp(1rem, 4vw, 3rem) 3rem;
}
[data-testid="stHeader"] { background: rgba(11,16,32,.85); }
.hero {
  padding: clamp(1.25rem, 4vw, 3rem);
  border: 1px solid rgba(196,181,253,.25);
  border-radius: 24px;
  background: linear-gradient(130deg, #111827 0%, #312e81 58%, #6d28d9 100%);
  box-shadow: 0 20px 60px rgba(0,0,0,.22);
}
.eyebrow {
  text-transform: uppercase; letter-spacing: .16em;
  font-size: .78rem; font-weight: 800; color: #c4b5fd;
}
.hero h1 { font-size: clamp(2.1rem, 6vw, 4rem); line-height: 1.08; margin: .6rem 0; color: white; }
.hero h2 { font-size: clamp(1.05rem, 2.8vw, 1.5rem); color: #e0e7ff; font-weight: 600; }
.hero p { color: #e5e7eb; max-width: 720px; }
.pill {
  display: inline-block; padding: .35rem .7rem; margin: .2rem .25rem .2rem 0;
  border: 1px solid #4b5563; border-radius: 999px; background: #111827;
  color: #e5e7eb; font-size: .85rem;
}
.project-card {
  min-height: 230px; height: 100%; padding: 1.1rem;
  border-radius: 16px; border: 1px solid #303a52;
  background: linear-gradient(155deg, #151d32, #101727);
}
.project-card h3 { color: #ddd6fe; margin: .25rem 0 .55rem; font-size: 1.08rem; }
.project-card p { color: #cbd5e1; font-size: .94rem; }
.project-meta { color: #a5b4fc; font-size: .8rem; font-weight: 700; }
.section-note { color: #cbd5e1; }
div[data-testid="stMetric"] {
  background: #151d32; border: 1px solid #303a52;
  padding: 1rem; border-radius: 14px;
}
a { color: #c4b5fd !important; }
@media (max-width: 640px) {
  .block-container { padding-top: 1rem; }
  .hero { border-radius: 16px; }
}
</style>
""", unsafe_allow_html=True)

with st.sidebar:
    st.markdown("##  Portfolio")
    st.caption("Python • Data • Software")
    section = st.radio(
        "Navigate",
        ["Home", "Projects", "Skills", "About", "Contact"],
        label_visibility="collapsed",
    )
    st.divider()
    st.caption("Replace the GitHub and email placeholders in app.py before publishing.")

st.markdown(f"""
<div class="hero">
  <div class="eyebrow">Python • Software Development • Data Projects</div>
  <h1>Hi, I'm {NAME} 👋</h1>
  <h2>Aspiring Python Developer | Computer Science Graduate</h2>
  <p>I build practical projects with Python, explore data-driven solutions, and keep improving my software development skills. This portfolio highlights selected projects, tools, and learning progress.</p>
  <span class="pill">Python</span><span class="pill">SQL</span>
  <span class="pill">Pandas</span><span class="pill">Git & GitHub</span>
  <span class="pill">Streamlit</span>
</div>
""", unsafe_allow_html=True)

st.write("")

if section in ["Home", "Projects", "Skills", "About", "Contact"]:
    c1, c2, c3 = st.columns(3)
    c1.metric("Portfolio projects", "12", "Selected work")
    c2.metric("Primary language", "Python")
    c3.metric("Portfolio format", "Responsive web app")

if section in ["Home", "Projects"]:
    st.markdown("## Featured Projects")
    st.markdown('<p class="section-note">Project summaries are included below. Add each verified repository URL before sharing this portfolio with recruiters.</p>', unsafe_allow_html=True)

    projects = [
        ("Skin Lesion Classification", "Computer vision project using the HAM10000 dataset to explore seven-class skin-lesion image classification. Document the evaluation metrics and limitations clearly.", "Python · TensorFlow/Keras · CNN", "Machine Learning"),
        ("AI Resume Analyzer & Job Matcher", "Compare resume text with a job description using text processing and similarity features. Treat matching as a helpful comparison, not a hiring or ATS score.", "Python · NLP · Scikit-learn", "NLP"),
        ("Customer Churn Prediction", "Analyze customer attributes and train a baseline model to estimate churn risk using a labeled dataset.", "Python · Pandas · Scikit-learn", "Machine Learning"),
        ("Student Performance Analysis", "Explore student data, visualize patterns, and explain which features correlate with academic outcomes.", "Python · Pandas · Matplotlib", "Data Analysis"),
        ("College FAQ Chatbot", "Answer common college questions from a small curated knowledge base and show how retrieval works.", "Python · Text Search", "Application"),
        ("Personal Finance Tracker", "Organize transactions, summarize categories, and visualize income and expenses.", "Python · Pandas · Charts", "Data Application"),
        ("Smart Expense Insights", "Explore expense patterns and generate category summaries from sample transaction data.", "Python · Data Analysis", "Automation"),
        ("Everyday Life Organizer", "Combine a task list, shopping list, bill reminders, notes, and a summary dashboard.", "Python · Jupyter", "Productivity"),
        ("Student Success Predictor", "Explore educational data and build a baseline prediction workflow with a discussion of limitations.", "Python · Machine Learning", "Machine Learning"),
        ("ML Model Evaluation Dashboard", "Compare model metrics and visualize classification performance in a compact dashboard.", "Python · Scikit-learn · Charts", "Data Science"),
        ("Household Energy Forecasting", "Analyze energy-usage history and create a baseline forecast with visual summaries.", "Python · Time Series", "Forecasting"),
        ("Python Portfolio Website", "This responsive portfolio app organizes projects, skills, and contact information in one place.", "Python · Streamlit · CSS", "Web App"),
    ]

    if section == "Projects":
        category = st.selectbox("Filter projects", ["All", "Machine Learning", "NLP", "Data Analysis", "Application", "Data Application", "Automation", "Productivity", "Data Science", "Forecasting", "Web App"])
        if category != "All":
            projects = [p for p in projects if p[3] == category]

    cols = st.columns(3)
    for idx, (title, description, tech, category) in enumerate(projects):
        with cols[idx % 3]:
            st.markdown(
                f'<div class="project-card"><div class="project-meta">{category}</div><h3>{title}</h3><p>{description}</p><div class="project-meta">{tech}</div></div>',
                unsafe_allow_html=True,
            )
            st.write("")
            with st.expander("Repository link / project status"):
                st.caption("Add the actual GitHub repository URL here after verifying the project is uploaded and working.")
                st.text_input("Repository URL", key=f"repo_{title}", placeholder="https://github.com/username/repository")
                st.selectbox("Status", ["In progress", "Tested", "Published"], key=f"status_{title}")

if section in ["Home", "Skills"]:
    st.markdown("## Technical Skills")
    skills = {
        "Programming": ["Python", "Basic JavaScript"],
        "Data & ML": ["Pandas", "NumPy", "Scikit-learn basics", "Data visualization"],
        "Databases": ["SQL fundamentals", "SQLite"],
        "Web & Tools": ["HTML", "CSS", "Streamlit", "GitHub", "Jupyter/Kaggle"],
    }
    for group, items in skills.items():
        st.markdown(f"### {group}")
        st.write("  ".join([f"`{item}`" for item in items]))
    st.info("Keep only skills you can explain confidently. Add proficiency levels honestly.")

if section in ["Home", "About"]:
    st.markdown("## About Me")
    st.write(
        "I'm a Computer Science graduate and aspiring Python Developer focused on learning by building. "
        "I enjoy breaking problems into manageable steps, writing readable code, exploring datasets, "
        "and documenting what I learn. I'm currently strengthening Python, SQL, debugging, testing, "
        "and application development."
    )
    st.markdown("### What recruiters can review")
    st.write("- Clear project descriptions and technologies used")
    st.write("- Source code and README documentation in GitHub")
    st.write("- Honest project status, limitations, and evaluation")
    st.write("- Ability to explain design choices and demonstrate the app")

if section in ["Home", "Contact"]:
    st.markdown("## Contact")
    st.write("For opportunities, collaboration, or project discussions:")
    col1, col2 = st.columns(2)
    with col1:
        st.markdown(f"**GitHub**  \n[Open GitHub profile](https://github.com/noy0ur)")
    with col2:
        st.markdown(f"**Email**  \n[{EMAIL}](mailto:{EMAIL})")
    st.caption("Before publishing: replace YOUR-GITHUB-USERNAME and YOUR-EMAIL@example.com in app.py. Never publish passwords, API keys, private data, or personal documents.")

st.divider()
st.caption(f"© {NAME} • Built with Python and Streamlit • Update this portfolio as projects become tested and published.")
