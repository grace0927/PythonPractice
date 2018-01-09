"""Retrieve and print words from an URL.

Usage:

    python3 words.py <URL>
"""

import sys
from urllib.request import urlopen

def fetch_words(url):
    """Fetch a list of words from an URL.

    Args:
        url: The URL of a UTF-8 text document.

    Returns:
        A list of strings containing the words from the document.
    """
    with urlopen(url) as story:
        story_words = []
        for line in story:
            line_words = line.decode('utf-8').split()
            for word in line_words:
                story_words.append(word)
    return story_words

def print_words(words):
    """Print one word per line.

    Args:
        words: An iterable series of printable words.
    """
    for word in words:
        print(word)

def main(url):
    """Print each word from a text document from an URL

    Args:
        url: An URL of a utf-8 text document
    """
    words = fetch_words(url)
    print_words(words)

if __name__ == '__main__':
    main(sys.argv[1]) # The 0th arg is the module filename
