import os.path
from HTMLParser import HTMLParser

class HtmlReader(HTMLParser):
    def __init__(self, url, file_path):
        HTMLParser.__init__(self)
        self.url = url
        self.output_file_path = file_path
        self.reading = 0

    def handle_starttag(self, tag, attributes):
        if tag == 'h1':
            self.reading += 1

    def handle_data(self, data):
        if self.reading:
            print data
            self.file.write(data.encode('utf8') + "\r\n\r\n")

    def handle_endtag(self, tag):
        if tag == 'h1' and self.reading:
            self.reading -= 1

    def feed(self, html):
        self.__ensure_dir_exists()
        self.file = open(self.output_file_path, 'w')
        HTMLParser.feed(self, html)
        # self.file.close

    def __ensure_dir_exists(self):
        dir = os.path.dirname(self.output_file_path)
        if not os.path.exists(dir):
            os.makedirs(dir)
