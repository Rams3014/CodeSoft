import re
import datetime

def chatbot():
    print("Hello! I'm a chatbot. Type 'exit' to end the conversation.")
    
    while True:
    
        user_input = input("You: ").lower()
        
        if user_input == 'exit':
            print("Chatbot: Goodbye! Have a great day!")
            break
        
      
        elif re.search(r"hello|hi|hey", user_input):
            print("Chatbot: Namaste! How can I assist you today?")
        elif re.search(r"how are you", user_input):
            print("Chatbot: I'm doing well, thank you for asking! How are you?")
        elif re.search(r"your name", user_input):
            print("Chatbot: I'm a simple chatbot, you can call me Bot!")
        elif re.search(r"help", user_input):
            print("Chatbot: Sure! I can help with general queries like date and time, greetings, and more!")
        elif re.search(r"india|indian", user_input):
            print("Chatbot: India is a beautiful country known for its rich history, culture, and diverse traditions!")
        elif re.search(r"capital of tamil nadu", user_input):
            print("Chatbot: The capital of Tamil Nadu is Chennai.")
        elif re.search(r"madurai", user_input):
            print("Chatbot: Madurai is a historic city in Tamil Nadu, known for the famous Meenakshi Amman Temple and its rich cultural heritage.")
        elif re.search(r"god of cricket", user_input):
            print("Chatbot: The God of Cricket is often referred to as Sachin Tendulkar, one of the greatest cricketers of all time!")
        elif re.search(r"stock market big bull", user_input):
            print("Chatbot: The 'Big Bull' of the Indian stock market is often associated with Rakesh Jhunjhunwala, who was one of the most influential investors in India.")
        elif re.search(r"famous personalities", user_input):
            print("Chatbot: Some famous personalities from India include Mahatma Gandhi, Jawaharlal Nehru, Sachin Tendulkar, and APJ Abdul Kalam.")
        elif re.search(r"about isro", user_input):
            print("Chatbot: ISRO (Indian Space Research Organisation) is India's national space agency, responsible for the development of space missions, satellite launches, and space exploration. It has made significant achievements like the Mars Orbiter Mission (Mangalyaan) and Chandrayaan missions to the moon.")
        elif re.search(r"father of constitution", user_input):
            print("Chatbot: Dr. B.R. Ambedkar is known as the Father of the Indian Constitution.")
        elif re.search(r"father of computers", user_input):
            print("Chatbot: Charles Babbage is known as the Father of Computers for his pioneering work in the development of the first mechanical computer.")
        elif re.search(r"author of harry potter series", user_input):
            print("Chatbot: The author of the Harry Potter series is J.K. Rowling.")
        elif re.search(r"date|time", user_input):
            current_datetime = datetime.datetime.now()
            formatted_datetime = current_datetime.strftime("%d-%m-%Y %H:%M:%S")
            print(f"Chatbot: The current date and time in India is {formatted_datetime}.")
        elif re.search(r"bye|goodbye", user_input):
            print("Chatbot: Goodbye! Have a wonderful day!")
            break
        else:
            print("Chatbot: Sorry, I didn't understand that. Can you ask something else?")

chatbot()
