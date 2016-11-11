The microphone volume control in the task bar still doesn't work.

The "Recent" files in nautilus doesn't work:
https://bugzilla.gnome.org/show_bug.cgi?id=773300

Adding "Environment=DISPLAY=:0" in the service file:
/usr/lib/systemd/user/gvfs-daemon.service, solves it.

Just put it at the end of the file and restart ubuntu.

I can't connect via VGA or display port to the projector in my classroom.

The connect to network in nautilus doesn't work: fix is:
http://askubuntu.com/questions/50197/cannot-connect-to-samba-share-from-nautilus
