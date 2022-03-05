#!/bin/bash
#!/usr/bin/env bash

>sw_ietf_mode

echo "CONFIGURE A TRUNK OR ACCESS PORT: "
read input
if (( $input = access )); then
        echo "START INTERFACE CONFIGURATION YES/NO: "
        read answer
        i=$answer
        while [ $i == yes ]
        do
            echo "Enter user interface: "
            read interface
            echo "Enter user vlan access: "
            read vlan
            echo "interface $interface" >> sw_ietf_mode
            echo "switchport mode access vlan $vlan" >> sw_ietf_mode
            echo "spanning-tree portfast" >> sw_ietf_mode
            echo "spanning-tree bpduguard enable" >> sw_ietf_mode
            echo "no shut" >> sw_ietf_mode
#THIS STATEMENT WILL REQUEST THE ENGINEER TO REENTER \"YES\" TO CONTINUE ADDING INTERFACES TO BE CONFIGURED 
            echo "START INTERFACE CONFIGURATION YES/NO: "
            read answer
            i=$answer
        done

    elif (( $input = trunk )); then
        echo "START INTERFACE CONFIGURATION YES/NO: "
        read answer
        i=$answer
        while [ $i == yes ]
        do
            echo "Enter user interface: "
            read interface
            echo "interface $interface" >> sw_ietf_mode
            echo "switchport trunk encapsulation dot1q" >> sw_ietf_mode
            echo "switchport mode trunk" >> sw_ietf_mode
            echo "switchport nonegotiate" >> sw_ietf_mode
            echo "no shut" >> sw_ietf_mode
#THIS STATEMENT WILL REQUEST THE ENGINEER TO REENTER \"YES\" TO CONTINUE ADDING INTERFACES TO BE CONFIGURED 
            echo "START INTERFACE CONFIGURATION YES/NO: "
            read answer
            i=$answer
        done
fi
