# Skycache

Inspired by some issues that people have had with scaling non-profit and personal mapping projects.

* TransitFuture
* TransitMixApp
* NYC Taxi Map

Upload an MBTiles and (future todo) choose an OSM layer.

Skycache caches the tiles that your site uses most. Yes, it's simple, but this is for suddenly-viral
projects. When you need it, you won't have the time to write it yourself.

## Issues with real map providers

Google, MapBox, CartoDB, and other map providers get expensive once you have large datasets.

It's against Terms of Service to move providers' tiles from their servers into your cache.

Google and MapBox have a customizeable and fast-updating baselayer, but they can't be cached and cost money.

Extracting and posting all of your tiles to S3 on your own is kinda slow, technical, and you probably didn't
do it yet. If you need a fast solution to get your tiles into the cloud, why not use this?

## Issues with Skycache

A prototype of Skycache helped power TransitFuture, but this needs a rewrite.

Skycache is not a full mapping service. You're just going to upload an MBTiles and get a tile URL back.

The baselayer will come in only a few flavors, and updates to OSM will be slow to appear.

I don't know what Skycache costs or how it'll scale. It might be better for you to run your own Skycache server.

The idea is to store the MBTiles on the server until it's actually requested, and then it'll be cached in a faster form. Your
first walkthrough will be slow. But for many high-traffic projects, people are looking at the same areas, which
will load quickly. For global map tiles, like the OSM layers, unexplored areas like Timbuktu will stay in an
MBTiles file until someone is using them. It's more efficient that way.

## Install Instructions

<a href="https://github.com/mapmeld/skycache/blob/master/INSTALL.md">Install How-To</a>
