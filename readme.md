# ⚡ AshuCLI - The Intelligent Voice-Controlled CLI 

![Python](https://img.shields.io/badge/Python-3.10-blue?logo=python)
![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20Linux-lightgrey)
![License](https://img.shields.io/badge/License-MIT-green)

AshuCLI is a powerful, voice-controlled and case-insensitive**, meaning commands can be typed in any letter case (e.g., WHOAMI, whoami, WhoAmI — all work) command-line interface designed to make your daily system and cloud operations faster and smarter. With support for **system utilities**, **file handling**, **network tools**, and even **AWS integration**, it's your all-in-one productivity CLI — enhanced with **speech recognition** and a built-in **voice assistant**.

---

## 🎯 Features

### 💻 System Utilities
- Launch commonly used commands via voice or text commands
- Check system information IP and processes
- Perform file operations: open, read, write

### 🌐 Networking Tools
- Run `ping`, `myip`, `netmap`, and more
- Check internet connection status
- View active ports and IPs

### 🧠 Voice Assistant
- Speech recognition using `SpeechRecognition` + `PyAudio`
- Text-to-speech feedback using `pyttsx3` or `AWS Polly`
- Execute commands via natural speech

### ☁️ AWS Cloud Integration
- AWS CLI features through `boto3`
- Interact with **S3**, **Lambda**, and **Polly**
- Automatically uses credentials from `.env` (never hardcoded!)

---

## 🚀 Getting Started

### ✅ Prerequisites
- Python 3.8+
- AWS account (for cloud features)
- Working microphone (for voice commands)

### 🔧 Installation

1. **Clone the Repository**
```bash
```git clone https://github.com/yourusername/AshuCLI.git
```cd AshuCLI
```pip install -r requirements.txt

Set Up Environment Variables
Create a .env file in the root directory:


AWS_ACCESS_KEY_ID=your_key
AWS_SECRET_ACCESS_KEY=your_secret
REGION_NAME=your_region

MY_DOCUMENTS_PATH=C:/Users/YourName/Documents
python ashucli.py

## 📸 Demo Screenshots

| Menu | Voice Command | AWS Polly | Netmap | Help Section |
|------|---------------|-----------|--------|--------------|
| ![](screenshot/1.bmp) | ![](screenshot/2.bmp) | ![](screenshot/3.bmp) | ![](screenshot/4.bmp) | ![](screenshot/5.bmp) | ![](screenshot/5.bmp) |


