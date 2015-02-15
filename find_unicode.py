#!/usr/bin/python
# find_unicode.py
#
# Author: Jonathan Hosmer
# Date: Sun Feb 15 14:06:15 2015
#

import os
import sys

def help():
    print 'Usage: {} [file, [file, ..]]'.format(__file__)
    print 'Displays line:character position of all non-ascii Unicode character(s) in a file'

def main():
    args = sys.argv[1:]
    if '-h' in args or '--help' in args:
        sys.exit(help())
    if not args:
        files = [sys.stdin]
        long_fname = len('stdin') + 1
    else:
        # make a flat list of all files
        ## if a dir is given as an arg then take all files in that dir [non-recursive]
        files = [f for f in args if os.path.isfile(f)] + [x for y in
                 [[f for f in os.listdir(d) if os.path.isfile(f)]
                  for d in args if os.path.isdir(d)]
                 for x in y]
        long_fname = max(map(len, files)) + 1
    chars = []
    out_str = '{{:<{}}} {{:03}}:{{:04}} {{chars:^5}} {{chars!r:^13}}'.format(long_fname)
    if sys.stdin not in files:
        header = '{{:^{}}} {{}}:{{}} {{:^5}} {{:^10}}'.format(long_fname)
        head_out = header.format('File', 'Line', 'Col', 'char', '(ord)')
        print head_out + '\n' + '-'*len(head_out)
    for f in files:
        if f is sys.stdin:
            infile = sys.stdin
            fname  = 'stdin'
        else:
            fname  = f
            infile = open(f)
        for line_i, line in enumerate(infile):
            for char_i, char in enumerate(line):
                if ord(char) > 126:
                    chars.append(char)
                else:
                    if chars:
                        print out_str.format(fname, line_i+1, char_i+1-len(chars),
                                             chars=''.join(chars))
                        chars = []


if __name__ == '__main__':
    sys.exit(main())
