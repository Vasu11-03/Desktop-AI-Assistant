import text_to_speech
import speech_to_text
import datetime
import webbrowser
import weather
import wikipedia
import pywhatkit
import os
import pyautogui
import psutil
import time
import time as time_module
import schedule
import pygame
import fitz 
import subprocess
import requests
import action
import pyperclip
import pygetwindow as gw
from googlesearch import search 
from plyer import notification
from bs4 import BeautifulSoup
import threading
import winsound
import pyttsx3
import pandas as pd
import text_to_speech


to_do_list = []

SPOTIFY_PATH = r"c:\Users\sanju\OneDrive\Desktop\Spotify.lnk"
def open_spotify():
    os.system(f'start {SPOTIFY_PATH}')
    time.sleep(5)

def focus_spotify():
    pyautogui.hotkey('alt', 'tab')

alarms = []

def set_alarm(task, alarm_time):
    alarms.append((task, alarm_time))
    threading.Thread(target=alarm_check, args=(task, alarm_time), daemon=True).start()
    return f"Alarm set for '{task}' at {alarm_time}"

def alarm_check(task, alarm_time):
    while True:
        current_time = time.strftime("%H:%M")  # 24-hour format
        if current_time == alarm_time:
            print("Alarm Time Reached!")
            notification.notify(
                title="Alarm Reminder",
                message=f"Time to {task}",
                timeout=10
            )
            for _ in range(5):
                winsound.Beep(1000, 500)
                time.sleep(1)
            break
        time.sleep(1)

def show_alarms():
    if alarms:
        alarm_list = "\n".join([f"{task} at {time}" for task, time in alarms])
        return f"Your Alarms:\n{alarm_list}"
    else:
        return "No alarms set."

def delete_alarm(task):
    for alarm in alarms:
        if alarm[0].lower() == task.lower():
            alarms.remove(alarm)
            return f"Alarm '{task}' deleted."
    return "Alarm not found."

#pdf
def get_chrome_processes():
    return {p.pid for p in psutil.process_iter(['name']) if p.info['name'] and 'chrome' in p.info['name'].lower()}

def is_any_chrome_process_alive(pids):
    for pid in pids:
        try:
            proc = psutil.Process(pid)
            if proc.is_running() and proc.status() != psutil.STATUS_ZOMBIE:
                return True
        except psutil.NoSuchProcess:
            continue
    return False

def open_pdf_and_read(pdf_path):
    if not os.path.exists(pdf_path):
        text_to_speech.text_to_speech("PDF file not found.")
        return "File not found."

    # Get existing Chrome processes before opening
    chrome_pids_before = get_chrome_processes()

    try:
        os.startfile(pdf_path)
        time.sleep(3)  # Wait for PDF to load in Chrome
    except Exception as e:
        text_to_speech.text_to_speech("Unable to open the PDF.")
        print("PDF open error:", e)
        return "Could not open PDF."

    try:
        with fitz.open(pdf_path) as doc:
            for page_num, page in enumerate(doc, start=1):
                if not is_any_chrome_process_alive(chrome_pids_before):
                    text_to_speech.text_to_speech("Chrome closed. Stopping reading.")
                    return "Stopped."

                text = page.get_text("text").strip()
                if text:
                    text_to_speech.text_to_speech(f"Reading page {page_num}")
                    text_to_speech.text_to_speech(text)
                else:
                    text_to_speech.text_to_speech(f"Page {page_num} is empty.")
                time.sleep(1)

        text_to_speech.text_to_speech("Finished reading the PDF.")
        return "Finished reading."

    except Exception as e:
        text_to_speech.text_to_speech("Error reading the PDF.")
        print("Read error:", e)
        return f"Error: {e}"

def get_news():
    api_key = "97f5512d12ef4f74a64149b91cfe66ec"
    url = f"https://newsapi.org/v2/top-headlines?country=us&apiKey={api_key}"

    response = requests.get(url)
    data = response.json()

    print("DEBUG: News API Response:", data)  # Debugging line

    if data.get("status") == "ok" and "articles" in data:
        articles = data["articles"][:5]  # Get top 5 articles
        headlines = [f"{i + 1}. {article['title']}" for i, article in enumerate(articles)]
        
        if headlines:
            news_summary = "Here are the top news headlines:\n" + "\n".join(headlines)
            text_to_speech.text_to_speech(news_summary)  # Speak the news
            return news_summary
        else:
            return "No news articles found."
    else:
        return "Sorry, I couldn't fetch the news at the moment."
    
def send_whatsapp(contact_name, message):
    try:
        # Open WhatsApp Desktop
        pyautogui.hotkey('win', 's')
        time.sleep(1)
        pyautogui.write('whatsapp')
        time.sleep(1)
        pyautogui.press('enter')
        time.sleep(5)

        # Search Contact
        pyautogui.hotkey('ctrl', 'f')
        time.sleep(1)
        pyperclip.copy(contact_name)
        pyautogui.hotkey('ctrl', 'v')
        time.sleep(1)

        # Select First Contact from Search Results
        pyautogui.press('down')
        time.sleep(1)
        pyautogui.press('enter')
        time.sleep(3)

        pyautogui.press('enter')
        time.sleep(2)

        pyperclip.copy(message)
        pyautogui.hotkey('ctrl', 'v')
        time.sleep(1)

        pyautogui.press('enter')

        return f"Message sent successfully to {contact_name}"

    except Exception as e:
        return f"Error: {str(e)}"
    
def make_whatsapp_call(contact_name):
    try:
        # Open WhatsApp Desktop
        pyautogui.hotkey('win', 's')
        time.sleep(1)
        pyautogui.write('whatsapp')
        time.sleep(1)
        pyautogui.press('enter')
        time.sleep(5)

        pyautogui.hotkey('ctrl', 'f')
        time.sleep(1)
        pyperclip.copy(contact_name)
        pyautogui.hotkey('ctrl', 'v')
        time.sleep(1)
        
        pyautogui.press('down')
        time.sleep(1)
        pyautogui.press('enter')
        time.sleep(3)

        for _ in range(5):   
            pyautogui.press('tab')
            time.sleep(0.3)

        pyautogui.press('enter')  
        time.sleep(2)

        return f"Voice Call started successfully with {contact_name}"

    except Exception as e:
        return f"Error: {str(e)}"
    
def make_video_call(contact_name):
    try:
        # Open WhatsApp Desktop
        pyautogui.hotkey('win', 's')
        time.sleep(1)
        pyautogui.write('whatsapp')
        time.sleep(1)
        pyautogui.press('enter')
        time.sleep(5)

        pyautogui.hotkey('ctrl', 'f')
        time.sleep(1)
        pyperclip.copy(contact_name)
        pyautogui.hotkey('ctrl', 'v')
        time.sleep(1)
        
        pyautogui.press('down')
        time.sleep(1)
        pyautogui.press('enter')
        time.sleep(3)

        for _ in range(4):   
            pyautogui.press('tab')
            time.sleep(0.3)

        pyautogui.press('enter')  
        time.sleep(2)

        return f"Voice Call started successfully with {contact_name}"

    except Exception as e:
        return f"Error: {str(e)}"

def load_imdb_data():
    # Load the datasets
    titles = pd.read_csv(r'C:\Users\sanju\OneDrive\Desktop\MAJOR\title.basics.tsv.gz', sep='\t', low_memory=False)
    ratings = pd.read_csv(r'C:\Users\sanju\OneDrive\Desktop\MAJOR\title.ratings.tsv.gz', sep='\t', low_memory=False)
        
    # Merge the datasets on the title ID
    merged_data = pd.merge(titles, ratings, on='tconst', how='inner')
    
    return merged_data

def load_imdb_data():
    basics = pd.read_csv("title.basics.tsv", sep="\t", dtype=str, na_values="\\N")
    ratings = pd.read_csv("title.ratings.tsv", sep="\t", dtype=str, na_values="\\N")

    merged = pd.merge(basics, ratings, on="tconst")
    merged = merged[merged["titleType"] == "movie"]
    merged = merged.dropna(subset=["primaryTitle", "startYear", "averageRating", "numVotes"])

    merged["startYear"] = pd.to_numeric(merged["startYear"], errors='coerce')
    merged["averageRating"] = pd.to_numeric(merged["averageRating"], errors='coerce')
    merged["numVotes"] = pd.to_numeric(merged["numVotes"], errors='coerce')

    return merged


def recommend_movies(language):
    try:
        data = load_imdb_data()
        print("IMDb data loaded successfully.")

        # Only trending = Recent + enough votes
        trending = data[
            (data["startYear"] >= 2024) & (data["numVotes"] >= 1000)
        ]

        # Get top 5 based on rating
        top_movies = trending.nlargest(5, "averageRating")

        if not top_movies.empty:
            movie_list = top_movies[["primaryTitle", "averageRating", "startYear"]]
            movies = "\n".join(
                f"{row['primaryTitle']} ({row['startYear']}) - Rating: {row['averageRating']}"
                for _, row in movie_list.iterrows()
            )
            return f"🔥 Trending Top 5 Movies (simulated in {language.title()}):\n{movies}"
        else:
            return f"Sorry, couldn't find trending movies in {language.title()}."

    except Exception as e:
        return f"Something went wrong while fetching movie details: {str(e)}"



def get_recipe(dish_name):
    try:
        query = f"{dish_name} recipe site:allrecipes.com"
        headers = {
            "User-Agent": "Mozilla/5.0"
        }

        # Use Google search to find a recipe link
        search_results = list(search(query, num_results=5))
        recipe_url = None
        for link in search_results:
            if "allrecipes.com/recipe" in link:
                recipe_url = link
                break

        if not recipe_url:
            return "Sorry, I couldn't find a recipe link from Google search."

        # Fetch and parse the recipe page
        recipe_page = requests.get(recipe_url, headers=headers, timeout=10)
        recipe_soup = BeautifulSoup(recipe_page.text, "html.parser")

        # Get the title
        title_tag = recipe_soup.find("h1")
        title = title_tag.get_text(strip=True) if title_tag else dish_name.capitalize()

        # Extract ingredients using various selectors
        ingredients = recipe_soup.select('[data-ingredient]')
        if not ingredients:
            ingredients = recipe_soup.select("span.ingredients-item-name")
        if not ingredients:
            ingredients = recipe_soup.select("li.ingredients-item")
        if not ingredients:
            ingredients = recipe_soup.select("div.section-body")

        ingredient_list = [item.get_text(strip=True) for item in ingredients if item.get_text(strip=True)]

        if ingredient_list:
            limited_ingredients = ingredient_list[:5]
            recipe_summary = f"Here's the recipe for {title}. You will need: " + ", ".join(limited_ingredients)
            text_to_speech.text_to_speech(recipe_summary)
            return recipe_summary
        else:
            # Fallback: Open the recipe in browser
            fallback_message = f"I've opened the recipe for {title} in your browser."
            webbrowser.open(recipe_url)
            text_to_speech.text_to_speech(fallback_message)
            return fallback_message

    except Exception as e:
        return f"An error occurred while fetching the recipe: {str(e)}"
    
def Action(data):
    user_data=data.lower()

    if "what is your name" in user_data:
        text_to_speech.text_to_speech("my name is aiva")
        return "my name is iva"

    elif "hello" in user_data or "hye" in user_data:
        current_hour = datetime.datetime.now().hour

        if current_hour < 12:
            greeting = "Good morning"
        elif 12 <= current_hour < 18:
            greeting = "Good afternoon"
        else:
            greeting = "Good evening"

        text_to_speech.text_to_speech(f"hey {greeting}, how can I help you?")
        return f"hey {greeting}, how can I help you?"

    elif "good morning" in user_data:
        text_to_speech.text_to_speech("good morning ma'am")
        return "good morning ma'am"
    
    elif "good afternoon" in user_data:
        text_to_speech.text_to_speech("good afternoon ma'am")
        return "good afternoon ma'am"
    
    elif "good evening" in user_data:
        text_to_speech.text_to_speech("good evening ma'am")
        return "good evening ma'am"


    elif "time now" in user_data:
        time=datetime.datetime.now().strftime('%I:%M%p')
        text_to_speech.text_to_speech(time)
        return time
    
    elif 'date' in user_data:
        date=datetime.datetime.now().strftime('%d /%m /%Y')
        text_to_speech.text_to_speech(date)
        return date
    

    elif "shutdown" in user_data:
        text_to_speech.text_to_speech("okay ma'am")
        return "okay ma'am"


    elif "play music" in user_data:
        webbrowser.open("http://gaana.com/")
        text_to_speech.text_to_speech("gaana.com ready for you")
        return "gaana.com ready for you"


    elif "open youtube" in user_data:
        webbrowser.open("http://youtube.com/")
        text_to_speech.text_to_speech("youtube.com ready for you")
        return "youtube.com ready for you"


    elif "open google" in user_data:
        webbrowser.open("http://google.com/")
        text_to_speech.text_to_speech("google.com ready for you")
        return "google.com ready for you"
    
    elif "weather of " in user_data :
        city = user_data.replace('weather of', ' ').strip()
        ans = weather .weather(city)
        text_to_speech.text_to_speech(ans)
        return ans

    elif "who is" in user_data.lower():
        person = user_data.lower().replace("who is", "").strip()
        try:
            info = wikipedia.summary(person, sentences=2)
            text_to_speech.text_to_speech(info)
            return info
        except wikipedia.exceptions.DisambiguationError as e:
            text_to_speech.text_to_speech("The name is ambiguous. Please be more specific.")
            return "Ambiguous input."
        except Exception as e:
            text_to_speech.text_to_speech("Sorry, I couldn't find information about that person.")
            return "No information found." 
        
    elif "what is" in user_data.lower():
        topic = user_data.lower().replace("what is", "").strip()
        try:
            info = wikipedia.summary(topic, sentences=2)
            text_to_speech.text_to_speech(info)
            return info
        except wikipedia.exceptions.DisambiguationError as e:
            text_to_speech.text_to_speech("Please be more specific.")
            return "Ambiguous input."
        except Exception as e:
            text_to_speech.text_to_speech("Sorry, I couldn't find information about that person.")
            return "No information found."

    elif "video song" in user_data:
        song=user_data.replace('play'," ")
        text_to_speech.text_to_speech("playing"+song)
        pywhatkit.playonyt(song)

    elif "open spotify" in user_data:
        open_spotify()  
        text_to_speech.text_to_speech("Spotify is opening")
        return "Spotify is opening"

    elif "play spotify" in user_data :
        focus_spotify()
        pyautogui.press('space')  
        text_to_speech.text_to_speech("playing song on Spotify")
        return "playing song on spotify"
    
    elif "pause spotify" in user_data :
        focus_spotify()
        pyautogui.press('space')  
        text_to_speech.text_to_speech("pausing the song")
        return "pausing the song"
    
    elif "next song" in user_data:
        focus_spotify()
        pyautogui.hotkey('ctrl', 'right') 
        text_to_speech.text_to_speech("Skipping to the next song on Spotify")
        return "Skipping to the next song on Spotify"
    
    elif "previous song" in user_data:
        focus_spotify()
        pyautogui.hotkey('ctrl', 'left')
        time.sleep(0.2)
        pyautogui.hotkey('ctrl', 'left')  
        text_to_speech.text_to_speech("Going to the previous song on Spotify")
        return "Going to the previous song on Spotify"
    
    elif "split screen left" in user_data:
        pyautogui.hotkey('alt', 'tab')  
        time_module.sleep(0.2) 
        pyautogui.hotkey('win', 'left')  
        text_to_speech.text_to_speech("Splitting the screen to the left")
        return "Splitting the screen to the left"

    elif "split screen right" in user_data:
        pyautogui.hotkey('alt', 'tab')  
        time_module.sleep(0.2) 
        pyautogui.hotkey('win', 'right') 
        text_to_speech.text_to_speech("Splitting the screen to the right")
        return "Splitting the screen to the right"

    elif "split screen up" in user_data:
        pyautogui.hotkey('alt', 'tab')  
        time_module.sleep(0.2) 
        pyautogui.hotkey('win', 'up')  
        text_to_speech.text_to_speech("Splitting the screen to the top")
        return "Splitting the screen to the top"

    elif "split screen down" in user_data:
        pyautogui.hotkey('alt', 'tab')  
        time_module.sleep(0.2)
        pyautogui.hotkey('win', 'down') 
        text_to_speech.text_to_speech("Splitting the screen to the bottom")
        return "Splitting the screen to the bottom"

    elif "create to do list" in user_data:
        task = user_data.replace("create to do list", "").strip()
        if task:
            to_do_list.append(task)
            text_to_speech.text_to_speech(f"Task {task} has been added to you to do list")
            return f"Task {task} has been added to you to do list"
        else:
            text_to_speech.text_to_speech("please specify the task")
            return "please specify the task"
        
    elif "show to do list" in user_data:
        if not to_do_list:
            text_to_speech.text_to_speech("Your to do list is empty")
            return "Your to do list is empty"
        task_output = ""
        for i, task in enumerate(to_do_list):
            task_output += f"Task {i + 1}: {task}"

        text_to_speech.text_to_speech(f"Your to dolist contains {len(to_do_list)} tasks: {task_output}")
        return f"Your to do list contains:\n" + '\n'.join([f"{i + 1}. {task}" for i, task in enumerate(to_do_list)])
  
    elif "open and read pdf" in user_data:
        text_to_speech.text_to_speech("Please provide the PDF file path.")
        pdf_path = input("Enter the full PDF path: ").strip().replace('"', '')

        if os.path.exists(pdf_path):
            result = open_pdf_and_read(pdf_path)
            return result
        else:
            text_to_speech.text_to_speech("Invalid file path. Please check and try again.")
            return "Invalid file path."

            
    elif "news" in user_data:
        ans = get_news()  
        print(ans)  
        return ans  
    
    elif "recipe of" in user_data or "recipe for" in user_data:
        dish = user_data.replace("recipe of", "").replace("recipe for", "").strip()
        ans = get_recipe(dish)
        return ans

    elif "increase volume" in user_data:
        for _ in range(5):
            pyautogui.press("volumeup")
        text_to_speech.text_to_speech("volume increased")
        return "Increasing volume"

    elif "decrease volume" in user_data:
        for _ in range(5):
            pyautogui.press("volumedown")
        text_to_speech.text_to_speech("volume decreased")
        return "Decreasing volume"

    elif "mute" in user_data:
        pyautogui.press("volumemute")
        return "Muting system volume"
    
    elif "minimize all" in user_data:
        pyautogui.hotkey("win", "d")
        text_to_speech.text_to_speech("All windows minimized")
        return "All windows minimized"
    
    elif "take screenshot" in user_data or "screenshot" in user_data:
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        screenshot_path = os.path.join(os.getcwd(), f"screenshot_{timestamp}.png")
        pyautogui.screenshot(screenshot_path)
        text_to_speech.text_to_speech(f"Screenshot taken and saved as {screenshot_path}")
        return f"Screenshot saved at: {screenshot_path}"
    
    elif "send message" in user_data:
        try:
            
            user_data = user_data.replace("send message to ", "")
            contact_name, message = user_data.split(" ", 1)
            result = send_whatsapp(contact_name, message)
            return result

        except Exception as e:
            return "Sorry, I didn't understand the contact or message."
    
    elif "make a call to" in user_data:
        try:
            user_data = user_data.replace("make a call to ", "")
            contact_name = user_data.split(" ", 1)
            result = make_whatsapp_call(contact_name)
            return result
        except Exception as e:
            return "Sorry, I didn't understand the contact or message"
        
    elif "make a video to" in user_data:
        try:
            user_data = user_data.replace("make a call to ", "")
            contact_name = user_data.split(" ", 1)
            result = make_video_call(contact_name)
            return result
        except Exception as e:
            return "Sorry, I didn't understand the contact or message"
    elif "recommend movies in" in user_data.lower():
        try:
            language = user_data.lower().replace("recommend movies in", "").strip()
            
            if not language:
                print("Please specify a language.")
            else:
                result = recommend_movies(language)
                print(result)

        except Exception as e:
            print(f"Sorry, something went wrong: {str(e)}")


    elif "set alarm" in user_data:
        if "at" in user_data:
            task = user_data.split("set alarm")[1].split("at")[0].strip()
            time_str = user_data.split("at")[1].strip()
            response = set_alarm(task, time_str)
        else:
            response = "Please specify time using 'at' keyword."

        text_to_speech.text_to_speech(response)
        return response

    elif "delete alarm" in user_data:
        text_to_speech.text_to_speech("Which alarm do you want to delete?")
        task = speech_to_text.speech_to_text()
        response = delete_alarm(task)
        text_to_speech.text_to_speech(response)
        return response

    elif "show alarms" in user_data:
        response = show_alarms()
        text_to_speech.text_to_speech(response)
        return response


    else:
        text_to_speech.text_to_speech("I am not able to understand")
        return "I am not able to understand"

