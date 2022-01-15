#!/usr/bin/env bash

# This will backup the /home/moorepants/Music directory of this computer to the
# Synology Disk Station's shared music directory.

HOSTNAME=$(hostname)

# Create two files adjacent to this script file with the IP and the port.
IP=$(cat "$HOME/bin/sivaip.txt")
PORT=$(cat "$HOME/bin/sivaport.txt")

echo $IP
echo $PORT

# --delete: delete files on destination that are not present on source
# --delete-excluded: delete excluded files from destination directory
# --rsync-path: path to rsync on destination server
rsync -av -e "ssh -p $PORT" \
  --rsync-path /bin/rsync \
  --log-file "/home/rsync-backup.log" \
  /home/moorepants/Music/ moorepants@$IP:/var/services/music
