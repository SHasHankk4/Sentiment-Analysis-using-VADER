import pandas as pd

# Load the dataset
df = pd.read_csv('Reviews.csv')

# Define sentiment labels based on score
df['Sentiment'] = df['Score'].apply(lambda x: 1 if x > 3 else 0)  # 1 for positive, 0 for negative

# Save the processed file
df.to_csv('processed_reviews.csv', index=False)
