import gtts
from playsound import playsound
def txt_to_voice(str1):
    tts=gtts.gTTS(str1)
    tts.save("Hello.mp3")
    playsound("Hello.mp3")
            
Text=input("Enter the text to convert to voice: ")
txt_to_voice(Text)
