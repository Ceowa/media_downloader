# Media Content Downloader Script

This Python script extracts media links from a web page and allows you to download these media files to a directory of your choice. 

## Requirements

- Python 3.x
- Required Python packages:
  - `requests`
  - `beautifulsoup4`
  - `tkinter` (usually included with Python's standard library)

## Installation

1. **Install required packages:**

   You can install the required packages using `pip`. Open your terminal or command prompt and run:
   ```bash
   pip install requests beautifulsoup4
   ```

2. **Save the script:**

   Copy the Python script into a file named `media_downloader.py`.

## Usage

1. **Run the script:**

   Open your terminal or command prompt, navigate to the directory where you saved `media_downloader.py`, and run:
   ```bash
   python media_downloader.py
   ```

2. **Input the URL:**

   When prompted, enter the URL of the web page you want to extract media links from. For example:
   ```
   Enter the URL: https://2ch.hk/gg/res/1797027.html
   ```

3. **View extracted media links:**

   The script will print the unique media links found on the page.

4. **Choose to download media content:**

   When asked whether you want to download the media content, type `yes` to proceed or `no` to cancel.

5. **Select a directory:**

   If you choose to download the media content, a directory selection dialog will open. Choose or create a directory where the media files will be saved.

6. **Files are downloaded:**

   The script will download each media file and save it to the selected directory. You will see messages indicating the files being saved.

## Notes

- The script extracts media links that end with the following file extensions: `.png`, `.jpg`, `.webp`, `.webm`, `.mp4`, `.gif`.
- If the URL contains a numeric part before `.html`, it will be used to create a subdirectory within the selected directory.
- If there are any errors during requests or file operations, they will be printed to the console.

## Example

### Running the script:

```bash
python media_downloader.py
```

### Example interaction:

```
Enter the URL: https://2ch.hk/gg/res/1797027.html

Unique media files:
https://2ch.hk/gg/src/1797027.png
https://2ch.hk/gg/src/1797028.jpg

Do you want to download the media content? (yes/no): yes

[Directory selection dialog opens]

Saving files...
Saved file: /path/to/your/directory/1797027.png
Saved file: /path/to/your/directory/1797028.jpg
```
