import speech_recognition as sr
import pyttsx3

print("asdf")

r = sr.Recognizer()

def SpeakText(command):
  engine = pyttsx3.init()
  engine.say(command)
  engine.runAndWait()


with sr.Microphone() as source2:
  r.adjust_for_ambient_noise(source2, duration=0.2)
  audio2 = r.listen(source2)

  #using google to recognize audio
  text = r.recognize_google(audio2)

  SpeakText(text)