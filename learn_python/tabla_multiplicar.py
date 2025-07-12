#Ejercicio tabla de multiplicar

def tabla(numero):
    operacion = []
    for i in range(1,11):
        operacion.append(f"{numero} x {i} = {numero*i}")
    return operacion
    
#Pedimos el numero l usuario
soli = int(input("ingresa el numero del cual deseas la tabla: "))

#Se ejecuto la funcion creada
resultado = tabla(soli)

#Imprimimos la informacion, utilizando el for
#para poder imprimir cada linea
print("la tabla del numero que solicitaste es: ")
for linea in resultado:
    print(linea)





