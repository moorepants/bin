#!/usr/bin/env bash

sudo apt update
sudo apt -y upgrade
sudo apt -y autoremove
sudo apt -y autoclean
sudo apt -y clean
# zoom
# install deb-get with instructions here https://github.com/wimpysworld/deb-get
if [ -d "/opt/zoom" ]
then
  deb-get update
  deb-get upgrade
else
  deb-get install zoom
fi
# conda
if [ -d "$HOME/miniconda" ]
then
    conda update --all
    conda clean --all
fi
