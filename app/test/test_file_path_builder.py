import unittest
from ..lib.file_path_builder import FilePathBuilder

class FilePathBuilderTests(unittest.TestCase):
    def testUrlWithFileName(self):
        url = 'www.whatever.com/news/article.html'
        expected_path = './output/www.whatever.com/news/article.txt'
        self.assertEqual(self.__builder(url).build(), expected_path)

    def testUrlWithoutFileName(self):
        url = 'www.whatever.com/news/topic/'
        expected_path = './output/www.whatever.com/news/topic/index.txt'
        self.assertEqual(self.__builder(url).build(), expected_path)

    def __builder(self, url):
        return FilePathBuilder(url)

if __name__ == '__main__':
    unittest.main()