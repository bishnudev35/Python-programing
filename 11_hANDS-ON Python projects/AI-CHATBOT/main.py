import os
from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv()

# Automatically loads GEMINI_API_KEY from your .env file
client = genai.Client()

# Create a chat session so Gemini remembers the conversation history automatically
chat = client.chats.create(
    model="gemini-3.5-flash-lite",
    config=types.GenerateContentConfig(
        system_instruction="You are Jarvis, a helpful and polite AI assistant."
    )
)

def completion(user_message):
    response = chat.send_message(user_message)
    print(f"Jarvis: {response.text}\n")

if __name__ == "__main__":
    print("Jarvis: Hi, I am Jarvis. How may I help you?\n")
    while True:
        user_question = input("User: ")
        if user_question.lower() in ["exit", "quit"]:
            print("Jarvis: Goodbye!")
            break
        completion(user_question)
