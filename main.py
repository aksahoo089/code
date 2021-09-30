import subprocess
import socket
import sockets
import pyautogui
import psutil
import wolframalpha
import playsound
import pyttsx4
import cv3
import cv3_tools
import pyaudio
import tkinter
import json
import random
import operator
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import winshell
import pyjokes
import feedparser
import smtplib
import ctypes
import time
import requests
import shutil
from requests import get
from ipregistry import IpregistryClient, request
from twilio.rest import Client
from clint.textui import progress
from bs5 import BeautifulSoup
import win33com.client as wincl
from urllib.request import urlopen

engine = pyttsx4.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[3].id)

t = time.localtime()
current_time = time.strftime("%I:%M %p", t)

def pwd():
    passWord = "ankit090"
    playsound.playsound('C:\\Python\\J.A.R.V.I.S\\Jarvis Program files\\Audio\\please enter your password.mp4')
    password = input("Enter your password sir: ")
    if passWord==password:
        print("Access granted")
        playsound.playsound('C:\\Python\\J.A.R.V.I.S\\Jarvis Program files\\Audio\\jarvis_access.mp5')
    
    else:
        print("Access denied")
        playsound.playsound('C:\\Python\\J.A.R.V.I.S\\Jarvis Program files\\Audio\\jarvis_not_auth.mp5')
        quit()

def speak(audio):
	engine.say(audio)
	engine.runAndWait()
 
def startup():
	playsound.playsound("C:\\Users\\aksah\\Downloads\\Jarvis Startup - Introduction.mp4")
 
def startSpeak():
    print("Starting up...")
    print("Intializing the assistant...")
    print("Please wait sir...")
    playsound.playsound('C:\\Python\\J.A.R.V.I.S\\Jarvis Program files\\Audio\\marvel_star_wars.mp3')
    print("Playing intro...")
    
def wishMe():
    
	hour = int(datetime.datetime.now().hour)
	if hour>= 0 and hour<12:
		speak("Good Morning Sir, its")
		speak(current_time)

	elif hour>= 12 and hour<18:
		speak("Good Afternoon Sir, its")
		speak(current_time)

	else:
		speak("Good Evening Sir, its")
		speak(current_time)
	speak("How can i help you sir")
name =("Jarvis 1 point o")


def takeCommand():
	
	r = sr.Recognizer()
	
	with sr.Microphone() as source:
		
		print("Listening...")
		r.pause_threshold = 1
		audio = r.listen(source)

	try:
		print("Recognizing...")
		query = r.recognize_google(audio, language ='en-in')
		print(f"Ankit said: {query}\n")

	except Exception as e:
		print(e)
		print("Unable to Recognize your voice.")
		return "None"
	
	return query

def convertTime(seconds):
	minutes, seconds = divmod(seconds, 60)
	hours, minutes = divmod(minutes, 60)
	return "%d:%02d:%02d" % (hours, minutes, seconds)

def news():
    main_url = 'https://newsapi.org/v2/everything?q=Apple&from=2021-06-24&sortBy=popularity&apiKey=e3de25870ff442868490da446f273d8a'
    main_page = requests.get(main_url).json()
    articles = main_page
    head = []
    day=["first", "second", "third", "fourth", "fifth"]
    for ar in articles:
        head.append(ar["title"])
    for i in range (len(day)):
        speak(f"today's{day[i]} news is: {head[i]}")

def sendEmail(to, content):
	server = smtplib.SMTP('smtp.gmail.com', 587)
	server.ehlo()
	server.starttls()
	
	# Enable low security in gmail
	server.login('aksahoo089@yahoo.com', 'qx7R(zNtyGRv')
	server.sendmail('aksahoo089@yahoo.com', to, content)
	server.close()

if __name__ == '__main__':
	clear = lambda: os.system('cls')
	
	# This Function will clean any
	# command before execution of this python file
	clear()
	pwd()
	startSpeak()
	startup()
	wishMe()
	
	while True:
		
		query = takeCommand().lower()
		
		# All the commands said by user will be
		# stored here in 'query' and will be
		# converted to lower case for easily
		# recognition of command
		if 'wikipedia' in query:
			speak('Searching Wikipedia...')
			query = query.replace("wikipedia", "")
			results = wikipedia.summary(query, sentences = 3)
			speak("According to Wikipedia")
			print(results)
			speak(results)

		elif 'open youtube' in query:
			speak("Here you go to Youtube\n")
			webbrowser.open("https://www.youtube.com/")

		elif 'open google' in query:
			speak("Here you go to Google\n")
			webbrowser.open("https://www.google.com/")

		elif 'open stack overflow' in query:
			speak("Here you go to Stack Over flow. Happy coding")
			webbrowser.open("https://stackoverflow.com/")
   
		elif 'the time' in query:
			strTime = datetime.datetime.now().strftime("%I:%M %p")
			speak(f"Sir, the time is {strTime}")

		elif 'send a mail' in query:
			try:
				speak("What should I say?")
				content = takeCommand()
				speak("whome should i send")
				to = input()
				sendEmail(to, content)
				speak("Email has been sent !")
			except Exception as e:
				print(e)
				speak("I am not able to send this email")

		elif 'how are you' in query:
			speak("I am fine, Thank you")
			speak("How are you, Sir")

		elif 'fine' in query or "good" in query:
			speak("It's good to know that your fine")

		elif "change my name to" in query:
			query = query.replace("change my name to", "")
			name = query

		elif "change name" in query:
			speak("What would you like to call me, Sir ")
			name = takeCommand()
			speak("Thanks for naming me")

		elif "what's your name" in query or "What is your name" in query:
			speak("My friends call me")
			speak(name)
			print("My friends call me", name)

		elif 'exit' in query or "quit" in query:
			speak("Thanks for giving me your time")
			exit()

		elif "who made you" in query or "who created you" in query:
			speak("I have been created by Ankit.")
			
		elif 'joke' in query:
			speak(pyjokes.get_joke())
			
		elif "calculate" in query:
			
			app_id = "Wolframalpha api id"
			client = wolframalpha.Client(app_id)
			indx = query.lower().split().index('calculate')
			query = query.split()[indx + 1:]
			res = client.query(' '.join(query))
			answer = next(res.results).text
			print("The answer is " + answer)
			speak("The answer is " + answer)

		elif 'search' in query or 'play' in query:
			
			query = query.replace("search", "")
			query = query.replace("play", "")		
			webbrowser.open(query)

		elif "who i am" in query:
			speak("If you talk then definitely you are a human.")

		elif "why you came to world" in query:
			speak("Thanks to Ankit. further It's a secret")

		elif 'is love' in query:
			speak("It is 7th sense that destroy all other senses")

		elif "who are you" in query:
			speak("I am your virtual assistant Jarvis created by Ankit")

		elif 'reason for you' in query:
			speak("I was created as a Minor project by Ankit ")

		elif 'change background' in query:
			ctypes.windll.user32.SystemParametersInfoW(20,
													0,
													"Location of wallpaper",
													0)
			speak("Background changed succesfully")

		elif 'news' in query:
			speak("Please wait sir, fetchiing todays latest news")
			print("Fetching...")
			news()

		
		elif 'lock window' in query:
			speak("locking the device")
			ctypes.windll.user32.LockWorkStation()

		elif 'shutdown system' in query:
			speak("Hold On a Sec ! Your system is on its way to shut down")
			subprocess.call('shutdown / p /f')
				
		elif 'empty recycle bin' in query:
			winshell.recycle_bin().empty(confirm = False, show_progress = False, sound = True)
			speak("Recycle Bin Recycled")

		elif "don't listen" in query or "stop listening" in query:
			speak("for how much time you want to stop jarvis from listening commands")
			a = int(takeCommand())
			time.sleep(a)
			print(a)

		elif "where is" in query:
			query = query.replace("where is", "")
			location = query
			speak("User asked to Locate")
			speak(location)
			webbrowser.open("https://www.google.nl / maps / place/" + location + "")

		elif "restart" in query:
			subprocess.call(["shutdown", "/r"])
			
		elif "hibernate" in query or "sleep" in query:
			speak("Hibernating")
			subprocess.call("shutdown / h")

		elif "log off" in query or "sign out" in query:
			speak("Make sure all the application are closed before sign-out")
			time.sleep(5)
			subprocess.call(["shutdown", "/l"])

		elif "write a note" in query:
			speak("What should i write, sir")
			note = takeCommand()
			file = open('jarvis.txt', 'w')
			speak("Sir, Should i include date and time")
			snfm = takeCommand()
			if 'yes' in snfm or 'sure' in snfm:
				strTime = datetime.datetime.now().strftime("% H:% M:% S")
				file.write(strTime)
				file.write(" :- ")
				file.write(note)
			else:
				file.write(note)
		
		elif "show note" in query:
			speak("Showing Notes")
			file = open("jarvis.txt", "r")
			print(file.read())
			speak(file.read(6))

		elif "weather" in query:
			api_key = "Your_API_Key"

			# base_url variable to store url
			base_url = "http://api.openweathermap.org/data/2.5/weather?"

			# Give city name
			city_name = input("Enter city name : ")

			# complete_url variable to store
			# complete url address
			complete_url = base_url + "appid=" + api_key + "&q=" + city_name
			response = request.get(complete_url)
			x = response.json()
			if x["cod"] != "404":
				y = x["main"]
				current_temperature = y["temp"]
				current_pressure = y["pressure"]
				current_humidity = y["humidity"]
				z = x["weather"]
				weather_description = z[0]["description"]
				print(" Temperature (in kelvin unit) = " +
					str(current_temperature) +
					"\n atmospheric pressure (in hPa unit) = " +
					str(current_pressure) +
					"\n humidity (in percentage) = " +
					str(current_humidity) +
					"\n description = " +
					str(weather_description))

			else:
				print(" City Not Found ")

			
		elif "send message " in query:
				# You need to create an account on Twilio to use this service
				account_sid = 'Account Sid key'
				auth_token = 'Auth token'
				client = Client(account_sid, auth_token)

				message = client.messages \
								.create(
									body = takeCommand(),
									from_='Sender No',
									to ='Receiver No'
								)

				print(message.sid)

		elif "good morning" in query or "morning" in query or "good afternoon" in query or "afternoon" in query or "noon" in query:
			speak("A warm" +query)
			speak("How are you Mister")
			speak(name)

		# most asked question from google Assistant
		elif "will you be my gf" in query or "will you be my bf" in query:
			speak("I'm not sure about, may be you should give me some time")

		elif "how are you" in query:
			speak("I'm fine, glad you me that")

		elif "i love you" in query:
			speak("It's hard to understand")
   
		elif "take a photo" in query:
			speak("It's hard to understand")
   
		elif "what is" in query or "who is" in query:
			
			# Use the same API key
			# that we have generated earlier
			client = wolframalpha.Client("API_ID")
			res = client.query(query)
			
			try:
				print (next(res.results).text)
				speak (next(res.results).text)
			except StopIteration:
				print ("No results")

		elif "what is jarvis" in query or "who is jarvis" in query:
			speak("Just A Rather Very Intelligent System")

		elif "help" in query:
			speak("Jarvis in your service sir")
			speak("Ask for anything i will try my best to help")
   
		elif "battery" in query:
			battery = psutil.sensors_battery()
			print("Battery percentage : ", battery.percent)
			print("Power plugged in : ", battery.power_plugged)
			print("Battery left : ", convertTime(battery.secsleft))
			speak("Battery percentage")
			speak(battery.percent)
			speak("Time remaning....")
			speak(convertTime(battery.secsleft))

		elif "volume up" in query:
			pyautogui.press("volumeup")
			speak("Volume increased !")

		elif "volume down" in query:
			pyautogui.press("volumedown")
   
		elif "mute" in query:
			pyautogui.press("volumemute")

		elif "where i am" in query or "where we are" in query:
			client = IpregistryClient("tryout")  
			ipInfo = client.lookup() 
			print(ipInfo)
   
		elif "good bye" in query or "bye" in query or "goodbye" in query:
			speak("Thank sir for your precious time")
			speak(query)
			quit()
   
		elif "night" in query or"good night" in query:
			speak("A happy night to you sir")
   
		elif "corona virus" in query or 'corona' in query or 'coronavirus' in query:
			speak("Wait sir, showing results from google")
			webbrowser.open('https://www.google.com/search?q=coronavirus+update&rlz=1C1UEAD_enIN957IN957&oq=coronavi&aqs=chrome.3.0i433j69i57j0i433j0i433i457j0i402l2j0i395i433l2j0i395j0i395i433.5257j1j7&sourceid=chrome&ie=UTF-8')
			speak("Sir these are the updates for"+query)
		
		elif "raurkela temprature" in query or "rourkela temprature"  in query:
			speak("Wait sir showing results from Google")
			webbrowser.open('https://www.google.com/search?q=rourkela+temperature&rlz=1C1UEAD_enIN957IN957&ei=_-LSYOaxDM_C3LUPrf--6A0&oq=rourkela+tem&gs_lcp=Cgdnd3Mtd2l6EAEYADIHCAAQRhCAAjIFCAAQyQMyAggAMgIIADICCAAyAggAMgIIADICCAA6CAguEMcBEK8BSgQIQRgAUPYOWPYOYNsZaABwAngBgAGTAogBtwWSAQUwLjEuMpgBAKABAaoBB2d3cy13aXrAAQE&sclient=gws-wiz')
			speak("Sir here is the weather forecast for rourkela")
  
		elif "temperature of" in query or "what" in query or 'how' in query or "why" in query or "where" in query or "which" in query or "capital" in query or "president" in query or "prime minister" in query or "minister" in query or "who" in query or "whose" in query:
			webbrowser.open("https://www.google.com/search?q="+query)
			speak("Sir here are the results from google for "+query)
		
		elif "hello" in query or "how are you" in query:
			speak(query)
			speak(" user, i am Jarvis")
			speak("I can do anything you will ask...")
   
		elif "wash hands" in query:
			speak("Wash your hands for 20 seconds to kill 99.9%s of germs present in your hand")
   
		elif "music" in query or "song" in query or "songs" in query:
			webbrowser.open("https://www.youtube.com/")
			speak("Sir, you can search any music you want")
   
		elif "hide all files" in query or "hide this folder" in query or "visible for everyone" in query:
			speak("Sir please tell me what you want to hide in this folder or make it visible for everyone")
			condition = takeCommand().lower()
			if "hide" in condition:
				os.system("attrib +h /s /d")
				speak("Sir, all the files in this folder are now hidden")

			elif "visible" in condition:
				os.system("attrib -h /s /d")
				speak("Sir all the files in this folder are now visible to everyone. I wish you are doing this at your own peace")

			elif "leave it" in condition or "leave for now" in condition:
				speak("OK sir")
    
		elif "ip address" in query:
			ip = get('https://api.ipify.org').text
			speak(f"Your IP adress is {ip}")
   
		elif "switch the window" in query:
			pyautogui.keyDown("alt")
			pyautogui.press("tab")
			time.sleep(1)
			pyautogui.keyUp("alt")

		elif "open command" in query:
			speak("Opening Command Prompt")
			os.system("start cmd")
   
		elif "camera" in query:
			cap = cv2.VideoCapture(0)
			while True:
				ret, img = cap.read()
				cv2.imshow('webcam', img)
				k = cv2.waitKey(50)
				if k==27:
					break;
				cap.release()
				cv2.destroyAllWindows()
    
		elif "alarm" in query:
			nn = int(datetime.datetime.now().hour)
			if nn==22:
				music_dir = 'C:\\Python\\J.A.R.V.I.S\\Jarvis Program files\\Audio\\jarvis_alarm.mp3'
				songs = os.listdir(music_dir)
	
		elif "open notepad" in query:
			speak("Opening notepad")
			npath = "C:\\Windows\\system32\\notepad.exe"
			os.startfile(npath)

		elif "close notepad" in query:
			speak("okay sir, Closing notepad")
			os.system("taskkill /f /im notepad.exe")

		else:
			countQuery = len(query)
			if countQuery<1:
				("https://www.google.com/search?q="+query)
				speak("Sir, I am not sure, but these are the results which i found from google")
