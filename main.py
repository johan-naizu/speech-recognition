import speech_recognition as sr
import threading

trigger=threading.Event()

def callback(recognizer, audio):
    try:
        text = recognizer.recognize_google(audio, language='en-US')
        print(f"\033[92mYou : {text}\033[0m")
        if 'stop' in text.lower() or 'exit' in text.lower() or 'quit' in text.lower() or 'bye' in text.lower() or 'goodbye' in text.lower() or 'close' in text.lower():
                print("\033[96mBye Bye!\033[0m")
                trigger.set()
    except sr.UnknownValueError:
        print("\033[93mGoogle could not understand audio\033[0m")
    except sr.RequestError as e:
        print(f"\033[93mCould not request results from Google Speech Recognition service; {e}\033[0m")
    except Exception as e:
        print(f"\033[93mUnknown exception occurred: {e}\033[0m")
def transribe():
    r=sr.Recognizer()
    mic = sr.Microphone()
    with mic as source: 
        r.adjust_for_ambient_noise(source)
    print("\033[96mListening...\033[0m")
    stop_listening = r.listen_in_background(mic, callback, phrase_time_limit=3)

    try:
        trigger.wait()
    except KeyboardInterrupt:
        print("\033[93mKeyboardInterrupt\033[0m")
    finally:
        stop_listening(wait_for_stop=False)


if __name__ == '__main__':
    transribe()

