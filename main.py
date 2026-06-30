import speech_recognition as sr
import webbrowser
import pyttsx3


recognizer = sr.Recognizer()
def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()
    engine.stop()
# speak("Hello,Sir! am Jarvis, your personal assistant. How can I help you today?")

if __name__ == "__main__":
    speak("Hello,Sir! am Jarvis, your personal assistant. How can I help you today?")
    while True:

        try:
            with sr.Microphone() as source:
                print("Listening for Jarvis...")
                audio = recognizer.listen(source,timeout=100,phrase_time_limit=10)
                print("Recognizing Jarvis...")
            wake = recognizer.recognize_google(audio)
            print(f"{wake}")
            if "jarvis" in wake.lower():
                print("Speaking to Jarvis")
                speak("Yes Sir, I am here to help you.")
                while True:
                    try:
                        with sr.Microphone() as source:
                            print("Listening...")
                            audio = recognizer.listen(source,timeout=10,phrase_time_limit=10)
                            print("Recognizing...")
                            command = recognizer.recognize_google(audio)
                            print(f"{command}")
                            if "open youtube" in command.lower():
                                speak("Opening YouTube")
                                webbrowser.open("https://www.youtube.com")
                            elif "open google" in command.lower():
                                speak("Opening Google")
                                webbrowser.open("https://www.google.com")
                            elif "open facebook" in command.lower():
                                speak("Opening Facebook")
                                webbrowser.open("https://www.facebook.com")
                            elif "open instagram" in command.lower():
                                speak("Opening Instagram")
                                webbrowser.open("https://www.instagram.com")
                            elif "who is gay" in command.lower():
                                speak("Raina is")
                            elif "how are you" in command.lower():
                                speak("I am fine, Sir. How are you?")
                            elif "fine" in command.lower():
                                speak("That's great to hear, Sir.")
                            elif "exit" in command.lower():
                                speak("Goodbye, Sir. Have a great day!")
                                exit()
                    except Exception as e:
                        print("Error:", str(e))
        except Exception as e:
            print("Error:", str(e))
            speak("Sorry, I didn't catch that. Please try again.")


