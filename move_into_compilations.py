#!/usr/bin/env python

"""Takes a Python regex expression to find directory names for a compilation
album that is spread across multiple artist directories and copies the contents
into a common directory under Compliations."""

import os
import re
import shutil
import argparse

MUSIC_SRC = os.path.expanduser('~/music-src')


def copytree(src, dst, symlinks=False, ignore=None):
    for item in os.listdir(src):
        s = os.path.join(src, item)
        d = os.path.join(dst, item)
        if os.path.isdir(s):
            shutil.copytree(s, d, symlinks, ignore)
        else:
            shutil.copy2(s, d)


def find_all_directories_matching(regex, pretend):

    for dir_name, subdir_list, file_list in os.walk(MUSIC_SRC):
        if re.match(regex, dir_name):
            #print('Matched directory: {}'.format(dir_name))
            artist_dir, album_name = os.path.split(os.path.join(MUSIC_SRC, dir_name))
            artist_name = os.path.split(artist_dir)[1]
            #print('Artist: {}'.format(artist_name))
            #print('Album: {}'.format(album_name))
            if artist_name == 'Compilations':
                pass
            else:
                destination = "{}/Compilations/{}".format(MUSIC_SRC, album_name)
                if not os.path.exists(destination):
                    os.makedirs(destination)
                source = "{}".format(dir_name)
                print("Copying contents of {} into {}".format(source, destination))
                if not pretend:
                    copytree(source, destination)

if __name__ == "__main__":

    p = argparse.ArgumentParser()
    p.add_argument('regex')
    p.add_argument('-p', '--pretend', action='store_true')
    args = p.parse_args()
    find_all_directories_matching(args.regex, args.pretend)
