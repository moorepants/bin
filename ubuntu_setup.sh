#!/usr/bin/env bash

# Get aptitude -q=2 -y and update/upgrade
echo "Aptitude and update"
apt-get -y install aptitude
aptitude -q=2 -y update
aptitude -q=2 -y upgrade

# Version Control
echo "Version Control"
aptitude -q=2 -y install git gitk subversion mercurial bzr subversion
git config --global user.email "moorepants@gmail.com"
git config --global user.name "Jason K. Moore"
chmod +x /usr/share/doc/git/contrib/subtree/git-subtree.sh
ln -s /usr/share/doc/git/contrib/subtree/git-subtree.sh /usr/lib/git-core/git-subtree

TITLE=$( hostname )
if [[ $TITLE == vagrant* ]]; then
	PASSPHRASE=$( cat /vagrant/passphrase.txt )
else
	PASSPHRASE=$( cat passphrase.txt )
fi
ssh-keygen -t rsa -C "moorepants@gmail.com" -N $PASSPHRASE -f $HOME/.ssh/id_rsa
KEY=$( cat $HOME/.ssh/id_rsa.pub )
JSON=$( printf '{"title": "%s", "key": "%s"}' "$TITLE" "$KEY" )
if [[ $TITLE == vagrant* ]]; then
	TOKEN=$( cat /vagrant/github_token.txt )
else
	TOKEN=$( cat github_token.txt )
fi
aptitude -q=2 -y install curl
curl -s -d "$JSON" "https://api.github.com/user/keys?access_token=$TOKEN"

# Scripts
echo "Scripts"
git clone git@github.com:moorepants/bin.git $HOME/bin

# Dot Files
echo "Dot Files"
git clone git@github.com:moorepants/dotfiles.git $HOME/src/dotfiles
if [ ! -f $HOME/.bashrc ]; then
	rm $HOME/.bashrc
fi
ln -s $HOME/src/dotfiles/bashrc $HOME/.bashrc
if [ ! -f $HOME/.vimrc ]; then
	rm $HOME/.vimrc
fi
ln -s $HOME/src/dotfiles/vimrc $HOME/.vimrc
mkdir -p $HOME/.vim/after/ftplugin
ln -s $HOME/src/dotfiles/html.vim $HOME/.vim/after/ftplugin/html.vim
ln -s $HOME/src/dotfiles/matlab.vim $HOME/.vim/after/ftplugin/python.vim
ln -s $HOME/src/dotfiles/tex.vim $HOME/.vim/after/ftplugin/tex.vim
ln -s $HOME/src/dotfiles/matlab.vim $HOME/.vim/after/ftplugin/matlab.vim
ln -s $HOME/src/dotfiles/rst.vim $HOME/.vim/after/ftplugin/rst.vim

# Software Development
echo "Software Development"
aptitude -q=2 -y install build-essential gfortran python-dev cmake cmake-curses-gui
aptitude -q=2 -y install python-pip
pip install -U pip # upgrade pip
pip install virtualenv virtualenvwrapper
mkdir $HOME/envs

# General
echo "General"
wget https://www.dropbox.com/download?dl=packages/debian/dropbox_1.6.0_amd64.deb -O $HOME/Downloads/dropbox_1.6.0_amd64.deb
dpkg -i $HOME/Downloads/dropbox_1.6.0_amd64.deb
aptitude -q=2 -y install keepassx
aptitude -q=2 -y install hamster-applet hamster-indicator
aptitude -q=2 -y install go2
aptitude -q=2 -y install icedtea-plugin
aptitude -q=2 -y install gparted grsync colordiff chromium-browser
aptitude -q=2 -y install hal

# Graphics
echo "Graphics"
aptitude -q=2 -y install gimp jhead imagemagick
aptitude -q=2 -y install inkscape pstoedit pdf2svg
hg clone https://bitbucket.org/pv/textext $HOME/src/textext
cp $HOME/src/textext/textext.py $HOME/.config/inkscape/extensions/
cp $HOME/src/textext/textext.inx $HOME/.confing/inkscape/extensions/
aptitude -q=2 -y install libjpeg62-dev zlib1g-dev libfreetype6-dev liblcms1-dev
aptitude -q=2 -y install libexiv2-dev libtool libgirepository1.0-dev m4
git clone git://git.yorba.org/gexiv2 $HOME/src/gexiv2
$HOME/src/gexiv2/configure --enable-introspection
make -C $HOME/src/gexiv2
make install -C $HOME/src/gexiv2

# Communication
echo "Communication"
aptitude -q=2 -y install gwibber
aptitude -q=2 -y install xchat

# Document Processing
echo "Document Processing"
aptitude -q=2 -y install texlive texlive-bibtex-extra
aptitude -q=2 -y install pandoc
pip install pybtex

# Reference Management
echo "Reference Management"
aptitude -q=2 -y install jabref
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
aptitude -q=2 -y install virtualbox
wget http://files.vagrantup.com/packages/0ac2a87388419b989c3c0d0318cc97df3b0ed27d/vagrant_1.3.4_x86_64.deb -O $HOME/Downloads/vagrant_1.3.4_x86_64.deb
dpkg -i $HOME/Downloads/vagrant_1.3.4_x86_64.deb

# BLAS/LAPACK
echo "Installing BLAS and LAPACK"
aptitude -q=2 -y install libblas3 libatlas3-base libopenblas-base liblapack3
update-alternatives --set libblas.so.3 /usr/lib/atlas-base/atlas/libblas.so.3
update-alternatives --set liblapack.so.3 /usr/lib/atlas-base/atlas/liblapack.so.3

# SciPy Stack
echo "Installing the SciPy Stack"
aptitude -q=2 -y install libzmq-dev libzmq1
aptitude -q=2 -y install python-tables mayavi2
pip install cython
pip install numpy scipy nose pandas theano
aptitude -q=2 -y install libzmq-dev libzmq1
pip install ipython[notebook]
aptitude -q=2 -y build-dep python-matplotlib
pip install matplotlib

# R
echo "Installing R"
aptitude -q=2 -y install r-base

# Adobe Reader
echo "Install Adobe Reader"
add-apt-repository "deb http://archive.canonical.com/ raring partner"
aptitude -q=2 -y update
aptitude -q=2 -y install acroread
