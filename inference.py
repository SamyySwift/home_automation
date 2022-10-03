import json
import requests


API_TOKEN = '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'
headers = {"Authorization": f"Bearer {API_TOKEN}"}


def query(filename, lang):
    """
    Function to get inference for three languages
    
    """
    if (lang == 'ha'):
        API_URL = "https://api-inference.huggingface.co/models/abdulqahar47/wav2vec2-large-xls-r-300m-hausa-v1.2"
        with open(filename, "rb") as f:
            data = f.read()
            
        try:
            response = requests.request("POST", API_URL, headers=headers, data=data)
            command = json.loads(response.content.decode("utf-8"))
            command = command['text']
            if command != '':
                print(command)
                return command
            else:
                print('No response yet')
        except KeyError as e:
            print('Model is still loading, please wait!')
            # return 'Model is still loading, please wait!'

 
    elif (lang == 'yo') and (filename is not None):
        API_URL = "https://api-inference.huggingface.co/models/Ayoola/cdial-yoruba-test"
        with open(filename, "rb") as f:
            data = f.read()
        
        try:
            response = requests.request("POST", API_URL, headers=headers, data=data)
            command = json.loads(response.content.decode("utf-8"))
            command = command['text']
            if command != '':
                print(command)
                return command
            else:
                pass
        except KeyError as e:
            print('model is still loading, please wait!')
            # return 'Model is still loading, please wait!'

    
    elif (lang == 'en') and (filename is not None):
        API_URL = "https://api-inference.huggingface.co/models/facebook/wav2vec2-base-960h"
        with open(filename, "rb") as f:
            data = f.read()
        try:
            response = requests.request("POST", API_URL, headers=headers, data=data)
            command = json.loads(response.content.decode("utf-8"))
            command = command['text']
            if command != '':
                print(command)
                return command.lower()
            else:
                print('No response yet')
        except KeyError as e:
            print('model is still loading..., please wait!')
            # return 'Model is still loading, please wait!'


    else:
        pass
