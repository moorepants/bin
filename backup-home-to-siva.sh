#!/bin/bash

# This will backup the home directory of this computer to the Synology Disk
# Station.

HOSTNAME=$(hostname)

# Create two files adjacent to this script file with the IP and the port.
IP=$(cat "sivaip.txt")
PORT=$(cat "sivaport.txt")

rsync -av -e "ssh -p $PORT" \ #  --delete \
  --delete-excluded \  # delete excluded files from destination directory
  --rsync-path /bin/rsync \
  --log-file "/home/rsync-backup.log" \
  --include-from "$HOME/bin/${HOSTNAME}-rsync-include.txt" \
  --exclude-from "$HOME/bin/${HOSTNAME}-rsync-exclude.txt" \
  /home/ moorepants@$IP:/var/services/homes/moorepants/backup/$HOSTNAME
