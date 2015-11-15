sudo apt-get install $(grep -vE "^\s*#" ubuntu-install-list.txt  | tr "\n" " ")
mkdir -p ~/src
if [ ! -d "~/src/dotfiles" ]; then
  git clone git@github.com:moorepants/dotfiles.git ~/src/dotfiles
fi
rm ~/.bashrc ~/.vimrc ~/.gitconfig
ln -s ~/src/dotfiles/bashrc ~/.bashrc
ln -s ~/src/dotfiles/vimrc ~/.vimrc
ln -s ~/src/dotfiles/gitconfig ~/.gitconfig
mkdir -p ~/.vim/after/ftplugin
rm ~/.vim/after/ftplugin/*
for plugin in cpp htmljinja html jinja matlab python rst r tex
do
  ln -s ~/src/dotfiles/$plugin.vim ~/.vim/after/ftplugin/$plugin.vim
done
if [ ! -d "~/.vim/bundle/vundle" ]; then
  git clone https://github.com/gmarik/vundle.git ~/.vim/bundle/vundle
fi
