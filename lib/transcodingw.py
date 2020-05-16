import base64
from urllib import parse

"""
base64编码与解码
参数:
    somestring:你想要进行编码或者解码的字符串
"""
def base64encode(somestring):
    encodestring = str(base64.b64encode(somestring.encode("utf-8")), "utf-8")
    
    print("The result of the base64 encoding is:" + encodestring)
    return encodestring

def base64decode(somestring):
    decodestring = str(base64.b64decode(somestring),"utf-8")

    print("The result of the base64 decoding is:" + decodestring)
    return decodestring

"""
url编码与解码
参数:
    somestring:你想要进行编码或者解码的字符串
"""
def urlencode(somestring):
    encodestring = parse.quote(somestring)

    print("The result of the url encoding is:" + encodestring)
    return encodestring

def urldecode(somestring):
    decodestring = parse.unquote(somestring)

    print("The result of the url decoding is:" + decodestring)
    return decodestring

"""
字符与十六进制数互相转换
ascii hex

"""
def strtohex(s):
   
    hexencode = "0x" + ''.join([hex(ord(c)).replace('0x', '') for c in s])
    print("The result of the hex encode is:" +  hexencode)
    return hexencode

def hextostr(s):
    tmp = s.replace('0x','')
    tmp = tmp.replace('\\x','')
    tmp = tmp.replace(' ','')
    hexdecode = ""
    
    for x in range(0,int(len(tmp)),2):
        hexdecode += chr(int(tmp[x:x+2],16))
    
    print("The result of the hex decode is:" + hexdecode)
    return hexdecode

"""
字符与二进制数互相转换

"""

def strtobin(s):

    binencode = ''.join([bin(ord(c)).replace('0b', '') for c in s])
    print("The result of the bin encode is:" + binencode)
    return binencode

def bintostr(s):
    tmp = s.replace('0b','')
    tmp = tmp.replace(' ','')
    bindecode = ""

    for x in range(0,int(len(tmp)),7):
        bindecode += chr(int(tmp[x:x+7],2))

    print("The result of the bin decode is:" + bindecode)
    return bindecode

def strtobinspace(s):

    binencode = ' '.join([bin(ord(c)).replace('0b', '') for c in s])
    print("The result of the bin encode is:" + binencode)
    return binencode
