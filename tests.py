import unittest
from unittest.mock import patch
from unittest.mock import MagicMock
from unittest.mock import self


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
          'value' : 'Hello world'
       }
       mock_requests.get.return_value = mock_response
       self.assertEqual(get_joke(), 'Hello world')

    @patch('main.requests')
    def test_fail_get_joke(self, mock_requests):
        mock_response = MagicMock(status_code=403)
        mock_requests.get.return_value = mock_response
        self.assertEqual(get_joke(), 'No jokes')


    if __name__ == '__main__':
        unittest.main()