from optparse import OptionParser
from file_path_builder import FilePathBuilder
from html_reader import HtmlReader

def main():
    parser = OptionParser()
    parser.add_option('-u', '--url', dest='url', help='source page URL to parse', metavar='URL')
    options, args = parser.parse_args()
    url = options.url

    if not (url):
        print('Error: Source URL not defined')
        exit()

    builder = FilePathBuilder(url)
    file_path = builder.build()

    html_reader = HtmlReader(url, file_path)
    html_reader.parse()
    print('Saved content to %s' % file_path)

if __name__ == '__main__':
    main()