


import boto3
import json
import csv

# Initialize the Kinesis client
kinesis = boto3.client('kinesis', endpoint_url='http://localhost:4566')

# Open the CSV file containing the reviews
with open('processed_reviews_v2.csv', mode='r') as file:
    reader = csv.DictReader(file)
    
    # Iterate through the rows and stream them to Kinesis
    for row in reader:
        # Prepare the record to send to Kinesis
        record = {
            'Id': row['Id'],
            'ProductId': row['ProductId'],
            'UserId': row['UserId'],
            'ProfileName': row['ProfileName'],
            'HelpfulnessNumerator': row['HelpfulnessNumerator'],
            'HelpfulnessDenominator': row['HelpfulnessDenominator'],
            'Score': row['Score'],
            'Time': row['Time'],
            'Summary': row['Summary'],
            'Text': row['Text'],
        }
        # Send the data to Kinesis stream
        if row['Id']:
            kinesis.put_record(
            StreamName='reviews-stream',  # Your stream name
            Data=json.dumps(record),      # Data should be in JSON format
            PartitionKey=row['Id']        # Partition key is review Id
        )
        print(f"Sent record with ID: {row['Id']}")
        
    else:print(f"Skipped record with empty ID")