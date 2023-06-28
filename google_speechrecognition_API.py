import speech_recognition as sr
import webbrowser

# Set the microphone device index
sr.Microphone(device_index=1)

r = sr.Recognizer()
r.energy_threshold = 5000

with sr.Microphone() as source:
    print('Speak!!')
    audio = r.listen(source)
    
    try:
        text = r.recognize_google(audio)
        print('You Said: {}'.format(text))
        
        url = "https://www.google.co.in/search?q="
        search_url = url + text
        webbrowser.open(search_url)
        
    except sr.UnknownValueError:
        print('Could not understand audio')
        
    except sr.RequestError as e:
        print('Could not request results; {0}'.format(e))