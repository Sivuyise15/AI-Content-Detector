import uvicorn
from fastapi import FastAPI
import socket
from pydantic import BaseModel

class main:
    def __init__(self, port):
        self.port = port
        self.app = FastAPI(
            title="AI-Content Detector",
            description="API for detecting AI generated content",
            version="1.0.0"
        )
        self.setup_routes()
        self.health_check()

    def setup_routes(self):
        @self.app.get("/")
        async def root():
            return {
                "message":"AI Content detector for detecting AI generated content",
                "version":"1.0.0",
                "docs":"/docs"
            }
    def health_check(self):
        @self.app.get("/api/v1/health")
        def health():
            serverIP = socket.gethostbyname(socket.gethostname())
            return {"message": f"The API is running at the IP address: {serverIP} and port: {self.port}"}
    
    # def content_detector(self):
    #     @self.app.post("api/v1/analyse")
    #     def analyse(content:str):


port = 8000
detector = main(port)
app = detector.app # This what uvicorn will use

if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host="172.20.214.100",
        port=port,
        reload=True
    )
