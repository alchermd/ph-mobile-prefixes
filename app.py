#!/usr/bin/env python3
from bs4 import BeautifulSoup
import urllib.request


def main():
    url = 'http://typist.ph/5620/mobile-number-prefixes-2017/'
    sauce = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(sauce, 'lxml')

    print(soup)


if __name__ == "__main__":
    main()
