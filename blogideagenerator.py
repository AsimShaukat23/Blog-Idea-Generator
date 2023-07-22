import os
import requests
import streamlit as st

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
    openai_api_key = os.getenv('OPENAI_KEY')
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {openai_api_key}",
    }
    data = {
        "engine": "text-davinci-002",
        "prompt": prompt,
        "max_tokens": 60
    }

    try:
        response = requests.post("https://api.openai.com/v1/engines/text-davinci-002/completions", json=data, headers=headers)

        # Print the API response for debugging
        print("API Response:", response.json())

        # Check if the API response is successful
        if response.status_code == 200 and "choices" in response.json():
            return response.json()["choices"][0]["text"].strip()
        else:
            return "Error: Unable to generate blog ideas. Please check your input and try again."

    except Exception as e:
        # Handle any exceptions that occur during the API call
        print("Error during API call:", e)
        return "Error: Unable to generate blog ideas. An error occurred during the API call."

def main():
    st.title("Streamlit Blog Idea Generator")

    # Ask the user to select an intent
    intent = st.selectbox("Please select an intent:", intents)

    # Ask the user to enter a keyword
    keyword = st.text_input("Please enter a keyword:")

    # Show the themes for the selected intent
    theme = st.selectbox("Please select a theme:", themes[intent])

    # Generate blog ideas
    if st.button("Generate"):
        prompt = f"Create a list of unique titles based on the following keyword: {keyword} {theme}. The title must have the exact keyword, must be unique and must capture the audience's attention. The title must be SEO optimized in the best ways possible. The title must be between 50-60 characters. It should not exceed the character length described."
        blog_ideas = generate_blog_ideas(prompt)
        st.subheader("Here are some blog ideas:")
        st.write(blog_ideas)

if __name__ == "__main__":
    main()
