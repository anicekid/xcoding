#!/usr/bin/python3
#-*- coding:utf-8 -*-
import sys
from parse import parse
from mconfig import mconfig

def main():
    
    parser = parse.getargs()
    args = parser.parse_args()
    c = mconfig.config()
    if len(sys.argv) < 2:
        parser.print_usage()
    else: 
        if args.version:
            print(c.VERSION,end='')
if __name__ == '__main__':
    main()
