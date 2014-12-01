import os.path

class HtmlReader:
    def __init__(self, url, file_path):
        self.url = url
        self.output_file_path = file_path

    def parse(self):
        self.__ensure_dir_exists()
        
        with open(self.output_file_path, 'w') as f:
            f.write(self.url)

    def __ensure_dir_exists(self):
        dir = os.path.dirname(self.output_file_path)
        if not os.path.exists(dir):
            os.makedirs(dir)
