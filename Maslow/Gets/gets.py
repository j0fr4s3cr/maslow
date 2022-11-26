import requests
import json
import re
import sys
import time
class Gets:
    
    def __init__(self):
        self.url = ""
        self.payload = None
        self.headers = {"Content-Type": "application/json","Accept": "application/json","X-Cisco-Meraki-API-Key": sys.argv[2]}
    def getOrganizations(self):
        try:
            self.url = "https://api.meraki.com/api/v0/organizations"
            response = requests.request("GET", self.url, headers=self.headers, data = self.payload)
            response = json.loads(response.text)
            for org in response:
                time.sleep(0.1)
                if 'errors' in response:
                    pass
                else:
                    yield org
        except Exception as e:
            print(e)
            
    def getNetworks(self):
        try:
            for org in self.getOrganizations():
                self.url = "https://api.meraki.com/api/v1/organizations/{id}/networks".format(id = org['id'])
                r = requests.request("GET",self.url, headers=self.headers, data = self.payload)
                r = json.loads(r.text)
                for i in r:
                    time.sleep(0.1)
                    if 'errors' in i:
                        pass
                    else:
                        yield i
        except Exception as e:
            print(e)   
                 
    def getDevices(self):
        try:
            for dev in self.getNetworks():
                self.url = "https://api.meraki.com/api/v1/networks/" + dev['id'] + "/devices"
                r = requests.request("GET",self.url, headers=self.headers, data = self.payload)
                r = json.loads(r.text)
                for i in r:
                    time.sleep(0.1)
                    if 'errors' in i:
                        pass
                    else:
                        yield i
        except Exception as e:
            print(e)
    
    @staticmethod
    def getTrafficAnalysis(self):
        try:
            for net in self.getNetworks():
                self.url = "https://api.meraki.com/api/v1/networks/{}/trafficAnalysis".format(net['id'])
                r = requests.request("GET",self.url, headers=self.headers, data = self.payload)
                r = json.loads(r.text)
                for i in r:
                    if 'errors' in r:
                        pass
                    else:
                        yield i
        except Exception as e:
            print(e)
                   
    @staticmethod 
    def getFirewallRulesl7(self):
        try:
            for net in self.getNetworks():
                self.url = "https://api.meraki.com/api/v1/networks/{}/l7FirewallRules".format(net['id'])
                r = requests.request("GET",self.url, headers=self.headers, data = self.payload)
                r = json.loads(r.text)
                for i in r:
                    if 'errors' in i:
                        pass
                    else:
                        yield i
                        
        except Exception as e:
            print(e)
            
    @staticmethod
    def getNetworksAlertSettings(self):
        try:
            for net in self.getNetworks():
                self.url = "https://api.meraki.com/api/v1/networks/{}/alerts/settings".format(net['id'])
                r = requests.request("GET",self.url, headers=self.headers, data = self.payload)
                r = json.loads(r.text)
                for i in r:
                    if 'errors' in i:
                        pass
                    else:
                        yield i
                        
        except Exception as e:
            print(e)
            
    @staticmethod
    def getOrganizationsAdmins(self):
        try:
            for org in self.getOrganizations():
                self.url = "https://api.meraki.com/api/v1/organizations/{}/admins".format(org['id'])
                r = requests.request("GET",self.url, headers=self.headers, data = self.payload)
                r = json.loads(r.text)
                for i in r:
                    if 'errors' in i:
                        pass
                    else:
                        yield i
        except Exception as e:
            print(e)
            
    @staticmethod
    def getOrganizationsInventoryDevices(self):
        try:
            for org in self.getOrganizations():
                self.url = "https://api.meraki.com/api/v1/organizations/{}}/inventoryDevices".format(org['id'])
                r = requests.request("GET",self.url, headers=self.headers, data = self.payload)
                r = json.loads(r.text)
                for i in r:
                    if 'errors' in i:
                        pass
                    else:
                        yield i
        except Exception as e:
            print(e)
            
    @staticmethod
    def getOrganizationsSnmp(self):
        try:
            for org in self.getOrganizations():
                self.url = "https://api.meraki.com/api/v1/organizations/{}/snmp".format(org['id'])
                r = requests.request("GET",self.url, headers=self.headers, data = self.payload)
                r = json.loads(r.text)
                for i in r:
                    if 'errors' in i:
                        pass
                    else:
                        yield i
        except Exception as e:
            print(e)
            
    @staticmethod
    def getOrganizationsConfigTemplate(self):
        try:
            
            for org in self.getOrganizations():
                self.url = "https://api.meraki.com/api/v1/organizations/{}/configTemplates".format(org['id'])
                r = requests.request("GET",self.url, headers=self.headers, data = self.payload)
                r = json.loads(r.text)
                for i in r:
                    if 'errors' in i:
                        pass
                    else:
                        yield i
        except Exception as e:
            print(e)          
    
    @staticmethod
    def getOrganizationLicences(self):
        try:
            contador = 0
            for org in self.getOrganizations():
                self.url = "https://api.meraki.com/api/v1/organizations/{}/licenses".format(org['id'])
                r = requests.request("GET",self.url, headers=self.headers, data = self.payload)
                r = json.loads(r.text)
                for i in r:
                    if 'errors' in i:
                        pass
                    else:
                        yield i
        except Exception as e:
            print(e)
    @staticmethod
    def getNetworksWirelessSsids(self):
        try:
            for device in self.getDevices():
                self.url = "https://api.meraki.com/api/v0/networks/{}/ssids".format(device['networkId'])
                r = requests.request("GET",self.url, headers=self.headers, data = self.payload)
                r = json.loads(r.text)
                for ssid in r:
                    if 'errors' in ssid:
                        pass
                    else:
                        
                        yield ssid    
        except Exception as e:
            print(e)