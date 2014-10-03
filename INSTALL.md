* Set up your instance on AWS, Digital Ocean, or other preferred PaaS. Don't use Heroku, AppEngine, or
other services where you can't write to the file system.

* Install <a href="https://github.com/mapbox/mbutil">MBUtil</a> from MapBox

```
easy_install mbutil
```

* Install <a href="http://webpy.org/">web.py</a>

```
sudo easy_install web.py
```

* Get SkyCache

```
git clone https://github.com/mapmeld/skycache.git
cd skycache
```

* Start SkyCache server and peace out

```
nohup python skycache.py 80 &
disown
exit
```
