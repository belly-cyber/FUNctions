#!/usr/bin/env python3
# coding: utf-8

# In[ ]:


import requests,re,socket,subprocess

host_list=['a',
 'admin',
 'alpha',
 'broadcast',
 'cisco',
 'dns',
 'dummy',
 'firewall',
 'ftp',
 'gate',
 'gateway',
 'gw',
 'home',
 'host',
 'host1',
 'host10',
 'host11',
 'host12',
 'host13',
 'host14',
 'host15',
 'host17',
 'host18',
 'host19',
 'host2',
 'host20',
 'host21',
 'host22',
 'host23',
 'host24',
 'host25',
 'host26',
 'host27',
 'host28',
 'host29',
 'host3',
 'host4',
 'host5',
 'host6',
 'host7',
 'host8',
 'host9',
 'ip',
 'jupiter',
 'mail',
 'mailhost',
 'mars',
 'mercury',
 'network',
 'news',
 'ns',
 'ns1',
 'ns2',
 'pc1',
 'pc10',
 'pc11',
 'pc12',
 'pc13',
 'pc14',
 'pc15',
 'pc16',
 'pc17',
 'pc18',
 'pc19',
 'pc2',
 'pc20',
 'pc21',
 'pc22',
 'pc23',
 'pc24',
 'pc25',
 'pc26',
 'pc27',
 'pc28',
 'pc29',
 'pc3',
 'pc30',
 'pc4',
 'pc5',
 'pc6',
 'pc7',
 'pc8',
 'pc9',
 'pluto',
 'ppp1',
 'ppp2',
 'proxy',
 'router',
 's0',
 'server',
 'smtp',
 'test',
 'user',
 'venus',
 'web',
 'ws1',
 'ws2',
 'www',
 'www2',
 'zeus']



domain_name=input('type in the website in question:  ')


# In[ ]:


website=requests.get('http://www.{}.com'.format(domain_name))
sub_domains=re.findall(r'[^/]*\.{}\.com'.format(domain_name),website.text)
whois_result=str(subprocess.check_output(['whois',domain_name+'.com']),'utf-8')
dns_ips={x.split(':')[1]for x in re.findall(r'Name Server:\s\S+',whois_result)}
for x in dns_ips:
    sub_domains.append(x.strip())
for host in host_list:
    sub_domains.append(host+'.'+domain_name+'.com')
ip_dic={}
for x in sub_domains:
    print(x)
    try:
        ip_dic.update({x:socket.gethostbyname(x)})
    except:
        pass
    
for k,v in ip_dic.items():
    print('{} : {}'.format(k,v))


# In[ ]:





# In[ ]:




