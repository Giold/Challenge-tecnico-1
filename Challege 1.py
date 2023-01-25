
import math

#Datos para la operacion#  
Latitud1 = 18.60646 
Latitud1rad = (math.pi*Latitud1)/180
Latitud1cos = math.cos(Latitud1rad)
Longitud1 = -90.73780
Latitud2 = -38.373825292521154
Latitud2rad = (math.pi*Latitud2)/180
Latitud2cos = math.cos(Latitud2rad)
Longitud2 = -69.67405073588125 
tiempo = 24 

v = (((math.pi*2)*(6371))*Latitud1cos)/tiempo
v1 = (((math.pi*2)*(6371))*Latitud2cos)/tiempo


print(v)
print(v1) 