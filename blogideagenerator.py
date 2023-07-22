import os
import openai
import random

# Define the intents
intents = ["Informational", "Commercial", "Navigational", "Transactional"]

# Define some themes for each intent
themes = {
    "Informational": ["Education", "Research", "Advice", "Guides", "Tutorials"],
    "Commercial": ["Product Reviews", "Comparisons", "Best of Lists", "Deals", "Shopping Guides"],
    "Navigational": ["Locations", "Directions", "Maps", "Travel Guides", "Local Businesses"],
    "Transactional": ["Online Shopping", "Booking", "Ordering", "Subscriptions", "Services"],
}

# Function to generate blog ideas using the OpenAI API
def generate_blog_ideas(prompt):
    openai.api_key = os.getenv('OPENAI_KEY')  # Get the API key from the environment variable
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=60
    )
    return response.choices[0].text.strip()

# Ask the user to select an intent
print("Please select an intent:")
for i, intent in enumerate(intents, 1):
    print(f"{i}. {intent}")
intent_index = int(input("Enter the number of your choice: ")) - 1
intent = intents[intent_index]

# Ask the user to enter a keyword
keyword = input("Please enter a keyword: ")

# Show the themes for the selected intent
print("Please select a theme:")
for i, theme in enumerate(themes[intent], 1):
    print(f"{i}. {theme}")
theme_index = int(input("Enter the number of your choice: ")) - 1
theme = themes[intent][theme_index]

# Generate blog ideas
prompt = f"Create a list of unique titles based on the following keyword: {keyword} {theme}. The title must have the exact keyword, must be unique and must capture the audience's attention. The title must be SEO optimized in the best ways possible. The title must be between 50-60 characters. It should not exceed the character length described."
blog_ideas = generate_blog_ideas(prompt)
print("Here are some blog ideas:")
print(blog_ideas)
