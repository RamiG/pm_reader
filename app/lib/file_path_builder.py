from urlparse import urlparse

class FilePathBuilder:
    def __init__(self, url):
      self.url = url

    def build(self):
        parsed_url = urlparse(self.url)
        parsed_file_name = parsed_url.path.split('/')[-1]

        if parsed_file_name != '':
            file_path = parsed_url.path.rsplit('.', 1)[0] + '.txt'
        else:
            file_path = parsed_url.path + 'index.txt'

        file_path = './output/' + parsed_url.netloc + file_path
        return file_path