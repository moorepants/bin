"""

Example use:

python change_photo_timezone "America/Los_Angeles" "Africa/Nairobi" /home/dir1 /home/dir2

Africa/Nairobi
Asia/Phnom_Penh
America/New_York

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
# %H is a 24 hour clock
DATE_FORMAT = '%Y:%m:%d %H:%M:%S'


def process_dir(home_tz, vacation_tz, directory, save=True):

    jpg_filenames = sorted([f for f in os.listdir(directory) if f.lower().endswith('.jpg')])

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


        # The moving isn't a good idea because you may move files into a
        # directory that you'd like to modify the date times of.

        # what directory should the file be in?
        correct_dir = vacation_time.strftime('/home/moorepants/Pictures/%Y/%m/%d')

        # if not in that directory, move it
        if correct_dir != directory:
            print('Moving {} to {}'.format(os.path.join(directory, filename),
                                           os.path.join(correct_dir, filename)))
            #os.rename(os.path.join(directory, filename),
                      #os.path.join(correct_dir, filename))


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
