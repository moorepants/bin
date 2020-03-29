Started with this question:

https://askubuntu.com/questions/1029249/how-to-encrypt-home-on-ubuntu-18-04

Which leads to this guide:

http://tlbdk.github.io/ubuntu/2018/10/22/fscrypt.html

First thing was to get the latest version of fscrypt installed (0.2.5) because
the permission bug has been fixed.

sudo apt install golang-go libpam0g-dev build-essential git libpam-fscrypt
fscrypt

go get -d github.com/google/fscrypt/...

cd ~/go/src/github.com/google/fscrypt
git checkout v0.2.5
make

Notes for the tlbdk guide:

export DEVICE=/nvme0p1 (this shoudl be the home partition)

After running pam-auth-update I had to reboot, not just logout/login. Also make
sure that all the things have * in the menu (use spacebar to add/remove the *).
Then make sure to hit Ok with <Alt>-O (I think).

sudo ~/go/src/github.com/google/fscrypt/bin/fscrypt setup /home

for the home partiion (don't need to to root partition)

After the test encryption of the directory you select 1 for using yoru login
password and that is the only time you have to do this for this user. Skip on
subsequent times.

Use <Alt>-F2 or something to get a TTY screen for the next stuff. sud su - puts
you in the root account. That all worked fine.

You can log into a test admin user the files in the encrypted directory shoudl
be all gobbly gooked named and you can open them!
