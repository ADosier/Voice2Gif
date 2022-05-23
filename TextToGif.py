import giphy_client
#from urllib.request import urlopen
#from urllib.request import urlretrieve
#import webbrowser
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from giphy_client.rest import ApiException

#read .config file and add ignore the config for github
gKey = ""
gInstance = giphy_client.DefaultApi()

chrome_options = Options()
chrome_options.add_argument("--kiosk") #kiosk relenquishes control

startup ="https://giphy.com/embed/KlrMS4vyq5KSY"


"""
while(query != "exit"):

    try:
        gResponse = gInstance.gifs_search_get(gKey, query, limit = 1)
        gifData = gResponse.data[0]

        urlretrieve(gifData.images.original.url, 'test.gif')
        print("Here is your gif ")
        #print(gifData.embed_url)
        webbrowser.open(gifData.embed_url, new=0, autoraise=True)
        query = input("what gif do you want: ")
    except ApiException as e:
        print("problem encounterd")
        query = "exit"
"""
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
                #urlretrieve(gifData.images.original.url, 'test.gif')
                # print("Here is your gif ")
                # print(gifData.embed_url)
                #webbrowser.open(gifData.embed_url, new=0, autoraise=True)
            except ApiException as e:
                print("Giphy exception found")