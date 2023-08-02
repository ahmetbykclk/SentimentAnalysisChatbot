## Sentiment Analysis Chatbot

This is a simple Python-based Sentiment Analysis Chatbot that uses the VADER (Valence Aware Dictionary and Sentiment Reasoner) lexicon from the Natural Language Toolkit (NLTK) library to analyze the sentiment of user input and respond accordingly.

## Table of Contents

- [Requirements](#requirements)
- [How it Works](#How-it-Works)
- [Usage](#usage)

## Requirements

- Python 3.x
- NLTK library (to install, run pip install nltk)

## How it Works

The Sentiment Analysis Chatbot works as follows:

1- It uses the VADER lexicon for sentiment analysis, which is a pre-trained model for text sentiment classification.

2-The chatbot prompts the user to enter a message.

3- The user's input is then analyzed for sentiment using the VADER model.

4- Based on the sentiment score obtained from VADER, the chatbot provides an appropriate response:

If the sentiment is positive (score >= 0.05), the chatbot responds with an encouraging message.

If the sentiment is negative (score <= -0.05), the chatbot expresses sympathy and offers assistance.

If the sentiment is neutral (score between -0.05 and 0.05), the chatbot expresses interest in the input.

## Usage

1- Clone the repository or download the SentimentAnalysisChatbot.py file.

2- Make sure you have Python 3.x installed on your system.

3- Install the required NLTK library by running pip install nltk.

4- Run the SentimentAnalysisChatbot.py script.

To use the chatbot, simply enter your message when prompted. To exit the conversation, type 'exit'.
