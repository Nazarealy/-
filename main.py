import openai

openai.api_key = 'PLACE_FOR_API' # люшній раз не показую

def generate_recipe(ingredients):
    # Формування запиту до GPT
    prompt = f"У мене є такі інгредієнти: {', '.join(ingredients)}. Чи можете ви згенерувати рецепт, використовуючи ці інгредієнти?"

    # Виклик API GPT-3
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=200
    )

    # Отримання згенерованого рецепту
    recipe = response.choices[0].text.strip()
    return recipe

# Введення інгредієнтів користувачем
user_ingredients = input("Будь ласка, введіть список інгредієнтів через кому: ").split(',')

# Генерація рецепту
recipe = generate_recipe([ingredient.strip() for ingredient in user_ingredients])

# Виведення згенерованого рецепту
print("\nОсь рецепт, який ви можете спробувати:\n")
print(recipe)
