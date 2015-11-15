sudo apt-get install git
git config --global user.email "moorepants@gmail.com"
git config --global user.name "Jason K. Moore"
git config --global core.editor "vim"
if [ ! -f "~/.ssh/id_rsa.pub" ]; then
  ssh-keygen -t rsa -C "moorepants@gmail.com"
fi
cat ~/.ssh/id_rsa.pub
echo "Please provide the above public ssh key to Github and press any key when done."
read -n 1 -s
git clone git@github.com:moorepants/bin.git ~/bin
sudo apt-get install $(grep -vE "^\s*#" ~/bin/ubuntu-install-list.txt  | tr "\n" " ")
mkdir -p ~/src
if [ ! -d "~/src/dotfiles" ]; then
  git clone git@github.com:moorepants/dotfiles.git ~/src/dotfiles
fi
for config in .bashrc .vimrc .gitconfig
do
  if [ ! -f "~/$config" ]; then
    rm ~/$config
  ln -s ~/src/dotfiles/$config ~/$config
  fi
done
mkdir -p ~/.vim/after/ftplugin
rm ~/.vim/after/ftplugin/*
for plugin in cpp htmljinja html jinja matlab python rst r tex
do
  ln -s ~/src/dotfiles/$plugin.vim ~/.vim/after/ftplugin/$plugin.vim
done
if [ ! -d "~/.vim/bundle/vundle" ]; then
  git clone git@github.com:gmarik/vundle.git ~/.vim/bundle/vundle
fi
hg clone https://bitbucket.org/pv/textext ~/src/textext/
cp ~/src/textext/textext.py ~/.config/inkscape/extensions/
cp ~/src/textext/textex.inx ~/.confing/inkscape/extensions/
git clone git@github.com:mathjax/MathJax.git ~/src/MathJax
git clone git@github.com:imakewebthings/deck.js.git ~/src/deck.js
cd ~/Downloads
wget https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh
cd -
bash ~/Downloads/Miniconda3-latest-Linux-x86_64.sh -b
source ~/.bashrc
conda install -y $(grep -vE "^\s*#" ~/bin/conda-install-list.txt  | tr "\n" " ")
