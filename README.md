# Python.tc Sitesi Çalışmaları



<p align="center"><img src="http://mkds.la/img/logo2x.png"></p>


**Linux için termianlde kısa yollar**
```sh
nano ~/.bash_aliases
```
```sh
alias kur='sudo apt-get install -y'
alias guncelle='sudo apt-get update && sudo apt-get upgrade -y'
alias sil='sudo apt-get purge -y'
alias dj_="python3 manage.py"
alias dj_m="python3 manage.py migrate"
alias dj_mm="python3 manage.py makemigrations"
alias dj_mmm="python3 manage.py makemigrations && python3 manage.py migrate"
alias dj_mmr="python3 manage.py makemigrations && python3 manage.py migrate && python3 manage.py runserver 0.0.0.0:8000"
alias dj_shell="python3 manage.py shell"
alias dj_run="python3 manage.py runserver 0.0.0.0:8000"
alias dj_app="python3 manage.py startapp"
alias dj_cs="python3 manage.py collectstatic"
alias dj_su="python3 manage.py createsuperuser"
alias tc='cd /home/muslu/django/pythontc/'
alias ev='cd /home/muslu/'
alias python3='/usr/bin/python3.6'
alias python='/usr/bin/python3.6'
```
```
source ~/.bash_aliases
```




1. Ubuntu 17.04
2. Python3.6
3. Pip3.6
```sh
certifi==2017.11.5
chardet==3.0.4
command-not-found==0.3
distro-info===0.14build1
Django==1.11.7
django-grappelli==2.10.1
idna==2.6
language-selector==0.1
mysqlclient==1.3.12
olefile==0.44
Pillow==4.3.0
pyasn1==0.3.7
pygobject==3.22.0
python-apt==1.4.0b2
python-debian==0.1.31
pytz==2017.3
PyYAML==3.12
requests==2.18.4
six==1.11.0
ssh-import-id==5.6
systemd-python==233
ufw==0.35
unattended-upgrades==0.1
urllib3==1.22
```
4. Apache
```sh
 core_module (static)
 so_module (static)
 watchdog_module (static)
 http_module (static)
 log_config_module (static)
 logio_module (static)
 version_module (static)
 unixd_module (static)
 access_compat_module (shared)
 alias_module (shared)
 auth_basic_module (shared)
 authn_core_module (shared)
 authn_file_module (shared)
 authz_core_module (shared)
 authz_host_module (shared)
 authz_user_module (shared)
 autoindex_module (shared)
 deflate_module (shared)
 dir_module (shared)
 env_module (shared)
 filter_module (shared)
 http2_module (shared)
 mime_module (shared)
 mpm_event_module (shared)
 negotiation_module (shared)
 reqtimeout_module (shared)
 setenvif_module (shared)
 status_module (shared)
 wsgi_module (shared)
```

