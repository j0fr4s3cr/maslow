import json
from time import sleep
import requests
import sys
from Gets import gets
import pandas as pd
import asyncio
from datetime import *
from exports import exports_to_file
class Devices:
    def __init__(self,api_key):
        self.api_key = api_key
        self.url = ""
        self.headers = {"Content-type": "application/json","Accept": "application/json","X-Cisco-Meraki-API-Key": self.api_key,"Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36"}
        self.payload = None
        self.devices = gets.Gets()
        print(f"Buscando el dispositivo, espera un momento...")
    async def getDevices(self,all):
        list = []
        if all == "all":
            contador = 0
            try: 
                for devices in self.devices.getDevices():
                    await asyncio.sleep(0.1)
                    print(devices)
                    contador += 1
                    list.append(devices)
                    
                df = pd.DataFrame(list)
                export = exports_to_file.export_file(df)
                message = input("¿Deseas exportar la información? y/n:>")
                if message == "y":
                    formato = input("Elige los formatos: csv/xls/txt:>")
                if message == "y" and formato == 'csv':
                   export.export_to_csv(f"Devices.-{date.today()}")
                elif message == 'y' and formato == 'xls':
                    export.export_to_xls(f"-Devices.-{date.today()}")
                elif message == 'y' and formato == 'txt':
                    export.export_to_txt(f"Devices.-{date.today()}") 
            except Exception as e: print(e)
        else:
            print("Ingresa all para imprimir todos los dispositivos")
    def getDevicesBySerialnumber(self,serial):
        list = []
        try:
            for devices in self.devices.getDevices():
                list.append(devices)
            
         
            data_look = pd.DataFrame(list)
            df = data_look[data_look.eq(serial).any(1)]
            if df.empty:
                print(f"{serial} No encontrado")
            else:
                
                df = df.iloc[:,0:]
                print(df)
            
                
        except Exception as e:
            print(e)
        
    
                