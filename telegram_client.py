import requests

telegram_token = "295227945:AAH8aElKnUzIitrlvuvD-RzkRz31U1-0HXw"
url = "https://api.telegram.org/bot"

def send_message(chat_id):
    action = "sendMessage"
    user_message = input("Enter message to be sent:-\n")
    response = requests.post(url+telegram_token+"/"+action, {'chat_id': chat_id, 'text': user_message}).json()
    return response

def get_updates():
    response = requests.get(url+telegram_token+'/'+'getUpdates').json()
    return response

send_message(173669942)
# usr = raw_input("Enter name")
