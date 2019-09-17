import urllib.request

import re

import pandas

from matplotlib import pyplot as plt

from bs4 import BeautifulSoup

from collections import Counter


def get_html(url):
    response = urllib.request.urlopen(url)
    return response.read()


def all_links(html):
    soup = BeautifulSoup(html, 'lxml')
    count = 0

    for link in soup.find_all('a'):
        link.get('href')
        count += 1

    return count


def all_images(html):
    soup = BeautifulSoup(html, 'lxml')
    count = 0

    for image in soup.find_all('img'):
        image.get('src')
        count += 1

    return count


def all_words(html):
    soup = BeautifulSoup(html, 'lxml')
    count = Counter()
    for word in soup.findAll('th', {'class': 'small pad-r'}):
        text = re.sub('[^\w0-9 ]', '', word.get_text().lower())
        count.update(text.split(" "))

    plt
    return count


def word_count(html):
    lengths = {}
    soup = BeautifulSoup(html, 'lxml')
    for word in soup.find_all():
        length = len(word)
        if length not in lengths:
            lengths[length] = 1
        else:
            lengths[length] += 1
    sd = sorted(lengths.items())

    plt.bar(lengths.keys(), lengths.values(), color='blue')
    plt.show()


def parse(html):
    soup = BeautifulSoup(html, 'lxml')
    table = soup.find('table', class_='dbi')

    dbs = []

    for row in table.find_all('tr')[3:]:
        cols = row.find_all('th')
        rank = row.find_all('td')
        score = row.find_all('td', class_='pad-l')

        dbs.append({
            'RANK': rank[0].text,
            'DBMS': cols[0].a.text.strip('vendor-provided information available'),
            'TYPE DB': cols[1].text,
            'SCORE': score[0].text.strip()
        })

    return dbs


def main():
    url = 'https://db-engines.com/en/ranking'
    print(parse(get_html(url)))
    print('Amount of links on page =', all_links(get_html(url)))
    print('Amount of images on page =', all_images(get_html(url)))
    print('Frequency of occurrence of DB types, which we can find on the page = ', all_words(get_html(url)))
    word_count(get_html(url))


if __name__ == '__main__':
    main()
