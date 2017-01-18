import unittest
import telegram_client

class TelegramBotTests(unittest.TestCase):
    def test_sends_message_successfully(self):
        # response after posting to telegram API
        response = telegram_client.send_message(173669942)
        # get a list of values(from dictionary) and gets the first - check of ok is true
        self.assertTrue(list(response.values())[0])

if __name__== '__main__':
    unittest.main()
