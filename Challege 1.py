
import math

#Datos para la operacion#  
Latitud1 = 18.60646 
Latitud1cos = math.cos(Latitud1)
Longitud1 = -90.73780
Latitud2 = -38.373825292521154
Latitud2cos = math.cos(Latitud2)
Longitud2 = -69.67405073588125 
tiempo = 24 

v = (((math.pi*2)*(6371))*Latitud1cos)/24
v1 = (((math.pi*2)*(6371))*Latitud2cos)/24
v2= math.cos(19.43)

print(v,v1,v2)
 
