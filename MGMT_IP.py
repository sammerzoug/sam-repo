import requests


def get_mgmt():

    address_list = []
    i = 0
    while True:
        ip_address = input("Enter A MGMT Ip Address: ")
        if ip_address == 'q':
            break
        else:
            address_list.append(ip_address)
            i += 1
    x = address_list
    return x

