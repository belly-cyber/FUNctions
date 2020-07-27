#!/usr/bin/env python
# coding: utf-8

# In[33]:


import sys,requests
from time import sleep


# In[80]:


website=sys.argv[1]

website="http://www.megacorpone.com"

if sys.argv[2]==1:
    if '--ballbuster' in sys.argv[2]:
        user_ans=input('are you sure you want to mouth fuck the website:\ntype yes or no\n')
        if 'y' in user_ans.lower():
            pass
        else:
            sys.exit
        import string,itertools
        my_strings=string.printable[:62]+'@#~.%_-'
        for number in range(1,len(my_strings)):
            for name in itertools.combinations_with_replacement(my_strings,number):
                extention=''.join(name)
                sleep(.5)
                full_address='{}/{}'.format(website,extention)
                response=requests.get(full_address)
                if 404 != response.status_code:
                    print('{}\t{}'.format(full_address,response))
                    
        
        
        
    else:
        print('using {} as wordlist'.format(sys.argv[2]))
        with open(sys.argv[2]) as f:
            wordlist=[x.strip('\n') for x in f.readlines()]
else:
    print('using default wordlist')
    with open('/usr/share/dirb/wordlists/common.txt') as f:
        wordlist=[x.strip('\n') for x in f.readlines()]



for extention in wordlist:
    sleep(.5)
    full_address='{}/{}'.format(website,extention)
    response=requests.get(full_address)
    if 404 != response.status_code:
        print('{}\t{}'.format(full_address,response))




# In[ ]:




