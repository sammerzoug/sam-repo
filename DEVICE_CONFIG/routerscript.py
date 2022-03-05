import paramiko
from netmiko import ConnectHandler
from getpass import getpass  #######THIS WILL GET PASSWORD
import time
from datetime import datetime

class RouterScript:

    start_time = datetime.now().replace(microsecond=0)

    with open ('router_list') as list:
        for IP in list:

            VIRL_DEVICES = {
               'device_type': 'cisco_ios',
               'host':   IP,
               'username': 'cisco',
               'password': 'cisco',
               'global_delay_factor': 4
            }

            print ('Connecting to the device ' + IP)
            net_connect = ConnectHandler(**VIRL_DEVICES)
            time.sleep(2)
            with open ('config', 'r') as CONFIG_LINES:
                CONFIG = CONFIG_LINES.readlines()
                time.sleep(1)
            output = net_connect.send_config_set(CONFIG)
            print(output)
            time.sleep(3)

    end_time = datetime.now().replace(microsecond=0)
    TNOW = end_time - start_time
    print('#' * 50)
    print(f'It took {TNOW} for the script to run.')
    print('#' * 50)

