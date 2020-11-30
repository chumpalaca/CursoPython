# -*- coding: utf-8 -*-
"""
Editor de Spyder

Este es un archivo temporal
"""

#funcion de ordenamiento
def ordenarMayorMenor(nombreLista):
    for i in range(0,len(nombreLista)-1,1):
      for j in range(0,len(nombreLista)-1,1):
        if nombreLista[j][1]<nombreLista[j+1][1]:
            aux=nombreLista[j+1]
            nombreLista[j+1]=nombreLista[j]
            nombreLista[j]=aux
 

#importar librería csv
import csv


#############################
########## OPCION 1  ########
#############################
rutas =[]
rutas_sin_repetir = []
with open("baseproyecto2.csv","r") as baseDatos:
    lector = csv.reader(baseDatos)
    for linea in lector:
        ruta = linea[2]+"-"+linea[3]
        rutas.append(ruta)

rutas_sin_repetir =list(set(rutas))
#print(rutas_sin_repetir)

#for i in range(0,len(rutas_sin_repetir)):
#    if rutas_sin_repetir[i]=="origin-destination":
#        posicion=i
        
#print("posicion ",posicion)
rutas_sin_repetir.pop(139)

rutas_y_veces = []
num_veces = 0

for i in range(0,len(rutas_sin_repetir)):
    for j in range(0,len(rutas)):
        
        if rutas[j] == rutas_sin_repetir[i]:
            
            num_veces = num_veces+1
        
    rutas_y_veces.append([rutas_sin_repetir[i],num_veces])
    num_veces = 0
    
ordenarMayorMenor(rutas_y_veces)

print("Las rutas más demandadas son:")
for i in range(0,10):
    info = "Ruta "+str(i+1)+" "+rutas_y_veces[i][0]+" se repite "+str(rutas_y_veces[i][1])+" veces"
    print(info)

#############################
########## OPCION 2  ########
#############################
transportes =[]
transportes_sin_repetir = []
with open("baseproyecto2.csv","r") as baseDatos:
    lector = csv.reader(baseDatos)
    for linea in lector:
        transporte = linea[7]
        transportes.append(transporte)

transportes_sin_repetir =list(set(transportes))
transportes_sin_repetir.pop(0)
#print(transportes_sin_repetir)


transportes_y_valor = []
with open("baseproyecto2.csv","r") as baseDatos:
    lector = csv.reader(baseDatos)
    for linea in lector:       
        transportes_y_valor.append([linea[7],linea[9]])

#print(transportes_y_valor)

transportes_y_valorTotal = []
valor_total = 0

for i in range(0,len(transportes_sin_repetir)):
    for j in range(0,len(transportes_y_valor)):
        
        if transportes_y_valor[j][0] == transportes_sin_repetir[i]:
            
            valor_total = valor_total+float(transportes_y_valor[j][1])
        
    transportes_y_valorTotal.append([transportes_sin_repetir[i],valor_total])
    valor_total = 0

ordenarMayorMenor(transportes_y_valorTotal)
#print(transportes_y_valorTotal)
print("\nLos medios de transporte más importantes considerando el valor de las importaciones y exportaciones son:")
for i in range(0,3):
    info = "Medio "+str(i+1)+" "+transportes_y_valorTotal[i][0]+" tiene valor "+str(transportes_y_valorTotal[i][1]) 
    print(info)

print("\nEl medio que se podría reducir es:")
info = "Medio "+str(4)+" "+transportes_y_valorTotal[3][0]+" tiene valor "+str(transportes_y_valorTotal[3][1]) 
print(info)

#############################
########## OPCION 3  ########
#############################

rutas_y_valor = []
with open("baseproyecto2.csv","r") as baseDatos:
    lector = csv.reader(baseDatos)
    for linea in lector:       
        rutas_y_valor.append([linea[2]+"-"+linea[3],linea[9]])

#print(rutas_y_valor)

rutas_y_valorTotal = []
valor_total = 0

for i in range(0,len(rutas_sin_repetir)):
    for j in range(0,len(rutas_y_valor)):
        
        if rutas_y_valor[j][0] == rutas_sin_repetir[i]:
            
            valor_total = valor_total+float(rutas_y_valor[j][1])
        
    rutas_y_valorTotal.append([rutas_sin_repetir[i],valor_total])
    valor_total = 0

ordenarMayorMenor(rutas_y_valorTotal)
#print(rutas_y_valorTotal)

#Obtención del valor total de todas las rutas
valor_total_global = 0
for i in range(0,len(rutas_y_valorTotal)):
    valor_total_global = valor_total_global + float(rutas_y_valorTotal[i][1])
  
info = "\nValor total global de exportaciones e importaciones:"+str(valor_total_global)
print(info)
ochenta_porciento_total_global = 0.8*valor_total_global
info = "El 80% del valor total global de exportaciones e importaciones es:"+str(ochenta_porciento_total_global)
print(info)



rutas_ochenta_porciento=[]
ochenta_porciento_aux = 0
for i in range(0,len(rutas_y_valorTotal)):
    if ochenta_porciento_aux <= ochenta_porciento_total_global:
        ochenta_porciento_aux = ochenta_porciento_aux + float(rutas_y_valorTotal[i][1])
        rutas_ochenta_porciento.append(rutas_y_valorTotal[i])

rutas_ochenta_porciento.pop(len(rutas_ochenta_porciento)-1)
ochenta_porciento_aux=0

for i in range(0,len(rutas_ochenta_porciento)):
    ochenta_porciento_aux=ochenta_porciento_aux + float(rutas_ochenta_porciento[i][1])
    
#print(rutas_ochenta_porciento)
#print(ochenta_porciento_aux)

info = "\nSynergy logistics debería enfocarse en los siguientes países que generan alrededor del 80% ("+str(ochenta_porciento_aux)+") del total global de las exportaciones e importaciones:"
print(info)
for i in range(0,len(rutas_ochenta_porciento)):
    info = "Ruta "+str(i+1)+" "+rutas_ochenta_porciento[i][0]+" con valor de "+str(rutas_ochenta_porciento[i][1])
    print(info)

