# Note that this is still a manual process, the entire script is unlikely to
# succeed.
# 1. Download the bin zip file.
# 2. Unzip it
# 3. cd into it
# 4. Create these files in the directory.
# First create a rsa_passphrase.txt and github_token.txt files.
# rsa_passphrase.txt: a single line with a new passphrase for this computer
# github_token.txt: the api token provided by your github account

# Install git and curl as the two essential dependencies to this script.
sudo apt-get -y install git curl
git config --global user.email "moorepants@gmail.com"
git config --global user.name "Jason K. Moore"
git config --global core.editor "vim"
if [ ! -f "$HOME/.ssh/id_rsa.pub" ]; then
  mkdir -p $HOME/.ssh
  PASSPHRASE=$( cat rsa_passphrase.txt )
  ssh-keygen -t rsa -C "moorepants@gmail.com" -N $PASSPHRASE -f $HOME/.ssh/id_rsa
fi

# Upload the public key to Github.
# If the key is already there, this fails gracefully.
TITLE=$( hostname )
KEY=$( cat $HOME/.ssh/id_rsa.pub )
JSON=$( printf '{"title": "%s", "key": "%s"}' "$TITLE" "$KEY" )
TOKEN=$( cat github_token.txt )
curl -s -d "$JSON" "https://api.github.com/user/keys?access_token=$TOKEN"

# Download the scripts and install everything from the Ubuntu repositories.
git clone git@github.com:moorepants/bin.git $HOME/bin
sudo apt-get -y install $(grep -vE "^\s*#" $HOME/bin/ubuntu-install-list.txt  | tr "\n" " ")

# Start the battery life software.
if [ "$( sudo dmidecode --string chassis-type )" = "Notebook" ]; then
  sudo tlp start
fi

# Install Nextcloud from their ppa
sudo add-apt-repository ppa:nextcloud-devs/client
sudo apt update
sudo install nexcloud-client

# Install Chrome manually.
cd $HOME/Downloads
wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
sudo dpkg -i google-chrome*.deb
cd -

# Setup all the configuration files.
mkdir -p $HOME/src
if [ ! -d "$HOME/src/dotfiles" ]; then
  git clone git@github.com:moorepants/dotfiles.git $HOME/src/dotfiles
fi
for config in bashrc vimrc gitconfig condarc
do
  if [ -f "$HOME/.$config" ]; then
    rm $HOME/.$config
  fi
  ln -s $HOME/src/dotfiles/$config $HOME/.$config
done
mkdir -p $HOME/.vim/after/ftplugin
rm $HOME/.vim/after/ftplugin/*
for plugin in cpp htmljinja html jinja matlab python rst r tex javascript
do
  ln -s $HOME/src/dotfiles/$plugin.vim $HOME/.vim/after/ftplugin/$plugin.vim
done
if [ ! -d "$HOME/.vim/bundle/vundle" ]; then
  git clone git@github.com:gmarik/vundle.git $HOME/.vim/bundle/vundle
fi

ln -s $HOME/bin/jupyter_custom.js $HOME/.jupyter/custom/custom.js

# Install textext for Inkscape.
if [ ! -d "$HOME/src/textext" ]; then
  git clone git@github.com:textext/textext.git $HOME/src/textext
fi
mkdir -p $HOME/.config/inkscape/extensions
cp $HOME/src/textext/textext.py $HOME/.config/inkscape/extensions/
cp $HOME/src/textext/textext.inx $HOME/.config/inkscape/extensions/

# Install miniconda and some base packages.
cd $HOME/Downloads
wget https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh
cd -
bash $HOME/Downloads/Miniconda3-latest-Linux-x86_64.sh -b -p $HOME/miniconda
export PATH=$HOME/miniconda/bin:$PATH
conda install -y $(grep -vE "^\s*#" $HOME/bin/conda-install-list.txt  | tr "\n" " ")

# Zotero
wget https://raw.github.com/smathot/zotero_installer/master/zotero_installer.sh -O /tmp/zotero_installer.sh
chmod +x /tmp/zotero_installer.sh
/tmp/zotero_installer.sh
# the following line ensures that zotero can update itself when run by
# moorepants
sudo chown -R moorepants:moorepants /opt/zotero/

# heruko
sudo add-apt-repository "deb https://cli-assets.heroku.com/branches/stable/apt ./"
curl -L https://cli-assets.heroku.com/apt/release.key | sudo apt-key add -
sudo apt-get update
sudo apt-get install heroku

cd $HOME/Downloads
wget https://github.com/PCGen/pcgen/releases/download/6.06.01/pcgen-6.06.01-full.zip
unzip pcgen-6.06.01-full.zip
sudo cp -r pcgen /opt/pcgen
cd -
