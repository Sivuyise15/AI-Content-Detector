from app.models.database import Base
from sqlalchemy import Column, Integer, String, Float, DateTime, Index
from datetime import datatime, timezone
import hashlib

class Analysis(Base):
    __tablename__ = "analyses"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    
    text_hash = Column(String(64), unique=True, nullable=False, index=True) # Encrypted text
    text_length = Column(Integer, nullable=False)
    ai_score = Column(Float, nullable=False)
    classification = Column(String(20), nullable=False)
    confidence = Column(String(10), nullable=False)

    # Metadata
    model_version = Column(String(50), nullable=False)
    processing_time_ms = Column(Integer, nullable=True)
    created_at = Column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc))

    # Indexes
    __table_args__ = (
        Index('idx_created_at', 'created_at'),
        Index('idx_classification', 'classification'),
    )

    def __repr__(self) -> str:
        return f"<Analysis(id={self.id},  score={self.ai_score}, classification={self.classification})>"

    def to_dict(self):
        return {
            "id": self.id,
            "text_hash": self.text_hash,
            "text_length": self. text_length,
            "ai_score": self.ai_score,
            "classification": self.classification,
            "confidence": self.confidence,
            "model_version": self.model_version,
            "processing_time_ms": self.processing_time_ms,
            "created_at": self.created_at.isoformat() if self.created_at else None
        }
    
    @staticmethod
    def hash_text(text: str) -> str:
        return hashlib.sha256(text.encode('utf-8')).hexdigest()

