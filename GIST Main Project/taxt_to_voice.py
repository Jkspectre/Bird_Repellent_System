import pyaudio
import wave
import speech_recognition as sr     
 
r = sr.Recognizer()                 
#with sr.Microphone() as source:
source = wave.open('practice.wav')
print("Speak Anything :")
audio = r.listen(source)     
try:
    text = r.recognize_google(audio,language='en-US' )   
    print("You said : {}".format(text))
except:
    print("Sorry could not recognize your voice")    
