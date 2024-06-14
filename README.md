# Reddit Sentiment Analysis

This program navigates through Reddit, identifies the most frequently mentioned stock tickers, and employs the Vader SentimentIntensityAnalyzer to calculate the compound sentiment value for each ticker.

## Program Parameters

```python
subs = []           # List of subreddits to search
post_flairs = {}    # Dictionary of post flairs to search; if None, all flairs are considered
goodAuth = {}       # Dictionary of authors whose comments can be counted multiple times
uniqueCmt = True    # Boolean to allow only one comment per author per symbol
ignoreAuthP = {}    # Set of authors to ignore for posts
ignoreAuthC = {}    # Set of authors to ignore for comments
upvoteRatio = 0.70  # Minimum upvote ratio for a post to be considered (0.70 = 70%)
ups = 100           # Minimum number of upvotes for a post to be considered
limit = 500         # Limit for 'replace more' in comments
upvotes = 20        # Minimum number of upvotes for a comment to be considered
picks = 10          # Number of top picks to display
picks_ayz = 5       # Number of top picks for sentiment analysis

### How to Run
pip install -r requirements.txt
python3 reddit-sentiment-analysis.py

### Sample Output
Analysis took 1574.61 seconds for 14236 comments across 8 posts in 1 subreddit.

Posts analyzed are saved in 'titles.txt'.

Top 10 most mentioned picks:
GME: 764 mentions
SPCE: 183 mentions
PLTR: 89 mentions
TSLA: 71 mentions
MVIS: 42 mentions
NVDA: 34 mentions
AMD: 30 mentions
F: 29 mentions
TLRY: 29 mentions
AAPL: 26 mentions

Sentiment analysis of top 5 picks:
Ticker  Bearish Neutral Bullish Total/Compound
GME     0.087   0.707   1.548   0.030
SPCE    0.119   0.645   1.618   0.027
PLTR    0.073   0.649   1.751   0.032
TSLA    0.088   0.650   1.543   0.049
MVIS    0.155   0.698   1.714  -0.020

The sentiment analysis visualizations are saved as ‘mentioned.png’ and ‘sentiment.png’.

### Data
The analysis includes U.S. stocks with a market cap greater than $100 million and a price above $3. Penny stocks are excluded. The data can be downloaded from the following source: US Stocks Data



