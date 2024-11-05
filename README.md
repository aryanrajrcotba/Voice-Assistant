# Voice-Assistant
This is a simple voice assistant application built with Python. The assistant listens for voice commands, interprets them, and performs actions like searching YouTube or looking up information on Wikipedia.

## Features
Speech Recognition: Uses Google Speech Recognition to convert voice commands into text.
Text-to-Speech (TTS): Utilizes pyttsx3 for speaking responses.
Web Interaction: Opens YouTube with the specified search term and retrieves summaries from Wikipedia.

## Requirements
Ensure you have the following Python packages installed:
pyttsx3: For text-to-speech functionality.
speech_recognition: To capture and interpret voice commands.
webbrowser: To open YouTube in a web browser.
wikipedia: For fetching Wikipedia summaries.

### To install these, run: pip install pyttsx3 SpeechRecognition wikipedia-api

# Usage
Initialize the assistant by running the script.

# Commands: Speak your command after the assistant starts listening. Supported commands include:
"open YouTube <search term>": Opens YouTube and searches for the specified term.
"search Wikipedia <search term>": Retrieves and reads a short Wikipedia summary of the specified term.

# Response: The assistant will respond audibly to valid commands or notify if it cannot understand the command.

## How It Works
Speech Recognition: The assistant listens to audio input via the microphone and uses Google Speech Recognition to transcribe the command.
Command Parsing: Based on keywords, the assistant distinguishes whether to open YouTube or search Wikipedia.
Error Handling: If the command is unclear or no relevant Wikipedia page is found, the assistant provides an error message.
Code Overview
speak(text): Speaks the text using the TTS engine.
takeCommand(): Listens for audio input and returns the transcribed text.
openYouTube(search): Opens YouTube with the search query.
searchWikipedia(search): Retrieves a brief summary from Wikipedia.

## Limitations
Requires an internet connection for both speech recognition and Wikipedia search.
Limited error handling for network issues or unclear audio input.
