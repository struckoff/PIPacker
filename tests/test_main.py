from main import TOKEN, updater
import pytest

import requests

class TestTelegramConnection:
    def test_token(self):
        response = requests.get(f'https://api.telegram.org/bot{TOKEN}/getMe')
        print(response.text)
        assert(response.ok == True)
        assert(response.json()['ok'] == True)
    def test_updater(self):
        assert(updater.running)