#!/usr/bin/env bash

sudo apt update
sudo apt -y upgrade
sudo apt -y autoremove
sudo apt -y autoclean
sudo apt -y clean
conda update --all
conda clean --all
