from inference import *
from script import *


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
