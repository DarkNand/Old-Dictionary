# Old-Dictionary
An old dictionary written in python with a GTK GUI, and a sqlite database.

# Supported Dictionaries
Currently, the program supports a version of gcide that I parsed from Json, and a version of an old webster dictionary from 1913 that I got off project gutenberg and parsed from a txt file.
The gcide version is kind of weird. The Json didn't contain all the fields that exists in the gcide xml where it originated. So I decided to assert a number for each definition. If a field is availiable (like Mus, or Zool) it will show also.
Maybe in the future I'll parse the xml files directly to the database, but I took a shortcut with the Json.

# Features
Multiple dictionaries. currently, two.
Gtk+ 3 interface and Dynamic tabs; you can have many tabs for many queries, or many tabs for the same query across dictionaries.
SQLite Database, which is both fast, and easy to modify.

The GUI depends on PyGObject. On debian, you can install it like this:
sudo apt-get install python-gobject

I made this software after I was disappointed in a gcide dictionary I got with my Debian distribution. It was simply too slow.
