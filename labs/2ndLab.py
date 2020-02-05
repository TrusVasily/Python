import collections
import re

from itertools import islice
from bs4 import BeautifulSoup
from requests import request
import matplotlib.pyplot as plt
import pandas as pd
import operator


def get_all_links(url):
    req = request('GET', url)
    soup = BeautifulSoup(req.text, 'lxml')
    href = []
    links = soup.find_all('a', href=True)
    print('Amount of links {}.'.format(len(links)))
    for a in links:
        href.append(a['href'])
    return list(filter(lambda a: a != '#', href))


def get_text(url):
    req = request('GET', url)
    soup = BeautifulSoup(req.text, 'lxml')

    for script in soup(["script", "style"]):
        script.extract()

    text = soup.get_text().replace(',', '').replace(' ', '').replace('\n', '').lower()

    result = ''

    for char in text:
        if re.match(r'^[а-яА-я]$', char):
            result += char
    return result


def get_all_words(url):
    req = request('GET', url)
    soup = BeautifulSoup(req.text, 'lxml')

    for script in soup(["script", "style"]):
        script.extract()

    text = soup.get_text()
    words = text.replace(',', '').split()

    for i, word in enumerate(words):
        if re.match(r'^\d+$', word):
            words.pop(i)

    return words


def count_chars(text):
    chars = collections.Counter(text)
    return chars


def count_words(words):
    c = collections.Counter(words)
    return dict(c)


def count_symbols(words):
    counter = []

    for word in words:
        counter.append(len(word))

    c = collections.Counter(counter)
    result = {}
    for key in sorted(c.keys()):
        result[key] = c[key]

    return result


def take(n, iterable):
    return dict(islice(iterable, n))


def draw_plot(values, lbx='xplot', lby='yplot'):
    plt.bar(range(len(values)), list(values.values()), align='center')
    plt.xlabel(lbx)
    plt.ylabel(lby)
    plt.xticks(range(len(values)), list(values.keys()))
    plt.show()


def main():
    link = 'http://tabletennis.by/tours/2019-09-29'
    results = {}
    counter = 0

    for url in get_all_links(link):
        counter += 1
        try:
            results[url] = {
                'urls': len(get_all_links(url)),
                'words': list(count_words(get_all_words(url)).keys()),
                'chars': list(count_symbols(get_all_words(url)).keys())
            }
        except:
            print('bad link')
        if counter > 3:
            break

    df = pd.DataFrame(data=results)
    print(df)

    sorted_words = {}
    for elem in sorted(count_words(get_all_words(link)).items(), key=operator.itemgetter(1), reverse=True):
        sorted_words[elem[0]] = elem[1]
    draw_plot(take(10, sorted_words.items()), 'Words', 'Occurrences')
    draw_plot(count_symbols(get_all_words(link)), 'Word length', 'Amount words')
    draw_plot(count_chars(get_text(link)), 'Letters', 'Amount')


if __name__ == '__main__':
    main()