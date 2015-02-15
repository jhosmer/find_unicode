# find_unicode
A python script to find all characters with an ord() value greater then 126

Usage:

```sh
[ 15:30 me@yourbase ~/dev/scripts ]$ ./find_unicode.py -h
Usage: ./find_unicode.py [file, [file, ..]]
Displays line:character position of all non-ascii Unicode character(s) in a file

[ 15:49 pythonforios@MacBookPro ~/dev/scripts ]$ ./find_unicode.py daemon/trunk/daemon/daemon.py
             File              Line:Col char    (ord)
--------------------------------------------------------
daemon/trunk/daemon/daemon.py  008:0013  ©    '\xc2\xa9'
daemon/trunk/daemon/daemon.py  008:0020  –  '\xe2\x80\x93'
daemon/trunk/daemon/daemon.py  011:0022  ü    '\xc3\xbc'
daemon/trunk/daemon/daemon.py  035:0044  ‘  '\xe2\x80\x98'
daemon/trunk/daemon/daemon.py  035:0050  ’  '\xe2\x80\x99'
daemon/trunk/daemon/daemon.py  110:0073  “  '\xe2\x80\x9c'
daemon/trunk/daemon/daemon.py  111:0022  ”  '\xe2\x80\x9d'

[ 15:45 me@yourbase ~/dev/scripts ]$ ./find_unicode.py daemon/trunk/daemon/
              File                Line:Col char    (ord)
-----------------------------------------------------------
daemon/trunk/daemon/__init__.py   004:0011  ‘  '\xe2\x80\x98'
daemon/trunk/daemon/__init__.py   004:0027  ’  '\xe2\x80\x99'
daemon/trunk/daemon/__init__.py   006:0020  –  '\xe2\x80\x93'
daemon/trunk/daemon/__init__.py   017:0018  “  '\xe2\x80\x9c'
daemon/trunk/daemon/__init__.py   017:0052  ”  '\xe2\x80\x9d'
daemon/trunk/daemon/_metadata.py  004:0011  ‘  '\xe2\x80\x98'
daemon/trunk/daemon/_metadata.py  004:0027  ’  '\xe2\x80\x99'
daemon/trunk/daemon/_metadata.py  006:0013  ©    '\xc2\xa9'
daemon/trunk/daemon/daemon.py     035:0050  ’  '\xe2\x80\x99'
daemon/trunk/daemon/daemon.py     110:0073  “  '\xe2\x80\x9c'
daemon/trunk/daemon/daemon.py     111:0022  ”  '\xe2\x80\x9d'
...

[ 15:49 me@yourbase ~/dev/scripts ]$ cat daemon/trunk/daemon/__init__.py | ./find_unicode.py
stdin  004:0011  ‘  '\xe2\x80\x98'
stdin  004:0027  ’  '\xe2\x80\x99'
stdin  006:0020  –  '\xe2\x80\x93'
stdin  017:0018  “  '\xe2\x80\x9c'
stdin  017:0052  ”  '\xe2\x80\x9d'
...
```
