from HTMLParser import HTMLParser
from textwrap import TextWrapper

class HtmlReader(HTMLParser):
    LINE_SEPARATOR = '\n'

    def __init__(self, url, config):
        HTMLParser.__init__(self)
        self.url = url
        self.config = config
        self.data = []
        self.data_adding = False
        self.tag_level = 0
        self.ignored_tag_level = 0
        self.current_href = ''

    def handle_starttag(self, tag, attributes):
        if tag in self.config.get('ParseOptions', 'search_tags').split():
            self.tag_level += 1

        if tag in self.config.get('ParseOptions', 'ignored_tags').split():
            self.ignored_tag_level += 1

        if self.tag_level and tag == 'a':
            for attr in attributes:
                if attr[0] == 'href':
                    self.current_href = attr[1]
                    break

    def handle_data(self, data):
        if not self.ignored_tag_level and self.tag_level and data.strip() != '':
            data = self.__sanitize(data)
            if self.current_href:
                data = data + ' [' + self.current_href + '] '

            self.data.append(data)
            self.data_adding = True

    def handle_endtag(self, tag):
        self.current_href = ''
        if tag in self.config.get('ParseOptions', 'search_tags').split() and self.tag_level:
            self.tag_level -= 1

            if self.data_adding:
                self.data.append(2 * self.LINE_SEPARATOR)
                self.data_adding = False

        if tag in self.config.get('ParseOptions', 'ignored_tags').split():
            self.ignored_tag_level -= 1

    def get_text(self):
        text = ''.join(self.data)
        text = text.replace('  ', ' ')
        text = text.splitlines()

        wrapper = TextWrapper()
        wrapper.replace_whitespace = False
        wrapper.width = int(self.config.get('FormatOptions', 'line_width'))
        wrapped_text = ''

        for line in text:
            wrapped_text += wrapper.fill(line) + self.LINE_SEPARATOR

        return wrapped_text

    def __sanitize(self, str):
        chars = ['laquo;', 'raquo;', 'nbsp;']
        for char in chars:
            str = str.replace(char, '')

        str = ' '.join(str.split())
        return str