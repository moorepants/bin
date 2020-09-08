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
sudo apt -y install git curl
git config --global user.email "moorepants@gmail.com"
git config --global user.name "Jason K. Moore"
git config --global core.editor "vim"
# Create an public/private key for this user and computer.
if [ ! -f "$HOME/.ssh/id_rsa.pub" ]; then
  mkdir -p $HOME/.ssh
  PASSPHRASE=$( cat rsa_passphrase.txt )
  ssh-keygen -t rsa -C "moorepants@gmail.com" -N $PASSPHRASE -f $HOME/.ssh/id_rsa
fi

# Upload the public key to Github.
# If the key is already there, this fails gracefully.
# Github now issues a warning that this API is being deprecated and some other way is needed.
TITLE=$( hostname )
KEY=$( cat $HOME/.ssh/id_rsa.pub )
JSON=$( printf '{"title": "%s", "key": "%s"}' "$TITLE" "$KEY" )
TOKEN=$( cat github_token.txt )
curl -s -d "$JSON" "https://api.github.com/user/keys?access_token=$TOKEN"

# Download the scripts and install everything from the Ubuntu repositories.
git clone git@github.com:moorepants/bin.git $HOME/bin
UBUNTUVERSION=$(lsb_release -r -s)
sudo apt-get -y install $(grep -vE "^\s*#" $HOME/bin/ubuntu-install-list-$UBUNTUVERSION.txt  | tr "\n" " ")

# Start the battery life software if on a laptop.
if [ "$( sudo dmidecode --string chassis-type )" = "Notebook" ]; then
  sudo tlp start
fi

# Install Insync
sudo apt-key adv --keyserver keyserver.ubuntu.com --recv-keys ACCAF35C
sudo echo "deb http://apt.insync.io/ubuntu bionic non-free contrib" > /etc/apt/sources.list.d/insync.list
sudo apt update
sudo apt install insync

# Install Chrome manually.
cd $HOME/Downloads
wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
sudo dpkg -i google-chrome*.deb
cd -

# Setup all the configuration files.
mkdir -p $HOME/src
if [ ! -d "$HOME/src/dotfiles" ]; then
  git clone git@github.com:moorepants/dotfiles.git $HOME/src/dotfiles
else
  cd $HOME/src/dotfiles
  git pull origin master
  cd -
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
for plugin in cpp html htmljinja javascript jinja matlab python r rst tex yaml
do
  ln -s $HOME/src/dotfiles/$plugin.vim $HOME/.vim/after/ftplugin/$plugin.vim
done
if [ ! -d "$HOME/.vim/bundle/Vundle.vim" ]; then
  git clone git@github.com:VundleVim/Vundle.vim.git $HOME/.vim/bundle/Vundle.vim
fi

mkdir -p $HOME/.jupyter/custom
ln -s $HOME/bin/jupyter_custom.js $HOME/.jupyter/custom/custom.js

# Install textext for Inkscape.
# TODO : Update this section. Inkscape 0.92 comes with Ubuntu 20.04. The new
# textext author dropped support for Inkscape 0.92 after textext version 0.11.
# But textext 0.11 (optionally requires) python-gtk2 and python-gtksourceview2
# which are no longer available via apt. So this makes it a bit hard to install
# textext on 20.04.
if [ ! -d "$HOME/src/textext" ]; then
  git clone git@github.com:textext/textext.git $HOME/src/textext
fi
cd $HOME/src/textext
git checkout 0.9.1
/usr/bin/python2 setup.py
cd -

# Install miniconda and some base packages.
cd $HOME/Downloads
# Having trouble installing a consistent set of packages with Python 3.8
#wget https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh
wget https://repo.anaconda.com/miniconda/Miniconda3-py37_4.8.3-Linux-x86_64.sh
cd -
#bash $HOME/Downloads/Miniconda3-latest-Linux-x86_64.sh -b -p $HOME/miniconda
bash $HOME/Downloads/Miniconda3-py37_4.8.3-Linux-x86_64.sh -b -p $HOME/miniconda
export PATH=$HOME/miniconda/bin:$PATH
conda install -y $(grep -vE "^\s*#" $HOME/bin/conda-install-list.txt  | tr "\n" " ")

# Zotero
# https://github.com/retorquere/zotero-deb
wget -qO- https://github.com/retorquere/zotero-deb/releases/download/apt-get/install.sh | sudo bash
sudo apt update
sudo apt install zotero

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
