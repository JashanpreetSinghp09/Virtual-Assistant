import datetime
import os
import pyaudio
import pyttsx3
import wikipedia
import webbrowser
import speech_recognition as sr
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[-3].id)  # multiple types of voices can be applied to the virtual assistant using


# different IDs


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        speak("Good Morning Sir!")
    elif 12 <= hour < 18:
        speak("Good Afternoon Sir!")
    else:
        speak("Good Evening Sir")
    speak("I am JARVIS, How may i assist you")


# function sends an email to requested person which can be changed and updated, user may include as many contact
# emails as his/her choice

def sendEmail(to, message):  # this function can be modified with your email and password to work
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    # enter your email and password here, don't forgot to allow smtp from your email for this to work
    server.login('email-id@gmail.com', 'your-password')
    # enter your email here
    server.sendmail('email-id@gmail.com', to, message)
    server.close()


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.....")
        r.pause_threshold = 0.7
        audio = r.listen(source)

    try:
        print("Recognizing....")
        query_language = r.recognize_google(audio)
        print(f"User said: {query_language}\n")

    except Exception as e:
        print(e)

        print("Sorry, can you please repeat...")
        return "None"
    return query_language


if __name__ == '__main__':
    wishMe()
    var = True;  # say word 'dismiss' to end the program
    while var:
        inst = takeCommand().lower()
        # inst refer to the spoken instruction
        # This allows the user to get some piece of information directly from wikipedia
        if 'wikipedia' in inst:
            speak('Searching in Wikipedia')
            inst = inst.replace("wikipedia", "")
            results = wikipedia.summary(inst, sentences=3)  # number of sentences to be read can be edited.
            speak("According to Wikipedia")
            speak(results)

        # you can include many more unlimited number of websites you want to open here
        elif 'open youtube' in inst:
            webbrowser.open("youtube.com")
        elif 'open google' in inst:
            webbrowser.open("google.com")
        elif 'open stackoverflow' in inst:
            webbrowser.open("stackoverflow.com")
        elif 'github' in inst:
            webbrowser.open("https://github.com/")

        # play music directory can be changed according to allocation in your local machine
        elif 'play music' in inst:
            music_dir = 'path-name '  # here you can put the path of directory you have your music stored in to play
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))
        elif 'the time' in inst:
            str_time = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir the Time is {str_time}")


        # modify the paths of the files you want to open

        elif 'open code' in inst:  # opens VS code
            code_path = "C:\\Users\\Gesha\AppData\\Local\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(code_path)
        elif 'mortal kombat' in inst:  # opens a game from my pc
            game_path = "C:\\Games\\Mortal Kombat 11\\Binaries\\Retail\\MK11.exe"
            os.startfile(game_path)
        elif 'resume' in inst:  # opens my resume
            path = "C:\\Users\\Gesha\\Documents\\CV.pdf"
            os.startfile(path)
        elif 'chrome' in inst:  # opens chrome browser
            path = "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
            os.startfile(path)



        # sending email : this functionality can be modified you can change the recipients email address for this to
        # work also you can add as many recipients.

        elif 'email to jake' in inst:
            try:
                speak("what should i say Sir?")
                message = takeCommand()
                # enter recipient's email id here
                to = "emailid@gmail.com"
                sendEmail = (to, message)
                speak("Email has been sent Sir")
            except Exception as e:
                print(e)
                speak("Sorry unable to Send")

        # to give a feel like a real-world Virtual assistant, can add as many queries as the user wants to
        elif 'who are you' in inst:
            speak("My name is JARVIS, I am your Virtual Assistant ")
        elif 'dismiss' in inst:
            var = False
            speak("Bye Sir!!")
            continue
        else:
            speak("Sorry can you repeat Sir?")
            continue
    exit(1)
