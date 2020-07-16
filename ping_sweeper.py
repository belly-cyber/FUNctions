#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import subprocess


# In[ ]:


subnet=input('type in the ip range example: 10.11.1.0\n')


# In[ ]:


for x in range(1,256):
    ip= subnet+str(x)
    result=subprocess.Popen(['ping','-n','-c1',ip],stdout=subprocess.PIPE,stderr=subprocess.PIPE).wait()
    if result==0:print(result,ip, 'active\n\n\n')
    
    else:
        print(result,ip,'inactive\n\n\n')


# In[ ]:




