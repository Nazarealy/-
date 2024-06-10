Встанови бібліотеки tweepy для роботи з Twitter API та textblob для аналізу настроїв:

pip install tweepy textblob

Опис коду
Імпорт бібліотек: Імпортуємо бібліотеки tweepy та textblob.
Twitter API ключі: Встановлюємо ключі доступу до Twitter API.
Аутентифікація до Twitter API: Налаштовуємо аутентифікацію з використанням tweepy.OAuth1UserHandler.
Функція analyze_sentiment:
Аналізуємо настрій тексту за допомогою TextBlob.
Функція fetch_and_analyze_tweets:
Отримуємо останні 10 твітів користувача за допомогою tweepy.API.user_timeline.
Аналізуємо кожен твіт та додаємо його до списку tweet_data.
Отримання імені користувача Twitter: Користувач вводить ім'я користувача Twitter.
Отримання та аналіз твітів: Викликаємо функцію fetch_and_analyze_tweets.
Виведення результатів: Виводимо аналіз настрою для кожного твіту.
