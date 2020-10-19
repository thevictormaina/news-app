import unittest
from app.models import Article

class TestArticle(unittest.TestCase):
    """
    Tests for Article class

    Args:
        unittest.TestCase: This class inherits from unittests
    """
    def setUp(self):
        """
        Runs before each test
        """
        self.new_article = Article(source_id="bbc-news", source_name="BBC News", author="Mariella Moon", title="'One day everyone will use China's digital currency'", description="China plans a digital version of its currency, which some say could become a big global payment system.", url="https://www.bbc.co.uk/news/business-54261382", url_to_image="https://ichef.bbci.co.uk/news/1024/branded_news/C414/production/_114569105_chandler.racks.jpg", published_at="2020-09-24T23:16:08Z")
    
    def tearDown(self):
        """
        Runs after each test
        """
    def test_init(self):
        """
        Test case to check if article object is properly initialized
        """
        self.assertIsInstance(self.new_article, Article
        )