import requests

telegram_token = "295227945:AAH8aElKnUzIitrlvuvD-RzkRz31U1-0HXw"
url = "https://api.telegram.org/bot"

def send_message(chat_id):
   action = "sendMessage"
   response = requests.post(url+telegram_token+"/"+action, {'chat_id': chat_id, 'text': 'Test'}).json()
   return response

def get_updates():
    response = requests.get(url+telegram_token+'/'+'getUpdates').json()
    return response
