import random

# Define a list of possible user greetings and bot responses
greetings = ["hello", "hi", "hey", "greetings", "good day"]
bot_responses = ["Hello! How can I assist you today?", "Hi there! How may I help you?", "Hey! How can I be of service?"]

# Define a list of possible user questions and bot responses
questions = ["how are you?", "what can you do?", "what are your hours?"]
question_responses = ["I'm a chatbot, so I don't have feelings, but thank you for asking!",
                     "I can provide information, answer questions, and assist with various tasks.",
                     "I'm available 24/7 to assist you!"]

# Define a list of possible user farewells and bot responses
farewells = ["bye", "goodbye", "see you", "take care"]
farewell_responses = ["Goodbye! Have a great day!", "Take care! See you next time.", "Goodbye! Feel free to come back anytime."]

# Function to generate a random response from a list of possible responses
def generate_response(responses):
    return random.choice(responses)

# Main chat loop
while True:
    user_input = input("User: ").lower()

    # Check for greetings
    if user_input in greetings:
        bot_response = generate_response(bot_responses)
        print("Bot:", bot_response)

    # Check for questions
    elif user_input in questions:
        bot_response = generate_response(question_responses)
        print("Bot:", bot_response)

    # Check for farewells
    elif user_input in farewells:
        bot_response = generate_response(farewell_responses)
        print("Bot:", bot_response)
        break

    else:
        print("Bot: Sorry, I didn't understand. Can you please rephrase your question?")
