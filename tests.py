import self
import unittest
from unittest.mock import patch
from unittest.mock import MagicMock

import requests.exceptions
from requests.exceptions import Timeout

from main import get_joke, len_joke


class TestJoke(unittest.TestCase):

    @patch('main.get_joke')
    def test_len_joke(self, mock_get_joke):
        mock_get_joke.return_value = 'one'
        self.assertEqual(len_joke(), 3)

    @patch('main.requests')
    def test_get_joke(self, mock_requests):
       mock_response = MagicMock()
       mock_response.status_code = 200
       mock_response.json.return_value ={
          'value' : 'Hello world'
       }
       mock_requests.get.return_value = mock_response
       self.assertEqual(get_joke(), 'Hello world')

    @patch('main.requests')
    def test_fail_get_joke(self, mock_requests):
        mock_response = MagicMock(status_code=403)
        mock_requests.get.return_value = mock_response
        self.assertEqual(get_joke(), 'No jokes')

    @patch('main.requests')
    def test_fail_get_joke_raises_exception(self, mock_requests):
        mock_requests.exceptions = requests.exceptions
        mock_requests.get.side_effect = Timeout ('not now')
        self.assertEqual(get_joke(), 'No jokes')

    @patch('main.requests')
    def test_fail_get_joke_raise_for_status(self, mock_requests):
        mock_requests.exceptions = requests.exceptions
        mock_response = MagicMock(status_code=403)
        mock_response.raise_for_status.side_effect = requests.exceptions.HTTPError()
        mock_requests.get.return_value = mock_response
        self.assertEqual(get_joke(), 'HTTPError was raised')


    if __name__ == '__main__':
        unittest.main()