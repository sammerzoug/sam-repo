from netmiko import ConnectHandler
from getpass import getpass

IP = input("Enter DEVICE IP: ")
username = input("Enter USERNAME: ")
password = getpass("Enter PASSWORD: ")
command = input("ENTER COMMAND: ")
VIRL_DEVICE = {
    'device_type': 'cisco_ios',
    'host':   IP,
    'username': username,
    'password': password,
}

net_connect = ConnectHandler(**VIRL_DEVICE)

output = net_connect.send_command(command)
print(output)

#config_commands = [ 'logging buffered 20000',
#                    'logging buffered 20010',
#                    'no logging console' ]

#output = net_connect.send_config_set(config_commands) ####THIS COMMAND SEND A DICT COMMAND
#print(output)
