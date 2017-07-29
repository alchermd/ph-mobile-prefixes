#!/usr/bin/env python3
from bs4 import BeautifulSoup
import urllib.request


def main():
    url = 'http://typist.ph/5620/mobile-number-prefixes-2017/'
    sauce = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(sauce, 'lxml')

    all_data = [data.string for data in soup.find_all('td')[2:]]
    pretty_data = []

    for i in range(0, len(all_data), 2):
        pretty_data.append({all_data[i]: all_data[i + 1]})

    print(pretty_data)


if __name__ == "__main__":
    main()
