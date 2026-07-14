"""
==========================================================
PaperBridge
Skill Gap Analysis
==========================================================

Compare Resume Skills with Required Job Skills

Author  : Al Akbar Himawan
Version : 1.0
==========================================================
"""


class SkillGap:

    def __init__(self, resume_data, career_result):

        self.resume_data = resume_data

        self.career_result = career_result

    # ======================================================
    # FIND MISSING SKILLS
    # ======================================================

    def analyze(self):

        if not self.career_result:
            return []

        top_job = self.career_result[0]

        required_skills = [
            skill.strip()
            for skill in top_job["required_skills"].split("|")
        ]

        resume_skills = [
            skill.lower()
            for skill in self.resume_data.get("skills", [])
        ]

        missing = []

        for skill in required_skills:

            if skill.lower() not in resume_skills:

                missing.append(skill)

        return missing