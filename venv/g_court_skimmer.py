import bs4
import requests
import os
import logging
import shutil

logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s- %(message)s')

def skim_g_c():
    destination_folder = r"C:\Users\Garrett\Documents\Webcomic Skims\gc"
    """
    The big loop starts here. It begins at the first page, downloads it, sends the image to the destination folder. 
    I'm going to start with a test loop that executes 10 times, to see if it works. Here's what it is supposed to do:
    1. Go to the URL it is given, find the image, download it. Then it advances the download number by 1, and sets
    the current url to the next page. It repeats this for a specific number of times, lending itself to a for loop. 
    """
    curr_url = r"https://www.gunnerkrigg.com/?p=1"
    comics_to_download = 10
    download_number = 1
    for comic_number in range(1,comics_to_download):
        #First, create a request to the first page of the archive.
        res = requests.get(curr_url)
        res.raise_for_status()
        logging.debug("Downloading page " +str(curr_url))
        soup_page = bs4.BeautifulSoup(res.text )
        #All right, now you have the page downloaded, and an object that contains all its information. Next, find the image.
        comic_elem = soup_page.select("body > div.comic > img")
        if comic_elem == []:
            logging.debug("Evidently, that tag wasn't the right one to find that image.")
        else:
                curr_image_url = r'https://www.gunnerkrigg.com' + comic_elem[0].get('src')
                logging.debug(curr_image_url)
                # Download the image.
                print('Downloading image %s...' % (curr_image_url))
                res = requests.get(curr_image_url)
                res.raise_for_status()
                imageFile = open(destination_folder+"\\"+str(download_number)+".jpg",'wb')
                for chunk in res.iter_content(100000):
                    imageFile.write(chunk)
                imageFile.close()
                download_number = download_number+1
                next_url = "https://www.gunnerkrigg.com/?p="+ str(download_number)
                curr_url = next_url


skim_g_c()