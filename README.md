# Subservient Ghostface Video Downloader

An automated tool designed to extract and download all unique promotional video assets from the interactive Ghostface website. By parsing the underlying front-end command mapping configuration, this script eliminates duplicates and downloads every active `.webm` clip cleanly to your local machine.

## Prerequisites

Before running the script, ensure you have Python installed on your system along with the `requests` library.

Install the required dependency using pip:

```bash
pip install requests
```[cite: 1]
```
## Project Structure

For the script to work properly, keep the files in the same directory:

```plaintext
├── downloader.py
└── subserviantghostfacevideos.txt
```

* **`downloader.py`**: The Python automation script.
* **`subserviantghostfacevideos.txt`**: The raw JSON data payload extracted from the website's source network bundle containing the full list of interactive trigger commands and video maps.

## Usage

1. Place your extracted `subserviantghostfacevideos.txt` file into the exact same folder as the `downloader.py` script.
2. Open your terminal or command prompt in that directory.
3. Execute the script:

```bash
python downloader.py
```

The script will automatically read the configuration file, compile a unique list of filenames, create a local directory named `ghostface_clips/`, and stream the video assets directly into it.

## Disclaimer

This repository is intended solely for educational, archival, and research purposes. All media assets, video clips, and promotional materials are the intellectual property of their respective copyright holders. The author of this script does not host, re-upload, or own any of the media elements, and is not responsible for how individuals choose to share, distribute, or use the downloaded videos online.[cite: 1]
