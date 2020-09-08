# This script scans the provided file that contains a package name per line an
# determines if it is not available in the available Ubuntu repositories.
# bash check_packages_exist.sh ubuntu-install-list.txt
RELEASE_NUM=$(lsb_release -r -s)
while read line; do
	if ! apt show $line &> /dev/null; then
		echo "$line is not available in the available Ubuntu $RELEASE_NUM apt repositories"
	fi
done < $1
