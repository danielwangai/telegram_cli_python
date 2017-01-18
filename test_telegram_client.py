import unittest
import requests
import telegram_client

class TelegramBotTests(unittest.TestCase):
    def setUp(self):
        self.correct_chat_id = 173669942
        self.incorrect_correct_chat_id = 12345
        self.correct_telegram_token = "295227945:AAH8aElKnUzIitrlvuvD-RzkRz31U1-0HXw"
        self.wrong_telegram_token = "123446789:ANT8aElKnUzIitrlvuvD-RzkRz31U1-0HXw"
        self.url = "https://api.telegram.org/bot"

    def test_sends_message_successfully(self):
        # response after posting to telegram API
        response = telegram_client.send_message(self.correct_chat_id)
        # get a list of values(from dictionary) and gets the first - check of ok is true
        self.assertTrue(list(response.values())[0])
    def test_wrong_chat_id(self):
        self.assertEqual(telegram_client.send_message(self.incorrect_correct_chat_id)['error_code'], 400)

    def test_that_bot_token_is_correct(self):
        response = requests.get(self.url+self.correct_telegram_token+'/'+'getme').json()
        self.assertTrue(response['ok'])

    def test_that_bot_token_is_not_correct(self):
        response = requests.get(self.url+self.wrong_telegram_token+'/'+'getme').json()
        # 401 is errorcode for wrong bot token
        self.assertEqual(response['error_code'], 401)

    def test_that_bot_retreives_updates(self):
        response = requests.get(self.url+self.correct_telegram_token+'/'+'getUpdates').json()
        self.assertTrue(response['ok'])
if __name__== '__main__':
    unittest.main()
