#!/usr/bin/env python3
# coding: utf-8

# In[ ]:


import requests,re,socket,subprocess

with open('/usr/share/seclists/Discovery/DNS/namelist.txt') as f:
    host_list=[f.readline().strip() for x in f]

domain_name=input('type in the website in question:  ')

website=requests.get('http://www.{}'.format(domain_name))
print('\t\tsearching for domains in www.{}\n'.format(domain_name))
sub_domains=re.findall(r'[^/]*\.{}'.format(domain_name),website.text)
print('\t\tsearching domains against whois\n')
whois_result=str(subprocess.check_output(['whois',domain_name]),'utf-8')
dns_ips={x.split(':')[1]for x in re.findall(r'Name Server:\s\S+',whois_result)}
for x in dns_ips:
    sub_domains.append(x.strip())
for host in host_list:
    sub_domains.append(host+'.'+domain_name)
ip_dic={}
print('\t\tresolving domain to IP\n')
for x in sub_domains:
    x=x.lower()
    try:
        ip_dic.update({x:socket.gethostbyname(x)})
        try:
            dns_tranfer=str(subprocess.check_output(['host','-l',domain_name,x]),'utf-8')
            print('\t\tperfoming zone tranfer on {}\n'.format(x))
        except:
            pass
    except:
        pass

for k in sorted(ip_dic.keys()):
    print('{} : {}'.format(k,ip_dic[k]))

print('\n\t\t{} domains found for {}'.format(len(ip_dic.keys()),domain_name))
