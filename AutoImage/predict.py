from PIL import Image
from art import *
from gtts import gTTS

import os

import os.path

import cloudsight

import time

import requests

# Fancy art for console
Art = text2art("ImageAI")

print(Art)

# Short description of program shown to the user in the console
print("Welcome to ImageAI, developed by Saif Hussain for Computational Creativity. \n")

print("The purpose of this program is to describe images to the user. \n")

print ("This is to allow visually impaired individuals the ability to understand what is happening in an image. \n")

print ("Once the image has been described to the user, it will also generate a joke. \n")

# User input required - how many images are going to be described
numImages = input("How many images would you like to describe? ")

# Turn the input (string) into an integer
numImages = int(numImages)

def main() :

    # Make API call for authentication with API key
    auth = cloudsight.SimpleAuth('gqPvkvZfv_mAwMO3Kaa9Zw')

    api = cloudsight.API(auth)

    # Iterate through the number of images the user would like described
    for x in range(numImages):
        string = str(x)
        # Files must be called from 0.jpg onwards so it knows how many to iterate
        file = string + '.jpg'
        # If the file doesn't exist, inform the user and exit the for loop
        if os.path.exists(file) == False:
            print("The file " + file + " does not exist. Please check the filenames are correctly formatted. \n")
            print("Now exiting the loop. Please rerun the program. \n")
            break
        # Open the image and downsize the file so it is easier and faster to upload
        im = Image.open(file)
        im.thumbnail((600, 600))
        # Save the smaller image so we can upload to the API
        im.save(string + 'cloudsight.jpg')
        # Open the image and make the request to the API
        with open(string + 'cloudsight.jpg', 'rb') as f:
            response = api.image_request(f, string + 'cloudsight.jpg', {'image_request[locale]': 'en-US', })
            # Maximum waiting time of 30 seconds - just in case
            status = api.wait(response['token'], timeout=30)

        # Print out the caption returned
        output = status['name']
        print(output)
        print("Preparing text to speech. \n")
        # Call the text to speech function with caption as parameter
        textSpeech("The image can be described as " + output)
        # Wait so the text to speech can finish before starting to say the joke
        wait()
        # Call the joke function with the caption as a parameter
        dadJoke(output)


def textSpeech(output) :
    language = 'en'

    # Generate the speech with the text and chosen language
    speak = gTTS(text = output, lang = language, slow = False)

    # Save the speech file
    speak.save("speech.mp3")

    # Run the speech file
    os.system("open speech.mp3")

def cleanFiles() :
    # Remove the created files that are no longer needed
    print("Cleaning directory. \n")
    # if os.path.exists("speech.mp3") == False:
    #     print("Directory cleaned. Exiting Loop \n")
    # If there is a speech file, remove it
    if os.path.exists("speech.mp3") == True:
        os.remove("speech.mp3")
        print("Directory cleaned. Exiting Loop \n")

    # For the smaller images created, iterate through them and remove them
    for x in range(numImages):
        string = str(x)
        cleanFiles = string + 'cloudsight.jpg'
        if os.path.exists(cleanFiles) == False:
            print("Directory cleaned. Exiting Loop \n")
            break
        os.remove(cleanFiles)
        print ("Directory cleaned.")

def wait() :
    # Wait for a given amount of time
    time.sleep(7)

def dadJoke(string) :
    # Define URL to access joke API
    url = 'https://icanhazdadjoke.com/search?term='
    # Take the caption and split it into a list of words
    listString = string.split()
    # Define the integer for last element in the list
    last = len(listString) - 1
    # Iterate through the list
    for i, x in enumerate(listString):
        # If we are at the last element in the list, append limit=1 so we can have 1 joke
        if i == last:
            url = url + x + '&limit=1'
        else:
            url = url + x + '&'
    # Return the response as plain text rather than a json object for example - we only want the joke
    response = requests.get(url, headers={"Accept": "text/plain"})
    results = response.text
    print(results)
    # Call the text to speech function with the joke as the parameter
    textSpeech("The joke for the image is " + results)
    wait()


# Run the files
main()
wait()
cleanFiles()