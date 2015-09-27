apt-get install $(grep -vE "^\s*#" ubuntu-install-list.txt  | tr "\n" " ")
