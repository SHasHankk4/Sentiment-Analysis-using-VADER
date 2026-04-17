import base64
import json

# Create the payload data
payload_data = {
  "Text": "There is a great product",
  "Score": 5,
  "Id": "1"
}

# Convert payload to JSON
json_payload = json.dumps(payload_data)

# Encode the JSON string into base64
encoded_payload = base64.b64encode(json_payload.encode('utf-8')).decode('utf-8')

print(f"Base64 Encoded Payload: {encoded_payload}")
