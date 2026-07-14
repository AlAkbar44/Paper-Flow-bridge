# 📄 PaperFlow Bridge 2 – AI Resume Analyzer & Career Recommendation

PaperFlow Bridge 2 is an AI-powered web application that helps job seekers evaluate their resumes, analyze ATS compatibility, identify skill gaps, and receive personalized career recommendations.

Built with **Python** and **Streamlit**, the application combines resume parsing, ATS scoring, skill gap analysis, and job matching into a single interactive platform.

---

## 🚀 Features

- 📄 Upload Resume (PDF)
- 🤖 AI Resume Parsing
- 📊 ATS Compatibility Score
- 🎯 Career Recommendation
- 📈 Skill Gap Analysis
- 💼 Job Recommendation Dataset
- 📑 PDF Report Generator
- 🌐 Interactive Streamlit Interface

---

## 🛠️ Tech Stack

| Category | Technology |
|----------|------------|
| Language | Python |
| Framework | Streamlit |
| Data Processing | Pandas |
| Resume Parsing | PyPDF2 / PDF Parser |
| Machine Learning | Scikit-learn |
| Data Storage | CSV Dataset |
| Visualization | Streamlit Components |

---

## 📂 Project Structure

```
PaperFlow Bridge 2/
│
├── app.py
├── requirements.txt
├── README.md
│
├── data/
│   └── jobs.csv
│
├── models/
│   └── career_matcher.py
│
└── utils/
    ├── ats_score.py
    ├── pdf_parser.py
    ├── report_generator.py
    ├── resume_parser.py
    └── skill_gap.py
```

---

## ⚙️ Installation

Clone the repository

```bash
git clone https://github.com/AlAkbar44/Paper-Flow-bridge.git
```

Go to the project

```bash
cd "PaperFlow Bridge 2"
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run Streamlit

```bash
streamlit run app.py
```

---

## 📊 Workflow

```text
Upload Resume (PDF)
        │
        ▼
Resume Parsing
        │
        ▼
ATS Score Calculation
        │
        ▼
Skill Gap Analysis
        │
        ▼
Career Matching
        │
        ▼
Generate PDF Report
```

---

## 🎯 Main Modules

### 📄 Resume Parser

Extracts resume information including:

- Personal Information
- Skills
- Education
- Experience

---

### 📊 ATS Score

Evaluates resume compatibility based on:

- Skill Matching
- Keyword Coverage
- Resume Completeness

---

### 🎯 Career Recommendation

Suggests suitable career paths based on extracted skills and resume content.

---

### 📈 Skill Gap Analysis

Identifies missing skills required for targeted job positions.

---

### 📑 Report Generator

Automatically generates a downloadable summary report containing:

- Resume Summary
- ATS Score
- Career Recommendation
- Skill Gap Analysis

---

## 📌 Future Improvements

- Large Language Model (LLM) Integration
- RAG-based Resume Evaluation
- LinkedIn Profile Analysis
- Real-time Job Scraping
- Multi-language Resume Support
- Dashboard Analytics
- Cloud Deployment

---

## 👨‍💻 Author

**Al Akbar Himawan**

Digital Business Student | Data Analyst | Machine Learning Enthusiast

GitHub:
https://github.com/AlAkbar44

LinkedIn:
https://www.linkedin.com/in/alakbarhimawan/

---
```

## ⭐ If you find this project useful, don't forget to leave a star!
