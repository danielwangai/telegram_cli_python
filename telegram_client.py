import requests

telegram_token = "295227945:AAH8aElKnUzIitrlvuvD-RzkRz31U1-0HXw"
url = "https://api.telegram.org/bot"

def send_message(chat_id, message_from_user):
    action = "sendMessage"
    response = requests.post(url+telegram_token+"/"+action, {'chat_id': chat_id, 'text': message_from_user}).json()
    return response

def get_updates():
    response = requests.get(url+telegram_token+'/'+'getUpdates').json()
    return response

system_commands = ['/update']

def get_user_commands(input_from_user):
    if input_from_user != "":
        if input_from_user in system_commands:
            if input_from_user == "/update":
                first_name = get_updates()['result'][0]['message']['chat']['first_name']
                last_name = get_updates()['result'][0]['message']['chat']['last_name']
                print("A new user "+first_name+" "+last_name+" used the bot.")
                return 1
        else:
            print("command not recognized")
            return 2
    else:
        print("Input cannot be empty.")
        return 0
#
# def send_message_from_cli(message):
#     if message == "":
#         print("Message cannot be empty!")
#         return 0
#     else:
#         if send_message():
#             pass

user_message = input("Enter message to be sent:-\n")
user_input = input("Enter command")
get_user_commands(user_input)
