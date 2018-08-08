import requests
import sys
import json
import pprint
import time
from collections import Counter

from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

class functionLib(object):
	#"""Init"""
	def __init__(self, vmanage_ip, username, password):
		self.vmanage_ip = vmanage_ip
		self.username = username
		self.password = password
		self.session = requests.session()
		self.login()

	#"""Login"""
	def login(self):
		"""Login to vmanage"""
		base_url_str = 'https://%s/'%self.vmanage_ip
		login_action = '/j_security_check'

		#Format data for loginForm
		login_data = {'j_username' : self.username, 'j_password' : self.password}

		#Url for posting login data
		login_url = base_url_str + login_action
		url = base_url_str + login_url
		self.session = requests.session()
		print self.session
		headers = {'Content-Type': 'application/x-www-form-urlencoded'}

		#If the vmanage has a certificate signed by a trusted authority change verify to True
		login_response = self.session.post(url=login_url, headers = headers, data=login_data, timeout=10, verify=False)
		print login_response.cookies

	#"""Get request"""
	def get_request(self):
			getUrl1 = 'https://172.16.130.171/dataservice/system/device/vedges' #Get device template ID
			#getUrl2 = 'https://172.16.130.171/dataservice/device' #Get device info
			#getUrl3 = 'https://172.16.130.171/dataservice/template/device/' #Get template only
			print getUrl3
			response = self.session.get(getUrl3, verify=False)
			print(self.session.cookies)
			requestData = response.content
			json_data = json.loads(requestData)
			#numElement = json.load(requestData)
			#print(json_data['data'][0]['templateId'])
			#for element in json_data:
			print ("Total Template: %s\n"%len(json_data['data']))
    			#for value in json_data['data']:
			numArrayLen = len(json_data['data'])
			for x in range(0, numArrayLen):
					y = x+1
        				print ("Template: %d" % y)
					print("Device Name: %s"%json_data['data'][x]['hostName'])
					print("Template Name: %s"%json_data['data'][x]['templateName'])
					print("Template ID: %s\n"%json_data['data'][x]['templateId'])

	def get_requestDeviceInfo(self):
		getUrl2 = 'https://172.16.130.171/dataservice/device/action/changepartition?deviceId=1.1.1.11'
		print getUrl2
		response = self.session.get(getUrl2, verify=False)
		print(self.session.cookies)
		requestData = response.content
		json_data = json.loads(requestData)
		print json_data

	def post_activateSoftware(self):
        	postUrl = 'https://172.16.130.171/dataservice/device/action/changepartition'

		payload =	{
			  "action":"changepartition",
			  "devices":[
				{
				  "version":"17.2.5",
				  "deviceIP":"1.1.1.21",
				  "deviceId":"1920C408170593"
				}
			  ],
			  "deviceType":"vedge"
}
		#"""Push Firmware to vEdges"""
		response = self.session.post(url=postUrl, data=json.dumps(payload), headers={'Content-Type': 'application/json'}, verify=False)
		json_data = json.loads(response.text)
		print(json_data["id"])

	#"""POST request"""
	def post_request(self):
        	postUrl = 'https://172.16.130.171/dataservice/device/action/install'

		payload =	{
				  "action":"install",
				  "input":{
					"vEdgeVPN":0,
					"vSmartVPN":0,
					"version":"17.2.5",
					"versionType":"vmanage",
					"reboot":False,
					"sync":True
				  },
				  "devices":[
					{
					  "deviceIP":"1.1.1.21",
					  "deviceId":"1920C408170593"
					}
				  ],
				  "deviceType":"vedge"
				}
		#"""Push Firmware to vEdges"""
		response = self.session.post(url=postUrl, data=json.dumps(payload), headers={'Content-Type': 'application/json'}, verify=False)
		json_data = json.loads(response.text)
		print(json_data["id"])
		#return json_data

		#"""Monitor Status"""
		getUrl = 'https://172.16.130.171/dataservice/device/action/status/%s'%json_data["id"]
		print getUrl
		statusResponse = self.session.get(getUrl, verify=False)
		print(statusResponse)
		print(statusResponse.text)
		json_monitorState = json.loads(statusResponse.text)
		print(json_monitorState)

	def post_requestAttachTemplateInput(self):
        	postUrl = 'https://172.16.130.171/dataservice/template/device/config/input' #Get Device Input for Attach Template

		payload =	{
				  "templateId":"279cce51-27bb-4475-acfc-aba3d1982784",
				  "deviceIds":
					[
					  "11OG119161802"
					],
				  "isEdited":False,
				  "isMasterEdited":False
				  }

		#"""Push Firmware to vEdges"""
		response = self.session.post(url=postUrl, data=json.dumps(payload), headers={'Content-Type': 'application/json'}, verify=False)
		json_data = json.loads(response.text)
		print json_data
		#return json_data

	def post_requestAttachTemplate(self):
        	postUrl = 'https://172.16.130.171/dataservice/template/device/config/attachfeature'

		payload =	{
				  "deviceTemplateList":[
				  {
					"templateId":"279cce51-27bb-4475-acfc-aba3d1982784",
					"device":[
					{
					  "csv-status":"complete",
					  "csv-deviceId":"11OG119161802",
					  "csv-deviceIP":"1.1.1.11",
					  "csv-host-name":"VE11",
					  "//system/host-name":"VE11",
					  "//system/system-ip":"1.1.1.11",
					  "//system/site-id":"10",
					  "csv-templateId":"dd11b5b3-07f7-4e46-86dd-f5e99c9830f5",
					  "selected":"true"
					}
					],
					"isEdited":False,
					"isMasterEdited":False
				  }
				  ]
				}
		#"""Attach template to vEdges"""
		response = self.session.post(url=postUrl, data=json.dumps(payload), headers={'Content-Type': 'application/json'}, verify=False)
		print response
		json_data = json.loads(response.text)
		print(json_data)
		#return json_data
		#"""Monitor Status"""
		getUrl = 'https://172.16.130.171/dataservice/device/action/status/%s'%json_data["id"]
		print getUrl
		statusResponse = self.session.get(getUrl, verify=False)
		print(statusResponse)
		print(statusResponse.text)
		json_monitorState = json.loads(statusResponse.text)
		print("\n"%json_monitorState)
		print("First Status: %s"%json_monitorState['validation']['status'])
		return json_data

	def checkStatus(self):
		#dataReturn = self.post_requestAttachTemplate()
		#getUrl = 'https://172.16.130.171/dataservice/device/action/status/%s'%dataReturn['id']
		getUrl = 'https://172.16.130.171/dataservice/device/action/status/change_partition-4e198f98-dbce-4724-bc9b-724167e1cec1'
		print getUrl
		statusResponse = self.session.get(getUrl, verify=False)
		print(statusResponse)
		print(statusResponse.text)
		json_monitorState = json.loads(statusResponse.text)
		print(""%json_monitorState)
		print("\nActivity: %s"%json_monitorState['data'][0]['activity'])
		print("\nValidation-Status: %s"%json_monitorState['validation']['status'])
		print("\nSuccess-Status: %s"%json_monitorState['data'][0]['statusId'])
		print("\nSummary: %s"%json_monitorState['summary']['status'])
		print("\nCount: %s"%json_monitorState['summary']['count'])
		print("\nActive-Version: %s"%json_monitorState['data'][0]['active-partition'])
		statusNum = json_monitorState['data'][0]['statusId']
		return statusNum


def main():
	test = functionLib('172.16.130.171', 'admin', 'admin')
	#testGetDeviceInfo = test.get_requestDeviceInfo()
	#test1 = test.post_activateSoftware()
	#testPost = test.post_requestAttachTemplateInput()
	testPost = test.checkStatus()


main()

