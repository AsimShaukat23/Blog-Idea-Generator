# Blog-Idea-Generator

Streamlit Blog Idea Generator - README
Introduction
This is a Streamlit-based Blog Idea Generator application. The application makes use of OpenAI's GPT-4 model to generate unique and attention-capturing blog post titles. The user can specify an intent and a theme for the blog post. A keyword can also be given as input which is incorporated into the generated blog post titles. The generated titles are SEO optimized and adhere to an appropriate length.

Prerequisites
Python 3.6 or above
An OpenAI account with API Key for GPT-4
Required Python Libraries
openai
os
streamlit
Setup
Clone this repository or download the Python script.

Install the required Python libraries, if not already installed. You can use pip to install them:

bash
Copy code
pip install streamlit openai
Get your OpenAI API Key. Go to the OpenAI website and create a new account if you don't have one. You will find your API key in the OpenAI Dashboard.

Set your OpenAI API Key as an environment variable on your machine. You can do it with the following command in your terminal:

bash
Copy code
export OPENAI_KEY="your-api-key-here"
How to Run
Open your terminal and navigate to the directory where you have saved the Python script.

Run the following command:

bash
Copy code
streamlit run your_script_name.py
Your Streamlit app will open in a new tab on your default web browser.

How to Use
Select an intent from the provided list.

Enter a keyword of your choice.

Based on your selected intent, a list of themes will be shown. Select a theme from the list.

Click on the "Generate" button.

The application will generate unique blog post titles incorporating the selected intent, theme, and keyword.

Enjoy your newly found blog post ideas!

Disclaimer
This application is for idea generation purposes only. It is not guaranteed that all generated ideas will be unique or applicable to all situations. User discretion is advised.
