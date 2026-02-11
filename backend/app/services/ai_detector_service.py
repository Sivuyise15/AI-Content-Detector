from transformers import pipeline

class AIDetectorService:

    def __init__(self):
        self.pipe = pipeline("text-classification", model="Hello-SimpleAI/chatgpt-detector-roberta")


    def detect_ai(text: str) -> float:
        return self.pipe(text)

detect = AIDetectorService()
val = detect.detect_ai("Hello world!")


if __name__ == "__main__":
    print(val)