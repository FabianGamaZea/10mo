import matplotlib.pyplot as plt
import numpy as np

def triangulo(i,j,k):
    plt.plot([i,j,k],[0,1,0]) 
    
funciones = 3
rango = [15,30]

distancia_media =(((rango[0])-(rango[1])).__abs__())/(funciones+1)
puntos = []
inicial = rango [0]
puntos.append(inicial)

for i in range(funciones+1):
    inicial = inicial+ distancia_media
    puntos.append(inicial)

triangulos = []

print(puntos)

j = 1
for i in range(funciones):
    triangulos.append([puntos[j-1],puntos[j],puntos[j+1]])
    triangulo(puntos[j-1],puntos[j],puntos[j+1])
    j = j+1
print(triangulos)   
    
    
#print(distancia_media)


#plt.plot([15,18.75,22.5],[0,1,0]) 
plt.title("Triangular")
#plt.plot(x)
plt.ylabel("Eje X")
plt.xlabel("Eje Y")
plt.show()


