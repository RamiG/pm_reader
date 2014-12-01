from optparse import OptionParser
from html_reader import HtmlReader

def main():
    parser = OptionParser()
    parser.add_option('-u', '--url', dest='url', help='source page URL to parse', metavar='URL')
    options, args = parser.parse_args()
    url = options.url

    if not (url):
        print('Error: Source URL not defined')
        exit()

    html_reader = HtmlReader(url)
    html_reader.parse()
    print('Saved content to %s' % html_reader.file_path)

if __name__ == '__main__':
    main()