nandi (Dell Latitude 7300)
==========================

Dell Latitude 7300

https://en.wikipedia.org/wiki/Dell_Latitude

Using Ubuntu 20.04 LTS

The Ubuntu installer pauses and says the computer has Intel RST that may need
to be disabled and points to this online information:

https://discourse.ubuntu.com/t/ubuntu-installation-on-computers-with-intel-r-rst-enabled/15347

On startup press F12 for the boot menu and then select the BIOS utilitly. In
the BIOS settings System Configuration > SATA Operation select AHCI instead of
RAID On. "RAID On" is the Intel RST technology.

Also disable the UEFI secure boot mode in the Bios as this makes it harder to
get the DisplayLink drivers working on Ubuntu.

Once in BIOS settings look at Secure Boot>Secure Boot Enable

In the BIOS disable the touchscreen.

In Ubuntu install dialog Select to install optional software.

Setup the partitions manually. Erase everything that was there.

Create a 200 MB "EFI System Partition" as a primary partition first. (not sure
why i need this with secure boot disabled)
Then a 50 GB EXT 4 and mount at /
Then a 200 GB EXT4 and mount at /home
Then a swap area with the remaining ~6GB.

Terminal Bell
-------------

Turn off the terminal bell sound by going to Preferences in the terminal application and unchecking "Tereminal Bell". Read that here: https://vitux.com/how-to-mute-disable-hardware-beep-sound-in-ubuntu-terminal/

sudo apt update && sudo apt upgrade

Fn Keys
-------

Note that <Fn> + Esc lets you toggle whether the function keys are the default
or the special keys, e.g. brightness.

Docking Station
---------------

Looks like the Dell D6000 docking station requires some speical drivers that
are not installable via apt. Find them here: https://www.displaylink.com/downloads/ubuntu
I found this https://github.com/AdnanHodzic/displaylink-debian, but it looks
like DisplayLink provies a working driver for 20.04 now, but there was helpful
info on the secure boot issue.

unzip the download
chmod +x <filename>.run
disconnect the dock
sudo ./(filename>.run
reboot on prompt

It tried to reboot but it hung on the Bios startup screen (says TU DElft in this case).
Forced a shutdown with the poer button and started it back up.
It booted to Ubuntu this time.

After rebooting and connecting the dock, the monitors work. Note that they will
not work if the secure boot UEFI is enabled (found this out on first attempt to
install).

Encrypt /home/moorepants
------------------------

Encrypt the /home partition with fscrypt. I orginally followed this guide:

http://tlbdk.github.io/ubuntu/2018/10/22/fscrypt.html

but this one also has some help things:

https://wiki.archlinux.org/index.php/Fscrypt

::

   sudo apt install fscrypt libpam-fscrypt

   export DEVICE=/dev/nvme0n1p3

Check that these two commands return the same value::

   getconf PAGE_SIZE

   sudo tune2fs -l $DEVICE | grep 'Block size'

Set up device for encryption (I had to add sudo here, which is different that
the guide)::

   sudo tune2fs -O encrypt $DEVICE


Create the file ``/usr/share/pam-configs/keyinit-fix`` (need sudo rights) and
fill with the following::

   Name: keyinit fix
   Default: yes
   Priority: 0
   Session-Type: Additional
   Session:
      optional	pam_keyinit.so force revoke

Now::

   sudo pam-auth-update

Use the space bar to make a ``*`` next to each item in the list. I made them
all ``*``. And press "enter" to confirm.

::

   sudo reboot

General fscrypt setup::

   sudo fscrypt setup

Setup the ``/home`` directory for encryption::

   sudo fscrypt setup /home

Use <ctrl> + <fn> + <alt> + F3 to open a tty temrinal (note that the function
keys default to the special operations, e.g. volume, brightness, that is what
<fn> is included in this command). Once in tty swith to the root account::

   sudo su -

   export USERNAME=user1
   mv /home/$USERNAME /home/$USERNAME.bak
   mkdir /home/$USERNAME
   chown $USERNAME:$USERNAME /home/$USERNAME
   fscrypt encrypt /home/$USERNAME --user=$USERNAME

on the ``fscrypt encrypt`` line I got::

   fscrypt encrypt: filesystem /: not setup fo ruse with fscrypt

So I did this::

   fscrypt setup /
   fscrypt encrypt /home/$USERNAME --user=$USERNAME

And then ::

   rsync -avH /home/$USERNAME.bak/ /home/$USERNAME/
   rm -rf /home/$USERNAME.bak

::

   sudo reboot

Software
--------

Download https://github.com/moorepants/bin/archive/master.zip and follow
instructions.

Install nextcloud::

   sudo apt install nextcloud-desktop

Open nextcloud desktop and connect to https://nextcloud.moorepants.info.

Boot stalls (unfixed)
---------------------

The boot process stalls and it seems that there is not enough "entropy" to
complete the boot. If you CTRL+ALT+F2 it'll move to tty2, login, and then
CTRL+ALT+F1 to go back to tty1 and now there is enough entropy to boot to the
graphical interface. I also installed haveged, which supposedly helps create
enough entropy on boot and it seemed to fix things::

   sudo apt install haveged

Actually this `haveged` package doesn't seem to fix things. Maybe I needed to
enable and start it::

   sudo systemctl enable haveged
   sudo systemctl start haveged

Sound not working after reboot
------------------------------

I added a starup program with the command ``pulseaudio --start`` via the
startup applications gui and this corrects things. Still not sure why this is
needed.

garuda (Thinkpad X250)
======================

On startup press enter and the F1 to load bios config.

Config > USB:

 - USB 3.0 Mode set to Auto

If USB 3.0 is set to exclusively 3.0 it will fail to read my older USB sticks
with the Ubuntu image.

Config > Keyboard/Mouse

- F1-F12 as Primary Function: Enabled
- Fn and Ctrl Key swap: Enabled

Security > Secure Boot

- Secure Boot : Disabled

Startup > UEFI/Legacy Boot: Legacy Only

To install Ubuntu 15.10, restart with new bios settings, press enter on startup
and then F12 for the boot device selection. Select the USB stick with the
Ubuntu image. Then this will show up:

   Missing parameter in configuration file. Keyword: path gfxboot.c32: not a
   COM32R image

This is an Ubuntu bug. To get around it type "help" and press press enter. Then
press enter on next screen and it will boot to USB.

caramelmonkey (ASUS U31SG)
==========================

In the software-properties-gtk gui select the nvidia driver in the proprietary
drivers if you want the discrete graphics card to work.

enable the nvidia driver and restart

primeindcaotr lests you switch between graphics cards
sudo add-apt-repository ppa:nilarimogard/webupd8
sudo apt-get update
sudo apt-get install prime-indicator

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

ASUS EEEPc
==========

XMBC
----

sudo apt-get install python-software-properties pkg-config
sudo apt-get install software-properties-common
sudo add-apt-repository ppa:team-xbmc/ppa
sudo apt-get update
sudo apt-get install xbmc

Asus UL30A
==========

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

Make the git subtree command work (only needed in Ubuntu 13.04, not 13.10)::

   $ sudo chmod +x /usr/share/doc/git/contrib/subtree/git-subtree.sh
   $ sudo ln -s /usr/share/doc/git/contrib/subtree/git-subtree.sh /usr/lib/git-core/git-subtree

Wallpapers (note that this will show NSFW wallpapers without any config)::

   $ sudo add-apt-repository ppa:peterlevi/ppa
   $ sudo aptitude update
   $ sudo aptitude install variety

Sound switcher::

   sudo apt-add-repository ppa:yktooo/ppa
   sudo apt-get update
   sudo apt-get install indicator-sound-switcher

Ubuntu Settings
===============

In "System Settings>Appearance" set the dash icons to be smaller and pick a
nice background, enable hiding of dash, enable workspaces.

Package Management
==================

Set the server to the UCD server (if in Davis/Sacramento) using this gui::

   $ sudo software-properties-gtk

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

Generate a ssh key::

   $ ssh-keygen -t rsa -C "moorepants@gmail.com"

git-svn::

   $ sudo aptitude install git-svn

git-annex::

   $ sudo aptitude install git-annex openssh-server

Dot Files
=========

::
   $ git clone git@github.com:moorepants/dotfiles.git ~/src/dotfiles

Make symlinks to dot files::

   $ ln -s ~/src/dotfiles/bashrc ~/.bashrc
   $ ln -s ~/src/dotfiles/vimrc ~/.vimrc
   $ ln -s ~/src/dotfiles/gitconfig ~/.gitconfig
   $ ln -s ~/src/dotfiles/html.vim ~/.vim/after/ftplugin/html.vim
   $ ln -s ~/src/dotfiles/matlab.vim ~/.vim/after/ftplugin/python.vim
   $ ln -s ~/src/dotfiles/tex.vim ~/.vim/after/ftplugin/tex.vim
   $ ln -s ~/src/dotfiles/matlab.vim ~/.vim/after/ftplugin/matlab.vim
   $ ln -s ~/src/dotfiles/rst.vim ~/.vim/after/ftplugin/rst.vim
   $ ln -s ~/src/dotfiles/cpp.vim ~/.vim/after/ftplugin/cpp.vim

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

Run BundleInstall in vim.

Software Development
====================

::

   $ sudo aptitude install build-essential gfortran python-dev cmake cmake-curses-gui doxygen valgrind swig clang

Switching between gcc and clang for C++::

   $ sudo update-alternatives --config c++

shellcheck::

   sudo aptitude install shellcheck

General
=======

Install Dropbox::

   $ sudo aptitude install dropbox

Install KeePassX::

  $ sudo aptitude install keepassx

Install Hamster::

  $ sudo aptitude install hamster-applet hamster-indicator

Add the hamster indicator to startup applications (found in dash)::

   name= "Hamster Indicator"
   command= "hamster-indicator"

Link to the hamster database::

   ln -s ~/Dropbox/hamster.db ~/.local/share/hamster-applet/hamster.db`
   ln -s ~/Nextcloud/hamster.db ~/.local/share/hamster-applet/hamster.db`

Install rememberthemilk Firefox addon (or just sync firefox):

http://www.rememberthemilk.com/services/gmail/addon/

Go2::

   $ sudo aptitude install go2

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

Allows interaction with Mac HFS+ filesystem (format option in gparted)::

   $ sudo apt-get install hfsprogs

Installing hal is supposed to let me watch Flash videos with DRM, but I can't
get a purchased Youtube movie to work::

   $ sudo aptitude install hal

Wine::

   $ sudo add-apt-repository ppa:ubuntu-wine/ppa
   $ sudo apitude update
   $ sudo aptitude install wine

CPU load and cpu frequency selection::

   $ sudo apt-get install indicator-multiload
   $ sudo apt-get install indicator-cpufreq

See here for more stuff:
http://www.webupd8.org/2013/10/8-things-to-do-after-installing-ubuntu.html

PDF editing::

   $ sudo aptitude install pdftk

Battery life

Pre 15.10::

   sudo add-apt-repository ppa:linrunner/tlp
   sudo aptitude update
   sudo aptitude install tlp tlp-rdw

Post 15.10 (extra packages are for thinkpads)::

   sudo aptitude install tlp tlp-rdw tp-smapi-dkms acpi-call-dkms

Start it::

   sudo tlp start

Count Lines of Code (cloc)::

   $ sudo aptitude install cloc

linkchecker::

   $ sudo aptitud install linkchecker

Flash for Chromium::

   $ sudo aptitude install pepperflashplugin-nonfree

Samba cifs-utils allows mounting shares from the command line::

   $ sudo aptitude install cifs-utils

Bluetooth::

   $ sudo aptitude install bluez-tools

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

Gexiv2::

   $ sudo aptitude install libexiv2-dev libtool libgirepository1.0-dev m4
   $ git clone git://git.yorba.org/gexiv2 ~/src/gexiv2
   $ cd gexiv2
   $ ./configure --enable-introspection
   $ make
   $ sudo make install

After that you can use it in virtualenvs:

http://stackoverflow.com/questions/17472124/how-to-install-gexiv2-on-a-virtualenv

IPE vector drawing editor::

   $ sudo aptitude install ipe

Communication
=============

Install the google talk plugin in Firefox http://www.google.com/intl/en/chat/voice/

Document Processing
===================

Get a LaTeX distribution and biblatex::

   $ sudo aptitude install texlive texlive-bibtex-extra biber texlive-xetex texlive-fonts-extra texlive-science texlive-humanities

Sympy's uses xelatex to build it's docs.

Pandoc::

   $ sudo aptitude install pandoc

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

If you want to be able to have autoupdates from in the software and install to
/opt/ with sudo then you must make the directory writeble by the users that
want to do the update.

sudo chown moorepants:moorepants /opt/zotero
or
sudo chmod o+w /opt/zotero

Web Development
===============

MathJax

git clone git://github.com/mathjax/MathJax.git ~/src/MathJax

deck.js

git clone git@github.com:imakewebthings/deck.js.git ~/src/deck.js

Virutalbox::

   $ sudo aptitude install virtualbox

Vagrant 1.4.3::

   $ sudo aptitude install vagrant

I had this error when using vagrant and it needed to download a box::

   moorepants@moorepants-2170p:plonedev.vagrant((4.3.3))$ curl https://cloud-images.ubuntu.com/vagrant/trusty/current/trusty-server-cloudimg-i386-vagrant-disk1.box
   curl: (77) error setting certificate verify locations:
     CAfile: /etc/pki/tls/certs/ca-bundle.crt
     CApath: none

I found a solution here: https://github.com/mitchellh/vagrant/issues/3227 ::

   echo insecure >> ~/.curlrc

Docker::

   $ sudo aptitude install docker.io

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

SymPy development (building docs) requires::

   $ sudo aptitude install librsvg2-bin

Install miniconda

wget https://repo.continuum.io/miniconda/Miniconda-latest-Linux-x86_64.sh
bash Miniconda-latest-Linux-x86_64.sh -b
export PATH=$HOME/miniconda/bin:$PATH
# Adds the path prepend to bashrc
echo "PATH=$HOME/miniconda/bin:$PATH" >> $HOME/.bashrc
# Install all the Python dependencies
conda install -y python=2.7 pip numpy scipy cython matplotlib pandas pytables ipython-notebook mpmath fastcache

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

Octave
======

sudo apt-add-repository ppa:octave/stable
sudo apt-get update
sudo aptitude install octave liboctave-dev

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

IPOPT
=====

This didn't really seem to work::

   sudo aptitude install coinor-libipopt1 coinor-libipopt-dev coinor-libipopt-doc

So I did it from source (after removing the above):

svn co https://projects.coin-or.org/svn/Ipopt/stable/3.11 CoinIpopt

$ cd CoinIpopt/ThirdParty/Blas
$ ./get.Blas
$ cd ../Lapack
$ ./get.Lapack
$ cd ../ASL
$ ./get.ASL

That gets the slower reference BLAS, but you could use your own but need this
complilation flag: --with-blas="-L$HOME/lib -lmyblas"

Get the HSL code (not required because Mumps can be used) (this can be link
after compiling ipopt too)

cd ../Mumps
./get.Mumps
cd ../Metis
./get.Metis

cd ~/src/CoinIpopt
mkdir build
cd CoinIpopt/build
../configure # maybe want to --prefix /usr/local, alsocan tell it where blas is and stuff here

for pardiso
mkdir ThirdParty/Pardiso
cp <.so file> ThirdParty/Pardiso
--with-pardiso="-qsmp=omp $HOME/lib/libpardiso_P4AIX51_64_P.so"

openmp support for hsl_ma86 and hsl_ma97: ADD_CFLAGS=-fopenmp ADD_FFLAGS=-fopenmp ADD_CXXFLAGS=-fopenmp
make -j5
make test
sudo make install

Set paridiso ENV var

export OMP_NUM_THREADS=4

cyipopt
=======

This is needed if IPopt is not installed system wide.
export PKG_CONFIG_PATH=$PKG_CONFIG_PATH:~/src/CoinIpopt/lib/pkgconfig
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:~/src/CoinIpopt/lib
edit setup.py
python setup.py install

Plone
=====

Plone dependencies::

   $ sudo aptitude install libxml2-dev libxslt-dev build-essential libssl-dev libz-dev libjpeg-dev libreadline-dev libxml2-dev libxslt1-dev wv poppler-utils

libz-dev (probably changing to zlib1g-dev)

csympy
======

apt-get install libgmp-dev

git clone
cmake -DWITH_PYTHON=yes -DPYTHON_LIBRARY=/usr/bin/python .
make

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

Get libav for video editing.::

   $ sudo aptitude install libav-tools # for avconv

youtube-dl::

   $ sudo aptitude install youtube-dl

OpenShot::

   $ sudo aptitude install openshot openshot-doc

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

I should probably remove /usr/local/SimTK since I installed with the lastest
version that actually knows about preferred install paths in Linux.

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

Second time installing::

   conda create -n opensim numpy scipy ipython matplotlib
   sudo aptitude install cmake-gui g++-4.8 doxygen git openjdk-7-jdk python-dev swig
   mkdir ~/src/opensim
   cd ~/src/opensim
   git clone git@github.com:opensim-org/opensim-core.git
   cd opensim-core
   mkdir build
   cd build
   cmake \
      -DCMAKE_INSTALL_PREFIX=~/opt/opensim \
      -DCMAKE_BUILD_TYPE=Release \
      -DBUILD_EXAMPLES=On \
      -DBUILD_TESTING=On \
      -DBUILD_JAVA_WRAPPING=Off \
      -DBUILD_PYTHON_WRAPPING=On \
      -DPYTHON_EXECUTABLE=/home/moorepants/anaconda/envs/opensim/bin \
      -DPYTHON_INCLUDE_DIR=/home/moorepants/anaconda/envs/opensim/include/python2.7 \
      -DPYTHON_LIBRARY=/home/moorepants/anaconda/envs/opensim/lib/libpython2.7.so \
      -DSIMBODY_HOME=/usr/local \
   ..

   make doxygen
   make -j5
   ctest -j5
   sudo make -j5 install

   export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/opt/opensim/lib
   export PATH=/opt/opensim/bin:$PATH

Need to make the Opensim headers available.
