# print 'Wow Im in!'

from optparse import OptionParser
from urlparse import urlparse
import os

def main():
    parser = OptionParser()
    parser.add_option('-u', '--url', dest='url', help='source page URL to parse', metavar='URL')
    options, args = parser.parse_args()
    url = options.url

    if not (url):
        print('Error: Source URL not defined')

    parsed_url = urlparse(url)
    print parsed_url

    file_name = parsed_url.path.split('/')[-1]
    if file_name == '':
        file_name = 'index.txt'
    else:
        file_name = file_name.rsplit('.', 1)[0] + '.txt'
        file_path = parsed_url.path.rsplit('/', 1)[0]

    file_path = parsed_url.netloc + file_path
    print file_path

    if not os.path.exists(file_path):
        os.makedirs(file_path)


    with open(file_path + '/' + file_name, 'w') as f:
        f.write(url)

if __name__ == '__main__':
    main()