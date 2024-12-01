import random
responses = {
    "hello":["Hi there!", "Hello! How can I help you?", "Hey, how are you doing?"],
    "bye":["Goodbye!", "See you later!", "Bye!"],
    "thanks":["You're welcome!", "No problem!", "My pleasure!"],
    "how are you":["I'm doing great, thanks for asking!", "I'm good, how about you?", "I'm doing well, how can I help you?"],
    "default":["I'm sorry, I don't understand. Can you please rephrase?", "I'm not sure I understand. Can you please rephrase?", "I'm not sure how to help with that. Can you please rephrase?"],
}
def chatbot_response(user_message):
    user_message = user_message.lower()
    if user_message in responses:
        return random.choice(responses[user_message])
    else:
        return random.choice(responses["default"])
if __name__=="__main__":
    while True:
        user_message = input("You: ")
        if user_message == "exit":
            break
        response = chatbot_response(user_message)
        print("Chatbot: Hello! Type 'bye' to exit.")
        while True:
            user_message = input("You: ")
            if user_message.lower() == "bye":
                break
            response = chatbot_response(user_message)
            print("Chatbot:", response)