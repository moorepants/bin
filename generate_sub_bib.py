#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""This command line script allows you to extract the bibliographic entries
from a bibtex bib file based on the unique citations in a TeX/LaTeX file. I
keep all of my biblio information in a single database (bib file), but
desire to have a small bib file to include with the paper I'm writing. So
this script:

 - scans the tex file for the unique citation keys
 - gets the keys from the main bib file
 - generates a new bib file with only the entries that are cited in the tex
 file

 You use it like this:

    python generate_sub_bib.py paper.tex main.bib sub_bib.bib

 It requires the pybtex program:

    pip install pybtex

"""

# standard library
import re

# external libraries
from pybtex.database import BibliographyData
from pybtex.database.input import bibtex as input_bibtex
from pybtex.database.output import bibtex as output_bibtex


class SubBib(object):

    def __init__(self, path_to_tex, path_to_main, path_to_sub):
        self.path_to_tex = path_to_tex
        self.path_to_main = path_to_main
        self.path_to_sub = path_to_sub

        self.extract_unique_bibkeys()
        self.load_main_file()
        self.build_new_file()

    def extract_unique_bibkeys(self):
        with open(self.path_to_tex, 'r') as f:
            tex_text = f.read()

        citations = re.findall(r'\\cite\{(.*?)\}', tex_text)
        for citation in citations[:]:
            if ',' in citation:
                citations += citation.split(',')
                citations.remove(citation)
        self.unique_bibtex_keys = list(set(citations))

    def load_main_file(self):
        parser = input_bibtex.Parser()
        self.main_bib_data = parser.parse_file(self.path_to_main)

    def build_new_file(self):
        new_entries = {}
        for key in self.main_bib_data.entries.keys():
            if key in self.unique_bibtex_keys:
                new_entries[key] = self.main_bib_data.entries[key]
        database = BibliographyData(entries=new_entries)
        writer = output_bibtex.Writer()
        writer.write_file(database, self.path_to_sub)


if __name__ == "__main__":

    import argparse

    parser = argparse.ArgumentParser(
        description='Generate a sub bib file.')

    # python generate_sub_bib.py paper.tex main.bib subbib.tex

    parser.add_argument('paper', type=str,
        help="The tex file to find the citations.")

    parser.add_argument('mainbib', type=str,
        help="The main file.")

    parser.add_argument('subbib', type=str,
        help="The new subfile.")

    args = parser.parse_args()

    creator = SubBib(args.paper, args.mainbib, args.subbib)
