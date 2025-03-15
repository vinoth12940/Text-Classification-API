import requests
import json
from datetime import datetime
import argparse

def classify_emergency_message(text, timestamp=None, location=None):
    """
    Test the emergency classification API with the given text, timestamp, and location.
    
    Args:
        text (str): The emergency message to classify
        timestamp (datetime, optional): The timestamp of the message
        location (dict, optional): The location data
        
    Returns:
        dict: The API response
    """
    url = "http://127.0.0.1:8001/classify"
    
    # Prepare the payload
    payload = {"text": text}
    
    if timestamp:
        payload["timestamp"] = timestamp.isoformat()
        
    if location:
        payload["location"] = location
        
    # Make the API request
    headers = {"Content-Type": "application/json"}
    response = requests.post(url, json=payload, headers=headers)
    
    # Parse and return the response
    if response.status_code == 200:
        return response.json()
    else:
        return {"error": f"Request failed with status code {response.status_code}", "details": response.text}

def main():
    parser = argparse.ArgumentParser(description="Test emergency message classification with time and location")
    parser.add_argument("message", help="Emergency message to classify")
    parser.add_argument("--address", help="Address location")
    parser.add_argument("--city", help="City name")
    parser.add_argument("--country", help="Country name")
    parser.add_argument("--lat", type=float, help="Latitude coordinate")
    parser.add_argument("--lon", type=float, help="Longitude coordinate")
    args = parser.parse_args()
    
    # Prepare location data if provided
    location = None
    if any([args.address, args.city, args.country, args.lat, args.lon]):
        location = {}
        if args.address:
            location["address"] = args.address
        if args.city:
            location["city"] = args.city
        if args.country:
            location["country"] = args.country
        if args.lat is not None:
            location["latitude"] = args.lat
        if args.lon is not None:
            location["longitude"] = args.lon
    
    # Use current timestamp
    timestamp = datetime.now()
    
    # Call the API
    result = classify_emergency_message(args.message, timestamp, location)
    
    # Pretty print the result
    print(json.dumps(result, indent=2))

if __name__ == "__main__":
    main() 