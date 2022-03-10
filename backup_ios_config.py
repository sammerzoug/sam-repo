from netmiko import ConnectHandler
from getpass import getpass
from netmiko.ssh_exception import NetMikoTimeoutException
from netmiko.ssh_exception import NetMikoAuthenticationException
from paramiko.ssh_exception import SSHException
import datetime
import time
import schedule


def backup():
    ip_list = open('router_list', 'r')
    for ip in ip_list:
        rtr = {
            "device_type": 'cisco_ios',
            "host": ip,
            "username": 'sam',
            "password": 'Nikita1980!'
        }

        print(f'\n####Connecting to the device {ip}')
        try:
            net_connect = ConnectHandler(**rtr)

        except NetMikoTimeoutException:
            print('Device not reachable')
            continue

        except NetMikoAuthenticationException:
            print('Authentication Failure')
            continue

        except SSHException:
            print('Make sure SSH is enabled.')
            continue

        print('\n Initiating config backup \n')
        output = net_connect.send_command('show run')
        i = 0
        running_config = open('config_file', 'w')

        for i, line in enumerate(output.split('\n'), i):
            running_config.write('%s-  %s\n' % (i, line))
            i += 1
        running_config.close()
        print(running_config)

