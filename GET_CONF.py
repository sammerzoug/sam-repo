import requests


def get_conf(arg):

    URL = f'https://{arg}/restconf/data/Cisco-IOS-XE-native:native/interface'
    AUTH = ('sam', 'Nikita1980!')
    HEADERS = {'Accept': 'application/yang-data+json', 'content': 'application/yang-data+json'}

    # Retrieve configuration through RESTCONF
    response = requests.get(
        url=URL,
        auth=AUTH,
        headers=HEADERS,
        verify=False
    )

    return response.content
    # Pretty print our JSON response
    #printBytesAsJSON(response.content)