import bs4
import requests
import os

def skim_g_c():
    destination_folder = r"C:\Users\Garrett\Documents\Webcomic Skims\G_C"
    curr_url = r"https://www.gunnerkrigg.com/?p=1"
    #First, create a request to the first page of the archive.
    res = requests.get(curr_url)
    res.raise_for_status()
    print("Downloading page " +str(curr_url))
    soup_page = bs4.BeautifulSoup(res.text, 'features="html.parser"' )
    #All right, now you have the page downloaded, and an object that contains all its information. Next, find the image.
    comic_elem = soup_page.select()
skim_g_c()