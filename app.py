#!/usr/bin/env python3
from bs4 import BeautifulSoup
import urllib.request
import json


def main():
    # Setup
    url = 'http://typist.ph/5620/mobile-number-prefixes-2017/'
    sauce = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(sauce, 'lxml')

    # Transform soup into list of dicts.
    all_data = [data.string for data in soup.find_all('td')[2:]]
    key_val_data = []
    for i in range(0, len(all_data), 2):
        key_val_data.append({
            'number': all_data[i],
            'networkName': all_data[i + 1],
        })

    # Transform previous list into format used by the app.
    reduced_data = []
    for num in key_val_data:
        # Check if num.network is in reduced_data
        if num['networkName'] in [d['networkName'] for d in reduced_data]:
            list(filter(lambda d: d['networkName'] == num['networkName'],
                        reduced_data))[0]['numbers'].append(num['number'])
        else:
            reduced_data.append({
                'networkName': num['networkName'],
                'numbers': [num['number']]
            })

    # Save as a json file.
    with open('networks.json', 'w') as fp:
        json.dump({'data': reduced_data}, fp, indent=4)


if __name__ == "__main__":
    main()
