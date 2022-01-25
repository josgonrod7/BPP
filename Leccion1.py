from ast import Num
import csv
from os import sep
import pandas as pd


# lee el fichero
try:
    df = pd.read_csv('finanzas2020.csv', sep = '\t',thousands=".",decimal=",")
    col = df.columns
    print("he podido abrir bien el fichero y tiene", len(col),"columnas","\n")
    
except IOError as err:
    print("no he encontrado el archivo", err)

def comprobarValores(): 
    for i in df.index:
        for c in df.columns:
            value = df.loc[i, c]
            if type(value) == str:
                try:
                    value = float(value)
                except:
                    value = 0
                finally:
                    df.loc[i, c] = value

def SumaValores():
    comprobarValores()   
    for j in df.columns:
        print("mes",j,"dinero:",df[j].sum(axis=0))

def mediaValores():
    suma =0
    comprobarValores()
    for j in df.columns:
        suma = suma + df[j].sum(axis=0) 
    
    media=suma/12
    print("la media de gastos al año es:", media, "\n")
    
def ingresoTotal():
    ingreso=[]
    suma=0
    try:
        for i in df.index:
            for c in df.columns:
                value = df.loc[i, c]
                if value>0:
                    ingreso.append(value)
                    for g in ingreso:
                        suma+=g
        
        print("El ingreso total ha sido: ", suma)
    except Exception as e:
        print("se ha producido el siguiente error", e)
def gastoTotal():
    gasto=[]
    suma=0
    try:
        for i in df.index:
            for c in df.columns:
                value = df.loc[i, c]
                if value<0:
                    gasto.append(value)
                    for g in gasto:
                        suma+=g
        
        print("El gasto total ha sido: ", suma)
    except Exception as e:
        print("se ha producido el siguiente error", e)

def comprobarColumnas():
    col=[]
    Numcol=len(df.columns)
    try:
        for j in range(Numcol):
            for i in df.columns:
        #if df[i].values:
                col.append(df[i].values)
            if len(col[j])==0:
                print("esta colomuna esta vacia")
            else:
                print("esta columna esta llena")
    except IOError as err:
        print("se ha producido un error", err)



SumaValores()
mediaValores() 
ingresoTotal()   
gastoTotal()
comprobarColumnas()