# Testing the Emergency Text Classification API with Postman

This guide provides detailed instructions for testing your Emergency Text Classification API using the provided Postman collection.

## Prerequisites

1. Ensure your API server is running at `http://127.0.0.1:8001` (or update the collection variables if using a different port)
2. Install [Postman](https://www.postman.com/downloads/) on your machine
3. Import the Postman collection (see import instructions below)

## Importing the Collection

1. Open Postman
2. Click on "Import" button at the top-left corner
3. Select "File" > "Upload Files"
4. Browse and select the `Emergency_Text_Classification_API.postman_collection.json` file
5. Click "Import"

## Collection Structure

The collection is organized into four main folders:

1. **Health Check** - Tests the health check endpoint
2. **Classification** - Basic classification scenarios with different types of data
3. **Special Scenarios** - Tests specific use cases like public events and natural disasters
4. **Error Handling** - Tests error responses for invalid inputs

## Running the Tests

### 1. Testing Health Check Endpoint

Navigate to the "Health Check" folder and run the "Health Check Endpoint" request.

**Expected response:**
```json
{
    "status": "healthy"
}
```

### 2. Testing Basic Classification

Navigate to the "Classification" folder and run the following requests:

#### a. Basic Text Classification

Tests classification with only emergency text data.

**Request body:**
```json
{
    "text": "There is a fire in the building at 123 Main Street. People are trapped on the second floor."
}
```

#### b. Classification with Time

Tests classification with timestamp added.

**Request body:**
```json
{
    "text": "Medical emergency at 456 Park Avenue. Elderly man having chest pains and difficulty breathing.",
    "timestamp": "{{$isoTimestamp}}"
}
```

> Note: The `{{$isoTimestamp}}` variable will be automatically replaced with the current ISO 8601 timestamp.

#### c. Classification with Address

Tests classification with address-based location.

**Request body:**
```json
{
    "text": "Flooding in Downtown Central Park. Water levels rising quickly and people are stranded.",
    "timestamp": "{{$isoTimestamp}}",
    "location": {
        "address": "Central Park",
        "city": "New York",
        "country": "USA"
    }
}
```

#### d. Classification with GPS Coordinates

Tests classification with GPS coordinates.

**Request body:**
```json
{
    "text": "Car accident on the highway with multiple injuries. Several vehicles involved, need urgent medical assistance.",
    "timestamp": "{{$isoTimestamp}}",
    "location": {
        "latitude": 37.7749,
        "longitude": -122.4194
    }
}
```

#### e. Classification with Full Data

Tests classification with all available data fields.

**Request body:**
```json
{
    "text": "Explosion at the mall, several people injured. Smoke everywhere and people are running towards the exits.",
    "timestamp": "{{$isoTimestamp}}",
    "location": {
        "address": "Westfield Shopping Center",
        "city": "San Francisco",
        "country": "USA",
        "latitude": 37.7833,
        "longitude": -122.4167
    },
    "user_id": "emergency-operator-123",
    "context": {
        "reporter_role": "security_personnel",
        "priority": "high"
    }
}
```

### 3. Testing Special Scenarios

These scenarios test the API's web data integration and handling of specific emergency types.

#### a. Public Event Emergency

Tests a public event emergency that should trigger web data integration.

**Request body:**
```json
{
    "text": "Stampede at the concert in the stadium. Multiple injuries reported as panic spreads through the crowd.",
    "timestamp": "{{$isoTimestamp}}",
    "location": {
        "address": "Oracle Park",
        "city": "San Francisco",
        "country": "USA"
    }
}
```

#### b. Hospital Emergency

Tests a hospital emergency that should trigger web data integration.

**Request body:**
```json
{
    "text": "Power outage at the hospital affecting critical care units. Backup generators failing. Need immediate assistance.",
    "timestamp": "{{$isoTimestamp}}",
    "location": {
        "address": "SF General Hospital",
        "city": "San Francisco",
        "country": "USA"
    }
}
```

#### c. Natural Disaster

Tests a natural disaster scenario.

**Request body:**
```json
{
    "text": "Earthquake just hit. Buildings shaking and some collapsing. Many people trapped in debris.",
    "timestamp": "{{$isoTimestamp}}",
    "location": {
        "latitude": 37.7749,
        "longitude": -122.4194
    }
}
```

### 4. Testing Error Handling

These scenarios test the API's error handling capabilities.

#### a. Text Too Short

Tests error handling for messages that are too short.

**Request body:**
```json
{
    "text": "Help"
}
```

**Expected error:**
```json
{
    "detail": "Text is too short for classification"
}
```

#### b. Invalid Location Data

Tests error handling for invalid location data.

**Request body:**
```json
{
    "text": "There is a fire in the building. People are trapped on the second floor.",
    "location": {
        "latitude": "invalid-data",
        "longitude": -122.4194
    }
}
```

#### c. Invalid Timestamp

Tests error handling for invalid timestamp format.

**Request body:**
```json
{
    "text": "There is a fire in the building. People are trapped on the second floor.",
    "timestamp": "invalid-timestamp-format"
}
```

## Running the Entire Collection

To run all tests in sequence:

1. Click on the collection name ("Emergency Text Classification API") in the sidebar
2. Click the "Run" button at the top of the collection
3. In the Collection Runner window, you can select which requests to run
4. Click "Run Emergency Text Classification API" button

## Examining Results

After each request, examine:

1. **Status Code**: Should be 200 for successful requests
2. **Response Body**: The `analysis` object should contain relevant information about the emergency
3. **Response Time**: Indicates API performance

## Automated Tests

The collection includes automated tests that verify:

1. Status code is 200
2. Response has the required fields (either `status` for health checks or `analysis` for classification)

You can view test results in the "Test Results" tab of the Postman response panel.

## Customizing the Collection

To use the collection with a different server address:

1. Click on the collection name ("Emergency Text Classification API")
2. Go to the "Variables" tab
3. Update the "baseUrl" variable with your server address

## Troubleshooting

If you encounter issues:

1. **Connection refused**: Ensure your API server is running
2. **404 errors**: Check the URL path and port number
3. **Validation errors**: Review the request body for syntax errors
4. **500 errors**: Check your server logs for exceptions 