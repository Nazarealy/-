Встанови бібліотеки tweepy для роботи з X API та textblob для аналізу настроїв:

pip install tweepy textblob

Опис коду
Імпорт бібліотек: Імпортуємо бібліотеки tweepy та textblob.
X API ключі: Встановлюємо ключі доступу до X API.
Аутентифікація до X API: Налаштовуємо аутентифікацію з використанням tweepy.OAuth1UserHandler.
Функція analyze_sentiment:
Аналізуємо настрій тексту за допомогою TextBlob.
Функція fetch_and_analyze_tweets:
Отримуємо останні 10 твітів користувача за допомогою tweepy.API.user_timeline.
Аналізуємо кожен твіт та додаємо його до списку tweet_data.
Отримання імені користувача X: Користувач вводить ім'я користувача X.
Отримання та аналіз твітів: Викликаємо функцію fetch_and_analyze_tweets.
Виведення результатів: Виводимо аналіз настрою для кожного твіту.
