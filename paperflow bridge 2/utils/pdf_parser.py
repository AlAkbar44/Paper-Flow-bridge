from typing import Optional
import fitz  # PyMuPDF

class PDFParser:
    """
    PDF Parser using PyMuPDF.

    This class reads uploaded PDF files
    and converts them into plain text.
    """

    def __init__(self, uploaded_file):

        self.uploaded_file = uploaded_file

    # ======================================================
    # EXTRACT TEXT
    # ======================================================

    def extract_text(self) -> str:

        if self.uploaded_file is None:
            return ""

        try:

            pdf = fitz.open(
                stream=self.uploaded_file.read(),
                filetype="pdf"
            )

            pages = []

            for page in pdf:

                text = page.get_text("text")

                if text:

                    pages.append(text.strip())

            pdf.close()

            resume_text = "\n\n".join(pages)

            return resume_text

        except Exception as error:

            print(f"PDF Error : {error}")

            return ""

    # ======================================================
    # TOTAL PAGE
    # ======================================================

    def total_pages(self) -> int:

        if self.uploaded_file is None:
            return 0

        try:

            pdf = fitz.open(
                stream=self.uploaded_file.read(),
                filetype="pdf"
            )

            total = len(pdf)

            pdf.close()

            return total

        except:

            return 0
        
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
    # ALL DATA
    # ======================================================

    def parse(self):

        return {

            "name": self.extract_name(),

            "email": self.extract_email(),

            "phone": self.extract_phone(),

            "linkedin": self.extract_linkedin(),

            "github": self.extract_github(),

            "skills": self.extract_skills()

        }