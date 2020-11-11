import unittest
import redis
import my_app as app


class TestRedisMethods(unittest.TestCase):

    def test_redis_modules(self):
        modules = app.test_modules()
        self.assertNotEqual(len(modules), 0)

    def test_redis_vendors(self):
        vendors = app.test_vendors()
        self.assertNotEqual(len(vendors), 0)

if __name__ == '__main__':
    unittest.main()
