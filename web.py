from inference import *
from script import *
import librosa
import soundfile as sf
import numpy as np


# def preprocess_audio(audio_array):
#     try:
#         # _, array = audio_array
#         y, sr = librosa.load(audio_array, sr=16000)
#         sf.write('audio.wav', y, samplerate=16000, subtype='PCM_16')      
#         return 'audio.wav'
#     except TypeError as e:
#         pass


def interface(Audio_Inp, Language):
    # audio_path = preprocess_audio(Audio_Inp)

    if Language == 'Hausa':
        voice_command =  query(Audio_Inp, 'ha')
        command = activate_hausa(voice_command)
        return command
   
    # elif Language == 'English':
    #      command =  query(Audio, lang ='en')
    #      state = activate_english(command)
    #      return state
         
    elif Language == 'Yoruba':
        voice_command =  query(Audio_Inp, 'yo')
        command = activate_yoruba(voice_command)
        return command

    else:
        pass
