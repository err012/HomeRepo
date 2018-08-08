import requests
import sys
import json
import pprint
from collections import Counter
from requests.packages.urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)


class functionLib(object):

    # """Init"""
    def __init__(self, vmanage_ip, username, password):
        self.vmanage_ip = vmanage_ip
        self.username = username
        self.password = password
        self.session = requests.session()
        self.login()

    # """Login"""
    def login(self):
        """Login to vmanage"""
        base_url_str = 'https://%s/' % self.vmanage_ip
        login_action = '/j_security_check'

        # Format data for loginForm
        login_data = {'j_username': self.username, 'j_password': self.password}

        # Url for posting login data
        login_url = base_url_str + login_action
        url = base_url_str + login_url
        self.session = requests.session()
        print self.session
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}

        # If the vmanage has a certificate signed by a trusted authority change verify to True
        login_response = self.session.post(url=login_url, headers=headers, data=login_data, timeout=10, verify=False)
        print login_response.cookies

    # """Get request"""
    def get_requestDeviceTemplate(self, url):
        getUrl = 'https://%s/' % self.url
        print getUrl
        response = self.session.get(getUrl3, verify=False)
        print(self.session.cookies)
        requestData = response.content
        json_data = json.loads(requestData)
        # numElement = json.load(requestData)
        # print(json_data['data'][0]['templateId'])
        # for element in json_data:
        print ("Total Template: %s\n" % len(json_data['data']))
        # for value in json_data['data']:
        numArrayLen = len(json_data['data'])

        list = []
        for x in range(0, numArrayLen):
            y = x + 1
            hostname = json_data['data'][x]['hostName']
            templateName = json_data['data'][x]['templateName']
            templateId = json_data['data'][x]['templateId']
            list.append(hostname, templateName, templateId)

        return list
        #print ("Template: %d" % y)
        #print("Device Name: %s" % json_data['data'][x]['hostName'])
        #print("Template Name: %s" % json_data['data'][x]['templateName'])
        #print("Template ID: %s\n" % json_data['data'][x]['templateId'])
