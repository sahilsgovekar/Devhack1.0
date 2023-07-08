import speech_recognition as sr

class TS:
    def __init__(self):
        # Initialize the recognizer
        self.r = sr.Recognizer()

    # Function to convert speech to text
    def speech_to_text(self):
        # Use the default microphone as the audio source
        with sr.Microphone() as source:
            # Adjust the timeout and phrase_time_limit parameters as per your requirements
            self.r.adjust_for_ambient_noise(source)
            print("Speak something...")
            audio = self.r.listen(source, timeout=5, phrase_time_limit=5)
            # print("p1")
            try:
                # Use Google Speech Recognition to convert audio to text
                text = self.r.recognize_google(audio)
                # print("p2")
                print("You said:", text)
                return text.lower()
            except sr.UnknownValueError:
                print("Sorry, could not understand audio.")
            except sr.RequestError as e:
                print("Sorry, could not request results. Error:", str(e))

# # Create an instance of the TS class
# t = TS()

# # Call the speech_to_text() method
# userin = t.speech_to_text()
