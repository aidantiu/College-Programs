# Ask for user input
# Convert the text to speech using the pyttsx3 init() function
# Initialize functions to convert text to speech


import pyttsx3

text_speech = pyttsx3.init()

answer = input("Enter the text you want to convert to speech: ")
text_speech.say(answer)
text_speech.runAndWait()