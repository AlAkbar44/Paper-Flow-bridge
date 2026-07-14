"""
==========================================================
PaperBridge
ATS Score Engine
==========================================================

Calculate Resume ATS Score

Author  : Al Akbar Himawan
Version : 1.0
==========================================================
"""


class ATSScore:

    def __init__(self, resume_data):

        self.data = resume_data

    # ======================================================
    # CONTACT
    # ======================================================

    def contact_score(self):

        score = 0

        if self.data["email"] != "Not Found":
            score += 8

        if self.data["phone"] != "Not Found":
            score += 6

        if self.data["linkedin"] != "Not Found":
            score += 3

        if self.data["github"] != "Not Found":
            score += 3

        return score

    # ======================================================
    # EDUCATION
    # ======================================================

    def education_score(self):

        if len(self.data["education"]) > 0:
            return 20

        return 0

    # ======================================================
    # EXPERIENCE
    # ======================================================

    def experience_score(self):

        total = len(self.data["experience"])

        if total >= 3:
            return 25

        elif total == 2:
            return 20

        elif total == 1:
            return 15

        return 0

    # ======================================================
    # SKILLS
    # ======================================================

    def skills_score(self):

        total = len(self.data["skills"])

        if total >= 10:
            return 35

        elif total >= 7:
            return 30

        elif total >= 5:
            return 25

        elif total >= 3:
            return 18

        return 10

    # ======================================================
    # FINAL SCORE
    # ======================================================

    def calculate(self):

        contact = self.contact_score()

        education = self.education_score()

        experience = self.experience_score()

        skills = self.skills_score()

        total = contact + education + experience + skills

        if total > 100:
            total = 100

        return {

            "contact": contact,

            "education": education,

            "experience": experience,

            "skills": skills,

            "total": total

        }