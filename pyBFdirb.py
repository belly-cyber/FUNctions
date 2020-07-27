#!/usr/bin/env python
# coding: utf-8

# In[4]:


import sys,requests
from time import sleep
import multiprocessing as mp

default_timer=.5
website=sys.argv[1]
website='http://www.megacorpone.com'


def web_checker(dirc):
    sleep(default_timer)
    full_address='{}/{}'.format(website,dirc)
    print(full_address)
    response=requests.get(full_address)
    if 404 != response.status_code:
        print('{}\t{}'.format(full_address,response))

def mp_web_checker(dirc):
    sleep(default_timer)
    dirc=''.join(dirc)
    full_address='{}/{}'.format(website,dirc)
    print(full_address)
    response=requests.get(full_address)
    if 404 != response.status_code:
        print('{}\t{}'.format(full_address,response))


# In[5]:


man='''
    pyBFdirb.py http://<host/website> <optional wordlist> options           )
    
    
    --ballbuster\twill try and bruteforce directories 
    
    --timer\twill change the default time between calls in seconds
'''


if 'help' in sys.argv:
    print(man)
    sys.exit()
elif len(sys.argv) <2:
    print(man)
    sys.exit()
    
if len(sys.argv)==2:
    print('using default wordlist')
    with open('/usr/share/dirb/wordlists/common.txt') as f:
        wordlist=[x.strip('\n') for x in f.readlines()]
    

    
elif len(sys.argv)>2:
    if '--ballbuster' in sys.argv[2]:
        user_ans=input('are you sure you want to mouth fuck the website:\ntype yes or no\n')
        if 'y' in user_ans.lower():
            pass
        else:
            sys.exit()
        import string,itertools
        my_strings=string.printable[:62]+'@#~._-'
        for number in range(1,len(my_strings)):
            for name in itertools.combinations_with_replacement(my_strings,number):
                pool=mp.Pool(mp.cpu_count())
                pool.map(mp_web_checker,itertools.combinations_with_replacement(my_strings,number))
                pool.join()
                pool.close()                    
    else:
        print('using {} as wordlist'.format(sys.argv[2]))
        with open(sys.argv[2]) as f:
            wordlist=[x.strip('\n') for x in f.readlines()]
else:
    print(man)
    sys.exit()



pool=mp.Pool(mp.cpu_count())
pool.map(web_checker,wordlist)
pool.join()
pool.close()


# In[ ]:




