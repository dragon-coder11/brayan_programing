# Importo la libreria time para hacer las pausas
import time


# Defino la funcion para hacer la cuenta regresiva
def cuenta_regresiva():
    lista = []
    for i in range(10, 0, -1):
        lista.append(i)
    return lista


# Inicio del bucle
while True:
    # Pregunta accion al usuario
    inicio = input("ingresa S para inicar o Q para salir: ").upper()

    # Se ejecuta la funcion y se hace la pausa de un segundo
    if inicio == "S":
        resultado = cuenta_regresiva()
        print("en 10 segundos se ejecutará $ rm -rf    en tu terminal.")
        for linea in resultado:
            print(linea)
            time.sleep(1)

        # Se imprime feli navidad
        print("Feliz navidad!!!")

    # Se hace la salida
    elif inicio == "Q":
        print("Gracias por usar nuestro sistema")
        break

    # Salida para caracter equivocado
    else:
        print("caracter equivocado")
