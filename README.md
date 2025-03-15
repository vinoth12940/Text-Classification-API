# Advanced Text Classification API with Gemini

A powerful text classification API using Google's Gemini 2.0 Flash model, enhanced with time, location, and web data integration capabilities. This API analyzes text content and provides detailed insights, entity extraction, and contextual understanding.

## Features

- **Text Analysis**: Deep semantic analysis of messages and content
- **Entity Extraction**: Identify key entities like locations, people, concepts, and more
- **Time-Aware Analysis**: Incorporates timestamp data for temporal context
- **Location-Enhanced Processing**: Uses address or GPS coordinates for spatial context
- **Web Tool Integration**: Enriches analysis with relevant web data
- **Flexible Classification**: Works with various types of text content, not limited to specific domains

## Use Cases

- **Emergency Response**: Analyzing incident reports and emergency messages
- **Customer Service**: Classifying and prioritizing customer inquiries
- **Content Moderation**: Identifying potentially problematic content
- **Social Media Analysis**: Understanding trending topics and sentiment
- **News Categorization**: Classifying news articles by topic and relevance

## Setup Instructions

### Prerequisites

- Python 3.9+ installed
- pip package manager
- An API key from [Google AI Studio](https://ai.google.dev/) for Gemini

### Installation

1. Clone the repository
   ```bash
   git clone <repository-url>
   cd Text_Classification
   ```

2. Create a virtual environment
   ```bash
   python -m venv myenv
   source myenv/bin/activate  # On Windows: myenv\Scripts\activate
   ```

3. Install dependencies
   ```bash
   pip install -r requirements.txt
   ```

4. Create a `.env` file in the project root
   ```
   GEMINI_API_KEY=your_api_key_here
   ```

### Running the API

Start the server with:
```bash
uvicorn app.main:app --reload --port 8000
```

The API will be available at `http://127.0.0.1:8000`

## API Usage

### API Endpoints

#### 1. Classify Text (`POST /classify`)

Analyzes and classifies text content with optional time and location context.

**Request Format:**

```json
{
  "text": "Your text message to classify",
  "timestamp": "2025-03-15T18:30:00",  // Optional
  "location": {  // Optional
    "latitude": 37.7749,
    "longitude": -122.4194,
    "address": "123 Main St",
    "city": "San Francisco",
    "country": "USA"
  },
  "user_id": "optional-user-id",  // Optional
  "context": {  // Optional
    "additional": "context data"
  }
}
```

**Response Format:**

```json
{
  "analysis": {
    "primary_intent": "Classification result",
    "secondary_intent": "Additional context",
    "entities": [
      {
        "entity": "Entity name",
        "type": "Entity type",
        "context": "Contextual information"
      }
    ],
    "actionable_responses": [
      "Action 1",
      "Action 2"
    ]
  }
}
```

#### 2. Health Check (`GET /health`)

Checks if the API is running correctly.

**Response:**

```json
{
  "status": "healthy"
}
```

## Testing

### Command Line Testing

Test the API using the included test client:

```bash
# Basic message
python -m app.utils.test_client "Your text to classify"

# With address
python -m app.utils.test_client "Your text to classify" --address "123 Main St" --city "San Francisco" --country "USA"

# With GPS coordinates
python -m app.utils.test_client "Your text to classify" --lat 37.7749 --lon -122.4194
```

### Postman Testing

A Postman collection is included in the repository for comprehensive API testing. See the `Postman_Testing_Guide.md` for detailed instructions.

## Architecture

The system uses a pipeline architecture:

1. **Input Processing**: Sanitization, validation, and preparation of input data
2. **Context Enhancement**: Addition of time, location, and web data context
3. **Gemini Analysis**: Processing through Google's Gemini 2.0 Flash model
4. **Response Formatting**: Structured output generation with relevant insights

## Web Data Integration

The API intelligently determines when to fetch web data based on content keywords and context. This provides additional information for more accurate classification and insights.

## Notes

- The Gemini API requires a valid API key from Google AI Studio
- For production use, implement appropriate security measures and rate limiting
- Consider privacy implications when processing location data or personal information

## License

MIT 