# Sentiment Analysis Using VADER

Small Python project for preprocessing Amazon reviews, streaming them through LocalStack Kinesis, and scoring sentiment with VADER in an AWS Lambda-style handler.

## Files

- `preprocess.py` and `preprocess1.py` prepare review data from `Reviews.csv`.
- `stream.py` sends processed review rows to a local Kinesis stream.
- `sentiment_analysis.py` reads review events and stores sentiment scores in DynamoDB.
- `test.py` and `test_event.json` provide a simple local event payload for testing.
- `docker-compose.yml` starts LocalStack for local AWS service emulation.

## Setup

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Notes

- Generated files, archives, vendored packages, and local database artifacts are intentionally excluded from Git.
- `boto3` is listed in `requirements.txt` for local development convenience.
