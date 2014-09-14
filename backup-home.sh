#!/bin/bash

rsync -avtopg --delete --log-file '/home/rsync.log' --exclude-from '/home/rsync-exclude.txt' /home/ /media/moorepants/moorepantsbackup/ul30a
