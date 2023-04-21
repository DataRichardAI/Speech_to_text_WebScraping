# TASK 1

## Speech_to_text_WebScraping
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

You will also need the Chrome web driver installed on your system. You can download it from the official website or use the webdriver-manager to download it automatically. The path directory to this driver installation will be needed to be specified as a command line argument.

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
Replace '<url>' with the URL of the course website, 
'<path>' with the path to the directory containing the Chrome web driver, 
and '<path>' with the path to the directory where you want to save the pdf files.

### License
This script is released under the MIT License.

# TASK 2
  
## Preprocessing Audio: Bash Script Description

Here I developed a bash script that can be used to preprocess audio files. The script takes in three inputs:

1. The input directory where the audio files are stored
2. The output directory where the processed audio files will be saved
3. The number of parallel processes to use for the conversion

The script uses [ffmpeg](https://www.ffmpeg.org/) to convert audio files to WAV format with a 16KHz sampling rate and mono channel. It converts all MP3 files in the input directory to WAV format and saves them in the output directory. The script limits the number of parallel processes to the value provided as input.

## Requirements

- [ffmpeg](https://www.ffmpeg.org/) must be installed to run the script.

## Usage

To use the script, run the following command in a terminal:

```
$ bash preprocessaudio.sh /path/to/input/directory /path/to/output/directory num_parallel_processes
```

For example, to preprocess audio files stored in `/home/richard/Downloads/Final_run/Audios/` and save the processed files in `/home/richard/Downloads/Final_run/audio_wav/` using 4 parallel processes, run:

```
$ bash preprocessaudio.sh /home/richard/Downloads/Final_run/Audios/ /home/richard/Downloads/Final_run/audio_wav/ 4
```
  
# TASK 3 & TASK 4
  
## Creating the training manifest file

This step is used to split audio files and generate a training manifest for speech recognition models.

### Prerequisites
Before running the script, the following need to be installed additionally.

- pdfminer.six (conda install pdfminer.six)
- pydub
- num2words
- pydub

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

# Task 5
  
# Creates a Speech Data Explorer Dashboard

I am using NeMo to create the Speech Data Explorer dashboard to visualize interesting statistics of a dataset.

## Requirements

- NeMo library
- Jsonlines
  


## Usage
  
First clone the NeMO repository with the following command
```
git clone  https://github.com/NVIDIA/NeMo.git
```
  
Navigate to the data_explorer.py : NeMo/tools/speech_data_explorer/data_explorer.py

Run the script with the following command:
  
```
python data_explorer.py --manifest_file <path_to_jsonl_file>
```

Replace `<path_to_jsonl_file>` with the directory path of the JSONL manifest file.

The script calculates statistics such as total hours, total utterances, vocabulary and alphabet used in the dataset. It also creates four plots for duration, words, characters, and alphabet distribution.

The SDE dashboard is created and figures are added to it. Finally, the dashboard is displayed.

This will create an SDE dashboard for the dataset specified in `manifest.jsonl` file located in the `data` directory.
  
### Observations:

- The script to download mp3 file by web scraping will work only for websites with similar webpage layout.
- On extracting the text from the pdf files, some corrupted pdf pages will trigger an error and this pdf will and the corresponding mp3 file will be skipped, displaying an error message. eg: 95.pdf
- I also encountered some pdf files where the timestamps were not extracted properly so the audio and text chuncks were not generated efficiently.
- Make sure to install the pdfminer.six instead of the pdfminer.
- A seperate python environment was created for the preprocessing python scripts whereas the web scraping part i.e. Task 1 was run on the base environment.
- Some unwanted unicode characters are getting generated which were not originally present in the pdf file. Other text extraction modules can be tried to see if this can be avoided.
- The numbers which are concatinated to a text is not being converted into it's word form, I have avoided doing so as it would lead to a word which has no meaning.
- The preprocessing of the text has been done after the creation of the jsonl format chuncks as the timestamps (Refer Slide: 04:45) was required to obtain the audio and text chunks to create the jsonl format.
- A stable internet is recommended to efficiently and smoothly runs the python scripts, If unusual delays occur in loading the webpage the next task in the program will get exceuted without the required prerequisites. This will lead to error in executions of the program.
- Make sure you have created a different environment to install all the required modules and libraries to avoid alteration of previously installed modules and libraries.
 

