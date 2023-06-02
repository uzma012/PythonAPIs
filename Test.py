import speech_recognition as sr

# Initialize recognizer class (for recognizing the speech)
r = sr.Recognizer()

# Reading Microphone as source
with sr.Microphone() as source:
    print("Speak anything:")
    # Adjust for ambient noise
    r.adjust_for_ambient_noise(source)
    # Record audio
    audio = r.listen(source)
# Speech recognition using Google Speech Recognition
try:
    recog = r.recognize_google(audio, language='en-US')
    print(recog)
except sr.UnknownValueError:
    print("Google Speech Recognition could not understand audio")
except sr.RequestError as e:
    print(
        "Could not request results from Google Speech Recognition service; {0}".format(e))