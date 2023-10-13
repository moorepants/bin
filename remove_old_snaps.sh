#!/bin/bash
# From: https://superuser.com/questions/1310825/how-to-remove-old-version-of-installed-snaps
# Removes old revisions of snaps
# CLOSE ALL SNAPS BEFORE RUNNING THIS
set -eu

LANG=C snap list --all | awk '/disabled/{print $1, $3}' |
    while read snapname revision; do
        snap remove "$snapname" --revision="$revision"
    done

# clear the cache also
rm -rf /var/lib/snapd/cache/*
