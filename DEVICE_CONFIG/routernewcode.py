#import paramiko
#from netmiko import ConnectHandler
#from getpass import getpass
#import time
#from datetime import datetime
class Routerscript:

    IP = " "
    username = " "
    password = " "

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
        time.sleep(3)

    def start_time(self):
        start_time = datetime.now().replace(microsecond=0)
        return start_time

    def end_time(self):
        end_time = datetime.now().replace(microsecond=0)
        return end_time

