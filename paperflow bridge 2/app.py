# ==========================================================
# 1. IMPORTS
# ==========================================================

import time

import streamlit as st

from utils.pdf_parser import PDFParser
from utils.resume_parser import ResumeParser
from utils.ats_score import ATSScore
from utils.skill_gap import SkillGap
from utils.report_generator import ReportGenerator
from models.career_matcher import CareerMatcher

# ==========================================================
# 2. STREAMLIT PAGE CONFIGURATION
# ==========================================================

st.set_page_config(
    page_title="PaperBridge",
    page_icon="🌉",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ==========================================================
# 3. SESSION STATE
# ==========================================================

DEFAULT_SESSION = {
    "analysis_done": False,
    "resume_text": "",
    "resume_data": {},
    "ats_score": 0,
    "career_result": [],
    "skill_gap": [],
    "recommendation": [],
    "uploaded_filename": "",
    "processing": False
}

for key, value in DEFAULT_SESSION.items():
    if key not in st.session_state:
        st.session_state[key] = value

# ==========================================================
# 4. CUSTOM CSS
# ==========================================================

st.markdown("""
<style>

.main{
    padding-top:1rem;
}

.block-container{
    padding-top:2rem;
    padding-bottom:2rem;
}

.paperbridge-card{
    background:#FFFFFF;
    padding:25px;
    border-radius:15px;
    border:1px solid #E5E7EB;
    box-shadow:0 3px 12px rgba(0,0,0,0.05);
}

.title-center{
    text-align:center;
}

.subtitle{
    color:#6B7280;
    text-align:center;
    font-size:17px;
}

.footer{
    text-align:center;
    color:gray;
    font-size:13px;
}

</style>
""", unsafe_allow_html=True)

# ==========================================================
# 5. SIDEBAR
# ==========================================================

with st.sidebar:

    st.title("🌉 PaperBridge")

    st.write(
        """
AI Resume Analyzer powered by
Natural Language Processing
and Machine Learning.
"""
    )

    st.divider()

    st.subheader("Features")

    st.markdown("""
- 📄 Resume Parsing
- 📊 ATS Score
- 🎯 Career Matching
- 📈 Skill Gap Analysis
- 💡 Recruiter Insight
- 📥 PDF Report
""")

    st.divider()

    st.subheader("Technology")

    st.markdown("""
- Python
- Streamlit
- PyMuPDF
- Sentence-BERT
- Scikit-Learn
""")

    st.divider()

    st.caption("PaperBridge Version 1.0")

# ==========================================================
# 6. HEADER
# ==========================================================

st.markdown(
    """
<h1 class="title-center">
🌉 PaperBridge
</h1>
""",
    unsafe_allow_html=True
)

st.markdown(
    """
<p class="subtitle">

AI Resume Analyzer &
Career Matching System

</p>
""",
    unsafe_allow_html=True
)

st.write("")

st.info(
    """
Upload your resume in PDF format.

PaperBridge will automatically:

✅ Extract Resume Information

✅ Calculate ATS Score

✅ Recommend Career Paths

✅ Identify Skill Gaps

✅ Provide Recruiter Insight
"""
)

st.divider()

# ==========================================================
# 7. UPLOAD SECTION
# ==========================================================

left, right = st.columns([2, 1])

with left:

    uploaded_file = st.file_uploader(
        "Upload Resume (PDF)",
        type=["pdf"]
    )

with right:

    analyze = st.button(
        "🚀 Analyze My Resume",
        use_container_width=True,
        type="primary"
    )

st.divider()

# ==========================================================
# 8. ANALYZE ACTION
# ==========================================================

if analyze:

    # ------------------------------------------------------
    # 8.1 Upload validation
    # ------------------------------------------------------

    if uploaded_file is None:

        st.warning("⚠️ Please upload your resume first.")

    else:

        st.session_state.processing = True
        st.session_state.uploaded_filename = uploaded_file.name

        # --------------------------------------------------
        # 8.2 Progress bar
        # --------------------------------------------------

        progress_text = st.empty()
        progress_bar = st.progress(0)

        for i in range(101):
            progress_bar.progress(i)
            progress_text.markdown(f"**Analyzing Resume... {i}%**")
            time.sleep(0.01)

        progress_bar.empty()
        progress_text.empty()

        # --------------------------------------------------
        # 8.3 PDF extraction
        # --------------------------------------------------

        pdf_parser = PDFParser(uploaded_file)
        resume_text = pdf_parser.extract_text()

        st.session_state.resume_text = resume_text

        # --------------------------------------------------
        # 8.4 Resume parsing
        # --------------------------------------------------

        resume_parser = ResumeParser(resume_text)
        resume_data = resume_parser.parse()

        st.session_state.resume_data = resume_data

        # --------------------------------------------------
        # 8.5 ATS score
        # --------------------------------------------------

        ats = ATSScore(resume_data)
        score = ats.calculate()

        st.session_state.ats_score = score

        # --------------------------------------------------
        # 8.6 Career matching
        # --------------------------------------------------

        matcher = CareerMatcher("data/jobs.csv")
        career_result = matcher.match(resume_data)

        st.session_state.career_result = career_result

        # --------------------------------------------------
        # 8.7 Skill gap analysis
        # --------------------------------------------------

        skill_gap = SkillGap(resume_data, career_result)
        gap_result = skill_gap.analyze()

        st.session_state.skill_gap = gap_result

        # --------------------------------------------------
        # 8.8 / 8.9 Save state and mark analysis complete
        # --------------------------------------------------

        st.session_state.analysis_done = True
        st.session_state.processing = False

# ==========================================================
# 9. RESULT SECTION
# ==========================================================

if st.session_state.analysis_done:

    st.success("✅ Resume uploaded successfully!")

    # ------------------------------------------------------
    # 9.1 Resume Preview
    # ------------------------------------------------------

    with st.expander("📄 Resume Preview"):

        if st.session_state.resume_text:
            st.text(st.session_state.resume_text[:4000])
        else:
            st.warning("No text found inside the PDF.")

    st.write("")

    col1, col2 = st.columns([2, 1])

    # ------------------------------------------------------
    # 9.2 Resume Information
    # ------------------------------------------------------

    with col1:

        st.subheader("📄 Resume Information")

        data = st.session_state.resume_data

        st.write(f"### 👤 {data['name']}")

        st.write(f"**📧 Email:** {data['email']}")
        st.write(f"**📱 Phone:** {data['phone']}")
        st.write(f"**🔗 LinkedIn:** {data['linkedin']}")
        st.write(f"**💻 GitHub:** {data['github']}")

        st.markdown("### 🎓 Education")

        if data["education"]:
            for item in data["education"]:
                st.write(f"• {item}")
        else:
            st.write("-")

        st.markdown("### 💼 Experience")

        if data["experience"]:
            for item in data["experience"]:
                st.write(f"• {item}")
        else:
            st.write("-")

        st.markdown("### 🛠 Skills")

        if data["skills"]:
            cols = st.columns(3)
            for index, skill in enumerate(data["skills"]):
                cols[index % 3].success(skill)
        else:
            st.write("No skills detected.")

    # ------------------------------------------------------
    # 9.3 ATS Score
    # ------------------------------------------------------

    with col2:

        st.subheader("📊 ATS Score")

        score = st.session_state.ats_score

        st.metric(
            "ATS Score",
            f"{score['total']} / 100"
        )

        st.progress(score["total"] / 100)

        st.markdown("### 📋 Score Details")

        st.write(f"📧 Contact : {score['contact']} / 20")
        st.write(f"🎓 Education : {score['education']} / 20")
        st.write(f"💼 Experience : {score['experience']} / 25")
        st.write(f"🛠 Skills : {score['skills']} / 35")

    st.divider()

    # ------------------------------------------------------
    # 9.4 Career Match
    # ------------------------------------------------------

    st.subheader("🎯 Career Match")

    career = st.session_state.career_result

    if career:

        for i, job in enumerate(career):

            with st.container():

                st.markdown(f"## {i + 1}. {job['job_title']}")

                st.progress(job["match_score"] / 100)

                st.write(f"**Match Score:** {job['match_score']}%")

                job_col1, job_col2 = st.columns(2)

                with job_col1:

                    st.write(f"**Category:** {job['category']}")
                    st.write(f"**Level:** {job['level']}")

                with job_col2:

                    st.write("**Required Skills**")

                    skills = job["required_skills"].split("|")

                    for skill in skills:
                        st.success(skill)

                st.write(job["description"])

                st.divider()

    else:

        st.info("No career recommendation available.")

    # ------------------------------------------------------
    # 9.5 Skill Gap
    # ------------------------------------------------------

    st.subheader("📈 Skill Gap Analysis")

    gap = st.session_state.skill_gap

    if gap:

        st.warning(
            "The following skills are recommended to improve your career match."
        )

        gap_cols = st.columns(2)

        for index, skill in enumerate(gap):
            gap_cols[index % 2].error(skill)

    else:

        st.success(
            "Excellent! No significant skill gap detected."
        )

    st.divider()

    # ------------------------------------------------------
    # 9.6 Recruiter Insight
    # ------------------------------------------------------

    st.subheader("💡 Recruiter Insight")

    st.info(
        "Recruiter insight will appear here."
    )

    st.divider()

    # ------------------------------------------------------
    # 9.7 Download PDF Report
    # ------------------------------------------------------

    st.subheader("📄 Download Report")

    if st.button("Generate PDF Report"):

        report = ReportGenerator(
            st.session_state.resume_data,
            st.session_state.ats_score,
            st.session_state.career_result,
            st.session_state.skill_gap
        )

        output_file = "PaperBridge_Report.pdf"

        report.generate(output_file)

        with open(output_file, "rb") as file:

            st.download_button(
                label="⬇️ Download Report",
                data=file,
                file_name="PaperBridge_Report.pdf",
                mime="application/pdf"
            )