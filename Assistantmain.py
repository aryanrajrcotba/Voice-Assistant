import pyttsx3
import speech_recognition as sr
import webbrowser
import wikipedia

# Initialize the speech recognition engine
r = sr.Recognizer()

# Initialize the text-to-speech engine
engine = pyttsx3.init()

# Function to speak
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Function to take command
def takeCommand():
    try:
        # Listen for audio
        with sr.Microphone() as source:
            print("Listening...")
            audio = r.listen(source)

        # Recognize the speech
        command = r.recognize_google(audio)
        print(f"User said: {command}")
    except sr.UnknownValueError:
        print("Could not understand audio")
        command = None
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")
        command = None

    return command

# Function to open YouTube
def openYouTube(search):
    webbrowser.open(f"https://www.youtube.com/results?search_query={search}")

# Function to search Wikipedia
def searchWikipedia(search):
    try:
        # Search Wikipedia for the given query
        results = wikipedia.summary(search, sentences=2)
        print(results)
        speak(results)
    except wikipedia.PageError:
        print(f"No page found for {search}")
        speak(f"No page found for {search}")

# Main loop
while True:
    # Take command from user
    command = takeCommand()

    if command:
        # Check if the user wants to open YouTube
        if "open YouTube" in command:
            search_term = command.replace("open YouTube", "")
            openYouTube(search_term)

        # Check if the user wants to search Wikipedia
        elif "search Wikipedia" in command:
            search_term = command.replace("search Wikipedia", "")
            searchWikipedia(search_term)

        # Other commands
        else:
            print("Invalid command")
            speak("Invalid command")
