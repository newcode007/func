from ipaddress import *
c=0
for ip in ip_network('192.168.32.160/255.255.255.240'):
    print(ip)
    c+=1
print(c)