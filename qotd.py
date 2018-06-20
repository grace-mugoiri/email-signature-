"""import necessary modules"""
from contextlib import closing
import json
try:
    from urllib import urlopen
except ImportError:
    from urllib.request import urlopen

QOTD_URL = "https://www.brainyquote.com/quote_of_the_days"
def qotd():
    """define the qoute of the day function"""
    with closing(urlopen(QOTD_URL)) as f:
        data = json.loads(f.read().decode("utf-8"))
    if data:
        quote, author = data["quote"], data["author"]
    else:
        quote, author = "I hear cats.", "theAuthor"
    return '"%s" ~%s' % (quote, author)
