from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Dict, Any, Optional
import uvicorn
from datetime import datetime

from .classifier import EnhancedGeminiAnalyzer

app = FastAPI(
    title="Emergency Text Classifier API",
    description="API for classifying emergency text messages using Google's Gemini model",
    version="1.0.0"
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Location model
class Location(BaseModel):
    latitude: Optional[float] = None
    longitude: Optional[float] = None
    address: Optional[str] = None
    city: Optional[str] = None
    country: Optional[str] = None

# Request model
class MessageRequest(BaseModel):
    text: str
    user_id: Optional[str] = None
    context: Optional[Dict[str, Any]] = None
    timestamp: Optional[datetime] = None
    location: Optional[Location] = None

# Initialize analyzer
analyzer = EnhancedGeminiAnalyzer()

@app.post("/classify")
async def classify_text(request: MessageRequest):
    """
    Classify emergency text and return analysis
    """
    if not request.text or len(request.text.strip()) < 5:
        raise HTTPException(status_code=400, detail="Text is too short for classification")
    
    result = analyzer.analyze_message(
        request.text,
        timestamp=request.timestamp,
        location=request.location.dict() if request.location else None
    )
    return result

@app.get("/health")
async def health_check():
    """Health check endpoint"""
    return {"status": "healthy"}

if __name__ == "__main__":
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True) 