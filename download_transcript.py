import time
import argparse
import urllib.request as url
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

def main():
    #Create an Argument parser
    parser = argparse.ArgumentParser(description="Downloaded pdf transcript files from given url")

    # Set directory path for downloaded file
    directory = '/home/richard/Downloads/AI4Bharat/Final_run/pdf/'

    # Set up the web driver
    PATH = "/home/richard/Downloads/AI4Bharat/chromedriver.exe"

    #Add the requirement arguments
    parser.add_argument('--course_url',default="https://nptel.ac.in/courses/106106184", required=True, help='Url of the required website to access')
    parser.add_argument('--driver_directory', required = True, default = PATH, help = "Give the path to the driver directory")
    parser.add_argument('--output_path', required = True,   default = directory, help = 'Give the output folder path to store the mp3 files')

    #Parse the command line arguments
    args = parser.parse_args()

    course_url = args.course_url
    driver_directory = args.driver_directory
    output_path = args.output_path    
    
    driver = webdriver.Chrome(service=Service(executable_path = driver_directory))

    # Navigate to the website
    driver.get(course_url)
    driver.maximize_window()
    # Wait for the website to load
    time.sleep(5)

    # Click the "Downloads" button
    download_button = driver.find_element(By.XPATH ,"//span[@class='tab']")
    download_button.click()

    # Wait for the website to load
    time.sleep(2)

    # Click the "View Transcripts" button
    view_transcripts_button = driver.find_element(By.XPATH ,"/html/body/app-root/app-course-details/main/section/app-course-detail-ui/div/div[3]/app-course-downloads/div/div[2]/div[1]/h3[1]")
    view_transcripts_button.click()

    # Wait for the website to load
    time.sleep(2)

    chapter_list = driver.find_elements(By.CLASS_NAME,"c-name")
    chapter_count = len(chapter_list)
    chapter_name_list = []

    # Loop through each chapter
    for i in range(chapter_count-1):
        # Click the "Language" button
        language_button = driver.find_element(By.XPATH ,f"/html/body/app-root/app-course-details/main/section/app-course-detail-ui/div/div[3]/app-course-downloads/div/div[2]/div[2]/div[{i+2}]/div[1]/app-nptel-dropdown/div/span")
        language_button.click()

        # Wait for the website to load
        time.sleep(2)

        # Click the "English" button
        english_button = driver.find_element(By.XPATH ,f"/html/body/app-root/app-course-details/main/section/app-course-detail-ui/div/div[3]/app-course-downloads/div/div[2]/div[2]/div[{i+2}]/div[1]/app-nptel-dropdown/ul/li")
        english_button.click()

        chapter_name_list.append(chapter_list[i+1].text)

    drive_links = driver.find_elements(By.XPATH,"//a[contains(@href,'drive.google.com')]")
    pdf_links = [link.get_attribute("href") for link in drive_links]

    # Create a directory to store the downloaded files
    # if not os.path.exists('/home/richard/Downloads/AI4Bharat/Final_run/pdf'):
    #     os.makedirs('./pdf_files')

    # Download each PDF file and save it to the directory
    chapter_name = 1
    for i in range(len(pdf_links)-1):
        link = pdf_links[i]
        # Get the filename from the link
        filename = link.split('/')[5]

        # Construct the download url for the file
        download_url = f"https://drive.google.com/uc?id={filename}&export=download"

        # Send a GET request to the link
    #     response = requests.get(download_url)
        filename=f'/home/richard/Downloads/AI4Bharat/Final_run/pdf/{chapter_name}.pdf'
        url.urlretrieve(download_url,filename)

        # Chapter name
    #     chapter_name = chapter_name_list[i]

        # Save the PDF file to the directory
    #     with open(f'/home/richard/Downloads/AI4Bharat/Final_run/pdf/{chapter_name}.pdf', 'wb') as f:
    #         f.write(response.content)
        chapter_name+=1
        


    # Close the browser window
    driver.quit()

if __name__=="__main__":
    main()
