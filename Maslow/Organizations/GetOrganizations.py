from tkinter import E
import requests
import json
import sys
import pandas as pd
import core
import time
class Organization:
    
    def __init__(self,api_key):
        self.url = "https://api.meraki.com/api/v1/organizations"
        self.payload = None
        self.contador = 0
        self.headers = {"Content-type": "application/json","Accept": "application/json","X-Cisco-Meraki-API-Key": str(api_key)}
        self.message = "Wait a moment, please searching organizations...".rjust(50)
        print(core.Core.message(self.message))
    
    def json_format(self,data):
        json_data = json.loads(data)
        return json_data
    #construccion de la funcion para buscar por nombre o id
    def SearchByNameorID(self,request,nombre):
        list = []
        for i in request:
            list.append(i)
            self.contador += 1
        data_look = pd.DataFrame(list)
        df = data_look[data_look.eq(nombre).any(1)]
        if df.empty:
            print(f"{nombre} No encontrado")
        else:
            
            df = df.iloc[:,0:3]
            print(f"Buscando en:{self.contador} Organizaciones")
            time.sleep(2)
            print(df)
             
    def Find_OrganizationsByName(self,nombre):
        try:
            r_org = requests.request("GET",self.url,headers=self.headers,data=self.payload)
            r_org = self.json_format(r_org.text)
            self.SearchByNameorID(r_org,nombre)          
                  
        except Exception as e:
            print(e)
            
    def AllOrganizations(self,total):
        contador = 0
        if total == "all":
            try:
                r_org = requests.request("GET",self.url,headers=self.headers,data=self.payload)
                r_org = self.json_format(r_org.text)
                
                for i in r_org:
                    print(i)
                    contador+=1
                print(f"Tienes: {contador} organizaciones")
            except Exception as e:
                print(e)
        else:
            print("Ingresa el comando valido")