# -*- encoding:utf-8 -*-
__author__ = 'Administrator'
import os

ip_block = raw_input("Please input ip block: ")
start_ip = raw_input("Please input the start ip: ")
# gate_way = raw_input("Please input the GateWay")
ipmi = raw_input("If you have enabled ?(y/n) ")



def caculate_ip(ip_block):
        ip_infor = {}
        ip_number_at_block2 = 32 - int(ip_block.split("/")[1])
        ip_number_at_block = pow(2, ip_number_at_block2)
        netmask_last = 256 - ip_number_at_block
        ip_infor['netmask'] = '255.255.255.'+str(netmask_last)
        ip_infor['ipnumber'] = ip_number_at_block - 3
        return ip_infor
ip_info=caculate_ip(ip_block)
c_block = start_ip.split(".")
if ipmi == 'y':
    for x in range(ip_info['ipnumber']-1):
        deviceId= str("eth0:"+ str(x))
        str_to_write = deviceId+"\n"+"BOOTPROTO=static"+"\n"+"ONBOOT=yes"+"\n"+"IPADDR="+c_block[0]+'.'+c_block[1]+'.'+c_block[2]+'.'+str(int(c_block[3])+x)+"\n"+"NETMASK="+ip_info['netmask']
        print deviceId
        file_object = open(deviceId, 'w')
        file_object.write(str_to_write)
        file_object.close()
else:
    for x in range(ip_info['ipnumber']-1):
        deviceId= "eth0:"+ str(x)
        str_to_write = deviceId+"\n"+"BOOTPROTO=static"+"\n"+"ONBOOT=yes"+"\n"+"IPADDR="+c_block[0]+'.'+c_block[1]+'.'+c_block[2]+'.'+str(int(c_block[3])+x)+"\n"+"NETMASK="+ip_info['netmask']
        file_object = open(deviceId, 'w')
        file_object.write(str_to_write)
        file_object.close()
os.system("service network restart")




