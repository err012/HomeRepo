import FirmwareUpgrade as funcStore
import requests
import sys
import json

#Login
#x = funcStore.login('funcStore.self', '172.16.130.171', 'admin', 'admin')
#print("Login returned " + str(x))

#Get
y = funcStore.get_request('funcStore.self')
