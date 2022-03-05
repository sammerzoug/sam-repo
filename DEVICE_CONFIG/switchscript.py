import datetime
from netmiko import ConnectHandler
from getpass import getpass  #######THIS WILL GET PASSWORD
import time


with open ('switch_list') as list:
    for IP in list:

#        hostname = input ('ENTER THE HOSTNAME: ')
#        username = input ('ENTER YOUR USERNAME: ')
#        password = getpass()
        VIRL_DEVICES = {
           'device_type': 'cisco_ios',
           'host':   IP,
           'username': 'cisco',
           'password': 'cisco',
        }
        print ('Connecting to the device ' + IP)
        net_connect = ConnectHandler(**VIRL_DEVICES)
        time.sleep(2)
        with open ('config', 'r') as CONFIG_LINES:
            CONFIG = CONFIG_LINES.readlines()
        output = net_connect.send_config_set(CONFIG)
        print(output)
