#!/usr/bin/env python3
# coding: utf-8

# In[ ]:


import requests,re,socket,subprocess

with open('/usr/share/seclists/Discovery/DNS/namelist.txt') as f:
    host_list=[f.readline().strip() for x in f]

domain_name=input('type in the website in question:  ')

website=requests.get('http://www.{}'.format(domain_name))
sub_domains=re.findall(r'[^/]*\.{}'.format(domain_name),website.text)
whois_result=str(subprocess.check_output(['whois',domain_name]),'utf-8')
dns_ips={x.split(':')[1]for x in re.findall(r'Name Server:\s\S+',whois_result)}
for x in dns_ips:
    sub_domains.append(x.strip())
for host in host_list:
    sub_domains.append(host+'.'+domain_name)
ip_dic={}
for x in sub_domains:
    try:
        ip_dic.update({x:socket.gethostbyname(x)})
        try:
            dns_tranfer=str(subprocess.check_output(['host','-l',domain_name,x]),'utf-8')
            print('perfoming zone tranfer on {}'.format(x))
            print(dns_tranfer)
        except:
            pass
    except:
        pass
    
for k,v in ip_dic.items():
    print('{} : {}'.format(k,v))


# In[ ]:





# In[ ]:




