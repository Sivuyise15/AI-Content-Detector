from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional

class ContentRequest(BaseModel):
    text: str = Field(
       min_length=50,
       max_length=5000,
       regex=r"^\S+$" 
    )

class AnalysisData(BaseModel):
    ai_score: float
    classification: str
    confidence: str

class ResponseMetadata(BaseModel):  
    timestamp: datetime
    model_version: str

class ContentResponse(BaseModel):
    success: bool
    data: AnalysisData
    metadata: ResponseMetadata

class ErrorDetail(BaseModel):
    code: str
    message: str
    details: Optional[dict] = None

class ErrorResponse(BaseModel):
    success: bool
    error: ErrorDetail
