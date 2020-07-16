#!/usr/bin/env python3
# coding: utf-8

# In[ ]:


import requests,re,socket,subprocess


# In[ ]:


domain_name=input('type in the website in question:  ')


# In[ ]:


website=requests.get('http://www.{}.com'.format(domain_name))
sub_domains=re.findall(r'[^/]*\.{}\.com'.format(domain_name),website.text)
whois_result=str(subprocess.check_output(['whois',domain_name+'.com']),'utf-8')
dns_ips={x.split(':')[1]for x in re.findall(r'Name Server:\s\S+',whois_result)}
for x in dns_ips:
    sub_domains.append(x.strip())
    
ip_dic={x:socket.gethostbyname(x) for x in sub_domains}

for k,v in ip_dic.items():
    print('{} : {}'.format(k,v))


# In[ ]:





# In[ ]:




