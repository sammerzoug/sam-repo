#!/bin/bash
>sw_ietf_conf
echo "conf t" >> sw_ietf_conf
echo "no ip routing" >> sw_ietf_conf
echo "Create VLAN: "
read vlan
echo "vlan $vlan"  >> sw_ietf_conf
echo "VLAN NAME: "
read name
echo "name $name"  >> sw_ietf_conf
echo "CREATE AN SVI: "
read svi
echo "interface vlan $svi"  >> sw_ietf_conf
echo "ASSIGN AN IP TO YOUR SVI: "
read ip_add
echo "ip address $ip_add"  >> sw_ietf_conf
echo "no shut"  >> sw_ietf_conf
echo "end"  >> sw_ietf_conf

