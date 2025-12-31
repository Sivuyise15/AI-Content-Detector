from pydantic import BaseModel

class ContentRequest(BaseModel):
    text: str


class ContentResponse(BaseModel):
    success: bool
    data: AnalysisData
    metadata: ResponseMetadata


class ErrorResponse(BaseModel):
    success: bool
    error: ErrorDetail
