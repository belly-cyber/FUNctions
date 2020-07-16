#!/usr/bin/env python3
# coding: utf-8

# In[70]:


import os,requests,re,stat
from getpass import getuser


# In[71]:


raw_url='https://raw.githubusercontent.com/lanarhoades-source/FUNctions/'
path='/home/{}/'.format(getuser())


# In[30]:


if os.path.exists(path+'scripts/') == False:
    os.mkdir(path+'scripts/')
    
with open(path+'.bashrc','a') as f:
    f.write('export PATH={}scripts:$PATH'.format(path))
with open(path+'.bash_aliases','a') as f:
    f.write(requests.get('https://raw.githubusercontent.com/lanarhoades-source/bash_aliases/master/aliases'))


# In[34]:


responde=requests.get('https://github.com/lanarhoades-source/FUNctions').text
script_list=re.findall(r'master/.*?py',responde)


# In[69]:


for x in script_list:
    complete_url=raw_url+x
    filename=path+'scripts/'+x
    with open(filename,'w') as f:
        f.write(requests.get(complete_url))
    os.chmod(filename,stat.S_IRWXU)
    
# In[ ]:




