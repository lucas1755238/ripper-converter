# 🎬 Ripper Converter

A fast, lightweight, and 100% local command-line media downloader for **YouTube**, **Instagram**, and **Twitter (X)**.  
Download videos in High Quality **MP4** or extract audio directly to **MP3 (320kbps)**.

---

## ✨ Features

- **Multi-Platform Support:** Seamlessly downloads from YouTube, Instagram, and Twitter (X).
- **Auto Platform Detection:** Automatically identifies the source platform from the provided URL.
- **Two Download Formats:**
  - **MP4:** High-definition video with merged high-quality audio.
  - **MP3:** Audio extraction encoded at 320 kbps.
- **100% Local & Private:** No third-party servers, web APIs, or tracking involved—traffic is strictly between your machine and the media platform.
- **Auto User Directory:** Automatically locates and stores downloads inside your default system `Downloads` folder.
- **Persistent Session:** Stays running in your terminal/CMD so you can download multiple links sequentially without restarting.
- **Authentication Support:** Cookie detection (`cookies.txt`) allows downloading private or restricted posts where login is required.

---

## 🚀 For Regular Users (Windows Executable)

No Python installation required:

1. Navigate to the **[Releases](../../releases)** tab on the right side of this repository.
2. Under the latest release (e.g., `Ripper Converter v1.0.0`), download the **`RipperConverter.exe`** binary from the **Assets** section.
3. Double-click **`RipperConverter.exe`** to open the terminal interface.
4. Paste the media link (YouTube, Instagram, or Twitter/X), select your preferred format (`1` for MP4, `2` for MP3), and press **Enter**.
5. The downloaded file will be saved directly into your **Downloads** folder.
6. Type `0` or `exit` to close the application when finished.

> **Note for Instagram/Twitter (X):** If an Instagram Reel/post or a Twitter/X video requires login to be viewed, export your browser cookies as `cookies.txt` and place the file in the exact same directory as `RipperConverter.exe`.

---

## 💻 For Developers (Running from Source)

### 1. Prerequisites
- Python 3.8 or higher installed on your system.
- Git installed.

### 2. Clone the Repository
```bash
git clone https://github.com/SEU-USUARIO/ripper-converter.git
cd ripper-converter
```

### 3. Set Up a Virtual Environment (Recommended)
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux / macOS
python3 -m venv venv
source venv/bin/activate
```

### 4. Install Dependencies
```bash
pip install -r requirements.txt
```

> **Note on FFmpeg:** The project uses `imageio-ffmpeg` to bundle and point to an FFmpeg binary automatically. No manual system PATH configuration for FFmpeg is needed.

### 5. Run the Application
```bash
python main.py
```

---

## 📦 Building the Executable with PyInstaller

If you want to package the source code into a standalone `.exe` on Windows:

```bash
pip install pyinstaller
pyinstaller --onefile --name "RipperConverter" --copy-metadata yt-dlp main.py
```

The compiled standalone executable will be located inside the generated `dist/` directory.

---

## 📄 License & Credits

Developed by **Luqueta Codes©** — All rights reserved.
