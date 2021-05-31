**Background**
--
Calameo is a website providing everyone with books or magazines. However, the lack of downloading option makes it harder to keep and read contents offline .

**Installation**
--
To install files:
`````
git clone https://github.com/tanguy-launay/calameo-downloader
`````
To Install Required Modules:
`````
pip install -r requirements.txt
`````

**Usage**
--
`````
usage: urls_scrapper.py [-h] -u URLS [URLS ...] [-n [NAMES [NAMES ...]]]

optional arguments:
  -h, --help            show this help message and exit
  -u URLS [URLS ...], --urls URLS [URLS ...]
                        calameo url list of the book(s) you want to download, separated by spaces
  -n [NAMES [NAMES ...]], --names [NAMES [NAMES ...]]
                        the output name of the PDF book, if not specified, it
                        will be the one on the website
`````
Configurations are done within the urls_scrapper.py file.
These configurations include:

* List of book links
* Possibility to change the names
* Option to only download PDF version
* Choosing another directory

Given a list of calmeo.com books, the script will go through all the pages and dowload them.
If `only_pdf` is set to false, the script will not clean intermediate files (images, single page pdf, ...)

**Credits**
--
This project is a fork from https://github.com/whoisoscar/calameo-downloader
The 2 functions to convert images to pdf are copied pasted from the original.
