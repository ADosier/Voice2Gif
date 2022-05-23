import giphy_client
#from urllib.request import urlopen
#from urllib.request import urlretrieve
#import webbrowser
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from giphy_client.rest import ApiException

#read .config file and add ignore the config for github
info = []
with open("info.config", 'r', encoding='utf-8') as f:
    info = f.read().splitlines()

gKey = info[0] # this is my API key. sorry, you can't have it.
gInstance = giphy_client.DefaultApi()

chrome_options = Options()
chrome_options.add_argument("--kiosk") #this is the full screen command for chrome

# There is a delay on startup for the voice recognition to function
# This is just a filler gif until it starts recognizing speech
startup ="https://giphy.com/embed/KlrMS4vyq5KSY"

class TextToGif:
    def __init__(self):
        self.query = ""
        self.driver = webdriver.Chrome(options=chrome_options) # opens new browser
        self.driver.get(startup)
    def __del__(self):
        self.driver.close()

    def DisplayGif(self, text):
        self.query = text

        if self.query == "exit":
            return 1
        else:
            try:
                gResponse = gInstance.gifs_search_get(gKey, self.query, limit=1)
                gifData = gResponse.data[0]
                self.driver.get(gifData.embed_url)
            except ApiException as e:
                print("Giphy exception found")