from HTMLParser import HTMLParser

class HtmlReader(HTMLParser):
    SEPARATED_TAGS = ['h1', 'h2', 'h3', 'h4', 'p']
    TAGS = ['a', 'span'] + SEPARATED_TAGS

    def __init__(self, url,):
        HTMLParser.__init__(self)
        self.url = url
        self.level = 0
        self.data = []
        self.data_added = False

    def get_text(self):
        return u''.join(self.data)

    def handle_starttag(self, tag, attributes):
        if tag in self.TAGS:
            self.level += 1

    def handle_data(self, data):
        if self.level and data.strip() != '':
            self.data.append(self.__sanitize(data))
            self.data_added = True
            print data.strip()

    def handle_endtag(self, tag):
        if tag in self.TAGS and self.level:
            self.level -= 1
            if self.data_added:
                self.data.append('\r\n\r\n')
                self.data_added = False

    def __sanitize(self, str):
        chars = ['laquo;', 'raquo;', 'nbsp;']
        for char in chars:
            str = str.replace(char, '')
        return str.strip('\n')
