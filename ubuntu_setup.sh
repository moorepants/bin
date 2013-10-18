#!/usr/bin/env bash

# This script sets up a base Ubuntu installation for a new machine with all the
# pacakges that I commonly use. It attempts to automate the installation
# instructions included in ubuntu_setup.rst.

alias aptitude="aptitude -q=2 -y"

# Get aptitude and update/upgrade
echo "Aptitude and update"
apt-get -y install aptitude
aptitude update
aptitude upgrade

# Version Control
echo "Version Control"
aptitude install git gitk subversion mercurial bzr subversion
git config --global user.email "moorepants@gmail.com"
git config --global user.name "Jason K. Moore"
chmod +x /usr/share/doc/git/contrib/subtree/git-subtree.sh
ln -s /usr/share/doc/git/contrib/subtree/git-subtree.sh /usr/lib/git-core/git-subtree

# Generate an SSH key if one doesn't already exist
TITLE=$( hostname )
if [[ $TITLE == vagrant* ]]; then
	PASSPHRASE=$( cat /vagrant/passphrase.txt )
else
	PASSPHRASE=$( cat passphrase.txt )
fi
if [ ! -f $HOME/.ssh/id_rsa.pub ]; then
	ssh-keygen -t rsa -C "moorepants@gmail.com" -N $PASSPHRASE -f $HOME/.ssh/id_rsa
fi
# Upload the public ssh key to Github using their API.
# TODO : What if key already exists?
KEY=$( cat $HOME/.ssh/id_rsa.pub )
JSON=$( printf '{"title": "%s", "key": "%s"}' "$TITLE" "$KEY" )
if [[ $TITLE == vagrant* ]]; then
	TOKEN=$( cat /vagrant/github_token.txt )
else
	TOKEN=$( cat github_token.txt )
fi
aptitude install curl
curl -s -d "$JSON" "https://api.github.com/user/keys?access_token=$TOKEN"

# Scripts
echo "Scripts"
git clone git@github.com:moorepants/bin.git $HOME/bin

# Dot Files
echo "Dot Files"
git clone git@github.com:moorepants/dotfiles.git $HOME/src/dotfiles
if [ -f $HOME/.bashrc ]; then
	rm $HOME/.bashrc
fi
ln -s $HOME/src/dotfiles/bashrc $HOME/.bashrc
if [ -f $HOME/.vimrc ]; then
	rm $HOME/.vimrc
fi
ln -s $HOME/src/dotfiles/vimrc $HOME/.vimrc
mkdir -p $HOME/.vim/after/ftplugin
ln -s $HOME/src/dotfiles/html.vim $HOME/.vim/after/ftplugin/html.vim
ln -s $HOME/src/dotfiles/matlab.vim $HOME/.vim/after/ftplugin/python.vim
ln -s $HOME/src/dotfiles/tex.vim $HOME/.vim/after/ftplugin/tex.vim
ln -s $HOME/src/dotfiles/matlab.vim $HOME/.vim/after/ftplugin/matlab.vim
ln -s $HOME/src/dotfiles/rst.vim $HOME/.vim/after/ftplugin/rst.vim

# Vim
echo "Installing Vim"
aptitude install vim-gtk exuberant-ctags
git config --global core.editor "vim"
git clone https://github.com/gmarik/vundle.git ~/.vim/bundle/vundle

# Software Development
echo "Software Development"
aptitude install build-essential gfortran python-dev cmake cmake-curses-gui
aptitude install python-pip
pip install -U pip # upgrade pip
pip install virtualenv virtualenvwrapper
mkdir $HOME/envs

# General
echo "General"
wget https://www.dropbox.com/download?dl=packages/debian/dropbox_1.6.0_amd64.deb -O $HOME/Downloads/dropbox_1.6.0_amd64.deb
dpkg -i $HOME/Downloads/dropbox_1.6.0_amd64.deb
aptitude install keepassx
aptitude install hamster-applet hamster-indicator
aptitude install go2
aptitude install icedtea-plugin
aptitude install gparted grsync colordiff chromium-browser
aptitude install hal

# Graphics
echo "Graphics"
aptitude install gimp jhead imagemagick
aptitude install inkscape pstoedit pdf2svg
mkdir -p $HOME/src
hg clone https://bitbucket.org/pv/textext $HOME/src/textext
cp $HOME/src/textext/textext.py $HOME/.config/inkscape/extensions/
cp $HOME/src/textext/textext.inx $HOME/.confing/inkscape/extensions/
aptitude install libjpeg62-dev zlib1g-dev libfreetype6-dev liblcms1-dev
aptitude install libexiv2-dev libtool libgirepository1.0-dev m4
git clone git://git.yorba.org/gexiv2 $HOME/src/gexiv2
$HOME/src/gexiv2/configure --enable-introspection
make -C $HOME/src/gexiv2
make install -C $HOME/src/gexiv2

# Communication
echo "Communication"
aptitude install gwibber
aptitude install xchat

# Document Processing
echo "Document Processing"
aptitude install texlive texlive-bibtex-extra
aptitude install pandoc
pip install pybtex

# Reference Management
echo "Reference Management"
aptitude install jabref
wget http://download.zotero.org/standalone/4.0.9/Zotero-4.0.9_linux-x86_64.tar.bz2 -O $HOME/Downloads/Zotero-4.0.9_linux-x86_64.tar.bz2
tar -jxvf $HOME/Downloads/Zotero-4.0.9_linux-x86_64.tar.bz2
mkdir /opt/zotero
cp -r $HOME/Downloads/Zotero_linux-x86_64/ /opt/zotero

STRING=$( cat <<EOF
[Desktop Entry]
Name=Zotero
GenericName=Reference Manager
Comment=Open-source reference manager (standalone version)
Exec=/opt/zotero/zotero
Icon=/opt/zotero/chrome/icons/default/default48.png
Type=Application
StartupNotify=true
Categories=Office
EOF
)

touch $HOME/.local/share/applications/zotero.desktop
cat $HOME/.local/share/applications/zotero.desktop $STRING > $HOME/.local/share/applications/zotero.desktop

# Web development
echo "Web Development"
pip install fabric hyde requests slumber pyyaml simplejson
aptitude install virtualbox
wget http://files.vagrantup.com/packages/0ac2a87388419b989c3c0d0318cc97df3b0ed27d/vagrant_1.3.4_x86_64.deb -O $HOME/Downloads/vagrant_1.3.4_x86_64.deb
dpkg -i $HOME/Downloads/vagrant_1.3.4_x86_64.deb

# BLAS/LAPACK
echo "Installing BLAS and LAPACK"
aptitude install libblas3 libatlas3-base libopenblas-base liblapack3
aptitude install libblas-dev libatlas-dev libopenblas-dev liblapack-dev
update-alternatives --set libblas.so.3 /usr/lib/atlas-base/atlas/libblas.so.3
update-alternatives --set liblapack.so.3 /usr/lib/atlas-base/atlas/liblapack.so.3

# SciPy Stack
echo "Installing the SciPy Stack"
aptitude install libzmq-dev libzmq1
aptitude install python-tables mayavi2
pip install cython
pip install numpy scipy nose pandas theano
aptitude install libzmq-dev libzmq1
pip install ipython[notebook]
aptitude build-dep python-matplotlib
pip install matplotlib
python -c 'import numpy; numpy.test()'
python -c 'import scipy; scipy.test()'
python -c 'import matplotlib; matplotlib.test()'

# R
echo "Installing R"
aptitude install r-base

# Adobe Reader
echo "Install Adobe Reader"
add-apt-repository "deb http://archive.canonical.com/ raring partner"
aptitude update
aptitude install acroread

# Plone Dependencies
aptitude install libxml2-dev libxslt-dev build-essential libssl-dev
aptitude install libz-dev libjpeg-dev libreadline-dev libxml2-dev libxslt1-dev
aptitude install wv poppler-utils

# Video
aptitude install libav-tools
