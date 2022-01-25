from ast import Num
import csv
from os import sep
import pandas as pd

"""
Este es el codigo de la actividad de la leccion 1
donde realizamos distintas operaciones y metodos que explicaremos uno a uno

atributos
---------
columnas = df.colums
filas = df.index

metodos
--------
SumaValores()-->suma todas las cantidades del mes
mediaValores() --> saca la media anual
ingresoTotal()--> el dinero que ingresa en el año
gastoTotal()--> el dinero que gasta en el año
comprobarColumnas()--> comprueba que las columnas de los meses no estan vacias
"""
# lee el fichero
try:
    df = pd.read_csv('finanzas2020.csv', sep = '\t',thousands=".",decimal=",")
    col = df.columns
    print("he podido abrir bien el fichero y tiene", len(col),"columnas","\n")
    
except IOError as err:
    print("no he encontrado el archivo", err)

def comprobarValores():
    """
    comprueba que todos los valores del dataframe sean validas para operar con ellos
    si no son validos o son caracteres extraños los pondra a 0
    """ 
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
    """
    suma todas las cantidades de un mes para saber el resultado mensual
    """
    comprobarValores()   
    for j in df.columns:
        print("mes",j,"dinero:",df[j].sum(axis=0))

def mediaValores():
    """
    realiza la media anual
    """
    suma =0
    comprobarValores()
    for j in df.columns:
        suma = suma + df[j].sum(axis=0) 
    
    media=suma/12
    print("la media de gastos al año es:", media, "\n")
    
def ingresoTotal():
    """
    comprueba todos los valores que estan en positivo y los suma para
    saber el ingreso anual
    """
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
    """
    comprueba todos los valores que estan en negativo y los suma para
    saber el gasto anual
    """
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
    """
    comprueba que las columnas no esten vacias
    """
    col=[]
    Numcol=len(df.columns)
    try:
        for j in range(Numcol):
            for i in df.columns:
        #if df[i].values:
                col.append(df[i].values)
            if len(col[j])<0:
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