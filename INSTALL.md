* Set up your instance on AWS, Digital Ocean, or other preferred PaaS. Don't use Heroku, AppEngine, or
other services where you can't write to the file system.

* Install <a href="https://github.com/mapbox/mbutil">MBUtil</a> from MapBox

```
easy_install mbutil
```

* Install and start memcached

```
sudo apt-get install memcached
```

* Install <a href="http://webpy.org/">web.py</a>

```
sudo easy_install web.py
```

* Start Skycache server

```
python skycache.py &
```
