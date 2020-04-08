from PIL import Image
from art import *
from gtts import gTTS

import os

import os.path

import cloudsight

def consoleText() :
    Art = text2art("ImageAI")
    print(Art)
    print("Welcome to ImageAI, developed by Saif Hussain for Computational Creativity. \n")
    # print ()
    print("The purpose of this program is to describe images to the user. \n")
    # print ()
    print ("This is to allow visually impaired individuals the ability to understand what is happening in an image. \n")
    # print ()

def userInput() :
    numImages = input("How many images would you like to describe? ")
    # global numImages
    numImages = int(numImages)
    return numImages

def main() :
    value = userInput()

    auth = cloudsight.SimpleAuth('gqPvkvZfv_mAwMO3Kaa9Zw')

    api = cloudsight.API(auth)

    for x in range(value):
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


def textSpeech(output) :
    language = 'en'

    speak = gTTS(text = output, lang = language, slow = False)

    speak.save("speech.mp3")

    os.system("open speech.mp3")

consoleText()
main()