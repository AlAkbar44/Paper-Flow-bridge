"""
==========================================================
PaperBridge
Career Matcher Engine
==========================================================

Career Matching using Sentence-BERT
Optimized Version

Author  : Al Akbar Himawan
Version : 2.0
==========================================================
"""

import pandas as pd
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity


class CareerMatcher:

    def __init__(self, jobs_path):

        self.jobs = pd.read_csv(jobs_path)

        self.model = SentenceTransformer(
    "all-MiniLM-L6-v2",
    device="cpu"
)

        self.job_texts = []

        self.job_embeddings = None

        self.build_database()

    # ======================================================
    # BUILD JOB DATABASE
    # ======================================================

    def build_database(self):

        self.job_texts = []

        for _, row in self.jobs.iterrows():

            text = (
                str(row["Job Title"]) + " " +
                str(row["Description"]) + " " +
                str(row["Required Skills"])
            )

            self.job_texts.append(text)

        self.job_embeddings = self.model.encode(
            self.job_texts,
            convert_to_tensor=False
        )

    # ======================================================
    # BUILD RESUME PROFILE
    # ======================================================

    def build_resume_profile(self, resume_data):

        profile = []

        profile.extend(resume_data.get("skills", []))
        profile.extend(resume_data.get("education", []))
        profile.extend(resume_data.get("experience", []))

        return " ".join(profile)

    # ======================================================
    # CAREER MATCHING
    # ======================================================

    def match(self, resume_data, top_k=5):

        profile = self.build_resume_profile(resume_data)

        if profile.strip() == "":
            return []

        resume_embedding = self.model.encode(
            profile,
            convert_to_tensor=False
        )

        similarities = cosine_similarity(
            [resume_embedding],
            self.job_embeddings
        )[0]

        results = []

        for index, score in enumerate(similarities):

            row = self.jobs.iloc[index]

            results.append({

                "job_title": row["Job Title"],

                "category": row["Category"],

                "level": row["Level"],

                "description": row["Description"],

                "required_skills": row["Required Skills"],

                "match_score": round(float(score * 100), 2)

            })

        results.sort(
            key=lambda x: x["match_score"],
            reverse=True
        )

        return results[:top_k]