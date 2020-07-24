#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import socket

with open('/usr/share/seclists/Usernames/Names/names.txt') as f:
    names=[x.strip('\n')for x in f.readlines()]

my_s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

for x in range(1,254):
    connect = my_s.connect(('10.11.1.'+str(x),25))
# Receive the banner
    banner = s.recv(1024)
    print(banner)
# VRFY a user
    for x in names:
        s.send('VRFY ' +x+ '\r\n')
        result = s.recv(1024)
        print(result)
# Close the socket
        s.close()


# In[ ]:




