import pandas as pd
import core
from genericpath import exists
class export_file:
    def __init__(self,dataframe):
        self.dataframe = dataframe
        
    def export_to_csv(self,name):
        self.dataframe.to_csv(f"{name}.csv",index=False)
        if exists(f"{name}.csv"):
            print("Archivo creado con exito")
        else:
            print("No se pudo crear el archivo")
            
    def export_to_xls(self,name):
        self.dataframe.to_excel(f"{name}.xlsx",index=False)
        if exists(f"{name}.xlsx"):
            print("Archivo creado con exito")
        else:
            print("No se pudo crear el archivo")
            
    def export_to_txt(self,name):
        self.dataframe.to_csv(f"{name}.txt",sep='\t',index=False)
        if exists(f"{name}.txt"):
            print("Archivo creado con exito")
        else:
            print("No se pudo crear el archivo")