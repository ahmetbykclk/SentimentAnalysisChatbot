import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer

# Download the VADER lexicon if not already downloaded
nltk.download('vader_lexicon')

# Initialize the SentimentIntensityAnalyzer
analyzer = SentimentIntensityAnalyzer()

# Function to get the sentiment score of a text
def get_sentiment_score(text):
    return analyzer.polarity_scores(text)['compound']

# Function to get the sentiment label based on the sentiment score
def get_sentiment_label(score):
    if score >= 0.05:
        return 'positive'
    elif score <= -0.05:
        return 'negative'
    else:
        return 'neutral'

# Function to respond to user input based on sentiment
def chatbot_response(user_input):
    sentiment_score = get_sentiment_score(user_input)
    sentiment_label = get_sentiment_label(sentiment_score)

    if sentiment_label == 'positive':
        response = "I'm glad to hear that you're feeling positive!"
    elif sentiment_label == 'negative':
        response = "I'm sorry to hear that you're feeling negative. Is there anything I can do to help?"
    else:
        response = "That sounds interesting. Tell me more!"

    return response

# Main loop for the chatbot
if __name__ == "__main__":
    print("Chatbot: Hi, I'm your sentiment analysis chatbot. Type 'exit' to end the conversation.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            print("Chatbot: Goodbye!")
            break
        else:
            response = chatbot_response(user_input)
            print("Chatbot:", response)
