import requests
from bs4 import BeautifulSoup
import os
import re
import tkinter as tk
from tkinter import filedialog

# Valid file extensions we're interested in
VALID_EXTENSIONS = ('.png', '.jpg', '.webp', '.webm', '.mp4', '.gif')

def is_valid_extension(url):
    """ Checks if the URL has a valid file extension """
    return url.lower().endswith(VALID_EXTENSIONS)

def extract_media_links(url):
    """ Extracts unique media links from the given URL page """
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        links = {f"https://2ch.hk{link.get('href')}" for link in soup.find_all('a') if link.get('href') and is_valid_extension(link.get('href'))}
        return links
    except requests.RequestException as e:
        print(f"Error requesting URL: {e}")
        return set()

def select_directory():
    """ Opens a dialog to select a directory """
    root = tk.Tk()
    root.withdraw()  # Hide the main window
    root.lift()  # Bring the window to the top of all others
    root.attributes('-topmost', True)  # Make the window always on top
    directory = filedialog.askdirectory()
    root.attributes('-topmost', False)  # Reset the attribute
    return directory

def save_media_files(links, save_dir):
    """ Saves media files to the specified directory """
    if not os.path.exists(save_dir):
        os.makedirs(save_dir)

    for link in links:
        try:
            response = requests.get(link)
            response.raise_for_status()
            file_name = link.split('/')[-1]
            file_path = os.path.join(save_dir, file_name)
            with open(file_path, 'wb') as file:
                file.write(response.content)
            print(f"Saved file: {file_path}")
        except requests.RequestException as e:
            print(f"Error downloading file {link}: {e}")

def create_save_directory(base_dir, url):
    """ Creates a directory for saving files based on the URL """
    match = re.search(r'/(\d+)(\.html)?(#.*)?/?$', url)
    if match:
        dir_name = match.group(1)
        return os.path.join(base_dir, dir_name)
    return base_dir

def main():
    """ Main function to run the script """
    url = input("Enter the URL: ").strip()
    media_links = extract_media_links(url)

    if media_links:
        print("\nUnique media files:")
        for link in media_links:
            print(link)

        download_choice = input("\nDo you want to download the media content? (yes/no): ").strip().lower()
        if download_choice == 'yes':
            save_dir = select_directory()
            if save_dir:
                save_dir = create_save_directory(save_dir, url)
                save_media_files(media_links, save_dir)
            else:
                print("Directory selection canceled.")
        else:
            print("Media content download canceled.")
    else:
        print("No media files found for download.")

if __name__ == "__main__":
    main()
