#!/usr/bin/env python3

import sys
import copy
from panflute import *

ATTACHMENT_BASEDIR = '.'
BASE_URL = "https://www.qubes-os.org"

def get_anchor(url):
    page, h, identifier = url.partition('#')
    anchor = '#' + page.strip('/').replace('/', '-')
    if h:
        anchor += '-' + identifier
    return anchor

def filter_link(elem, doc):
    if isinstance(elem, Image):
        if elem.url.startswith('/attachment') or elem.url.startswith('//attachment'):
            elem.url = ATTACHMENT_BASEDIR + elem.url
    elif isinstance(elem, Link):
        if elem.url.startswith('/'):
            elem.url = get_anchor(elem.url)
    elif isinstance(elem, Header):
        permalink = doc.metadata['permalink'].content[0].text
        link_prefix = permalink.strip('/').replace('/', '-')
        if not hasattr(doc, 'first_header_seen'):
            elem.identifier = link_prefix
            doc.first_header_seen = True
        else:
            elem.identifier = link_prefix + '-' + elem.identifier

def main(doc=None):
    return run_filter(filter_link, doc=doc)

if __name__ == "__main__":
    main()
