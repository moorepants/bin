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

There is one basic test which can be run like:

    python generate_sub_bib.py null null null --test

 It requires the pybtex program:

    pip install pybtex

"""

# standard library
import re
import os
import time
import StringIO

# external libraries
from pybtex.database import BibliographyData
from pybtex.database.input import bibtex as input_bibtex
from pybtex.database.output import bibtex as output_bibtex


class SubBib(object):

    def __init__(self, path_to_tex, path_to_main, path_to_sub, force=False):
        self.path_to_tex = path_to_tex
        self.path_to_main = path_to_main
        self.path_to_sub = path_to_sub

        if self.rebuild_is_needed() or force is True:
            self.extract_unique_bibkeys()
            self.load_main_file()
            self.build_new_file()
        else:
            print("{} is already up-to-date, add --force to force a rebuild".format(self.path_to_sub))

    def rebuild_is_needed(self):
        try:
            open(self.path_to_sub, 'r')
        except IOError:
            return True
        else:
            last_time_main_modified = \
                time.ctime(os.path.getmtime(self.path_to_main))

            last_time_sub_modified = \
                time.ctime(os.path.getmtime(self.path_to_sub))

            if last_time_main_modified > last_time_sub_modified:
                return True
            else:
                return False

    def extract_unique_bibkeys(self):
        with open(self.path_to_tex, 'r') as f:
            tex_text = f.read()

        citations = re.findall(r'\\n?o?cite\{(.*?)\}', tex_text, re.DOTALL)
        for citation in citations[:]:
            if ',' in citation:
                citations += [c.strip() for c in citation.strip().split(',')]
                citations.remove(citation)
        citations = [c.strip() for c in citations]
        while '' in citations:
            citations.remove('')
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


def test():
    main_bib_text = \
r"""\
@ARTICLE{Moses1986,
   author = {Moses Moses},
   title = {The Gnats and Gnus Document Preparation System},
   journal = {The Bible},
   year = 1986,
}

@ARTICLE{Moses1986a,
   author = {Moses Moses},
   title = {Document Preparation System},
   journal = {The Bible},
   year = 1986,
}

@ARTICLE{Judiah1986,
   author = {Moses Moses},
   title = {Document Preparation System},
   journal = {The Bible},
   year = 1986,
}

@ARTICLE{Peter1876,
   author = {Peter Lamb},
   title = {Document Preparation System},
   journal = {The Bible},
   year = 1876,
}

@ARTICLE{Dillan1987,
   author = {Bob Dillan},
   title = {Document Preparation System},
   journal = {The Bible},
   year = 1987,
}

@ARTICLE{Dillan1987a,
   author = {Bob Dillan},
   title = {On the road again},
   journal = {The Bible},
   year = 1987,
}

@ARTICLE{Ramone1988,
   author = {Joey Ramone},
   title = {On the road again},
   journal = {The Bible},
   year = 1987,
}

@ARTICLE{Harrison1967,
   author = {George Harrison},
   title = {Blasphemous},
   journal = {The Bible},
   year = 1987,
}"""

    example_text = \
r"""We are talking about \cite{Moses1986} and then
\cite{Moses1986a,Judiah1986} both went crazy. Don't cite this one
\nocite{Peter1876}.

Here is a funny list:
\nocite{
  Dillan1987
}
\nocite{Dillan1987a,
  Ramone1988,
  Harrison1967}
\cite{
  Dillan1987a,
  Ramone1988,
  Harrison1967,
}"""

    with open('test_main.bib', 'w') as f:
        f.write(main_bib_text)

    with open('example_tex_file.tex', 'w') as f:
        f.write(example_text)

    creator = SubBib('example_tex_file.tex', 'test_main.bib',
                     'test_sub_bib.bib')

    expected_unique_keys = ['Moses1986', 'Moses1986a', 'Judiah1986',
                            'Peter1876', 'Dillan1987', 'Dillan1987a',
                            'Ramone1988', 'Harrison1967']
    assert sorted(expected_unique_keys) == sorted(creator.unique_bibtex_keys)

    os.remove('test_main.bib')
    os.remove('example_tex_file.tex')
    os.remove('test_sub_bib.bib')

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

    parser.add_argument('--force', action='store_true',
        help="Add to force a rebuild of the sub bib.", default=False)

    parser.add_argument('--test', action='store_true',
        help="Ignores arguments and runs the test.", default=False)

    args = parser.parse_args()

    if args.test is True:
        test()
    else:
        creator = SubBib(args.paper, args.mainbib, args.subbib, force=args.force)
