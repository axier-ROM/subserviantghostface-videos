import json
import os
import requests

# Configuration
INPUT_FILE = "subserviantghostfacevideos.txt"
OUTPUT_FOLDER = "ghostface_clips"
BASE_URL = "https://subserviantghostface.com/clips/"

# Create output folder if it doesn't exist
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

try:
    # Load and parse the JSON file
    with open(INPUT_FILE, "r", encoding="utf-8") as f:
        data = json.load(f)
    
    # Use a set to automatically eliminate duplicate video filenames
    unique_videos = set()
    
    if "commands" in data:
        for command in data["commands"]:
            if "videos" in command:
                for video in command["videos"]:
                    if video:
                        unique_videos.add(video.strip())

    print(f"Extracted {len(unique_videos)} unique video clips.\n")

    # Download each video
    for video in sorted(unique_videos):
        full_url = f"{BASE_URL}{video}"
        save_path = os.path.join(OUTPUT_FOLDER, video)
        
        print(f"Downloading: {full_url} ... ", end="", flush=True)
        
        try:
            response = requests.get(full_url, stream=True, timeout=15)
            if response.status_code == 200:
                with open(save_path, "wb") as video_file:
                    for chunk in response.iter_content(chunk_size=8192):
                        if chunk:
                            video_file.write(chunk)
                print("SUCCESS")
            else:
                print(f"FAILED (Status Code: {response.status_code})")
        except Exception as e:
            print(f"ERROR ({str(e)})")

    print("\nAll processing completed.")

except FileNotFoundError:
    print(f"Error: Required file '{INPUT_FILE}' was not found in the current folder.")
except json.JSONDecodeError:
    print(f"Error: Failed to parse '{INPUT_FILE}'. Please verify it is a valid JSON file.")