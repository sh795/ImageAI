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
    # global numImages
numImages = int(numImages)

# def consoleText() :
#     Art = text2art("ImageAI")
#     print(Art)
#     print("Welcome to ImageAI, developed by Saif Hussain for Computational Creativity. \n")
#     # print ()
#     print("The purpose of this program is to describe images to the user. \n")
#     # print ()
#     print ("This is to allow visually impaired individuals the ability to understand what is happening in an image. \n")
#     # print ()

# def userInput() :
#     numImages = input("How many images would you like to describe? ")
#     # global numImages
#     numImages = int(numImages)
#     return numImages

def main() :
    # value = userInput()

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
        # im = Image.open(string + '.jpg')
        im.thumbnail((600, 600))
        im.save(string + 'cloudsight.jpg')
        with open(string + '.jpg', 'rb') as f:
            response = api.image_request(f, string + 'cloudsight.jpg', {'image_request[locale]': 'en-US', })
            status = api.wait(response['token'], timeout=30)

        output = status['name']
        print(output)
        # print(status['name'])
        print("Preparing text to speech. \n")
        textSpeech(output)
        # cleanFiles()


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
    time.sleep(5)

def dadJoke(string) :
    url = 'https://icanhazdadjoke.com/search?term='
    listString = string.split()
    last = len(listString) - 1
    print(last)
    for i, x in enumerate(listString):
        print(i)
        if i == last:
            url = url + x
            print("hit")
        else:
            url = url + x + '&'
    url = 'https://icanhazdadjoke.com/search?term=asphalt'
    response = requests.get(url, headers={"Accept": "text/plain"})
    print(response.text)



# main()
# wait()
# cleanFiles()
dadJoke()