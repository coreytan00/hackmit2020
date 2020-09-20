from google_images_search import GoogleImagesSearch
from dotenv import load_dotenv
import os
load_dotenv()

GCS_DEVELOPER_KEY=os.getenv("GCS_DEVELOPER_KEY")
GCS_CX=os.getenv("GCS_CX")

# you can provide API key and CX using arguments,
# or you can set environment variables: GCS_DEVELOPER_KEY, GCS_CX
gis = GoogleImagesSearch(GCS_DEVELOPER_KEY, GCS_CX)

import random
import numpy as np
from PIL import Image
import time

import speech_recognition as sr  

r = sr.Recognizer()

while True:                                                                             
	with sr.Microphone() as source:                                                                       
	    print("Speak:")                                                                                   
	    audio = r.listen(source, phrase_time_limit=2)   
	try:
		words = r.recognize_google(audio)
		print(words)
		# define search params:
		_search_params = {
		    'q': words,
		    'num': 10,
		    'safe': 'high',
		    'fileType': 'png',
		    'imgType': 'photo',
		    'imgSize': 'LARGE'
		}


		# search first, then download and resize afterwards:
		gis.search(search_params=_search_params)
		gis.results()[0].download('images/')
		lst = os.listdir('images/')
		img = Image.open('images/' + str(lst[0]))
		img.show()
		time.sleep(1)
		img.close()
		os.remove('images/' + str(lst[0]))

	except sr.UnknownValueError:
	    print("Could not understand audio")
	except sr.RequestError as e:
	    print("Could not request results; {0}".format(e))
