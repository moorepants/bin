#!/bin/bash

# bash backup-cd.sh /media/.../mycd mycd

HOSTNAME=$(hostname)

# Create two files adjacent to this script file with the IP and the port.
IP=$(cat "sivaip.txt")
PORT=$(cat "sivaport.txt")

rsync -av -e "ssh -p $PORT" \ #  --delete \
  --rsync-path /bin/rsync \
  "$1" moorepants@$IP:/var/services/homes/moorepants/backup/cds/$2
