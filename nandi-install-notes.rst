=====
nandi
=====

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

Select to install optional software.

Setup the partitions manually. Erase everything that was there.

Create a 200 MB "EFI System Partition" as a primary partition first. (not sure
why i need this with secure boot disabled)
Then a 50 GB EXT 4 and mount at /
Then a 200 GB EXT4 and mount at /home
Then a swap area with the remaining ~6GB.

sudo apt update && sudo apt upgrade

Docking Station
===============

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
========================

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
========

Install nextcloud::

   sudo apt install nextcloud-desktop

Open nextcloud desktop and connect to https://nextcloud.moorepants.info.


