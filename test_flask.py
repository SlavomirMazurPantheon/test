import unittest
import redis
import my_app as app

class TestFlaskMethods(unittest.TestCase):

    def test_flask(self):
        self.assertEqual(app.test(), 'bar')

if __name__ == '__main__':
    unittest.main()
