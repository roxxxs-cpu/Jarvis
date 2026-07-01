import speech_recognition as sr
import webbrowser
import pyttsx3
import songs
import spotipy

from dotenv import load_dotenv
import os

load_dotenv()

clientid = os.getenv("clientid")
clientsecret = os.getenv("clientsecret")
clienturi = os.getenv("clienturi")

from spotipy.oauth2 import SpotifyOAuth
sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        client_id=clientid,
        client_secret=clientsecret,
        redirect_uri=clienturi,
        scope="user-read-playback-state user-modify-playback-state"
    )
)

recognizer = sr.Recognizer()
def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()
    engine.stop()
# speak("Hello,Sir! am Jarvis, your personal assistant. How can I help you today?")
def processcommand():
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

    elif "play" in command.lower():

        song_name = command.lower().replace("play", "").strip()

        try:
            result = sp.search(
                q=song_name,
                type="track",
                limit=2)
            

            track = result["tracks"]["items"][0]

            uri = track["uri"]

            devices = sp.devices()["devices"]

            if not devices:
                speak("No active Spotify device found.")
                return

            device_id = devices[0]["id"]

            sp.start_playback(
                device_id=device_id,
                uris=[uri]
            )

            speak(f"Playing {track['name']} by {track['artists'][0]['name']}")

        except Exception as e:
            print(e)
            speak("Sorry Sir, I couldn't play that song.")

    elif "pause" in command.lower():
        sp.pause_playback()
        speak("Music paused.")

    elif "resume" in command.lower():
        sp.start_playback()
        speak("Resuming music.")

    elif "next" in command.lower():
        sp.next_track()
        speak("Skipping.")

    elif "previous" in command.lower():
        sp.previous_track()
        speak("Going back.")
    
    elif "exit" in command.lower():
        speak("   Goodbye, Sir. Have a great day!")
        exit()

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
                            processcommand()
                    except Exception as e:
                        print("Error:", str(e))
        except Exception as e:
            print("Error:", str(e))


