import json
import base64
import boto3
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

# Initialize DynamoDB client
dynamodb = boto3.client('dynamodb')

# Initialize VADER Sentiment Analyzer
analyzer = SentimentIntensityAnalyzer()

def lambda_handler(event, context):
    # Process each record in the event (since Kinesis sends multiple records at once)
    for record in event['Records']:
        # Decode the base64-encoded Kinesis data
        payload = base64.b64decode(record['kinesis']['data']).decode('utf-8')

        try:
            # Log the decoded payload to verify the structure
            print(f"Decoded Payload: {payload}")
            
            # Parse the decoded payload to JSON
            data = json.loads(payload)  # Now `data` is a dictionary
            
            # Check what fields exist in the payload
            print(f"Decoded Data: {data}")
            
            # Assuming the payload is in the form of a dictionary with the expected keys
            review_text = data['Text']  # Ensure these keys exist
            star_rating = data['Score']
            review_id = data['Id']

            # Perform sentiment analysis on the review text
            sentiment_score = analyzer.polarity_scores(review_text)['compound']
            
            # Create a result object with sentiment and other useful information
            result = {
                'review_id': review_id,
                'sentiment_score': sentiment_score,
                'star_rating': star_rating
            }

            # Save the result to DynamoDB
            dynamodb.put_item(
                TableName='sentiment-results',
                Item={
                    'review_id': {'S': result['review_id']},
                    'sentiment_score': {'N': str(result['sentiment_score'])},
                    'star_rating': {'N': str(result['star_rating'])}
                }
            )
        except Exception as e:
            print(f"Error processing record: {str(e)}")
            continue

    # Return a successful response
    return {
        'statusCode': 200,
        'body': json.dumps('Sentiment analysis completed and stored in DynamoDB')
    }
