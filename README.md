# Jarbis
Here's the **README.md** file for your project, outlining all the necessary steps and requirements.

---

# JARVIS - Desktop Voice Assistant

JARVIS is a Python-based desktop voice assistant capable of performing various tasks such as opening applications, fetching information from Wikipedia, playing music, taking screenshots, and more.

---

## **Features**
- Greet and interact with the user.
- Provide current time and date.
- Perform Wikipedia searches.
- Open commonly used websites (e.g., YouTube, Google, Stack Overflow).
- Play music from the user's system.
- Take screenshots.
- Remember and recall information.
- Open applications like Google Chrome.
- Perform voice-based searches on Chrome.

---

## **Prerequisites**
- **Python**: Ensure Python 3.7 or later is installed. Download it from [python.org](https://www.python.org/).
- Install the required Python libraries (listed below).

---

## **Installation**
1. Clone or download the repository to your local system.

2. Install the necessary Python packages:
   ```bash
   pip install pyttsx3
   pip install pyautogui
   pip install wikipedia
   pip install SpeechRecognition
   pip install pyaudio  # For microphone input
   pip install pywin32
   ```

3. Optional: Update `chromePath` to match the location of your Google Chrome installation.

---

## **How to Run**
1. Open a terminal or command prompt in the project directory.
2. Run the script:
   ```bash
   python jarvis.py
   ```

---

## **Usage**
- **Greeting**: Automatically greets the user and asks how it can assist.
- **Commands**:
  - **"time"**: Get the current time.
  - **"date"**: Get the current date.
  - **"who are you"**: Learn about JARVIS.
  - **"wikipedia"**: Search for information on Wikipedia.
  - **"open [application]"**: Opens applications or websites.
  - **"play music"**: Plays a random song from the system's music folder.
  - **"search on chrome"**: Perform a voice-based search on Google Chrome.
  - **"remember that"**: Ask JARVIS to remember specific information.
  - **"do you remember anything"**: Recall saved information.
  - **"screenshot"**: Take a screenshot.
  - **"offline"**: Exit the program.

---

## **Folder Structure**
```
jarvis/
├── jarvis.py          # Main script
├── data.txt           # File for storing remembered information
└── README.md          # Project documentation
```

---

## **Troubleshooting**
- **Audio Input Issues**:
  Ensure the microphone is properly connected and working. Check system permissions for microphone access.
  
- **Missing PyAudio**:
  If you encounter issues installing `pyaudio`, download the appropriate `.whl` file from [PyAudio unofficial binaries](https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyaudio) and install it manually:
  ```bash
  pip install [filename].whl
  ```

- **Application Path Errors**:
  Verify paths (e.g., Chrome) and update them in the script if needed.

---

## **Future Improvements**
- Integrate natural language processing (NLP) for more intuitive conversations.
- Add more features such as sending emails or controlling IoT devices.

---

Feel free to customize this README file based on your needs!
