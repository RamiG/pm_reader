import unittest
import ConfigParser
from ..lib.html_reader import HtmlReader

class ConfigStub:
    def get(self, section, key):
        if section == 'FormatOptions' and key == 'line_width':
            return 3

        if section == 'ParseOptions':
            if key == 'search_tags':
                return 'h1 a'
            if key == 'ignored_tags':
                return 'header'

class HtmlReaderTests(unittest.TestCase):
    def setUp(self):
        url = 'www.somenews.com/article.index.html'
        config = ConfigStub()
        self.html_reader = HtmlReader(url, config)

    def testGetText(self):
        self.html_reader.data = ['aaa bbb ccc ', 'ddd', 'e f g h']
        expected_text = 'aaa\nbbb\nccc\nddd\ne f\ng h\n'

        self.assertEqual(self.html_reader.get_text(), expected_text)

    def testFeed(self):
        html = '<header>Hello</header><h1>Good news</h1><a href="/thursday">Today is Thursday</a>'
        self.html_reader.feed(html)

        expected_data = ['Good news', '\n\n', 'Today is Thursday [/thursday] ', '\n\n']
        self.assertEqual(self.html_reader.data, expected_data)

if __name__ == '__main__':
    unittest.main()