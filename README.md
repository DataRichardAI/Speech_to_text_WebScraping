# Speech_to_text_WebScraping
Create a data engineering pipeline to curate a Speech-To-Text dataset from publicly available lectures on NPTEL, to train speech recognition models.

---
## MP3 Lecture Downloader:
This Python script is used to download MP3 lecture files from a specified course website. It uses the yt-dlp library to extract audio from NPTEL videos and saves them as MP3 files.

## Prerequisites
Before running the script, you must have the following installed on your system:
- Python 3.x
- yt-dlp
- selenium
- webdriver-manager
- tqdm
- argparse

You will also need the Chrome web driver installed on your system. You can download it from the official website or use the webdriver-manager to download it automatically.

### Usage
To use the script, open a command prompt and navigate to the directory where the script is saved. Then run the following command:

```python 
python download_lectures.py --course_url <url> --driver_directory <path> --output_path <path>
```
Replace '<url>' with the URL of the course website, '<path>' with the path to the directory containing the Chrome web driver, and '<path>' with the path to the directory where you want to save the MP3 files.


---
## Download PDF Transcript files from NPTEL website
This is a Python script to download PDF transcript files from the NPTEL website. The script uses Selenium to navigate to the website and retrieve the download links for the PDF files.

### Prerequisites
Before running the script, you must have the following additionally installed on your system:
- urllib

You will also need the Chrome web driver installed on your system. You can download it from the official website or use the webdriver-manager to download it automatically.

### Usage
To use the script, open a command prompt and navigate to the directory where the script is saved. Then run the following command:

```python 
python download_transcript.py --course_url <url> --driver_directory <path> --output_path <path>
```
Replace '<url>' with the URL of the course website, '<path>' with the path to the directory containing the Chrome web driver, and '<path>' with the path to the directory where you want to save the pdf files.

### License
This script is released under the MIT License.

## Preprocessing Audio: Bash Script Description
This script takes audio files in mp3 format from an input directory and converts them to WAV format with a 16KHz sampling rate and mono channel. It uses ffmpeg for audio conversion and limits the number of parallel processes to a specified number.

### Dependencies
- ffmpeg

### Usage
```bash
./mp3_to_wav.sh input_directory output_directory num_parallel_processes
```
This command will convert all mp3 files in the input_files directory to WAV format and save them in the output_files directory with a maximum of 4 parallel processes running at a time.

- input_directory: path to the directory containing input mp3 files
- output_directory: path to the directory where output WAV files will be saved
- num_parallel_processes: maximum number of parallel processes to run at a time (integer value)

## Creating the training manifest file

This step is used to split audio files and generate a training manifest for speech recognition models.

### Prerequisites
Before running the script, the following need to be installed additionally.

- pdfminer.six (conda install pdfminer.six)
- pydub
- num2words

### Usage
```python
python preprocess_pdf_argparse.py --audio_file_path <path-to-audio-files> --pdf_file_path <path-to-pdf-files> --output_file_path <path-to-output-files> --manifest_path <path-to-manifest-file>
```
The script takes the following arguments:

audio_file_path: Path to the directory containing audio files
pdf_file_path: Path to the directory containing PDF files
output_file_path: Path to the directory where audio chunks will be saved
manifest_path: Path to the output training manifest file

### Functionality

The script does the following:

1. Extracts the text and timestamps from each PDF file in the given directory using **pdfminer.high_level.extract_text** and **re.findall**
2. Splits the audio files into chunks based on the timestamps using **pydub.AudioSegment**
3. Preprocesses the text by converting all text to lowercase, removing all punctuations, and converting all digits to their spoken form using **string.punctuation** and **num2words**
4. Generates a training manifest file containing the audio file path, duration, and preprocessed text using **json.dump**







