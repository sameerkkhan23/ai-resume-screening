def rank_resumes(resume_names, similarity_scores):
    """
    Rank resumes based on similarity score
    """
    ranked = list(zip(resume_names, similarity_scores))
    ranked.sort(key=lambda x: x[1], reverse=True)
    return ranked
