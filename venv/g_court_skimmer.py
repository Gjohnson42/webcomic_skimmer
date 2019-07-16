import bs4
import requests
import os
import logging
import shutil

logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s- %(message)s')

def skim_g_c():
    destination_folder = r"C:\Users\Garrett\Documents\Webcomic Skims\gc"
    download_number = 1
    curr_url = r"https://www.gunnerkrigg.com/?p=1"
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
            imageFile = open(destination_folder+"\\"+str(download_number),'wb')
            for chunk in res.iter_content(100000):
                imageFile.write(chunk)
            imageFile.close()

skim_g_c()