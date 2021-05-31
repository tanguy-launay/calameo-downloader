import argparse
import os
import requests
from bs4 import BeautifulSoup
from book_maker import *
from itertools import zip_longest

def url_checker(calameo_url:str):
    if "calameo.com" not in calameo_url:
        raise argparse.ArgumentTypeError(f"No calameo book will be found there: {calameo_url}")
    else:
        return calameo_url

def valid_urls(urls:list):
    valid = []
    for url in urls:
        r = requests.get(url)
        if r.status_code == 200:
            valid.append(url)
        else:
            print(f"The url could not be processed successfully: {url}")
    return valid
# Construct the argument parser
ap = argparse.ArgumentParser()

# Add the arguments to the parser
ap.add_argument("-u", "--urls", nargs='+', type=url_checker, required=True,
   help="calameo url of the book you want to download")
ap.add_argument("-n", "--names", nargs='*', required=False, default=[],
   help="the output name of the PDF book, if not specified, it will be the one on the website")
ap.add_argument("-d", "--directory", required=False, default=os.getcwd(),
   help="the output directory, and if not specified, the working one")
args = vars(ap.parse_args())

books = {book:title for book,title in zip_longest(valid_urls(args["urls"]),args["names"],fillvalue="")}
pdf_maker(books, directory=args["directory"])
