#!/usr/bin/python3
#-*- coding:utf-8 -*-
import argparse
import sys
import platform

if platform.system() == "Windows":
    from lib import transcodingw as transcoding
else:
    from lib import transcoding

def getargs():    
    parser = argparse.ArgumentParser(description='This is an encoding converter. Suport:base64、url、hex、bin') #获取解析器对象,description为使用-h参数时输出的描述信息
    parser.add_argument('-b64e', '--base64encode', dest='b64e', type=transcoding.base64encode, help='encode your string by base64', action='store')
    parser.add_argument('-b64d', '--base64decode', dest='b64d', type=transcoding.base64decode, help='decode your string by base64', action='store')
    parser.add_argument('-ue', '--urlencode', dest='ue', type=transcoding.urlencode, help='urlencode')
    parser.add_argument('-ud', '--urldncode', dest='ud', type=transcoding.urldecode, help='urldecode')
    parser.add_argument('-hs', '--hextostr', dest='hs', type=transcoding.hextostr, help='convert the hex numbers to a string')
    parser.add_argument('-sh', '--strtohex', dest='sh', type=transcoding.strtohex, help='convert the string to hex numbers')
    parser.add_argument('-bs', '--bintostr', dest='bs', type=transcoding.bintostr, help='convert the binary numbers  to a string')
    parser.add_argument('-sb', '--strtobin', dest='sb', type=transcoding.strtobin, help='convert the string to binary numbers')
    parser.add_argument('-sbc', '--strtobinspace', dest='sbc', type=transcoding.strtobinspace, help='convert the string to binary numbers and separate each character with a space')
    parser.add_argument('--version', action='store_true', help='xcoding version')
    return parser

