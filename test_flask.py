import unittest
import redis
import my_app as app

class TestFlaskMethods(unittest.TestCase):

    def test_flask(self):
        self.assertEqual(app.test(), 'bar')

    def test_flask2(self):
        self.assertEqual(app.test2(), 'a')
        self.assertEqual(app.test3(), 'b')
        self.assertEqual(app.test4(), 'c')

if __name__ == '__main__':
    unittest.main()
