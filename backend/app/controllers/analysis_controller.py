# schemas
from app.services import (
    ContentRequest,
    ContntResponse,
    AnalysisData,
    ResponseMetadata,
    ErrorResponse,
    ErrorDetail
)

# services
from app.services import ai_detector_service
from app.services import classification_service

class AnalysisController():

    __init__(self):