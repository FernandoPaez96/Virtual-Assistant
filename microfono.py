import pyttsx3
from datetime import datetime
import speech_recognition as sr
from pydub import AudioSegment
from pydub.playback import play
from consulta_clima import clima
import pywhatkit

def welcome():
    engine = pyttsx3.init()
    voices = engine.getProperty("voices")
    engine.setProperty("voices", voices[1].id)
    engine.say("Bienvenido, soy tu asistente virtual, espero tus indicaciones!")
    engine.runAndWait()


def micro():

    song = AudioSegment.from_wav("ping.wav")

    r = sr.Recognizer()

    engine = pyttsx3.init()
    voices = engine.getProperty("voices")
    engine.setProperty("voices", voices[0].id)
    
    

    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source, duration=5)

        play(song)
        print("Di algo...")
        audio = r.listen(source)
        
        try:

            text = r.recognize_google(audio, language="es-ES")

            if "repro"in text.lower():
                music = text.lower().replace("reproduce", "")
                print("Reproduciendo " + music)
                engine.say("Reproduciendo:{}".format(music))
                pywhatkit.playonyt(music)
                engine.runAndWait()

            elif "hora" in text.lower():
                now = datetime.now()
                horas = now.hour
                minutos = now.minute
                hora = "Son las:{} horas {} minutos".format(horas, minutos)
                print(hora)
                engine.say(hora)
                engine.runAndWait()
            elif "clima" in text.lower():
                if "en" in text.lower():
                    texto = text.lower().split()
                    city = (texto[texto.index("en")+1])
                    engine.say(clima(city))
                    engine.runAndWait()
                else:
                    engine.say("Por favor se mas especifico")
                    engine.runAndWait()
            elif "búscame" in text.lower():
                texto = text.lower().split()
                search = ""
                texto = texto[texto.index("búscame")+1:]
                for n in texto:
                    search = search +" " + n
                print(pywhatkit.search(search))
            elif "busca" in text.lower():
                texto = text.lower().split()
                search = ""
                texto = texto[texto.index("busca")+1:]
                for n in texto:
                    search = search +" " + n
                print(pywhatkit.search(search))

            else:
                print("Dijiste: {}".format(text))
                engine.say("Dijiste:{}".format(text))
                engine.runAndWait()
        except:
            print(audio,"error")
    
    


if __name__ == "__main__":
    micro()