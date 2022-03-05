#!/bin/bash
>ssh_config_file.txt
echo "configure terminal" >> ssh_config_file.txt
echo "Enter the device hostname: "
read hostname
echo "hostname $hostname" >> ssh_config_file.txt
echo "!"  >>  ssh_config_file.txt
echo "Enter the username: "
read  username
echo "Enter the password: "
read password
echo "username $username priv 15 password $password"  >>  ssh_config_file.txt
echo "!"  >>  ssh_config_file.txt
echo "Enter the enable password: "
read password
echo "enable password $password" >>  ssh_config_file.txt
echo "!" >>  ssh_config_file.txt
echo 'ip domain name homeserver.net' >>  ssh_config_file.txt
echo "!" >>  ssh_config_file.txt
echo "crypto key generate rsa mod 2048" >>  ssh_config_file.txt
echo "!" >>  ssh_config_file.txt
echo "ip ssh version 2"  >>  ssh_config_file.txt
echo "!"  >>  ssh_config_file.txt
echo "line vty 0 15" >>  ssh_config_file.txt
echo "  login local" >>  ssh_config_file.txt
echo "  logging synchrounous" >> ssh_config_file.txt
echo "  transport input ssh" >> ssh_config_file.txt
echo "  transport preferred ssh" >> ssh_config_file.txt
echo "!" >>  ssh_config_file.txt
echo "end" >>  ssh_config_file.txt
