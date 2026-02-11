class classification_service:

    def __init__(self):

    def get_classification(ai_score: float) -> str:
        if ai_score <= 30:
            return "Human-Written"
        elif ai_score <= 70:
            return "Uncertain"
        else:
            return "AI-Generated"
    
    def get_confidence(ai_score: float) -> str:
        if ai_score <= 20 or ai_score >= 80:
            return "High"
        elif 40 < ai_score < 60:
            return "Low"
        else:
            return "Medium"
