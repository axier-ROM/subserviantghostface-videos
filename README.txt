# Subservient Ghostface Video Downloader[cite: 1]

An automated tool designed to extract and download all unique promotional video assets from the interactive Ghostface website. By parsing the underlying front-end command mapping configuration, this script eliminates duplicates and downloads every active `.webm` clip cleanly to your local machine.[cite: 1]

## Prerequisites[cite: 1]

Before running the script, ensure you have Python installed on your system along with the `requests` library.[cite: 1]

Install the required dependency using pip:[cite: 1]

```bash
pip install requests
```[cite: 1]

## Project Structure[cite: 1]

For the script to work properly, keep the files in the same directory:[cite: 1]

```plaintext
├── downloader.py
└── subserviantghostfacevideos.txt
```[cite: 1]

* **`downloader.py`**: The Python automation script.[cite: 1]
* **`subserviantghostfacevideos.txt`**: The raw JSON data payload extracted from the website's source network bundle containing the full list of interactive trigger commands and video maps.[cite: 1]

## Usage[cite: 1]

1. Place your extracted `subserviantghostfacevideos.txt` file into the exact same folder as the `downloader.py` script.[cite: 1]
2. Open your terminal or command prompt in that directory.[cite: 1]
3. Execute the script:[cite: 1]

```bash
python downloader.py
```[cite: 1]

The script will automatically read the configuration file, compile a unique list of filenames, create a local directory named `ghostface_clips/`, and stream the video assets directly into it.[cite: 1]

## Disclaimer[cite: 1]

This repository is intended solely for educational, archival, and research purposes. All media assets, video clips, and promotional materials are the intellectual property of their respective copyright holders. The author of this script does not host, re-upload, or own any of the media elements, and is not responsible for how individuals choose to share, distribute, or use the downloaded videos online.[cite: 1]