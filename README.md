# VoiceToGif
Voice to gif is what you think it is; a way to convert voice into gifs

The way this functions is:
=> convert voice to text using the open source machine learning Vosk
=> processes the text into meaningful key words
=> inputs some of those key words into tenor gif search API
=> displays the gif full screen using chrome driver

VoiceToText.py
 - Uses open source Vosk that uses deep learning to translate voice to text
 - REQUIRES A MACHINE LEARNING MODEL TO FUNCTION 
    - I use vosk-model-en-us-0.22 from the website https://alphacephei.com/vosk/models
    - I simply renamed it to us-large and kept it in the same directory
 
 TextToGif.py
  - uses Tenor's API to retrieve gif links from search terms
  - to get this working create a file "info.config" and paste in your own tenor API key
  - for display it uses chrome driver to take control of a Google Chrome instance and display gifs
  - to get this to function go to the chrome driver website, download it, and put it in the same directory
    - the link to this is https://chromedriver.chromium.org/downloads

This project was simply a proof of concept and I have been developing a mobile version of it that looks cleaner
The idea behind this project is to have a screen on a lanyard to bring to conventions and always have some goofy gif on display relevant to the conversations happening
This project as it stands uses a much larger model than a portible device can use, so the voice => text translation will be worse in application unless I create an API to offload the processing/memory requirements needed to obtain higher quality audio-> text translations.
