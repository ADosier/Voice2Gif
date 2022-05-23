from vosk import Model, KaldiRecognizer
import pyaudio

import os
from TextToGif import TextToGif

from nltk import word_tokenize
from nltk.corpus import stopwords
import re

MAX_QUERY = 2 # number of words to cram into the gif search bar

def process_text(text):
    # PREPROCESSING STEP => remove punctuation and whitespace
    text = re.sub(r'[.,?!;:(){}`\"\-\[\]\']', ' ', text.lower())

    # tokenize into words (also removes all whitespaces)
    tokens = word_tokenize(text)
    if len(tokens) == 0:
        return ""

    # remove all stopwords (filler words that aren't important terms)
    important_words = [t for t in tokens if t not in stopwords.words('english')]
    if len(important_words) == 0:
        return ""
    newText = ""
    counter = 0
    for word in important_words:
        if counter < MAX_QUERY:
            newText += word
            newText += " "
        counter += 1
    return newText

if __name__ == '__main__':
    # fetch model path for deep speech to work its magic
    modelPath = os.path.abspath(os.getcwd())
    modelPath += "\\us-small"

    # start screen display immediately just in case the setup takes too long
    ttg = TextToGif()

    model = Model(modelPath)
    recognizer = KaldiRecognizer(model, 16000)

    capture = pyaudio.PyAudio()
    stream = capture.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=8192)
    stream.start_stream()

    print("Recording activated")
    while True:
        data = stream.read(4096)
        if len(data) == 0:
            continue

        if recognizer.AcceptWaveform(data):
            result = recognizer.Result()
            text = result[14:-3]

            clean_text = process_text(text)

            if clean_text != "":
                print("Alec said \"", text, "\"")
                print("clean text: ", clean_text)
                if text == "exit":
                    break
                #ttg.DisplayGif(text)

    exit(0)