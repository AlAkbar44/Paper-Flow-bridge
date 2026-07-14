"""
==========================================================
PaperBridge
Resume Parser Module
==========================================================

Extract important information from resume text.

Author  : Al Akbar Himawan
Version : 1.0
==========================================================
"""

import re


SKILLS = [
    "python",
    "sql",
    "excel",
    "tableau",
    "power bi",
    "pandas",
    "numpy",
    "scikit-learn",
    "tensorflow",
    "pytorch",
    "machine learning",
    "deep learning",
    "statistics",
    "postgresql",
    "mysql",
    "git",
    "github",
    "streamlit",
    "looker studio",
    "spss",
    "html",
    "css",
    "javascript"
]

# ==========================================================
# SECTION HEADERS
# ==========================================================
# Used to detect where each resume section starts, so that
# lines belonging to that section can be collected until the
# next known section header is found.

SECTION_HEADERS = [
    "education",
    "experience",
    "work experience",
    "employment",
    "skills",
    "projects",
    "certification",
    "certifications",
    "summary",
    "objective",
    "contact",
    "organization",
    "organizational experience"
]

EDUCATION_HEADERS = ["education"]

EXPERIENCE_HEADERS = ["experience", "work experience", "employment"]


class ResumeParser:

    def __init__(self, resume_text):

        self.text = resume_text
        self.lower_text = resume_text.lower()

    # ======================================================
    # NAME
    # ======================================================

    def extract_name(self):

        lines = self.text.split("\n")

        for line in lines:

            line = line.strip()

            if 3 <= len(line.split()) <= 4:
                return line

        return "Not Found"

    # ======================================================
    # EMAIL
    # ======================================================

    def extract_email(self):

        pattern = r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}"

        match = re.search(pattern, self.text)

        return match.group() if match else "Not Found"

    # ======================================================
    # PHONE
    # ======================================================

    def extract_phone(self):

        pattern = r"(\+62|62|0)[0-9]{8,13}"

        match = re.search(pattern, self.text)

        return match.group() if match else "Not Found"

    # ======================================================
    # LINKEDIN
    # ======================================================

    def extract_linkedin(self):

        pattern = r"linkedin\.com/[^\s]+"

        match = re.search(pattern, self.lower_text)

        return match.group() if match else "Not Found"

    # ======================================================
    # GITHUB
    # ======================================================

    def extract_github(self):

        pattern = r"github\.com/[^\s]+"

        match = re.search(pattern, self.lower_text)

        return match.group() if match else "Not Found"

    # ======================================================
    # SKILLS
    # ======================================================

    def extract_skills(self):

        found = []

        for skill in SKILLS:

            if skill in self.lower_text:

                found.append(skill.title())

        return sorted(list(set(found)))

    # ======================================================
    # SECTION EXTRACTOR (HELPER)
    # ======================================================

    def _extract_section(self, target_headers):
        """
        Collect all lines that belong to a section whose header
        matches one of `target_headers`. Collection stops once
        another known section header is encountered.
        """

        lines = self.text.split("\n")

        collected = []
        inside_section = False

        for line in lines:

            stripped = line.strip()

            if not stripped:
                continue

            lower_line = stripped.lower().strip(":").strip()

            is_header = lower_line in SECTION_HEADERS

            if is_header:

                if lower_line in target_headers:
                    inside_section = True
                else:
                    inside_section = False

                continue

            if inside_section:

                # Remove common bullet characters before storing.
                cleaned = stripped.lstrip("•-*").strip()

                if cleaned:
                    collected.append(cleaned)

        return collected

    # ======================================================
    # EDUCATION
    # ======================================================

    def extract_education(self):

        return self._extract_section(EDUCATION_HEADERS)

    # ======================================================
    # EXPERIENCE
    # ======================================================

    def extract_experience(self):

        return self._extract_section(EXPERIENCE_HEADERS)

    # ======================================================
    # ALL DATA
    # ======================================================

    def parse(self):

        return {

            "name": self.extract_name(),

            "email": self.extract_email(),

            "phone": self.extract_phone(),

            "linkedin": self.extract_linkedin(),

            "github": self.extract_github(),

            "skills": self.extract_skills(),

            "education": self.extract_education(),

            "experience": self.extract_experience()

        }streamlit run app.py