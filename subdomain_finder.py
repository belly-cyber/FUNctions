#!/usr/bin/env python
# coding: utf-8

# In[17]:


import requests,re,socket


# In[26]:


domain_name=input('type in the website in question:  ')


# In[28]:


website=requests.get('http://www.{}.com'.format(domain_name))
sub_domains=re.findall(r'[^/]*\.{}\.com'.format(domain_name),website.text)
ip_dic={x:socket.gethostbyname(x) for x in sub_domains}
for k,v in ip_dic.items():
    print('{} : {}'.format(k,v))


# In[ ]:




