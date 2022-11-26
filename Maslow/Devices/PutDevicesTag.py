import requests
import json
import re
import time
class PutDevice:
    def __init__(self,api_key):
        self.api_key  = api_key
        self.url = ""
        self.headers = {"Content-type": "application/json","Accept": "application/json","X-Cisco-Meraki-API-Key": self.api_key,}
        self.payload = None
    
    
    def DeviceFindModel(self,request):
        for device in request:
            modelo = device['model']
            pattern = 'MX'
            match = re.match(pattern,modelo)
            if "errors" in device:
                continue
            if match:
                value = "MX"
                print( "Name:"+ device['name']+" modelo: "+ modelo +" tag: "+ value)
            pattern = 'MR'
            match = re.match(pattern,modelo)
            if match:
                value = "MR"
                print( "Name:"+ device['name']+" modelo: "+ modelo +" tag: "+ value)
            pattern = 'MS'
            match = re.match(pattern,modelo)
            if match:
                value = "MS"
                print( "Name:"+ device['name']+" modelo: "+ modelo+" tag: "+ value)
                #self.PutDevicesSerial(str(device['networkId']),str(device['serial']),value)  
              
    def OrganizationDevicesAddTag(self,org_id):
        self.url = f"https://api.meraki.com/api/v1/organizations/{str(org_id)}/devices"
        r = requests.request("GET",self.url,headers=self.headers,data=self.payload)
        r = json.loads(r.text)
        
        self.DeviceFindModel(r)     
               
    def PutDevicesSerialAddTag(self,network_id,serial,value):
        self.url = f"https://api.meraki.com/api/v0/networks/{str(network_id)}/devices/{str(serial)}"
        #Ese payload es el que se va a enviar solo que este es el principal y nosotros mandemos el payload que queremos
        """self.payload = '''{"name": "","lat": 37.4180951010362,"lng": -122.098531723022,"serial": "Q234-ABCD-5678","mac": "00:11:22:33:44:55","tags": " recently-added "}'''"""
        ##Este es el payload que se va a enviar con los datos que queremos
        self.payload ='''{
        "tags": " {} "
        }'''.format(value)
        r = requests.request("PUT",self.url,headers=self.headers,data=self.payload)
        print("PUT: ",r.text+" Status: "+ r.status_code)
               