A simple and beginner-friendly Python desktop application that converts spoken words into text using a microphone.

## ✨ Features

- 🎤 Voice input through microphone
- 📝 Speech-to-text conversion
- 🖥️ Clean Tkinter desktop interface
- 🧹 Clear recognized text
- 💾 Save text to a `.txt` file
- ⚠️ Handles microphone, timeout, and recognition errors

## 🛠️ Technologies

- Python 3
- Tkinter
- SpeechRecognition
- PyAudio
- Google Speech Recognition API

## 📁 Project Structure

```text
Speech_Recognition_System/
├── speech_recognition_app.py
├── requirements.txt
├── .gitignore
├── README.md
└── docs/
    └── PROJECT_REPORT.md
```

## 🚀 Installation

### 1. Clone the repository

```bash
git clone https://github.com/YOUR-USERNAME/Speech-Recognition-System.git
cd Speech-Recognition-System
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

Windows:

```bash
venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the application

```bash
python speech_recognition_app.py
```

## 🎯 How to Use

1. Connect a working microphone.
2. Run the Python application.
3. Click **Start Speaking**.
4. Speak clearly.
5. The recognized text appears in the text area.
6. Click **Save Text** to save the result.

## 🧠 How It Works

```text
Microphone
    ↓
Audio Capture
    ↓
SpeechRecognition Library
    ↓
Google Speech Recognition
    ↓
Text
    ↓
Tkinter GUI
    ↓
Save as TXT
```

## ⚠️ Notes

The Google speech recognition service requires an internet connection. The project does not store audio recordings.

## 🔮 Future Enhancements

- Support multiple languages
- Add continuous speech recognition
- Add text-to-speech
- Export to PDF/DOCX
- Add voice commands
- Add offline speech recognition

## 📚 Academic Use

This project demonstrates:

- Speech signal input
- Automatic speech recognition
- API-based processing
- Python GUI development
- Exception handling
- File handling


