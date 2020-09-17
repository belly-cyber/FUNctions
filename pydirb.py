#!/usr/bin/env python3
# coding: utf-8

import sys,requests
from time import sleep
import multiprocessing as mp

def mp_web_checker(dirc):
    sleep(default_timer)
    dirc=''.join(dirc)
    full_address='{}/{}'.format(website,dirc)
    #print(full_address)
    response=requests.get(full_address)
    if 404 != response.status_code:
        result = '{}\t{}'.format(full_address,response)
        print(result)
        return result

man='''
    pyBFdirb.py http://<host/website> <optional wordlist> options     
    
    
    --ballbuster\twill try and bruteforce directories 
    
    --timer\twill change the default time between calls in seconds
    
    -s or --save <filename> saves results to text file
    
    -l or --list <pathname> of wordlist you would like to use
'''
default_timer=.5
website=sys.argv[1]


if 'help' in sys.argv or 'man' in sys.argv:
    print(man)
    sys.exit()
elif len(sys.argv) < 2:
    print(man)
    sys.exit()
    
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
                try:
                    pool=mp.Pool(mp.cpu_count())
                    pool.map(mp_web_checker,itertools.combinations_with_replacement(my_strings,number))
                    pool.join()
                    pool.close()
                except KeyboardInterrupt:
                    print("Caught KeyboardInterrupt, terminating workers")
                    pool.terminate()
    
    elif "-l" in sys.argv or '--list' in sys.argv:
        wordlist_path = sys.argv[sys.argv.index('-l')+1]
        print('using {} as wordlist'.format(wordlist_path))
        with open(wordlist_path) as f:
            wordlist=[x.strip('\n') for x in f.readlines()]
    else:
        print('using default wordlist')
        with open('/usr/share/dirb/wordlists/common.txt') as f:
            wordlist=[x.strip('\n') for x in f.readlines()]
else:
    print(man)
    sys.exit()


try:
    if 'http' not in website:
        website = "http://"+website
    pool=mp.Pool(mp.cpu_count())
    results=pool.map(mp_web_checker,wordlist)
    if '-s' in sys.argv or '--save' in sys.argv:
        with open(sys.argv[-1],'w') as f:
            for x in results:
                if x != None:
                    f.write(x+'\n')
    pool.close()
    pool.join()
except KeyboardInterrupt:
    print("Caught KeyboardInterrupt, terminating workers")
    pool.terminate()

