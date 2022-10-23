#!/usr/bin/env bash

# This will backup the home directory of this computer to the Synology Disk
# Station.

HOSTNAME=$(hostname)

# Create two files adjacent to this script file with the IP and the port.
IP=$(cat "$HOME/bin/sivaip.txt")
PORT=$(cat "$HOME/bin/sivaport.txt")

echo $HOSTNAME
echo $IP
echo $PORT
echo $HOME

# --delete: delete files on destination that are not present on source
# --delete-excluded: delete excluded files from destination directory
# --rsync-path: path to rsync on destination server
sudo rsync -av -e "ssh -p $PORT" \
  --delete-excluded \
  --rsync-path /bin/rsync \
  --log-file "/home/rsync-backup.log" \
  --include-from "$HOME/bin/${HOSTNAME}-rsync-include.txt" \
  --exclude-from "$HOME/bin/${HOSTNAME}-rsync-exclude.txt" \
  /home/ moorepants@$IP:/var/services/homes/moorepants/backup/$HOSTNAME
