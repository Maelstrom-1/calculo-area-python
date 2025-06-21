import math


# Paso 1 : Solicitar al usuario que ingrese el radio del circulo.

radio = float(input("por favor ingrese el radio del circulo: "))

# Paso 2: Calcular el ara del circulo  utilizando la formula area = π * radio²

area = math.pi * (radio ** 2)

# Paso 3: Mostrar  al usuario el area calculada

print("el area del circulo con radio", radio, "es:", area)