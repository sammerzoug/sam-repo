#!/bin/bash
>Interface_configuration
echo "Enter interface type: "
read interface_type
echo "config t" >> Interface_configuration
echo "interface $interface_type" >> Interface_configuration
echo "Enter interface address: "
read ip_add
echo "ip address $ip_add" >> Interface_configuration
echo "no shut" >> Interface_configuration
echo "ip route 0.0.0.0 0.0.0.0 172.172.50.1 name GW" >> Interface_configuration
