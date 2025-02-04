import os
import pyttsx3
import speech_recognition as sr
from groq import Groq
from command_list import execute_command

# Initialize the voice engine
engine = pyttsx3.init()
engine.say("Initialization successful! How can I help you?")
engine.runAndWait()

voices = engine.getProperty("voices")

# Choosing an english voice
for voice in voices:
    if "en" in voice.id:
        engine.setProperty("voice", voice.id)
        break

# Get the API key from the environment
api_key = os.environ.get("GROQ_API_KEY")
if not api_key:
    print("Error: The Groq API key is not set. Please configure the 'GROQ_API_KEY' environment variable.")
    exit(1)

# Initialize the Groq API client
client = Groq(api_key=api_key)

while True:
    # Capture audio from the microphone
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Speak something...")
        audio = r.listen(source)

    try:
        text = r.recognize_google(audio, language="en").lower()
        print("You said:", text)
    except sr.UnknownValueError:
        print("Could not recognize speech.")
        continue
    except sr.RequestError:
        print("Error connecting to the speech recognition service.")
        continue

    # Check for predefined commands
    if execute_command(text):
        continue

    # If the command is "exit", terminate the program
    if "exit" in text:
        print("Exiting the program...")
        engine.say("Exiting the program")
        engine.runAndWait()
        break

    # Make a request to Groq
    chat_completion = client.chat.completions.create(
        messages=[
            {"role": "user", "content": text}
        ],
        model="llama-3.3-70b-versatile",
    )

    # Groq response
    response = chat_completion.choices[0].message.content
    print("Groq responded:", response)
    engine.say(response)
    engine.runAndWait()
