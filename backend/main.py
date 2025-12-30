import uvicorn
from fastapi import FastAPI

class main:
    def __init__(self):

        self.app = FastAPI(
            title="AI-Content Detector",
            description="API for detecting AI generated content",
            version="1.0.0"
        )
        self.setup_routes()

    def setup_routes(self):
        @self.app.get("/")
        async def root():
            return {
                "message":"AI Content detector for detecting AI generated content",
                "version":"1.0.0",
                "docs":"/docs"
            }

detector = main()
app = detector.app # This what uvicorn will use

if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host="172.20.214.100",
        port=8000,
        reload=True
    )
