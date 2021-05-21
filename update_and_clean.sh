#!/usr/bin/env bash

sudo apt update
sudo apt -y upgrade
sudo apt -y autoremove
sudo apt -y autoclean
sudo apt -y clean
# zoom
if [ -d "$HOME/src/zoom-mgr" ]
then
    cd $HOME/src/zoom-mgr
    git pull origin trunk  # update the repository
    $HOME/src/zoom-mgr/zoom-mgr.sh update  # update zoom
    cd -
fi
# conda
if [ -d "$HOME/miniconda" ]
then
    conda update --all
    conda clean --all
fi
