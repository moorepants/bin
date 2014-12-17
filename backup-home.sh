#!/bin/bash

rsync -avtopg --log-file '/home/rsync.log' --exclude-from '/home/rsync-exclude.txt' /home/ /media/moorepants/moorepantsbackup/ul30a
