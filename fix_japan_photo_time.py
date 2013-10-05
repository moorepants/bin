#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""This script converts the time/date stamp of photographs we took in Japan to
Japanese time/date from US Pacific time becaue we forgot to adjust the camera's
internal clock at the beginning of the trip."""

import os
import re
from datetime import datetime

import pytz
from gi.repository import GExiv2

# The Canon PowerShot SX200 IS date format.
DATE_FORMAT = '%Y:%m:%d %H:%M:%S'

# We snapped photos in Japan while using the current PST time (which is under
# Daylight Savings Time, but Japan is not).
pacific_tz = pytz.timezone("America/Los_Angeles")
japan_tz = pytz.timezone("Asia/Tokyo")

# Get a list of file names that match the time we were there and the camera
# filename format.
directory = "/media/Data/My Pictures"
pattern = r"/media/Data/My Pictures/2013-0[4-5]-\d\d/img_\d\d\d\d.jpg"

files_to_adjust = []

for root, dirnames, filenames in os.walk(directory):
    for filename in filenames:
        path = os.path.join(root, filename)
        result = re.match(pattern, path)
        # if a matching file is found, save it to the list
        if result:
            files_to_adjust.append(path)

# Now adjust the three timestamps (DateTime, DateTimeDigitized and
# DateTimeOriginal) for each file and save the results.

for filename in files_to_adjust:

    print('-' * 20)
    print(filename)
    print('-' * 20)

    metadata = GExiv2.Metadata(filename)

    for tag in metadata.get_exif_tags():
        if 'DateTime' in tag:
            timestamp = metadata[tag]
            pacific_time = pacific_tz.localize(datetime.strptime(timestamp,
                DATE_FORMAT))
            japan_time = pacific_time.astimezone(japan_tz)
            japan_timestamp = japan_time.strftime(DATE_FORMAT)
            print(tag)
            print('Current time stamp: {}.'.format(timestamp))
            print('Adjusted time stamp: {}.'.format(japan_timestamp))
            print('-' * 20)

            # Set the timestamp.
            metadata[tag] = japan_timestamp

    # Save the file with the adjusted timestamps.
    metadata.save_file()
