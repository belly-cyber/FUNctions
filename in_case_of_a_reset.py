#!/usr/bin/env python3
# coding: utf-8

import os,requests,re,stat,subprocess
from getpass import getuser


raw_url='https://raw.githubusercontent.com/belly-cyber/FUNctions/master/'
path='/home/{}/'.format(getuser())


if os.path.exists(path+'scripts/') == False:
    os.mkdir(path+'scripts/')
    
with open(path+'.bashrc','a') as f:
    f.write('export PATH={}scripts:$PATH'.format(path))
with open(path+'.bash_aliases','a') as f:
    f.write(requests.get('https://raw.githubusercontent.com/belly-cyber/bash_aliases/master/aliases').text)


responde=requests.get('https://github.com/belly-cyber/FUNctions').text
script_list=[x.split('/')[1] for x in re.findall(r'master/.*?\.py',responde)]


for x in script_list:
    complete_url=raw_url+x
    filename=path+'scripts/'+x
    with open(filename,'w') as f:
        f.write(requests.get(complete_url).text)
    os.chmod(filename,stat.S_IRWXU)

subprocess.call(['sudo','apt','update'])
subprocess.call(['sudo','apt','install','seclists'])
subprocess.call(['sudo','apt','install','mingw-w64'])
subprocess.call(['sudo','apt','install','nmap'])
subprocess.call(['sudo','apt','-y','install','python3-pip'])
subprocess.call(['sudo','apt','install','python3-paramiko'])
subprocess.call(['python3','-m','pip','install cffi'])



