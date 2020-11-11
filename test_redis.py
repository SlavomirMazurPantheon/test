import unittest
import redis
import my_blueprint as search_bp

class TestRedisMethods(unittest.TestCase):

    def test_redis_modules(self):
        modules = search_bp.get_modules()
        self.assertNotEqual(len(modules), 0)

    def test_redis_vendors(self):
        vendors = search_bp.get_vendors()
        self.assertNotEqual(len(vendors), 0)

if __name__ == '__main__':
    unittest.main()
