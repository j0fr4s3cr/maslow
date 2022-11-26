import requests
import json
import time
from Gets import gets
import pandas as pd
import openpyxl
import sys
from exports import exports_to_file
from datetime import *

class Network:
    
    def __init__(self,api_key):
        self.url = ""
        self.payload = None
        self.headers = {"Content-type": "application/json","Accept": "application/json","X-Cisco-Meraki-API-Key": str(api_key)}
        self.gets = gets.Gets()
        
    def getNetworks(self):
        try: 
            for network in self.gets.getNetworks():print(network)     
        except Exception as e:print(e)
        
    def getNetworksByOrganizationName(self,org):
        contador = 0
        try:
            self.url = "https://api.meraki.com/api/v1/organizations"
            response = requests.request("GET",self.url,headers=self.headers,data=self.payload)
            response = json.loads(response.text)
            list = []
            for i in response:
                if org in i['name'] or org in i['id']:
                    self.url = "https://api.meraki.com/api/v1/organizations/{}/networks".format(i['id'])
                    response = requests.request("GET",self.url,headers=self.headers,data=self.payload)
                    response = json.loads(response.text)
                    for i in response:
                        contador +=1
                        list.append(i)
                else:
                    pass
            prnt = input("Escriba i para visualizar las network o g para guardar:>")
            if prnt == 'i':
                for i in list:
                    print(i)
            else:
            
                df = pd.DataFrame(list)
                export = exports_to_file.export_file(df)
                print(f"Tienes: {contador} Networks")
                message = input("¿Deseas exportar la información? y/n:>")
                if message == "y":
                    formato = input("Elige los formatos: csv/xls/txt:>")
                    if message == "y" and formato == "csv":
                        export.export_to_csv(f"Networks_.{date.today()}")
                    elif message == 'y' and formato == "xls":
                        export.export_to_xls(f"Networks_.{date.today()}")
                    elif message == 'y' and formato == "txt":
                        export.export_to_txt(f"Networks_.{date.today()}") 
                else:
                    print("Gracias por usar Maslow :)")
             
            
        except Exception as e:
            print(e)   
                     