# print 'Wow Im in!'

from optparse import OptionParser
from reader import Reader

def main():
    parser = OptionParser()
    parser.add_option('-u', '--url', dest='url', help='source page URL to parse', metavar='URL')
    options, args = parser.parse_args()
    url = options.url

    if not (url):
        print('Error: Source URL not defined')

    reader = Reader(url)
    reader.prepare_dir()
    print reader.file_path
    print reader.file_name

    with open(reader.file_path + '/' + reader.file_name, 'w') as f:
        f.write(url)

if __name__ == '__main__':
    main()