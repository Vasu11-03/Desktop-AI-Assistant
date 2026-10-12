# AIVA – AI Desktop Assistant

A desktop-based AI voice assistant built with Python and Tkinter. AIVA allows users to interact through voice commands or text input to perform everyday tasks, retrieve information, control desktop functions, and automate activities.

## Quick Start

### 1. Clone the Repository

```bash
git clone <your-repository-url>
cd <your-project-folder>
```

### 2. Create a Virtual Environment (Optional)

```bash
python -m venv venv
```

Activate the environment:

**Windows**
```bash
venv\Scripts\activate
```

### 3. Install Dependencies

Install the required Python libraries:

```bash
pip install pillow SpeechRecognition PyAudio pyttsx3 wikipedia pywhatkit pyautogui psutil schedule pygame PyMuPDF requests pyperclip pygetwindow googlesearch-python plyer beautifulsoup4 pandas
```

You may also need to install or configure additional dependencies used by your `speech_to_text.py`, `text_to_speech.py`, and `weather.py` modules.

### 4. Configure Project Files

Ensure the project contains the required Python modules and assets, including:

- `main.py` — Tkinter graphical interface
- `action.py` — command processing and assistant functionality
- `speech_to_text.py` — speech recognition functionality
- `text_to_speech.py` — voice response functionality
- `weather.py` — weather information retrieval
- `assistant.png` — assistant interface image

Update any hardcoded local file paths in the code to match your computer.

### 5. Run the Application

```bash
python main.py
```

The AIVA desktop interface will open, allowing you to interact using voice commands or text input.

## How It Works

1. Launch the AIVA desktop application.
2. Click **ASK** and speak a command through your microphone.
3. Alternatively, type a command into the text field and click **Send** or press Enter.
4. The `action.py` module processes the command and executes the corresponding operation.
5. AIVA displays the response in the chat area and provides spoken feedback for supported commands.
6. Use **Delete** to clear the conversation display.

## Features

- **Voice Interaction:** Recognizes spoken commands using SpeechRecognition and Google Speech Recognition.
- **Text Interaction:** Accepts typed commands through the graphical interface.
- **Voice Responses:** Uses text-to-speech to provide spoken feedback.
- **Time and Date:** Announces the current time and date.
- **Web Navigation:** Opens Google, YouTube, and other supported websites.
- **Music Control:** Opens Spotify and supports playback, pause, next-track, and previous-track commands.
- **Weather Information:** Retrieves weather information for a specified city.
- **Wikipedia Search:** Provides short summaries about people and topics.
- **WhatsApp Automation:** Supports sending messages and initiating voice or video calls through desktop keyboard automation.
- **To-Do List:** Adds tasks and displays the current task list.
- **Alarm Reminders:** Sets alarms with desktop notifications and sound alerts.
- **PDF Reader:** Opens PDF files and reads their text aloud.
- **News Headlines:** Retrieves and reads the top five US news headlines through NewsAPI.
- **Recipe Finder:** Searches for recipes and extracts available ingredient information.
- **Movie Recommendations:** Uses IMDb datasets to identify highly rated recent movies, with a language label in the response.
- **Desktop Automation:** Takes screenshots, adjusts system volume, minimizes windows, and arranges windows using keyboard shortcuts.

## Tech Stack

| Layer | Technology |
|---|---|
| Programming Language | Python |
| GUI | Tkinter |
| Image Processing | Pillow |
| Speech Recognition | SpeechRecognition, Google Speech Recognition |
| Text-to-Speech | pyttsx3 and custom text-to-speech module |
| Web Automation | PyAutoGUI, PyWhatKit, Webbrowser |
| Information Retrieval | Wikipedia, Google Search |
| Weather | Custom weather module |
| News | NewsAPI |
| PDF Processing | PyMuPDF |
| Data Processing | Pandas |
| Movie Data | IMDb datasets |
| Desktop Notifications | Plyer |
| System Utilities | psutil, winsound, pygetwindow |

## External Resources

AIVA uses several external services and data sources:

- **Google Speech Recognition:** Converts voice input into text.
- **Wikipedia:** Retrieves summaries about people and topics.
- **NewsAPI:** Retrieves top news headlines.
- **Allrecipes:** Used as a source for recipe searches.
- **IMDb datasets:** Supplies movie titles, release years, ratings, and vote counts.

Some features require an internet connection. Microphone access is required for voice input.

## Project Structure

```text
AIVA/
├── main.py
├── action.py
├── speech_to_text.py
├── text_to_speech.py
├── weather.py
├── assistant.png
├── requirements.txt
├── title.basics.tsv
└── title.ratings.tsv
```

The exact file structure may vary depending on your project setup.

## Notes

- This project is primarily designed for Windows because it uses Windows-specific features such as `winsound`, `os.startfile`, and Windows keyboard shortcuts.
- Spotify automation requires Spotify to be installed and its path configured correctly.
- WhatsApp automation relies on desktop UI interactions and may require adjustments if the interface changes.
- Movie recommendations require the IMDb datasets to be available in the expected location.
- NewsAPI and other external services may require valid API access.
- Keep API keys and other credentials out of public repositories. Store them in environment variables or a local `.env` file.

## Future Improvements

- Add a more conversational AI model for natural-language interactions.
- Improve error handling and command recognition.
- Store to-do lists and alarms persistently.
- Add a configurable settings panel for paths and API keys.
- Improve GUI responsiveness and thread-safe UI updates.
- Add unit tests and a dependency file for easier installation.

## License

Choose and add an appropriate license before distributing this project publicly.
