# Old-Dictionary
An old public domain english dictionary with a GTK GUI, and a sqlite database

It is based on the works taken from here:
http://www.gutenberg.org/ebooks/29765
The license from the text file was stripped, which should put the contents back into the public domain (If I understand the gutenberg license correctly. If I made a mistake, please contact me).
Then I wrote a simple script that looped throughout the text file and inserted the data into a sqlite database.
Finally, I wrote a CLI script and a GUI to interface with the database.
The GUI depends on PyGObject. On debian, you can install it like this:
sudo apt-get install python-gobject

You can also use the CLI script, which doesn't require any external dependencies.
This is my first attempt at writing a database-centric application.
