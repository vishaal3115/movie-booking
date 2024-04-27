import unittest
from app import app


class TestApp(unittest.TestCase):

    def setUp(self):
        app.testing = True
        self.app = app.test_client()

    def test_index_page(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)

    def test_booking_success(self):
        data = {
            'movie_id': '1',
            'showtime': '10:00 AM',
            'num_tickets': '2'
        }
        response = self.app.post('/book', data=data)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Done', response.data)

    def test_invalid_movie_id(self):
        data = {
            'movie_id': '10',
            'showtime': '12:00 PM',
            'num_tickets': '2'
        }
        response = self.app.post('/book', data=data)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Movie not found', response.data)

    def test_invalid_showtime(self):
        data = {
            'movie_id': '1',
            'showtime': '9:00 AM',
            'num_tickets': '2'
        }
        response = self.app.post('/book', data=data)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Showtime not available', response.data)

    def test_invalid_num_tickets(self):
        data = {
            'movie_id': '2',
            'showtime': '11:00 AM',
            'num_tickets': '0'
        }
        response = self.app.post('/book', data=data)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Invalid no of tickets', response.data)

    def test_invalid_request_method(self):
        response = self.app.get('/book')
        self.assertEqual(response.status_code, 405)  # Method Not Allowed

    def test_missing_parameters(self):
        response = self.app.post('/book')
        self.assertEqual(response.status_code, 400)  # Bad Request


if __name__ == '__main__':
    unittest.main()
