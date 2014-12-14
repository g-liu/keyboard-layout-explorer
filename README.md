Keyboard layout explorer
========================

For some reason, my keyboard likes to switch from QWERTY to Dvorak layout spontaneously, often while I'm changing windows. Usually, I don't notice this change until I start typing and see a meaningless string of characters spew forth.

But there must be [some combination of keystrokes](http://g-liu.com/blog/2014/11/exploring-common-words-between-qwerty-and-dvorak/) that produce valid English words for both layouts...

Purpose and usage
-----------------
This small little script is meant to explore words common to both keyboard layouts. Just pass it in your dictionary file like so:

        py explore.py dict.txt

it will read each line of the dictionary one by one, and look for corresponding words when typed in Dvorak.

Additionally, you can print the matches to a file by redirecting to `stdout`:

        py explore.py dict.txt > matches.txt

Where to get dictionaries
-------------------------

I have included the Scrabble dictionary as a starter. You may find a plethora of other dictionary text files online just by searching. There is also one [available on Unix systems](http://stackoverflow.com/a/4456463/1387572): just type `cat /usr/share/dict/words > words.txt` and `words.txt` will contain your dictionary.

TODO
====

* Formal unit tests
