#!/usr/bin/env bash

sudo apt update
sudo apt -y upgrade
sudo apt -y autoremove
sudo apt -y autoclean
sudo apt -y clean
# TODO : The deb-get commands continue to run in the background after the conda
# commands start. Figure out how to prevent this.
# zoom
# install deb-get with instructions here https://github.com/wimpysworld/deb-get
if [ -d "/opt/zoom" ]
then
  deb-get update
  deb-get upgrade
else
  deb-get install zoom
fi
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
