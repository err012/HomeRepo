import myFunction as funcStore
import requests
import sys
import json




test = funcStore.login('172.16.130.171', 'admin', 'admin')
myTest = test.get_requestDeviceTemplate('https://172.16.130.171/dataservice/system/device/vedges')
#myTest = test.checkStatus()
#global myGlobal
#print myGlobal
print myTest
