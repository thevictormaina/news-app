import unittest
from app.models import Source
from app.requests import api_request

class SourceTest(unittest.TestCase):
    """
    Test class for Source class in models
    """

    def setUp(self):
        """
        Set up method to run before each test
        """
        self.new_source = Source("abc-news", "ABC News", "Your trusted source for breaking news, analysis, exclusive interviews, headlines, and videos at ABCNews.com.", "https://abcnews.go.com", "general", "us")
    
    def tearDown(self):
        """
        Method to reset instances after each test runs
        """
        pass

    def test_init(self):
        """
        Test if news source object is initialized properly
        """

        self.assertIsInstance(self.new_source, Source)