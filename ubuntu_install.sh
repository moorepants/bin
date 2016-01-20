# First create a rsa_passphrase.txt and github_token.txt files.

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
sudo tlp start

# Install Dropbox manually.
cd $HOME/Downloads
wget https://www.dropbox.com/download?dl=packages/ubuntu/dropbox_2015.10.28_amd64.deb -O dropbox_2015.10.28_amd64.deb
sudo dpkg -i dropbox_2015.10.28_amd64.deb
cd -

# Install Chrome manually.
cd $HOME/Downloads
sudo apt-get install libxss1 libappindicator1 libindicator7
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

# Install textext for Inkscape.
if [ ! -d "$HOME/src/textext" ]; then
  hg clone https://bitbucket.org/pv/textext $HOME/src/textext
fi
mkdir -p $HOME/.config/inkscape/extensions
cp $HOME/src/textext/textext.py $HOME/.config/inkscape/extensions/
cp $HOME/src/textext/textex.inx $HOME/.confing/inkscape/extensions/

# Install some source repos
git clone git@github.com:mathjax/MathJax.git $HOME/src/MathJax
git clone git@github.com:imakewebthings/deck.js.git $HOME/src/deck.js

# Install miniconda and some base packages.
cd $HOME/Downloads
wget https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh
cd -
bash $HOME/Downloads/Miniconda3-latest-Linux-x86_64.sh -b
export PATH=$HOME/miniconda3/bin:$PATH
conda install -y $(grep -vE "^\s*#" $HOME/bin/conda-install-list.txt  | tr "\n" " ")
