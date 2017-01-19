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

user_input = input("Enter command")
if user_input == "/updates":
    first_name = get_updates()['result'][0]['message']['chat']['first_name']
    last_name = get_updates()['result'][0]['message']['chat']['last_name']
    print("A new user "+first_name+" "+last_name+" used the bot.")
