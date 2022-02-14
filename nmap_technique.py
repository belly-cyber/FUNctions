import itertools
import time
import subprocess
from   random import shuffle

template_scan='nmap <options> -p {} {}'
########## sample data #############
network = '192.168.1.0'
raw_ports   = list(range(22,150))
blacklist=['192.168.1.5']
####################################

def subnetgenerator(network):
    'returns iter'
    octets=network.split('.')
    for last_octet in range(1,253):
        octets[-1]=str(last_octet)
        yield '.'.join(octets)

def port_pair_gen(port_list):
    'returns iter'
    shuffle(port_list)
    p_list=list(map(str,port_list))
    if len(p_list)%2!=0:
        p_list.append('')
    pairs = zip(p_list[::2],p_list[1::2])
    return pairs


def ip_port_combination(network,port_list):
    subnet=subnetgenerator(network)
    ip_pool=[] #contains all possible ip port combinations
    for ip in subnet:
        portpairs=port_pair_gen(port_list)
        for pair in portpairs:
            final_pair=(ip,','.join(pair))
            ip_pool.append(final_pair)
    return ip_pool
        


ip_pool = ip_port_combination(network,raw_ports) 
shuffle(ip_pool)


for ip,ports in ip_pool:
    if ip in blacklist:
        pass
    else:
        log_file='{}scanlog.txt'.format(time.strftime('%d%b%y',time.gmtime()))
        scan_command = template_scan.format(ports,ip)
        log_text= '{}\n{}\n\n'.format(time.asctime(),scan_command) 
        with open(log_file,'a') as log:
            log.write(log_text)
        print(scan_command)
        #subprocess.run(scan_command.split())
