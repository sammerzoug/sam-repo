from typing import BinaryIO
import requests
import json
import time
import MGMT_IP
from GET_CONF import get_conf as g
from datetime import datetime
from urllib3.exceptions import InsecureRequestWarning


requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)


# Print a stream of bytes as pretty JSON
def printBytesAsJSON(bytes):
	print(json.dumps(json.loads(bytes), indent=2))


li = MGMT_IP.get_mgmt()

y = ' '
for y in li:
	printBytesAsJSON(g(y))
