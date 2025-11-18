import requests
import re
import os
import sys

# --- Configuration Variables from Zapier Script ---
RSS_URL = "https://www.omnycontent.com/d/playlist/e73c998e-6e60-432f-8610-ae210140c5b1/0db4414e-bce3-43c7-a46c-b28900eb4ee3/6658c53e-d5b2-4ca8-8fa1-b28900eb4f04/podcast.rss"
OLD_EMAIL = "applepodcast@howstuffworks.com" # Corrected email from your final script
NEW_EMAIL = "hehbveh@gmail.com"
FILE_PATH = "omny.xml"

def fetch_modify_and_save():
    """Fetches the RSS feed, replaces the email, and saves the file locally."""
    try:
        # Step 1: Fetch the RSS content
        response = requests.get(RSS_URL, timeout=30)
        response.raise_for_status()
        rss_content = response.text
        print("Successfully fetched RSS content.")

        # Step 2: Replace the email address
        modified_content = rss_content.replace(OLD_EMAIL, NEW_EMAIL)

        # Check if the content is different from the currently checked-out file
        # This is a critical check to prevent unnecessary commits
        try:
            with open(FILE_PATH, 'r', encoding='utf-8') as f:
                current_content = f.read()
            if current_content == modified_content:
                print("Content is identical to current file. No update needed.")
                return False
        except FileNotFoundError:
            # File doesn't exist yet, so we proceed with writing
            pass

        # Step 3: Write the modified content locally
        with open(FILE_PATH, 'w', encoding='utf-8') as f:
            f.write(modified_content)
        print(f"Successfully wrote modified content to {FILE_PATH}")
        return True # Indicates that a change was made

    except requests.exceptions.RequestException as e:
        print(f"Error in processing: {e}")
        sys.exit(1) # Fail the action if fetching fails

if __name__ == "__main__":
    fetch_modify_and_save()
