import urllib
import os.path
import ConfigParser

from optparse import OptionParser
from app.lib.file_path_builder import FilePathBuilder
from app.lib.html_reader import HtmlReader

def ensure_dir_exists(file_path):
    dir = os.path.dirname(file_path)
    if not os.path.exists(dir):
        os.makedirs(dir)

def main():
    parser = OptionParser()
    parser.add_option('-u', '--url', dest='url', help='source page URL to parse', metavar='URL')
    options, args = parser.parse_args()
    url = options.url

    if not (url):
        print('Error: Source URL not defined')
        exit()

    config = ConfigParser.ConfigParser()
    config.read('default.cfg')

    f = urllib.urlopen(url)
    encoding = f.headers.getparam('charset') or 'utf-8'
    html = f.read().decode(encoding)
    html_reader = HtmlReader(url, config)
    html_reader.feed(html)

    builder = FilePathBuilder(url)
    output_file_path = builder.build()
    ensure_dir_exists(output_file_path)
    with open(output_file_path, 'w') as f:
       f.write(html_reader.get_text().encode('utf-8'))
    print('Saved content to %s' % output_file_path)

if __name__ == '__main__':
    main()