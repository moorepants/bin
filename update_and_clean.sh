#!/usr/bin/env bash

# apt
sudo apt update
sudo apt -y upgrade
sudo apt -y autoremove
sudo apt -y autoclean
sudo apt -y clean

# snap
sudo snap refresh
sudo bash $HOME/bin/remove_old_snaps.sh

# conda
if [[ -d "$HOME/miniconda" || -d "$HOME/miniconda3" || -d "$HOME/miniforge" || -d "$HOME/miniforge3" ]];
then
    echo "Found conda installation"
    conda update --all
    conda clean --all
fi

# deb-get for zoom
# NOTE : The deb-get commands continue to run in the background, so keep it as
# the last command.
# install deb-get with instructions here https://github.com/wimpysworld/deb-get
if [ -d "/opt/zoom" ]
then
  deb-get update
  deb-get upgrade
else
  deb-get install zoom
fi
