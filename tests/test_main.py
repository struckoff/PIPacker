from main import TOKEN
import pytest

import requests

class TestTelegramConnection:
    def test_updater(self):
        response = requests.get(f'https://api.telegram.org/bot{TOKEN}/getMe')
        print(response.text)
        assert(response.ok == True)
        assert(response.json()['ok'] == True)