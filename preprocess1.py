import pandas as pd

# Load the dataset
df = pd.read_csv('Reviews.csv')

# Handle missing values (if any)
df.fillna({'Text': '', 'Score': 0}, inplace=True)  # Fill missing reviews with empty string and scores with 0

# Create a new feature for the length of each review
df['Review_Length'] = df['Text'].apply(len)

# Sentiment Labeling based on score
# 1 for positive sentiment (Score > 3), 0 for negative sentiment (Score <= 3)
df['Sentiment'] = df['Score'].apply(lambda x: 1 if x > 3 else 0)

# Optional: Create a feature indicating if the review contains a certain keyword (e.g., "good", "bad")
df['Contains_Good'] = df['Text'].apply(lambda x: 1 if 'good' in x.lower() else 0)
df['Contains_Bad'] = df['Text'].apply(lambda x: 1 if 'bad' in x.lower() else 0)

# Save the processed data to a new CSV
df.to_csv('processed_reviews_v2.csv', index=False)

print("Data processing completed and saved to 'processed_reviews_v2.csv'.")
