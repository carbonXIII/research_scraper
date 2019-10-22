# Utils for the scraper

import os
from subprocess import Popen

import bs4 as soup
import requests
import random

bs4_parser = 'html.parser'

def write_as_bytes(f, s):
    f.write(s.encode())

def onerror(func, path, exc_info):
    """
    https://stackoverflow.com/questions/2656322/shutil-rmtree-fails-on-windows-with-access-is-denied
    Error handler for ``shutil.rmtree``.

    If the error is due to an access error (read only file)
    it attempts to add write permission and then retries.

    If the error is for another reason it re-raises the error.

    Usage : ``shutil.rmtree(path, onerror=onerror)``
    """
    import stat
    if not os.access(path, os.W_OK):
        # Is the error an access error ?
        os.chmod(path, stat.S_IWUSR)
        func(path)
    else:
        raise

def choose_subset(top, total):
    if total < top:
        top = total
    return random.sample(range(total), top)

def run_proc(cmarkdown, stdin=None, stdout=None):
    return Popen(cmarkdown,stdin=stdin,stdout=stdout)

def clone(url,repo_dir):
    run_proc(['git','clone',url,repo_dir]).wait()

def slurp(url):
    page = requests.get(url)
    if page.status_code is 200:
        return (soup.BeautifulSoup(page.content, features=bs4_parser), page.url)
    else:
        return (page.status_code, page.url)

