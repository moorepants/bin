Create a user account on initial login.
Enable admin and set a password.
Enable ssh in the Terminal tab of the control panel.
ssh with root using the admin password. (admin won't be able to edit
/etc/passwd)
Edit /etc/passwd and for the user of interest and change sbin/nologin to bin/sh
Also in the synology panel turn on the user home service so that users get a
home directory
This will allow that user to ssh in.

Got this from here:
http://techanic.net/2014/04/12/configuring_ssh_and_scp_sftp_on_dsm_5.0_for_synology_diskstations.html
