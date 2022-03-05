import paramiko
from netmiko import ConnectHandler
from getpass import getpass
import time
from datetime import datetime

class Routerscript:

    def __init__(self, IP, username, password):
        self.IP = IP
        self.username = username
        self.password = password

    def connect(self):
        VIRL_DEVICES = {
            'device_type': 'cisco_ios',
            'host': self.IP,
            'username': self.username,
            'password': self.password,
            'global_delay_factor': 4
        }

        print ('Connecting to the device ' + self.IP)
        net_connect = ConnectHandler(**VIRL_DEVICES)
        time.sleep(2)

        with open ('config', 'r') as CONFIG_LINES:
            CONFIG = CONFIG_LINES.readlines()
            time.sleep(1)
        output = net_connect.send_config_set(CONFIG)
        print(output)

        save_output = open('saved_output_' + self.IP, 'w')
        save_output.write(output)
        save_output.close
        print(f"Command Output has been saved.")
        time.sleep(3)

def get_ellapsed_time(start, end):
    TNOW = end_time - start_time
    print('#' * 50)
    print(f'It took {TNOW} for the script to run.') 
    print('#' * 50)


start_time = datetime.now().replace(microsecond=0)

list = open('router_list')

for IP in list:
    s = Routerscript(IP, "cisco", "cisco")
    s.connect()

end_time = datetime.now().replace(microsecond=0)

get_ellapsed_time(start_time, end_time)
