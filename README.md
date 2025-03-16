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

- **Content Analysis**: Analyzing documents, articles, and reports
- **Customer Service**: Classifying and prioritizing customer inquiries
- **Content Moderation**: Identifying potentially problematic content
- **Social Media Analysis**: Understanding trending topics and sentiment
- **News Categorization**: Classifying news articles by topic and relevance
- **Research Assistance**: Extracting key information from academic papers

## GitHub Repository

- **Repository**: [https://github.com/vinoth12940/Text-Classification-API](https://github.com/vinoth12940/Text-Classification-API)
- **Clone URL**: `git clone https://github.com/vinoth12940/Text-Classification-API.git`
- **Issues**: Report bugs or suggest features in the [Issues section](https://github.com/vinoth12940/Text-Classification-API/issues)

## Setup Instructions

### Prerequisites

- Python 3.9+ installed
- pip package manager
- An API key from [Google AI Studio](https://ai.google.dev/) for Gemini

### Installation

1. Clone the repository
   ```bash
   git clone https://github.com/vinoth12940/Text-Classification-API.git
   cd Text-Classification-API
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

## API Documentation

### Interactive Swagger UI

Once the API is running, you can access the interactive Swagger UI documentation at:

```
http://127.0.0.1:8000/docs
```

The Swagger UI provides:
- Interactive documentation for all endpoints
- Request and response schemas
- The ability to test API endpoints directly from your browser
- Examples of valid request bodies
- Detailed descriptions of all parameters and models

### Alternative Documentation (ReDoc)

For an alternative documentation view, you can access the ReDoc interface at:

```
http://127.0.0.1:8000/redoc
```

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

### Curl Examples

Test the API from the command line:

```bash
# Basic test
curl -X 'POST' \
  'http://127.0.0.1:8000/classify' \
  -H 'Content-Type: application/json' \
  -d '{
  "text": "Analysis needed for this important document about climate change policies in urban areas."
}'

# With location and timestamp
curl -X 'POST' \
  'http://127.0.0.1:8000/classify' \
  -H 'Content-Type: application/json' \
  -d '{
  "text": "Analysis needed for this important document about climate change policies in urban areas.",
  "timestamp": "2023-06-15T14:30:00",
  "location": {
    "address": "123 Main St",
    "city": "San Francisco",
    "country": "USA"
  }
}'
```

## Architecture

The system uses a pipeline architecture:

1. **Input Processing**: Sanitization, validation, and preparation of input data
2. **Context Enhancement**: Addition of time, location, and web data context
3. **Gemini Analysis**: Processing through Google's Gemini 2.0 Flash model
4. **Response Formatting**: Structured output generation with relevant insights

## Web Data Integration

The API intelligently determines when to fetch web data based on content keywords and context. This provides additional information for more accurate classification and insights.

## Contributing

Contributions are welcome! Here's how you can contribute:

1. **Fork the Repository**: Click the "Fork" button at the top right of the [repository page](https://github.com/vinoth12940/Text-Classification-API)
2. **Clone Your Fork**: `git clone https://github.com/YOUR-USERNAME/Text-Classification-API.git`
3. **Create a Branch**: `git checkout -b feature/your-feature-name`
4. **Make Changes**: Implement your changes or fixes
5. **Run Tests**: Ensure all tests pass
6. **Commit Changes**: `git commit -m "Description of changes"`
7. **Push to GitHub**: `git push origin feature/your-feature-name`
8. **Create a Pull Request**: Submit a PR through the GitHub interface

Please follow these guidelines:
- Follow the existing code style
- Add tests for new features
- Update documentation as needed

## Technologies Used

- **FastAPI**: Modern, high-performance web framework for building APIs
- **Google Gemini AI**: State-of-the-art large language model for text analysis
- **Pydantic**: Data validation and settings management
- **Uvicorn**: ASGI server for FastAPI
- **Python 3.9+**: Modern Python for robust development

## License

MIT 