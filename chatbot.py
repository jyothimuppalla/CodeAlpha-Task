import random

# A dictionary of predefined questions and responses
responses = {
    "hi": ["Hello!", "Hi there!", "Hey! How can I help you?"],
    "how are you": ["I'm good, thank you!", "I'm doing well, how about you?"],
    "bye": ["Goodbye!", "See you later!", "Have a great day!"],
    "what is your name": ["I am a chatbot.", "I'm your friendly chatbot!"],
    "default": ["I'm sorry, I didn't understand that.", "Can you please rephrase?", "I don't quite understand."]
}

def get_response(user_input):
    # Normalize the user input to lowercase
    user_input = user_input.lower()

    # Check if the user input matches any key in the responses dictionary
    for key in responses:
        if key in user_input:
            return random.choice(responses[key])
    
    # Return default response if no match is found
    return random.choice(responses["default"])

def chatbot():
    print("Chatbot: Hi! Type 'bye' to exit.")
    
    while True:
        user_input = input("You: ")
        
        # Exit the chatbot if the user types 'bye'
        if user_input.lower() == "bye":
            print("Chatbot: Goodbye!")
            break
        
        # Get and print the chatbot's response
        response = get_response(user_input)
        print(f"Chatbot: {response}")

# Run the chatbot
chatbot()
