import yt_dlp
import time
import argparse
from tqdm import tqdm
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service


def main():
    #Create an Argument parser
    parser = argparse.ArgumentParser(description="Downloaded mp3 lecture files from given url")

    #Add the requirement arguments
    parser.add_argument('--course_url', required=True, help='Url of the required website to access')
    parser.add_argument('--driver_directory', required = True, help = "Give the path to the driver directory")
    parser.add_argument('--output_path', required = True, help = 'Give the output folder path to store the mp3 files')

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

    # Get the list of week titles and live sessions
    week_list = driver.find_elements(By.CLASS_NAME ,"unit-title")
    live_list = driver.find_elements(By.LINK_TEXT,"Live Session")
    week_count = len(week_list) - len(live_list)

    # Get the video links for each week and lesson
    video_links = []
    for week in range(week_count-1):
        time.sleep(4)
        # Click the "Week" button
        week_button = driver.find_element(By.XPATH ,f"/html/body/app-root/app-course-details/main/nav/div/div["+str(week+2)+"]/div/span")
        week_button.click()

        lesson_list = driver.find_elements(By.XPATH,"//div[@class='unit selected']//ul[@class='lessons-list']//li[@class='lesson']")
        lesson_count = len(lesson_list)

        for lesson in range(lesson_count+1):

            # Click the "Lesson" button
            lesson_button = driver.find_element(By.XPATH ,f"/html/body/app-root/app-course-details/main/nav/div/div["+str(week+2)+"]/ul/li["+str(lesson+1)+"]/span")
            lesson_button.click()
            time.sleep(2)

            # Switch to frame id
            frame = driver.find_element(By.ID,"player")
            driver.switch_to.frame(frame)

            # Get video link
            youtube_link = driver.find_element(By.XPATH,"//a[@data-layer='8']")
            youtube_href = youtube_link.get_attribute('href')
            video_link = youtube_href.split('&')[0]
            video_links.append(video_link)

            # Switch back to the main frame
            driver.switch_to.default_content()

        # Navigate back to the main course page
        driver.get(course_url)
        driver.maximize_window()

    i = 1
        
    # download each audio file in the list of video links
    for link in tqdm(video_links):
        file_name = "{}".format(i)
        # Configure yt-dlp options for MP3 audio
        ydl_opts = {
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
            'outtmpl': output_path + file_name
        }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download(link)
        i += 1

    # Close the web driver
    driver.quit()

if __name__ == "__main__":
    main()   
