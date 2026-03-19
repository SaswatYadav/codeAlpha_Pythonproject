def simple_chatbot():
    print("Chatbot: Hello! Type 'bye' to exit the chat.")
    
    while True:
        # 1. Capture user input and normalize it (lowercase)
        user_input = input("You: ").lower().strip()

        # 2. Rule-based Logic (if-elif-else)
        if user_input == "hello" or user_input == "hi":
            print("Chatbot: Hi there!")
            
        elif user_input == "how are you":
            print("Chatbot: I'm doing great, thanks for asking!")
            
        elif user_input == "bye" or user_input == "goodbye":
            print("Chatbot: Goodbye! Have a nice day.")
            break  # This exits the loop and ends the program
            
        else:
            print("Chatbot: I'm sorry, I don't understand that yet.")

# Run the chatbot
if __name__ == "__main__":
    simple_chatbot()