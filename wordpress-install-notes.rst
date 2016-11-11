https://help.ubuntu.com/community/WordPress

sudo aptitude install wordpress mysql-server

set mysql root password

sudo ln -s /usr/share/wordpress /var/www/html/wordpress

sudo gzip -d /usr/share/doc/wordpress/examples/setup-mysql.gz
sudo bash /usr/share/doc/wordpress/examples/setup-mysql -n icsc2017wp localhost

libapache2-mod-php

sudo a2enmod php

sudo vim /etc/php/7.0/apache2/php.ini

upload_max_filesize = 200M

sudo chmod -R 0755 /usr/share/wordpress/
sudo chown -R www-data /usr/share/wordpress
sudo chown -R www-data /var/lib/wordpress/
sudo chmod -R 0755 /var/lib/wordpress

sudo aptitude install phpmyadmin

sudo vim /etc/apache2/apache2.conf
Include /etc/phpmyadmin/apache.conf
Alias /wp-content /var/lib/wordpress/wp-content

The above didn't work well because there are all these symlnks going from
/usr/hsare/wordpress to /var/lib/wordpress and /var/www/worpress. A big mess

So, do this instead:

https://www.digitalocean.com/community/tutorials/how-to-install-wordpress-with-lamp-on-ubuntu-16-04
sudo apt-get install php-curl php-gd php-mbstring php-mcrypt php-xml php-xmlrpc

make sure to chown www-data:www-data (not user name like int the tutorial so
that plugins installation works)

http://stackoverflow.com/questions/17922644/wordpress-asking-for-my-ftp-credentials-to-install-plugins
define('FS_METHOD', 'direct');
