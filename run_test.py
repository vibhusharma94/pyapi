import os

if __name__ == "__main__":
    import unittest
    os.environ['deploy'] = 'test'
    suite = unittest.TestLoader().discover("tests", pattern="*.py")
    unittest.TextTestRunner().run(suite)
