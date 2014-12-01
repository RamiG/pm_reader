from urlparse import urlparse
import os.path

class HtmlReader:
    def __init__(self, url):
        self.url = url
        self.__set_file_path()

    def parse(self):
        self.__ensure_dir_exists()
        
        with open(self.file_path, 'w') as f:
            f.write(self.url)

    def __set_file_path(self):
        parsed_url = urlparse(self.url)
        parsed_file_name = parsed_url.path.split('/')[-1]

        if parsed_file_name != '':
            self.file_path = parsed_url.netloc + parsed_url.path.rsplit('.', 1)[0] + '.txt'
        else:
            self.file_path = parsed_url.netloc + parsed_url.path + 'index.txt'

    def __ensure_dir_exists(self):
        dir = os.path.dirname(self.file_path)
        if not os.path.exists(dir):
            os.makedirs(dir)
