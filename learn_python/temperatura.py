#Programa de conversion de temperaturas
dec = "si"

while dec == "si":

#Pedimos la temperatura al usuario
    try:
        temperatura = float(input("ingresa la temperatura que deseas convertir: "))
    except ValueError:
        print("⚠️ Por favor, ingresa un número válido.")
        continue

    eleccion = input("elige la escala a convertir: F /fahrenheit C / celsius: ").upper() 


#Ejecutamos la operacion

    if eleccion == "F":
        operacion = (9/5 * temperatura) + 32
        print(f"El reusltado de la conversion a grados fahrenheit es {operacion:.2f}°")


    elif eleccion == "C":
        operacion = 5/9 * (temperatura - 32)
        print(f"El resultado de la conversion a grados celsius es {operacion:.2f}°")

    else:
        print("escala no valida usa F o C.")

    dec = input("deseas realizar alguna otra conversión si/ no: ")

