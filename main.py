from optparse import OptionParser
import urllib
from lib.file_path_builder import FilePathBuilder
from lib.html_reader import HtmlReader

def main():
    parser = OptionParser()
    parser.add_option('-u', '--url', dest='url', help='source page URL to parse', metavar='URL')
    options, args = parser.parse_args()
    url = options.url

    if not (url):
        print('Error: Source URL not defined')
        exit()

    builder = FilePathBuilder(url)
    output_file_path = builder.build()

    f = urllib.urlopen(url)
    encoding = f.headers.getparam('charset') or 'utf-8'
    html = f.read().decode(encoding)

    html_reader = HtmlReader(url, output_file_path)
    html_reader.feed(html)
    print('Saved content to %s' % output_file_path)

if __name__ == '__main__':
    main()