from HTMLParser import HTMLParser
from textwrap import TextWrapper

class HtmlReader(HTMLParser):
    TAGS = ['h1', 'h2', 'h3', 'h4', 'p']
    IGNORED_TAGS = ['head', 'header', 'noindex', 'aside', 'section', 'footer', 'table']

    LINE_WIDTH = 80
    LINE_SEPARATOR = '\n'

    def __init__(self, url,):
        HTMLParser.__init__(self)
        self.url = url
        self.data = []
        self.data_adding = False
        self.tag_level = 0
        self.ignored_tag_level = 0
        self.current_href = ''

    def get_text(self):
        text = ''.join(self.data)
        text = text.splitlines()

        wrapper = TextWrapper()
        wrapper.replace_whitespace = False
        wrapper.width = self.LINE_WIDTH
        wrapped_text = ''

        for line in text:
            wrapped_text += wrapper.fill(line) + LINE_SEPARATOR

        return wrapped_text

    def handle_starttag(self, tag, attributes):
        if tag in self.TAGS:
            self.tag_level += 1

        if tag in self.IGNORED_TAGS:
            self.ignored_tag_level += 1

        if self.tag_level and tag == 'a':
            for attr in attributes:
                self.current_href = attr[1]
                break

    def handle_data(self, data):
        if not self.ignored_tag_level and self.tag_level and data.strip() != '':
            data = self.__sanitize(data)
            if self.current_href:
                data = data + ' [' + self.current_href + '] '

            self.data.append(data)
            self.data_adding = True
            self.current_href = ''

    def handle_endtag(self, tag):
        if tag in self.TAGS and self.tag_level:
            self.tag_level -= 1

            if self.data_adding:
                self.data.append(2 * LINE_SEPARATOR)
                self.data_adding = False

        if tag in self.IGNORED_TAGS:
            self.ignored_tag_level -= 1

    def __sanitize(self, str):
        chars = ['laquo;', 'raquo;', 'nbsp;']
        for char in chars:
            str = str.strip().replace(char, '')
        return str