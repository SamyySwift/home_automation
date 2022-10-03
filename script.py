import requests


def activate_hausa(command):
    try:
        if ('kan' in command and 'pallo' in command.split()) or ('kan' in command and 'palo' in command.split()) or ('kan' in command and 'ballo' in command.split()) or ('kan' in command and 'faloo' in command.split()) or ('kan' in command and 'falo' in command.split()) or ('kann' in command and 'falo' in command.split()):
            requests.get('https://blynk.cloud/external/api/update?token=G8ynpU1qu1pivhBZuJwaI542ijnLAOsv&v0=1')
            return "Ok, i'm turning on the parlor light!"

        elif ('ka shi' in command and 'palloo' in command.split()) or ('ka shi' in command and 'paloo' in command.split()) or ('ka shi' in command and 'pallo' in command.split()) or ('ka shi' in command and 'palo' in command.split()) or ('ka shi' in command and 'ɓaloo' in command.split()) or ('ka shi' in command and 'falo' in command.split()) or ('ka shi' in command and 'baloo' in command.split()):
            requests.get('https://blynk.cloud/external/api/update?token=G8ynpU1qu1pivhBZuJwaI542ijnLAOsv&v0=0')
            return "Ok, i'm turning off the parlor light!"
        
        elif ('akan' in command and 'soƙet' in command.split()) or ('akan' in command and 'soketh' in command.split()) or ('akan' in command and 'soket' in command.split()) or ('a kan' in command and 'soketh' in command.split()) or ('a kan' in command and 'soket' in command.split()):
            requests.get('https://blynk.cloud/external/api/update?token=G8ynpU1qu1pivhBZuJwaI542ijnLAOsv&v2=0')
            return "Ok, i'm turning on the socket!"
        elif ('kashi' in command and 'soketh' in command.split()) or ('ka shi' in command and 'soketh' in command.split()) or ('kashi' in command and 'soket' in command.split()) or ('kashi' in command and 'soƙet' in command.split()) or ('ka shi' in command and 'soketh' in command.split()) or ('kashe' in command and 'soketh' in command.spilt()):
            requests.get('https://blynk.cloud/external/api/update?token=G8ynpU1qu1pivhBZuJwaI542ijnLAOsv&v2=1')
            return "Ok, i'm turning off the socket!"
        else:
            return "Couldn't quite understand that, try again!"
    except (TypeError, AttributeError) as e:
        pass


# def activate_english(command):
#     try:
#         if command == 'turn off parlor light':
#             requests.get('https://blynk.cloud/external/api/update?token=G8ynpU1qu1pivhBZuJwaI542ijnLAOsv&v0=0')
#             return "Ok, i'm turning on the parlor light"
#         elif  command == 'turn on parlor light':
#             requests.get('https://blynk.cloud/external/api/update?token=G8ynpU1qu1pivhBZuJwaI542ijnLAOsv&v0=1')
#             return "Ok, i'm turning off the parlor light"
#         else:
#             return "Couldn't quite understand that, try again"
#     except NoneType as e:
#         pass


def activate_yoruba(command):
    try:
        if ('tọn' in command and 'ìjẹ̀wó' in command.split()) or ('tan' in command and 'ìjẹ o' in command.split()) or ('tọ' in command and 'ìjẹ owù' in command.split()) or ('tan' in command and 'ìjẹ o' in command.split()) or ('ta' in command and 'ìjẹ̀ wó' in command.split()):
            requests.get('https://blynk.cloud/external/api/update?token=G8ynpU1qu1pivhBZuJwaI542ijnLAOsv&v0=1')
            return "Ok!, i'm turning on the parlor light"

        elif ('pá' in command and 'ìjẹ o' in command.split()) or ('pa' in command and 'ìjẹ̀ wú' in command.split()) or ('pa' in command and 'ìjẹ wó' in command.split()) or ('pà' in command and 'ìjẹ̀wó' in command.split()):
            requests.get('https://blynk.cloud/external/api/update?token=G8ynpU1qu1pivhBZuJwaI542ijnLAOsv&v0=0')
            return "Ok!, I'm turning off the parlor light"
        else:
            return "Couldn't quite understand that, try again"
    except (TypeError, AttributeError) as e:
        pass
        