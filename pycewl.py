#!/usr/bin/env python
# coding: utf-8

# In[1]:


'''
Python version of cewl by diginija https://github.com/digininja/CeWL 
work in progress
'''

import re
import requests
import string
import sys


# In[2]:


#website = sys.argv[1]
depth_lvl   = 3
word_length = '6'
regex       = '\S{'+word_length+',}'
re_obj      = re.compile(regex)
target      = "megacorpone"
websites    = {"http://www.{}.com".format(target)}


generic_header = {
                 "User-Agent" : "Mozilla/5.0 (X11; Linux x86_64; rv:68.0) Gecko/20100101 Firefox/68.0",
                 "Accept" : "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
                 "Accept-Language" : "en-US,en;q=0.5",
                 "Accept-Encoding": "gzip, deflate",
                 "Content-Type" : "application/x-www-form-urlencoded",
                 "Connection": "keep-alive",
                 "Upgrade-Insecure-Requests": "1"
                 }


# In[3]:


level = 0
possible_passwd=[]
while level < depth_lvl:
    for website in list(websites):
        try:
            content = requests.get(website,headers=generic_header).text
        except:
            pass
        possible_passwd += re.findall(re_obj,content)
        websites.update({x.replace('https','http') for x in re.findall(r"\w+://{0,1}\w*\.\w*\.\w*[/\w*]*",content) if target in x})
        level +=1
        


# In[4]:


print(websites)
print(sorted(set(possible_passwd)))

