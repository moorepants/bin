"""Changes the datetime stamps in the metadata of all JPG images in a set of
directories to the time another time zone. This is useful when you forget to
change the timezone before taking photos on vacation.

python2 change_photo_timezone.py \
    [--test] \
    "<time zone of current datetime stamp>" \
    "<time zone to switch to>" \
    <dir1> <dir2> ... <dirn>

Example use:

python2 change_photo_timezone.py "America/Los_Angeles" "Africa/Nairobi" /home/dir1 /home/dir2

Example time zone strings:

Africa/Nairobi
America/Buenos_Aires
America/Los_Angeles
America/New_York
Asia/Phnom_Penh
Asia/Tokyo

Dependencies:

- Python 2.7
- argparse
- pytz
- PyGObject https://pygobject.readthedocs.io
- GExiv2 https://gitlab.gnome.org/GNOME/gexiv2

"""

import os
import argparse
from datetime import datetime

import pytz
import gi
# prevents some warning message
gi.require_version('GExiv2', '0.10')
from gi.repository import GExiv2


# The Canon PowerShot SX200 IS date format.
# The Olympus TG-860 date format.
# %H is a 24 hour clock
DATE_FORMAT = '%Y:%m:%d %H:%M:%S'


def process_dir(home_tz, vacation_tz, directory, save=True):
    """Changes the datetime metadata of each JPG file in the directory to the
    corresponding time in the vacation time zone.

    Parameters
    ==========
    home_tz : string
        pytz time zone string representing the time zone in which the current
        time stamps are associated with.
    vacation_tz : string
        pytz time zone string representing the time zone in which the current
        time stamps should be associated with.
    directory : string
        The full path to a directory that contains JPG files with date time
        metadata.

    """

    jpg_filenames = sorted([f for f in os.listdir(directory)
                            if f.lower().endswith('.jpg')])

    # Now adjust the three timestamps (DateTime, DateTimeDigitized and
    # DateTimeOriginal) for each file and save the results.

    for filename in jpg_filenames:

        print('=' * 20)
        print(filename)
        print('=' * 20)

        metadata = GExiv2.Metadata(os.path.join(directory, filename))

        for tag in metadata.get_exif_tags():
            if 'Date' in tag:
                timestamp = metadata[tag]
                home_time = home_tz.localize(datetime.strptime(timestamp,
                                                               DATE_FORMAT))
                vacation_time = home_time.astimezone(vacation_tz)
                vacation_timestamp = vacation_time.strftime(DATE_FORMAT)
                print(tag)
                print('Home, {}, time stamp: {}.'.format(home_tz, timestamp))
                print('Vacation, {}, time stamp: {}.'.format(vacation_tz,
                                                             vacation_timestamp))
                print('-' * 20)

                # Set the timestamp.
                if save:
                    metadata[tag] = vacation_timestamp

        # Save the file with the adjusted timestamps.
        if save:
            metadata.save_file()
            print("{} metadata saved to file.".format(filename))

        # what directory should the file be in?
        subdir_template = '%Y/%m/%d/'
        correct_subdir = vacation_time.strftime(subdir_template)
        basedir = directory[:-11]  # YYYY/MM/DD is always 11 long
        subdir = directory[-11:]
        correct_dir = os.path.join(basedir, correct_subdir)

        print('This file should be in: {}'.format(correct_dir))
        print('This file is in: {}'.format(directory))

        # if not in that directory, move it
        if correct_subdir != subdir:
            print('Will move')
            tmp_dir = correct_dir + '-fixed-time/'
            if not os.path.exists(tmp_dir):
                os.makedirs(tmp_dir)
            print('Moving {} to {}'.format(os.path.join(directory, filename),
                                           os.path.join(tmp_dir, filename)))
            if save:
                os.rename(os.path.join(directory, filename),
                          os.path.join(tmp_dir, filename))


if __name__ == "__main__":

    p = argparse.ArgumentParser()
    p.add_argument('home', help=('The timezone designation that the camera was '
                                 'set to when taking the photographs'))
    p.add_argument('vacation', help=('The timezone designation that should '
                                     'have been set.'))
    p.add_argument('directories', nargs='*')
    p.add_argument('-t', '--test', action="store_true", help="Don't save,")
    args = p.parse_args()

    for directory in args.directories:
        process_dir(pytz.timezone(args.home), pytz.timezone(args.vacation),
                    directory, save=not args.test)
