import unittest
from app.models import Article
class newsarticletest(unittest.TestCase):
    """
    Test Class to test the behaviour of the Newsarticle class
    """

    def setUp(self):
        """
         Set up method that will run before every Test
        """

        self.new_article=Article('author','title','description','www.news.com','urltoimage','2020-04-03T10:09:32Z','content')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_article, Article))

    def test_init(self):
        self.assertEqual(self.new_article.author,'author')
        self.assertEqual(self.new_article.title,'title')
        self.assertEqual(self.new_article.description,'description')
        self.assertEqual(self.new_article.url,'www.news.com')
        self.assertEqual(self.new_article.urlToImage,'urltoimage')
        self.assertEqual(self.new_article.publishedAt,'2020-04-03T10:09:32Z')
        self.assertEqual(self.new_article.content,'content')