from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field
from typing import List, Dict, Any, Optional
import uvicorn
from datetime import datetime

from .classifier import EnhancedGeminiAnalyzer

app = FastAPI(
    title="Advanced Text Classification API",
    description="""
    A powerful text classification API using Google's Gemini 2.0 Flash model, enhanced with time, location, and web data integration capabilities.
    
    ## Features
    
    - **Text Analysis**: Deep semantic analysis of messages and content
    - **Entity Extraction**: Identify key entities like locations, people, concepts, and more
    - **Time-Aware Analysis**: Incorporates timestamp data for temporal context
    - **Location-Enhanced Processing**: Uses address or GPS coordinates for spatial context
    - **Web Tool Integration**: Enriches analysis with relevant web data
    
    ## Documentation
    
    For more detailed information, visit our [GitHub repository](https://github.com/vinoth12940/Text-Classification-API).
    """,
    version="1.0.0",
    contact={
        "name": "GitHub Repository",
        "url": "https://github.com/vinoth12940/Text-Classification-API",
    },
    license_info={
        "name": "MIT",
    },
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
    latitude: Optional[float] = Field(None, description="GPS latitude coordinate")
    longitude: Optional[float] = Field(None, description="GPS longitude coordinate")
    address: Optional[str] = Field(None, description="Street address")
    city: Optional[str] = Field(None, description="City name")
    country: Optional[str] = Field(None, description="Country name")
    
    class Config:
        schema_extra = {
            "example": {
                "latitude": 37.7749,
                "longitude": -122.4194,
                "address": "123 Main St",
                "city": "San Francisco",
                "country": "USA"
            }
        }

# Entity response model
class Entity(BaseModel):
    entity: str = Field(..., description="Name of the identified entity")
    type: str = Field(..., description="Type of entity (person, location, organization, etc.)")
    context: str = Field(..., description="Contextual information about the entity")

# Analysis response model
class AnalysisResponse(BaseModel):
    primary_intent: str = Field(..., description="Primary theme or intent of the text")
    secondary_intent: Optional[str] = Field(None, description="Secondary context or intent")
    entities: List[Entity] = Field([], description="List of entities identified in the text")
    actionable_responses: List[str] = Field([], description="Suggested actions or responses")

# Complete response model
class ClassificationResponse(BaseModel):
    analysis: AnalysisResponse

# Request model
class MessageRequest(BaseModel):
    text: str = Field(..., description="Text content to be classified", min_length=5)
    user_id: Optional[str] = Field(None, description="Optional identifier for the user")
    context: Optional[Dict[str, Any]] = Field(None, description="Additional context information")
    timestamp: Optional[datetime] = Field(None, description="Timestamp when the message was created")
    location: Optional[Location] = Field(None, description="Location information")
    
    class Config:
        schema_extra = {
            "example": {
                "text": "Analysis needed for this important document about climate change policies in urban areas.",
                "user_id": "user123",
                "timestamp": "2023-06-15T14:30:00",
                "location": {
                    "address": "123 Main St",
                    "city": "San Francisco",
                    "country": "USA"
                }
            }
        }

# Initialize analyzer
analyzer = EnhancedGeminiAnalyzer()

@app.post("/classify", response_model=Dict[str, Any], tags=["Classification"], 
         summary="Classify and analyze text content",
         description="""
         Analyzes and classifies text content with optional time and location context.
         
         The API will:
         - Perform deep semantic analysis
         - Extract entities and their context
         - Identify primary and secondary themes
         - Generate actionable insights
         - Incorporate temporal and spatial context if provided
         - Use web data to enhance analysis when relevant
         """)
async def classify_text(request: MessageRequest):
    if not request.text or len(request.text.strip()) < 5:
        raise HTTPException(status_code=400, detail="Text is too short for classification")
    
    result = analyzer.analyze_message(
        request.text,
        timestamp=request.timestamp,
        location=request.location.dict() if request.location else None
    )
    return result

@app.get("/health", tags=["System"], 
        summary="API health check",
        description="Verifies that the API is running correctly and all systems are operational.")
async def health_check():
    """Health check endpoint"""
    return {"status": "healthy"}

if __name__ == "__main__":
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True) 