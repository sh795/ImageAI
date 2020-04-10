from PIL import Image
from art import *
from gtts import gTTS

import os

import os.path

import cloudsight

import time

import requests

Art = text2art("ImageAI")

print(Art)

print("Welcome to ImageAI, developed by Saif Hussain for Computational Creativity. \n")

print("The purpose of this program is to describe images to the user. \n")

print ("This is to allow visually impaired individuals the ability to understand what is happening in an image. \n")

numImages = input("How many images would you like to describe? ")

numImages = int(numImages)

def main() :

    auth = cloudsight.SimpleAuth('gqPvkvZfv_mAwMO3Kaa9Zw')

    api = cloudsight.API(auth)

    for x in range(numImages):
        string = str(x)
        file = string + '.jpg'
        if os.path.exists(file) == False:
            print("The file " + file + " does not exist. Please check the filenames are correctly formatted. \n")
            print("Now exiting the loop. Please rerun the program. \n")
            break
        im = Image.open(file)
        im.thumbnail((600, 600))
        im.save(string + 'cloudsight.jpg')
        with open(string + '.jpg', 'rb') as f:
            response = api.image_request(f, string + 'cloudsight.jpg', {'image_request[locale]': 'en-US', })
            status = api.wait(response['token'], timeout=30)

        output = status['name']
        print(output)
        print("Preparing text to speech. \n")
        textSpeech("The image can be described as " + output)
        wait()
        dadJoke(output)


def textSpeech(output) :
    language = 'en'

    speak = gTTS(text = output, lang = language, slow = False)

    speak.save("speech.mp3")

    os.system("open speech.mp3")

def cleanFiles() :
    print("Cleaning directory. \n")
    if os.path.exists("speech.mp3") == False:
        print("Directory cleaned. Exiting Loop \n")

    if os.path.exists("speech.mp3") == True:
        os.remove("speech.mp3")
        print("Directory cleaned. Exiting Loop \n")

    for x in range(numImages):
        string = str(x)
        cleanFiles = string + 'cloudsight.jpg'
        if os.path.exists(cleanFiles) == False:
            print("Directory cleaned. Exiting Loop \n")
            break
        os.remove(cleanFiles)
        print ("Directory cleaned.")

def wait() :
    time.sleep(7)

def dadJoke(string) :
    url = 'https://icanhazdadjoke.com/search?term='
    listString = string.split()
    last = len(listString) - 1
    for i, x in enumerate(listString):
        if i == last:
            url = url + x + '&limit=1'
        else:
            url = url + x + '&'
    response = requests.get(url, headers={"Accept": "text/plain"})
    results = response.text
    print(results)
    textSpeech("The joke for the image is " + results)
    wait()



main()
wait()
cleanFiles()