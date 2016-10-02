# ended up not using dupeguru, using beets instead
#sudo add-apt-repository ppa:hsoft/ppa
#sudo aptitude update
#sudo aptitude install dupeguru-me # there are no wily builds
#sudo aptitude install python3-dev python3-pyqt5 pyqt5-dev-tools
#git clone dupeguru
#cd dupeguru
#python config.py --edition=me
#python build.py
#python run.py
sudo aptitude install beets
# http://unix.stackexchange.com/questions/76867/how-to-install-suggests-dependencies-of-a-package
sudo aptitude install '~Rsuggests:^beets$'
sudo aptitude install ubuntu-restricted-extras
kodi
