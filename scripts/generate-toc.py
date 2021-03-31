#!/usr/bin/env python3

import argparse
import os.path
import yaml

def generate_toc(sections, files):
    """

    :param sections: list of dicts describing section, each include at least 'title' and 'folder'
    :param files: list of files to include, must be relative to document root
     """
    section_files = {}
    for section in sections:
        section_files[section['folder']] = []
    for path in files:
        with open(path) as f:
            frontmatter = next(yaml.safe_load_all(f))
        path_dir = os.path.dirname(path)
        while path_dir and path_dir not in section_files:
            path_dir = os.path.dirname(path_dir)
        if not path_dir:
            # no matching section
            continue
        section_files[path_dir].append({
            'title': frontmatter['title'],
            'path': path,
            'permalink': frontmatter['permalink'],
        })
    print("---")
    print("permalink: /doc/")
    print("title: Qubes OS documentation")
    print("documentclass: scrartcl")
    print("---")
    print("# Table of contents")
    print("")
    for section in sections:
        print("##{} {}\n".format('#' * section['folder'].count('/'), section['title']))
        for doc in section_files[section['folder']]:
            print("* [{}]({})".format(doc['title'], doc['permalink']))
        print("\n")

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('sections'),
    parser.add_argument('files', nargs='*')
    args = parser.parse_args()
    with open(args.sections) as f:
        sections = yaml.safe_load(f)
    generate_toc(sections, args.files)

if __name__ == '__main__':
    main()
