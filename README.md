# find_unicode
A python script to find all characters with an ord() value greater then 126

Usage:

```sh
[ 15:30 me@yourbase ~/dev/scripts ]$ ./find_unicode.py -h
Usage: ./find_unicode.py [file, [file, ..]]
Displays line:character position of all non-ascii Unicode character(s) in a file

[ 15:45 me@yourbase ~/dev/scripts ]$ ./find_unicode.py daemon/trunk/daemon/
              File                Line:Col char    (ord)
-----------------------------------------------------------
daemon/trunk/daemon/__init__.py   004:0011  ‘  '\xe2\x80\x98'
daemon/trunk/daemon/__init__.py   004:0027  ’  '\xe2\x80\x99'
daemon/trunk/daemon/__init__.py   006:0013  ©    '\xc2\xa9'
daemon/trunk/daemon/__init__.py   006:0020  –  '\xe2\x80\x93'
daemon/trunk/daemon/__init__.py   017:0018  “  '\xe2\x80\x9c'
daemon/trunk/daemon/__init__.py   017:0052  ”  '\xe2\x80\x9d'
daemon/trunk/daemon/_metadata.py  004:0011  ‘  '\xe2\x80\x98'
daemon/trunk/daemon/_metadata.py  004:0027  ’  '\xe2\x80\x99'
daemon/trunk/daemon/_metadata.py  006:0013  ©    '\xc2\xa9'
daemon/trunk/daemon/daemon.py     004:0011  ‘  '\xe2\x80\x98'
daemon/trunk/daemon/daemon.py     004:0027  ’  '\xe2\x80\x99'
daemon/trunk/daemon/daemon.py     006:0013  ©    '\xc2\xa9'
daemon/trunk/daemon/daemon.py     006:0020  –  '\xe2\x80\x93'
daemon/trunk/daemon/pidfile.py    004:0011  ‘  '\xe2\x80\x98'
daemon/trunk/daemon/pidfile.py    004:0027  ’  '\xe2\x80\x99'
daemon/trunk/daemon/pidfile.py    006:0013  ©    '\xc2\xa9'
daemon/trunk/daemon/runner.py     004:0011  ‘  '\xe2\x80\x98'
daemon/trunk/daemon/runner.py     004:0027  ’  '\xe2\x80\x99'
daemon/trunk/daemon/runner.py     006:0013  ©    '\xc2\xa9'
...
```
