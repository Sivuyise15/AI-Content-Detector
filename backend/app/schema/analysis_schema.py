from pydantic import BaseModel, Field, field_validator
from datetime import datetime, timezone
from typing import Optional

class ContentRequest(BaseModel):
    text: str = Field(
       min_length=50,
       max_length=5000,
    )
    @field_validator("text")
    def validate_text(cls, value):
        value = value.strip()
        if not value:
            raise ValueError("Text cannot be empty or whitespaces only")
        return value


class AnalysisData(BaseModel):
    ai_score: float = Field(
        ge=0.0,
        le=100.0
    )
    classification: str # will be calculated by the controller
    confidence: str

class ResponseMetadata(BaseModel):  
    timestamp: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    model_version: str # Controller will check this too

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

# Will be adding the examples later
