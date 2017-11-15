#!/bin/bash
sudo sshfs root@185.122.201.240:/home/muslu/django/pythontc /home/muslu/pythontc/ -o allow_other -o nonempty -p 3522
sudo ssh root@185.122.201.240 -p 3522 -t "cd /home/muslu/django/pythontc; bash --login; clear"

#root:R2dxkf223
#muslu:R2dxkf223
#mysql:R2dxkf22









## Ubuntu 17.04 64bit Server
###################################################################################################################################
## Apache Son Sürüm
# add-apt-repository ppa:ondrej/apache2 -y; apt update; apt upgrade -y; apt install -f
###################################################################################################################################
# clear; apt autoremove -y; apt autoclean; apt update; apt upgrade -y; apt autoremove -y; apt autoclean; clear;
# clear; apt-get install -y software-properties-common python-software-properties python3.6 python3.6-dev libmysqlclient-dev apache2 apache2-utils libexpat1 ssl-cert libapache2-mod-wsgi-py3 mysql-client libmysqlclient-dev mysql-server perl libnet-ssleay-perl openssl libauthen-pam-perl libpam-runtime libio-pty-perl apt-show-versions python python-dev libjpeg-dev libfreetype6-dev zlib1g-dev unzip subversion; clear;
# a2enmod http2; apachectl restart; clear;
# clear; mkdir /home/muslu/django/; cd /home/muslu/django/; mkdir gerekli; cd gerekli; wget http://prdownloads.sourceforge.net/webadmin/webmin_1.860_all.deb; dpkg --install webmin_1.860_all.deb
# curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py; python3.6 get-pip.py
###################################################################################################################################
## MySQLDB
# https://pypi.python.org/pypi/mysqlclient
# wget mysqlclient-1.3.12.tar.gz; tar zxfv mysqlclient-1.3.12.tar.gz; cd mysqlclient-1.3.12/; python3.6 setup.py install


###################################################################################################################################
#ServerName pythontc.katoptrik.com
#DocumentRoot "/home/muslu/django/pythontc/"
#ServerAdmin musluyuksektepe@gmail.com

#Alias /media /home/muslu/django/pythontc/media/
####Alias /static/admin /usr/local/lib/python3.6/dist-packages/django/contrib/admin/static/admin/
#Alias /static /home/muslu/django/pythontc/static/
#Alias /favicon.ico /home/muslu/django/pythontc/static/favicon.ico


#Protocols h2 http/1.1

#ErrorLog "/home/muslu/django/pythontc/logs/error_log"

#WSGIScriptAlias / /home/muslu/django/pythontc/pythontc/wsgi.py
#WSGIDaemonProcess pythontc python-path=/usr/local/lib/python3.6/dist-packages/:/home/muslu/django/pythontc/
#WSGIProcessGroup pythontc
#WSGIApplicationGroup %{GLOBAL}


#<Directory /home/muslu/django/pythontc/pythontc/>
#<Files wsgi.py>
#Require all granted
#</Files>
#</Directory>

#<Directory /home/muslu/django/pythontc/>
 #Options FollowSymlinks
 #AllowOverride none
 #Require all granted
#</Directory>
#<Directory /home/muslu/django/pythontc/media/>
 #Options FollowSymlinks
 #AllowOverride none
 #Require all granted
#</Directory>

###################################################################################################################################




###################################################################################################################################
## Webmin && LetsEncrypt
# clear; apt autoremove -y; apt autoclean; apt update; apt upgrade -y; apt autoremove -y; apt autoclean; clear;
# clear; apt install -y python-letsencrypt-apache
# Webmin > Webmin Configuration > Module Config (sol üst çark) > Full path to Let’s Encrypt client command > /usr/bin/letsencrypt > Save
# Webmin > Webmin Configuration > Module Config (sol üst çark) > SSL Encryption (sağ üst tab) > Months between automatic renewal field > 2 > Request Certificate
###################################################################################################################################





###################################################################################################################################
# HTTP2 Apache
# nano /etc/apt/sources.list
# deb-src http://archive.ubuntu.com/ubuntu/ xenial main universe restricted multiverse
# deb-src http://security.ubuntu.com/ubuntu xenial-security main universe restricted multiverse
# deb-src http://archive.ubuntu.com/ubuntu/ xenial-updates main universe restricted multiverse


# clear; apt autoremove -y; apt autoclean; apt update; apt upgrade -y; apt autoremove -y; apt autoclean;
# clear; apt -y install curl devscripts build-essential fakeroot libnghttp2-dev

# mkdir ~/gerekli; cd ~/gerekli; mkdir apache; cd apache
# apt source apache2; apt build-dep apache2; cd apache2-2.4.18;
# fakeroot debian/rules binary; sudo cp debian/apache2-bin/usr/lib/apache2/modules/mod_http2.so /usr/lib/apache2/modules/

# nano /etc/apache2/mods-available/http2.load
#LoadModule http2_module /usr/lib/apache2/modules/mod_http2.so
#<IfModule http2_module>
#LogLevel http2:info
#</IfModule>
###################################################################################################################################

