import speech_recognition as sr
import pyttsx3

class Speech:
    def __init__(self) -> None:
        # initilise speech to text
        self.s2t = sr.Recognizer()
        self.r = sr.Recognizer()
        # initilise text to speech 
        self.t2s = pyttsx3.init()
        self.voice = self.t2s.getProperty('voices')
        # self.t2s.setProperty('voice', self.voice[1].id)
        self.t2s.setProperty('voice', self.voice[1].id if len(self.voice) > 1 else self.voice[0].id)


    # def Speech2Text(self) -> str:
    #     with sr.Microphone() as source:
    #         self.s2t.adjust_for_ambient_noise(source)
    #         print("mic reaady")

    #         listned_text = self.s2t.listen(source, phrase_time_limit=3)
    #         print(f"c1 {listned_text}")

    #         try:
    #             converted_text = self.s2t.recognize_google(listned_text)
    #             print(converted_text)
    #             return converted_text.lower()
    #         except:
    #             print("error")
    #             return "error in recognition"

    def Speech2Text (self):
            with sr.Microphone() as source:
                self.r.adjust_for_ambient_noise(source)
                print("Speak something...")
                audio = self.r.listen(source, timeout=5, phrase_time_limit=5)
                print("p1")
                try:
                    # Use Google Speech Recognition to convert audio to text
                    text = self.r.recognize_google(audio)
                    print("p2")
                    print("You said:", text)
                    return text.lower()
                except sr.UnknownValueError:
                    print("Sorry, could not understand audio.")
                except sr.RequestError as e:
                    print("Sorry, could not request results. Error:", str(e))
            

    def Text2Speech(self, message):
        self.t2s.say(message)
        self.t2s.runAndWait()


# s = Speech()

# print(s.speech_to_text())

