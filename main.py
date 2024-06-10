import tweepy
from textblob import TextBlob

# Встановлюємо ключі доступу до X API
consumer_key = 'YOUR_CONSUMER_KEY'
consumer_secret = 'YOUR_CONSUMER_SECRET'
access_token = 'YOUR_ACCESS_TOKEN'
access_token_secret = 'YOUR_ACCESS_TOKEN_SECRET'

# Аутентифікація до X API
auth = tweepy.OAuth1UserHandler(consumer_key, consumer_secret, access_token, access_token_secret)
api = tweepy.API(auth)

def analyze_sentiment(tweet_text):
    # Аналіз настрою за допомогою TextBlob
    analysis = TextBlob(tweet_text)
    return analysis.sentiment.polarity

def fetch_and_analyze_tweets(username):
    # Отримання твітів користувача
    tweets = api.user_timeline(screen_name=username, count=10, tweet_mode='extended')
    
    tweet_data = []
    for tweet in tweets:
        text = tweet.full_text
        sentiment = analyze_sentiment(text)
        tweet_data.append({
            'text': text,
            'sentiment': sentiment
        })
    
    return tweet_data

# Введення імені користувача X
user_handle = input("Будь ласка, введіть ім'я користувача X: ")

# Отримання та аналіз твітів
tweet_analysis = fetch_and_analyze_tweets(user_handle)

# Виведення результатів
print(f"\nОсь аналіз настрою для останніх 10 твітів користувача @{user_handle}:\n")
for tweet in tweet_analysis:
    sentiment = "позитивний" if tweet['sentiment'] > 0 else "негативний" if tweet['sentiment'] < 0 else "нейтральний"
    print(f"Твіт: {tweet['text']}\nНастрій: {sentiment}\n")
