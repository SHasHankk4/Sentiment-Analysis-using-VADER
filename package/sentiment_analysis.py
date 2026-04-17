import json
import base64
import boto3
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

# Initialize DynamoDB and VADER
dynamodb = boto3.client('dynamodb', endpoint_url="http://localhost:4566")
analyzer = SentimentIntensityAnalyzer()

def lambda_handler(event, context):
    for record in event['Records']:
        try:
            # Decode the base64-encoded data
            payload = base64.b64decode(record['kinesis']['data']).decode('utf-8')
            payload_json = json.loads(payload)

            # Ensure that payload contains the expected fields
            if 'Text' not in payload_json or 'Score' not in payload_json or 'Id' not in payload_json:
                print(f"Invalid payload: {payload_json}")
                continue

            # Perform sentiment analysis
            sentiment_score = analyzer.polarity_scores(payload_json['Text'])['compound']

            # Insert data into DynamoDB
            response = dynamodb.put_item(
                TableName='sentiment-results',
                Item={
                    'review_id': {'S': payload_json['Id']},
                    'sentiment_score': {'N': str(sentiment_score)},
                    'star_rating': {'N': str(payload_json['Score'])}
                }
            )
            print(f"Processed review: {payload_json['Id']}, Sentiment Score: {sentiment_score}")
            print(f"DynamoDB Response: {response}")
        except Exception as e:
            print(f"Error processing record: {str(e)}")
    
    return {
        'statusCode': 200,
        'body': json.dumps('Processed records successfully')
    }
