#!/usr/bin/python3
import base64
import os
import sys
import zipfile
from string import ascii_letters,printable
from random import choice,choices,shuffle

def segmenter(string,minlen=75,maxlen=100):
    '''iterates through given string and segments the string into randomized size
    between "minlen" and "maxlen". Giving it a key to associate to it for later.
    returns a dictinary of key(random_str):value(segmented string)'''
    dic={}
    while len(string) > 0:
        key_len   = choice(range(7,15))
        value_len = choice(range(minlen,maxlen))
        segment   = string[:value_len]
        string    = string.replace(segment,'',1)
        key       = ''.join(choices(ascii_letters,k=key_len))
        while key in dic:
            key=''.join(choices(ascii_letters,k=key_len))
        key = key+'.{}'.format(choice(['txt','dat','val','key']))
        dic[key]=segment
    return dic
    
payload_file=sys.argv[0]

with open(payload_file,'rb') as f:
    original_payload = f.read()

firstbase = base64.b64encode(original_payload).decode('utf-8')
obf_dic = {}
payload_dic   = segmenter(firstbase)

#random data to further obuscate
salt_string = ''.join(choices(printable,k=len(firstbase)//2))
salt_dic    = segmenter(salt_string)

#merges real and salted data
obf_dic.update(salt_dic)
obf_dic.update(payload_dic)
scrabled_list=list(obf_dic.keys())
shuffle(scrabled_list)

if 'datafolder' not in os.listdir():
    os.mkdir('datafolder')

with zipfile.ZipFile('temp.zip','w') as zipobj:
    for k,v in obf_dic.items():
        datfile= 'datafolder/'+k
        with open(datfile,'w') as f:
            f.write(v)
        zipobj.write(datfile)


with open('keylegend.txt','w') as f:
    for key in payload_dic.keys():
        f.write(f'{key}\n')
