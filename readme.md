# Ripper Converter

A command-line media downloader for YouTube, Instagram, and Twitter (X). Downloads MP4 video or extracts MP3 audio (320kbps) locally.

---

## Features

- **Multi-Platform:** Supports YouTube, Instagram, and Twitter (X).
- **Auto Detection:** Identifies the target platform directly from the URL.
- **Two Formats:** Best-quality MP4 video or 320kbps MP3 audio.
- **Fully Local:** Runs entirely on your machine; no external processing servers.
- **Automatic Output Path:** Saves files to your system `Downloads` folder.
- **Persistent CLI:** Download multiple links sequentially without reopening the app.
- **Cookie Support:** Loads `cookies.txt` for restricted or login-gated content.

---

## Windows Executable (No Python Required)

1. Open the [Releases](../../releases) section of this repository.
2. Download `rip.exe` under the latest release.
3. Run `rip.exe`.
4. Paste the media link, select `1` (MP4) or `2` (MP3), and press Enter.
5. Files are saved directly to your `Downloads` directory.
6. Enter `0` or `exit` to close the application.

> **Note:** If an Instagram or Twitter (X) link requires authentication, place your exported `cookies.txt` in the same directory as the executable.

---

## Running from Source

### 1. Requirements
- Python 3.8+
- Git

### 2. Setup
```bash
git clone https://github.com/lucas1755238/ripper-converter.git
cd ripper-converter

# Virtual environment
python -m venv venv
venv\Scripts\activate   # Linux/macOS: source venv/bin/activate

# Dependencies
pip install -r requirements.txt
```

### 3. Run
```bash
python main.py
```

---

## Build Standalone Executable

To compile into a single `.exe` via PyInstaller on Windows:

```bash
pip install pyinstaller
pyinstaller --onefile --name "RipperConverter" --copy-metadata yt-dlp main.py
```

Output binary: `dist/RipperConverter.exe`.

---

## License & Credits

Developed by **Luqueta Codes©** — All rights reserved.
