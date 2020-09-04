nandi
=====

Dell Latitude 7300

Using Ubuntu 20.04 LTS

The Ubuntu installer pauses and says the computer has Intel RST that may need
to be disabled and points to this online information:

https://discourse.ubuntu.com/t/ubuntu-installation-on-computers-with-intel-r-rst-enabled/15347

On startup press F12 for the boot menu and then select the BIOS utilitly. In
the BIOS settings System Configuration > SATA Operation select AHCI instead of
RAID On. "RAID On" is the Intel RST technology.

Also disable the UEFI secure boot mode in the Bios as this makes it harder to
get the DisplayLink drivers working on Ubuntu.

Once in BIOS settings looke at Secure Boot>Secure Boot Enable

Select to install optional software.

Setup the partitions manually. Erase everything that was there.

Create a 200 MB "EFI System Partition" as a primary partition first. (not sure
why i need this with secure boot disabled)
Then a 50 GB EXT 4 and mount at /
Then a 200 GB EXT4 and mount at /home
Then a swap area with the remaining ~6GB.

sudo apt update && sudo apt upgrade

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

Encrypt the /home partition with fscrypt.
