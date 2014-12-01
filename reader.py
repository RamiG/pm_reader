from urlparse import urlparse
import os.path

class Reader:
    def __init__(self, url):
        self.url = url

    def prepare_dir(self):
        parsed_url = urlparse(self.url)
        parsed_file_path = parsed_url.path
        parsed_file_name = parsed_file_path.split('/')[-1]

        if parsed_file_name != '':
            parsed_file_name = parsed_file_name.rsplit('.', 1)[0] + '.txt'
            parsed_file_path = parsed_file_path.rsplit('/', 1)[0]
        else:
            parsed_file_name = 'index.txt'

        self.file_path = parsed_url.netloc + parsed_file_path
        self.file_name = parsed_file_name

        if not os.path.exists(self.file_path):
            os.makedirs(self.file_path)