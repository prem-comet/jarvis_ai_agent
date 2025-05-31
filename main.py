import pyttsx3
import speech_recognition as sr
import random 
import webbrowser 
import datetime
from plyer import notification 
import time
import pyautogui
import wikipedia
import pywhatkit as pwk
import user_config
import smtplib , ssl



engine = pyttsx3.init()

voices = engine.getProperty('voices')       #getting details of current voice
engine.setProperty('voice', voices[1].id)

rate = engine.getProperty('rate')   # getting details of current speaking rate
print (rate)                        #printing current voice rate
engine.setProperty('rate', 200)
    




def speak(audio):
    engine.say(audio)
    engine.runAndWait()



def command():
    content = " "
    while content == " ":
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Say something!")
            audio = r.listen(source)
        try:
            content = r.recognize_google(audio, language = 'en-in')
            print("you said..." + content )
        except Exception as e :
            print("please try again ....")
        return content    

def main_process():
    while True:  
        request = command().lower()
        if "hello" in request:
            speak("welcome How can i help you ")
        elif "play music" in request: 
            song = random.randint(1,3)
            if song == 1:
                webbrowser.open("https://www.youtube.com/watch?v=mlWV7m2uH6o")
            elif song == 2:
                webbrowser.open("https://www.youtube.com/watch?v=n_oP9Onj0r0&list=RDGMEM916WJxafRUGgOvd6dVJkeQ&start_radio=1&rv=mlWV7m2uH6o")
            elif song == 3:
                webbrowser.open("https://www.youtube.com/watch?v=WnU0lH6C0EA&list=RDGMEM916WJxafRUGgOvd6dVJkeQ&index=3")
        elif "tell me time" in request:
            curr_time = datetime.datetime.now().strftime("%H :%M")
            speak("now current time is "+ str(curr_time))
            print(curr_time)

        elif "tell me date" in request:
            curr_date = datetime.datetime.now().strftime("%d %B %Y")
            speak("current date is "+ str(curr_date))
            print(curr_date)

        elif "new task" in request:
            task = request.replace("new task", " ")
            task = task.strip()
            if task != "":
                speak("adding task" +task )
                with open ("todo.txt" , "a")as file:
                    file.write(task + "\n")

        elif "speak task" in request:
            with open("todo.txt", "r") as file:
                text = file.read()
                if text != "":
                    print(text)
                    speak(text)
                # else:
                #     speak("there is no content inside file")
                #     print("nothing is here")
        elif "show work" in request:
            with open("todo.txt", "r") as file:
                tasks = file.read()
            notification.notify(
                title="Today's Work",
                message=tasks,
                app_name='Python Test App',
                # timeout=10   time after which it disappear ...but it is not working i will fix it later
            )
        elif "open youtube" in request:
            webbrowser.open("www.youtube.com")
        elif "open" in request:
            query = request.replace("open" , "")
            pyautogui.press("super")
            pyautogui.typewrite(query)
            pyautogui.sleep(3)
            pyautogui.press("enter")

        elif "wikipedia" in request:
            request = request.replace("jarvis" ,"")
            request = request.replace("search wikipedia", "")
            result = wikipedia.summary(request, sentences=2)
            speak(result)

        elif "search google" in request:
            request = request.replace("jarvis" ,"")
            request = request.replace("search google", "")
            webbrowser.open("https://www.google.com/search?q="+request)

        elif "send whatsapp" in request:
            request = request.replace("jarvis" ,"")
            request = request.replace("send whatsapp", "")
            # Same as above but Closes the Tab in 2 Seconds after Sending the Message
            pwk.sendwhatmsg("+917987788758", "Hi taklu behra chamunda", 1, 42, 30)
           
        # elif "send email" in request:
        #     pwk.send_mail("premkushwah7987788758@gmail.com", user_config.gmail_password, "hello", "how are u prem i am genius","rakeahtw256@gmail.com")

        # using library sending email this is alternate way of above lines code
        elif "send email" in request:
            s = smtplib.SMTP('smtp.gmail.com',587)
            s.starttls()
            s.login("premkushwah7987788758@gmail.com",user_config.gmail_password)
            message="""
            this is message 

            thanks by prem kushwah
            """
            s.sendmail( "premkushwah7987788758@gmail.com", "rakeahtw256@gmail.com", message)
            s.quit()
            speak("emailsent")
  

        
main_process()