#!/bin/bash

# This script backups up the entire home directory to the external hard drive.

HOSTNAME=$(hostname)

rsync -av --log-file '/home/rsync-backup.log' --exclude-from 'rsync-exclude.txt' /home/ /media/moorepants/moorepantsbackup/$HOSTNAME
