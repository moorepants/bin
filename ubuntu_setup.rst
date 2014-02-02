LiveUSB on Asus UL30A
=====================

Download the Ubuntu 13.04 ISO::

  $ wget <url>

Use gparted to format a flash drive, at least 2Gb I think (don't use the
"disks" program it seems to be broken for formatting). Install netbootin and
use it to make a bootable usb (startup disk creator seems to be broken too)::

   $ sudo aptitude install unetbootin

Restart the Asus UL30A with the drive in place and press F2 to open the BIOS
interface. Set the primary harddrive in the boot menu to the flash disk instead
of the onboard disk so that the computer boots to the USB drive.

Install Ubuntu and set 60 gb for the primary root partition, 445 gb for the
home directory, and the remainder ~5gb for swap (I have 4 gb of ram).

Ubuntu Settings
===============

In "System Settings>Appearance" set the dash icons to be smaller and pick a
nice background, enable hiding of dash, enable workspaces.

Package Management
==================

Get aptitude::

   $ sudo apt-get install aptitude

And then upgrade and update::

   $ sudo aptitude update
   $ sudo aptitude upgrade

Version Control
===============

Get the main players::

   $ sudo aptitude install git gitk subversion mercurial bzr subversion

Configure Git::

   $ git config --global user.email "moorepants@gmail.com"
   $ git config --global user.name "Jason K. Moore"

Make the git subtree command work (only needed in Ubuntu 13.04, not 13.10)::

   $ sudo chmod +x /usr/share/doc/git/contrib/subtree/git-subtree.sh
   $ sudo ln -s /usr/share/doc/git/contrib/subtree/git-subtree.sh /usr/lib/git-core/git-subtree

Generate a ssh key::

   $ ssh-keygen -t rsa -C "moorepants@gmail.com"

Hub::

   $ git clone git@github.com:github/hub.git ~/src/hub
   $ cd ~/src/hub
   $ sudo rake1.9.1 install

git-svn::

   $ sudo aptitude install git-svn

Dot Files
=========

::
   $ git clone git@github.com:moorepants/dotfiles.git ~/src/dotfiles

Make symlinks to dot files::

   $ ln -s ~/src/dotfiles/bashrc ~/.bashrc
   $ ln -s ~/src/dotfiles/vimrc ~/.vimrc
   $ ln -s ~/src/dotfiles/html.vim ~/.vim/after/ftplugin/html.vim
   $ ln -s ~/src/dotfiles/matlab.vim ~/.vim/after/ftplugin/python.vim
   $ ln -s ~/src/dotfiles/tex.vim ~/.vim/after/ftplugin/tex.vim
   $ ln -s ~/src/dotfiles/matlab.vim ~/.vim/after/ftplugin/matlab.vim
   $ ln -s ~/src/dotfiles/rst.vim ~/.vim/after/ftplugin/rst.vim

Vim
===

If you install vim-gtk from the gvim package, the +clipboard stuff is compiled
(see `this comment`_)::

   $ sudo aptitude install vim-gtk exuberant-ctags

.. _this comment: http://askubuntu.com/questions/256782/how-to-copy-paste-contents-in-vi-editor

Make vim the default Git editor::

   $ git config --global core.editor "vim"

Vundle::

   $ git clone https://github.com/gmarik/vundle.git ~/.vim/bundle/vundle

Software Development
====================

::

   $ sudo aptitude install build-essential gfortran python-dev cmake cmake-curses-gui doxygen valgrind swig

Install pip::

   $ sudo aptitude install pip

Virtualenv::

   $ sudo pip install virtualenv virtualenvwrapper
   $ mkdir ~/envs

Add this to bashrc::

   # virtualenvwrapper
   export WORKON_HOME=$HOME/envs
   source /usr/local/bin/virtualenvwrapper.sh

Numpydoc for Sphinx::

   $ sudo pip install numpydoc

Coverage::

   $ sudo pip install coverage

check-manifest::

   $ pip install check-manifest

General
=======

Download latest dropbox https://www.dropbox.com/install?os=lnx::

$ wget https://www.dropbox.com/download?dl=packages/debian/dropbox_1.6.0_amd64.deb -O ~/Downloads/dropbox_1.6.0_amd64.deb
$ dpkg -i ~/Downloads/dropbox_1.6.0_amd64.deb

Install KeePassX::

  $ sudo aptitude install keepassx

Install Hamster::

  $ sudo aptitude install hamster-applet hamster-indicator

Add the hamster indicator to startup applications (found in dash)::

   name= "Hamster Indicator"
   command= "hamster-indicator"

Link to the hmaster database::

   ln -s ~/Dropbox/hamster.db ~/.local/share/hamster-applet/hamster.db`

Install rememberthemilk

http://www.rememberthemilk.com/services/gmail/addon/

Go2::

   $ sudo aptitude install go2

Add to ~/.bashrc::

   # go2
   [ -e /usr/lib/go2/go2.sh ] && source /usr/lib/go2/go2.sh
   alias cd='go2 --cd' # caches all directorys you change to with cd

Hibernate is not on by default. To see if hibernate works::

   $ sudo pm-hibernate

If it does then edit this file::

   $ sudo vim /etc/polkit-1/localauthority/50-local.d/com.ubuntu.enable-hibernate.pkla

by adding this::

   [Re-enable hibernate by default]
   Identity=unix-user:*
   Action=org.freedesktop.upower.hibernate
   ResultActive=yes

Now in System Setting you have the option to hibernate for various things. I
hibernate when power is critically low.

Install icedtea to use openjdk in firefox::

   $ sudo aptitude install icedtea-plugin

Random::

   $ sudo aptitude install gparted grsync colordiff chromium-browser

Installing hal is supposed to let me watch Flash videos with DRM, but I can't
get a purchased Youtube movie to work::

   $ sudo aptitude install hal

Wine::

   $ sudo aptitude install wine

Applets

CPU load and cpu frequency selection::

   $ sudo apt-get install indicator-multiload
   $ sudo apt-get install indicator-cpufreq

See here for more stuff:
http://www.webupd8.org/2013/10/8-things-to-do-after-installing-ubuntu.html

Wallpapers:

   $ sudo add-apt-repository ppa:peterlevi/ppa
   $ sudo aptitude update
   $ sudo aptitude install variety

   $ sudo aptitude install pdftk

Battery life::

   sudo add-apt-repository ppa:linrunner/tlp
   sudo apt-get update
   sudo apt-get install tlp tlp-rdw
   sudo tlp start

Graphics
========

::

   $ sudo aptitude install gimp jhead imagemagick shutter

Get Inkscape and some helper programs for LaTeX::

   $ sudo aptitude install inkscape pstoedit pdf2svg

Get the textext_ extension too::

   $ hg clone https://bitbucket.org/pv/textext ~/src/textext/
   $ cp ~/src/textext/textext.py ~/.config/inkscape/extensions/
   $ cp ~/src/textext/textex.inx ~/.confing/inkscape/extensions/

.. _textext: http://pav.iki.fi/software/textext/

Need these for building PIL::

   $ sudo aptitude install libjpeg62-dev zlib1g-dev libfreetype6-dev liblcms1-dev

Gexiv2::

   $ sudo aptitude install libexiv2-dev libtool libgirepository1.0-dev m4
   $ git clone git://git.yorba.org/gexiv2 ~/src/gexiv2
   $ cd gexiv2
   $ ./configure --enable-introspection
   $ make
   $ sudo make install

After that you can use it in virtualenvs:

http://stackoverflow.com/questions/17472124/how-to-install-gexiv2-on-a-virtualenv

ffmpeg::

   $ sudo aptitude install ffmpeg

Communication
=============

Install gwibber (it is now technically friends app and gwibber will be going
away)::

   $ sudo aptitude install gwibber

XChat::

   $ sudo aptitude install xchat

Add these favorite channels to xchat::

#ipython,#plone,#pydy,#scipy,#matplotlib,#sympy

Startup app for xchat:

http://www.erickjohncuevas.com/how-tos/xchat-how-to-auto-connect-and-minimize-on-startup/

install the google talk plugin http://www.google.com/intl/en/chat/voice/

Document Processing
===================

Get a LaTeX distribution and biblatex::

   $ sudo aptitude install texlive texlive-bibtex-extra biber

Pandoc::

   $ sudo aptitude install pandoc

Pybtex::

   $ sudo pip install pybtex

Reference Management
====================

JabRef::

  $ sudo aptitude install jabref

Install Zotero::

   wget http://download.zotero.org/standalone/4.0.17/Zotero-4.0.17_linux-x86_64.tar.bz2
   tar -jxvf Zotero-4.0.17_linux-x86_64.tar.bz2
   sudo cp -r Zotero_linux-x86_64/ /opt/zotero

   vim ~/.local/share/applications/zotero.desktop

   [Desktop Entry]
   Name=Zotero
   GenericName=Reference Manager
   Comment=Open-source reference manager (standalone version)
   Exec=/opt/zotero/zotero
   Icon=/opt/zotero/chrome/icons/default/default48.png
   Type=Application
   StartupNotify=true
   Categories=Office

Also install the firefox extension and link it to the standalone.

Add .bashrc alias::

   alias zotero=/opt/zotero/zotero

Web Development
===============

::

   $ sudo pip install fabric hyde

MathJax

git clone git://github.com/mathjax/MathJax.git ~/src/MathJax

deck.js

git clone git@github.com:imakewebthings/deck.js.git ~/src/deck.js

Virutalbox::

   $ sudo aptitude install virtualbox

Vagrant. Go to http://downloads.vagrantup.com to download the latest x86_64 deb file and
then click on it::

   $ wget http://files.vagrantup.com/packages/0ac2a87388419b989c3c0d0318cc97df3b0ed27d/vagrant_1.3.4_x86_64.deb -O ~/Downloads/vagrant_1.3.4_x86_64.deb
   $ dpkg -i ~/Downloads/vagrant_1.3.4_x86_64.deb

::
   $ sudo pip install requests slumber pyyaml simplejson

Node::

sudo aptitude install nodejs npm phantomjs
sudo npm install -g phantom-jasmine
ln -s /usr/bin/nodejs /usr/bin/node
# https://github.com/joyent/node/issues/3911
sudo aptitude remove nodejs npm
sudo add-apt-repository ppa:chris-lea/node.js
sudo apt-get update
sudo aptitude install nodejs npm

BLAS/LAPACK
===========

This gets BLAS, ATLAS, OpenBLAS, and LAPACK. The first three being different
implementations of libblas.so.3. ATLAS also provides a second optimized
implementation of LAPACK::

   $ sudo aptitude install libblas3 libatlas3-base libopenblas-base liblapack3

Select the Atlas versions for both (see note below, because the openblas
implementation may be better)::

   $ sudo update-alternatives --config libblas.so.3
   $ sudo update-alternatives --config liblapack.so.3

By default NumPy builds with and uses the ATLAS implementation of BLAS. You
must edit site.cfg to choose other implementations.

http://stackoverflow.com/questions/11443302/compiling-numpy-with-openblas-integration

SciPy Stack
===========

IPython dependencies::

   $ sudo aptitude install libzmq-dev libzmq1

Install these from the package manager::

   $ sudo aptitude install python-tables mayavi2

Install from source::

   $ sudo pip install cython # theano and pandas use to build
   $ sudo pip install numpy scipy nose pandas theano sympy

SymPy development (building docs) requires::

   $ sudo aptitude install librsvg2-bin

IPython needs the ZMQ libs::

   $ sudo aptitude install libzmq-dev libzmq1
   $ sudo pip install ipython[notebook]

Matplotlib has dependencies and should be installed after NumPy because it is
not fully pip compatible::

   $ sudo aptitude build-dep python-matplotlib
   $ sudo pip install matplotlib

Run the tests of all the packages::

   $ python -c 'import numpy; numpy.test()'
   $ python -c 'import matplotlib; matplotlib.test()'
   $ python -c 'import scipy; scipy.test()'

TODO: Add tests for all packages.

I got this error though:

ERROR: Failure: ImportError (/usr/local/lib/python2.7/dist-packages/scipy/lib/lapack/clapack.so: undefined symbol: clapack_sgesv)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/usr/local/lib/python2.7/dist-packages/nose/loader.py", line 413, in loadTestsFromName
    addr.filename, addr.module)
  File "/usr/local/lib/python2.7/dist-packages/nose/importer.py", line 47, in importFromPath
    return self.importFromDir(dir_path, fqname)
  File "/usr/local/lib/python2.7/dist-packages/nose/importer.py", line 94, in importFromDir
    mod = load_module(part_fqname, fh, filename, desc)
  File "/usr/local/lib/python2.7/dist-packages/scipy/lib/lapack/__init__.py", line 162, in <module>
    from . import clapack
ImportError: /usr/local/lib/python2.7/dist-packages/scipy/lib/lapack/clapack.so: undefined symbol: clapack_sgesv

So I found this: http://danielnouri.org/notes/2012/12/19/libblas-and-liblapack-issues-and-speed,-with-scipy-and-ubuntu/

$ sudo update-alternatives --config libblas.so.3
There are 2 choices for the alternative libblas.so.3 (providing /usr/lib/libblas.so.3).

  Selection    Path                                    Priority   Status
------------------------------------------------------------
* 0            /usr/lib/atlas-base/atlas/libblas.so.3   35        auto mode
  1            /usr/lib/atlas-base/atlas/libblas.so.3   35        manual mode
  2            /usr/lib/libblas/libblas.so.3            10        manual mode

Press enter to keep the current choice[*], or type selection number: 1

$ sudo update-alternatives --config liblapack.so.3
There are 2 choices for the alternative liblapack.so.3 (providing /usr/lib/liblapack.so.3).

  Selection    Path                                      Priority   Status
------------------------------------------------------------
* 0            /usr/lib/lapack/liblapack.so.3             10        auto mode
  1            /usr/lib/atlas-base/atlas/liblapack.so.3   5         manual mode
  2            /usr/lib/lapack/liblapack.so.3             10        manual mode

Press enter to keep the current choice[*], or type selection number: 2

I still got the error so I changed to:

$ sudo update-alternatives --config liblapack.so.3
There are 2 choices for the alternative liblapack.so.3 (providing /usr/lib/liblapack.so.3).

  Selection    Path                                      Priority   Status
------------------------------------------------------------
  0            /usr/lib/lapack/liblapack.so.3             10        auto mode
  1            /usr/lib/atlas-base/atlas/liblapack.so.3   5         manual mode
* 2            /usr/lib/lapack/liblapack.so.3             10        manual mode

Press enter to keep the current choice[*], or type selection number: 1

The tests passed at this point.

Slycot
======

numpy, blas/lapack, gfortran are required

git clone git@github.com:avventi/Slycot.git
cd Slycot
sudo python setup.py install

python-control
==============

git svn -s http://svn.code.sf.net/p/python-control/code python-control
cd python-control
sudo python setup.py install

Matlab
======

Read the included pdf and this https://help.ubuntu.com/community/MATLAB

sudo /media/moorepants/MATHWORKS_R2007B/install -debug

Install matlab from a mounted iso or disk

sudo ./install

I thought the installation thingy would let you set up symlinks, but it didn't
do it for me even though I selected custom install. So I added this::

   $ ln -s /usr/local/MATLAB/R2013a/bin/matlab ~/bin/matlab

Put this in bashrc because I rarely use the gui::

   alias matlab='matlab -nodesktop -nosplash'

Anaconda
--------

$ wget http://09c8d0b2229f813c1b93-c95ac804525aac4b6dba79b00b39d1d3.r79.cf1.rackcdn.com/Anaconda-1.8.0-Linux-x86_64.sh
$ sudo bash Anaconda-1.8.0-Linux-x86_64.sh

Choose the install directory to be ``/opt/anaconda``.

Do not add the path statement to .bashrc.

chrpath is required to build some packages:

$ sudo aptitude install chrpath

Octave
======

sudo apt-add-repository ppa:octave/stable
sudo apt-get update

sudo aptitude install octave liboctave-dev

sudo pip install oct2py

To install from source, first get the dependencies::

   sudo apt-get install \
   autoconf \
   automake \
   bison \
   doxygen \
   epstool \
   flex \
   freeglut3 \
   freeglut3-dev \
   gcc \
   g++ \
   gfortran \
   glpk \
   gnuplot \
   gperf \
   graphviz \
   mercurial \
   libarpack2 \
   libarpack2-dev \
   libblas3gf \
   libblas-dev \
   libcurl4-openssl-dev \
   libfftw3-3 \
   libfftw3-dev \
   libfltk1.3 \
   libfltk1.3-dev \
   libfontconfig1 \
   libfontconfig1-dev \
   libfreetype6 \
   libfreetype6-dev \
   libgl2ps-dev \
   libgraphicsmagick++1-dev \
   libhdf5-serial-dev \
   liblapack-dev \
   liblapack3gf \
   libpcre3 \
   libpcre3-dev \
   libqhull5 \
   libqhull-dev \
   libqscintilla2-dev \
   libqt4-dev \
   libqrupdate1 \
   libqrupdate-dev \
   libreadline6 \
   libreadline6-dev \
   libsuitesparse-dev \
   libtool \
   llvm \
   openjdk-7-jdk \
   openjdk-7-jre \
   pkg-config \
   transfig \
   zlibc \
   zlib1g \
   zlib1g-dev \

   hg clone http://hg.savannah.gnu.org/hgweb/octave/

   cd octave
   ./bootstrap
   mkdir build
   cd build
   ../configure
   make

Biomechanics Tool Kit
=====================

Dependencies are: swig python-numpy octave liboctave-dev doxygen libvtk5-dev

sudo aptitude install libvtk5-dev libphonon4 libqtscript4-phonon libphonon-dev phonon-backend-gstreamer libvtk5.8-qt4

You need libphonon-dev for
/usr/lib/x86_64-linux-gnu/qt4/plugins/designer/libphononwidgets.so

See http://packages.ubuntu.com/saucy/amd64/libphonon-dev/filelist

I'm not sure the other phonon packages are needed.

I had to specifiy the moc, uic, and python paths exactly to prevent errors in
cmake finding them.

git clone git@github.com:Biomechanical-ToolKit/BTKCore.git ~/src/BTKCore
git clone git@github.com:Biomechanical-ToolKit/BTKData.git ~/Data/BTKData
cd ~/src/BTKCore
mkdir build
cd build
cmake \
   -DCMAKE_BUILD_TYPE:CHAR=Release \
   -DBUILD_SHARED_LIBS:BOOL=1 \
   -DBTK_WRAP_PYTHON:BOOL=1 \
   -DBTK_WRAP_OCTAVE:BOOL=1 \
   -DBUILD_TESTING:BOOL=1 \
   -DBTK_TESTING_DATA_PATH:CHAR=~/Data/BTKData \
   -DBTK_EXTRA_COMPILER_WARNINGS:BOOL=1 \
   -DBUILD_DOCUMENTATION:BOOL=1 \
   -DBUILD_DOCUMENTATION_API:BOOL=1 \
   -DBUILD_DOCUMENTATION_API_UNSELECTED_MODULES:BOOL=1 \
   -DBUILD_EXAMPLES:BOOL=1 \
   -DPYTHON_LIBRARY:CHAR=/usr/lib/x86_64-linux-gnu/libpython2.7.so \
   -DPYTHON_INCLUDE_DIR:CHAR=/usr/include/python2.7 \
   -DBTK_USE_VISSUPPORT:BOOL=1 \
   -DBTK_USE_VTK:BOOL=1 \
   -DBUILD_TOOLS:BOOL=1 \
   -DQT_MOC_EXECUTABLE:PATH=/usr/bin/moc \
   -DQT_UIC_EXECUTABLE:PATH=/usr/bin/uic \
   -G "Unix Makefiles" ..
make # or make -j4
sudo make install

There are also these:

But cmake didn't automatically detect VTK on my first try. Will need to
revisit.

this may require the LD_LIBRARY_PATH environment variable to be set to use it

Plone
=====

Plone dependencies::

   $ sudo aptitude install libxml2-dev libxslt-dev build-essential libssl-dev libz-dev libjpeg-dev libreadline-dev libxml2-dev libxslt1-dev wv poppler-utils

libz-dev (probably changing to zlib1g-dev)

csympy
======

apt-get install libgmp-dev

Lua
===

sudo aptitude install lua5.2

numlua
sudo aptitude install luarocks

sudo aptitude install libblas-dev liblapack-dev libfftw3-dev libhdf5-serial-dev

git clone git@github.com:carvalho/numlua.git
sudo luarocks make numlua-0.3-1.rockspec
follow instructions here: https://github.com/carvalho/numlua

This ended up installing numlua to lua5.1 (/usr/local/share/lua/5.1) instead of
the default lua.

So if I run

$ lua5.1
> require "numlua.rng"

that seems to work, but then i get errors trying to call rng.rnorm()

or

> require "numlua.matrix"
/usr/local/share/lua/5.1/numlua/matrix.lua:9: attempt to index global 'matrix'
(a nil value)
stack traceback:
   /usr/local/share/lua/5.1/numlua/matrix.lua:9: in main chunk
      [C]: in function 'require'
         stdin:1: in main chunk
            [C]: ?

So it seems the build failed or something.

R
==

::

   $ sudo aptitude install r-base

Adobe Reader
============

::

   $ sudo add-apt-repository "deb http://archive.canonical.com/ raring partner"
   $ sudo aptitude update
   $ sudo aptitude install acroread

Video
=====

Get libav for video editing.

::
   $ sudo aptitude install libav-tools # for avconv

SimpleScreenRecorder::

   $ sudo add-apt-repository ppa:maarten-baert/simplescreenrecorder
   $ sudo apt-get update
   $ sudo apt-get install simplescreenrecorder

Simbody
=======

Here is some step by step instructions for installing on Ubuntu 12.04. I'm not
sure which version of the software is was:

http://simtk-confluence.stanford.edu:8080/pages/viewpage.action?pageId=5114489

These requirements are already installed in the software dev and blas/lapack
sections::

   $ sudo aptitude install build-essential cmake cmake-curses-gui

This will get all the headers for the BLAS/LAPACK versions that are available::

   $ sudo aptitude install libblas-dev libatlas-dev libopenblas-dev liblapack-dev

Visualizer requires::

   $ sudo aptitude install freeglut3-dev libxmu-dev libxi-dev

::
   $ mkdir ~/src/simbody
   $ cd ~/src/simbody
   $ git clone git@github.com:simbody/simbody.git
   $ mkdir build
   $ mkdir build_d
   $ cd build
   $ ccmake ../simbody

Set CMAKE_INSTALL_PREFIX to /usr/local/SimTK
In ccmake type 'c' for configure, 't' to toggle to advanced mode, edit any
values, 'c' again for configure, and 'g' for generate.

::

   $ cd ../build_d
   $ ccmake ../simbody

In ccmake change `CMAKE_BUILD_TYPE` to `Debug`.

::
   $ make -j2 # -j2 specifies the number of cores you have
   $ make test
   $ ./ExamplePendulum # should show visualization
   $ make doxygen

The following puts everything in /usr/local, but it should have went into
/usr/local/SimTK. See https://github.com/simbody/simbody/issues/47 for more
info.

::

   $ sudo make install
   $ cd ../build
   $ make -j2
   $ make test
   $ sudo make install

Now try out using the libraries from an arbitrary directory. First, copy the
raw C++ files for the examples to a new directory to play with::

   $ cp -r ~/src/simbody/simbody/Simbody/examples ~/src/simbody-examples
   $ cd ~/src/simbody-examples
   $ export LD_LIBRARY_PATH=/usr/local/lib/
   $ export SIMBODY_HOME=/usr/local

Comment out this line in the Makefile because I'm on a 64 bit system::

   M32FLAG = -m32

I also changed this line to::

   SimTK_HOME=/usr/local

to reflect where my libs were actually installed. Now try running the example::

   $ make ExamplePendulum
   $ ./ExamplePendulum

The gui should pop up. You can build all examples with::

   $ make all

I've read that having to set the LD_LIBRARY_PATH should only be used for
testing. You shouldn't have to do this for standard installs. So I think the
Simbody devs should fix this. Also the compiled examples can't find the
/usr/local/bin directory unless I set SIMBODY_HOME. Otherwise it looks in
/usr/local/SimTK/bin which doesn't exist. When I originally ran ccmake it
didn't give me an option to set the installation directory and the default
seems to have been /usr/local instead of /usr/local/SimTK.

I need to uninstall and go into the advanced toggle in ccmake and set
`CMAKE_INSTALL_PREFIX` to `/usr/local/SimTK` and then reinstall.

OpenSim
=======

::

   mkdir ~/src/opensim
   cd ~/src/opensim
   $ svn checkout https://simtk.org/svn/opensim/Trunk
   $ mkdir build
   $ cd build
   $ ccmake ../Trunk

Type 'c' and add::

   SimTK_INSTALL_DIR=/usr/local/SimTK

   CMAKE_INSTALL_PREFIX=/usr/local/OpenSim

   Enable python wrapping. The default is to build it with Python3.3 so you
   have to manually set it for Python 2.7 (haven't done this yet).

Type 'c' and then 'g'.

::

   $ make test

These tests failed on the trunk::

   32/51 Test #32: testOptimizationExampleRuns ..................***Timeout 1500.03 sec
         Start 33: testOptimizationExample
   33/51 Test #33: testOptimizationExample ......................***Failed    0.28 sec

Install anyway::

   $ sudo make install
   $ cd /usr/local/OpenSim/sdk/python
   $ sudo python setup.py install

   $ cd ~
   $ export LD_LIBRARY_PATH=/usr/local/SimTK/lib:/usr/local/OpenSim/lib
   $ python3
   >>> import opensim

Old
===

Setup Conky

https://help.ubuntu.com/community/SettingUpConky
http://www.noobslab.com/2012/06/install-infinity-conky-in-ubuntulinux.html
sudo apt-get install conky curl lm-sensors hddtemp
sudo add-apt-repository ppa:noobslab/noobslab-conky
sudo apt-get update
sudo apt-get install infinity-conky

# I'm removing infinity-conky it doesn't really seem to work well. It often has
a grey back ground and if it doesn't it doesn't allow my icons on my desktop to
show through.

Logout and log back in then, open conky setup menu from the dash.

XMBC
====

sudo apt-get install python-software-properties pkg-config
sudo apt-get install software-properties-common
sudo add-apt-repository ppa:team-xbmc/ppa
sudo apt-get update
sudo apt-get install xbmc

HP 2170p
========

These are specific instructions for the HP Elitebook 2170p I use at work. The
brightness controls (f9, f10, and system settings) did not work by default.

To fix the brightness controls you must edit (sudo) the ``/etc/default/grub``
file and add this argument to ``GRUB_CMDLINE_LINUX``::

   GRUB_CMDLINE_LINUX="acpi_backlight=vendor"

Then run::

   $ sudo update-grub && shutdown -r now

The the f9 and f10 keys work for changing brightness.
