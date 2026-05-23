#!/bin/bash
# Goes through each snap and shows which core it depends on.
packagenames=`snap list --all | awk '{print $1;}'`
for item in $packagenames
do
	echo $item
	snap info --verbose $item | grep 'base:' | awk '{ print $2 }'
	echo "==============================="
done

