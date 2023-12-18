import os

print("Hello world from ...")
os.system("python --version")


# Repaso 
# Control Flow Python 
# A
def primero_más_último(lista):
    return lista[0] + lista[-1]

lista = [1, 2, 3, 4, 5]
print(primero_más_último(lista))

# B
# Suma a Diez (NO): Para empezar, vamos a comprobar si la suma de dos valores NO es igual a diez.

"""
Se le dan dos números almacenados (num1 y num2). Si la suma de num1 y num2 NO es igual a 10, entonces almacena True en una variable llamada "not_ten", de lo contrario almacena False en "not_ten".
"""

# Variables
num1 = 6
num2 = 3

# Condicional if, else:
if num1 + num2 != 10:
    no_diez = True
else:
    no_diez = False

print("¿La suma de los números es igual a 10? " + str(no_diez))

# C Excederse del Presupuesto:

"""
Supongamos que estamos intentando ahorrar algo de dinero y vigilamos nuestro presupuesto. Tenemos que asegurarnos de que el resultado de nuestros gastos es inferior a la cantidad total que hemos asignado a cada una de las categorías.

 - Te dan un presupuesto mensual y algunos gastos y necesitas comprobar si la suma de los gastos supera el presupuesto.

- En primer lugar, almacena el total de todos los gastos en una variable llamada total.

- A continuación, comprueba si el total es superior al presupuesto. Si lo es, almacena True en una variable llamada sobre_presupuesto, de lo contrario almacena False en sobre_presupuesto.

"""

# Presupuesto mensual
presupuesto = 2000

# Gastos mensuales
factura_comida = 200
factura_electricidad = 100
factura_internet = 60
alquiler = 1500

# Calcular el monto total de gastos
monto_total = factura_comida + factura_electricidad + factura_internet + alquiler


# Comprobar si el total es mayor que el presupuesto y almacenar el resultado en exceso_presupuesto
# Condicional if, else 
if monto_total > presupuesto:
    exceso_presupuesto = True
else:
    exceso_presupuesto = False



print("Total: " + str(monto_total))
print("¿Está sobre el presupuesto? " + str(exceso_presupuesto))


# D Gran Potencia: Funciones Condicionales

"""
Para el siguiente reto de código, vamos a añadir funciones a la mezcla. Creamos una función que comprueba si el resultado de sumar la potencia de un número a otro número proporciona una respuesta mayor que 5000. Usaremos una sentencia condicional para devolver True si el resultado es mayor que 5000 o devolver False si no lo es. Para lograr esto, necesitaremos los siguientes pasos:

1 ) Definir la función para que acepte dos parámetros de entrada llamados base y exponente.
2 ) Calcular el resultado de base a la potencia del exponente
3 ) Utilizar una sentencia if para comprobar si el resultado es mayor que 5000. Si lo es, devuelve True. En caso contrario, devuelve False

"""
# Escribe aquí tu función gran_potencia:
def gran_potencia(base, exponente):
    if base ** exponente > 5000:
        return True
    else:
        return False
        
# Descomenta estas llamadas de función para probar tu función gran_potencia:
print(gran_potencia(490, 2))
print(gran_potencia(2, 12))

# E El doble de grande:

"""
En este reto, determinaremos si un número es dos veces mayor que otro número. Para ello, compararemos el primer número con el doble del segundo.

1 - Definir nuestra función con dos entradas num1 y num2.
2 - Multiplicar el segundo parametro por 2.(Dentro del if)
3 - Utilice una sentencia if para comparar el resultado del último cálculo con la primera entrada.
4 - Si num1 es mayor entonces devuelve True (return True) en caso contrario devuelve False (return False).

"""

def dos_veces_mayor(num1, num2):
    if num1 > num2 * 2:
        return True
    else: 
        return False

print(dos_veces_mayor(10,5))
print(dos_veces_mayor(11,5))

# F Divisible por diez:

"""
Por último, ¡hagamos las cosas un poco más difíciles! Vamos a crear una función que determine si un número es o no divisible por diez. Un número es divisible por diez si el resto del número dividido por 10 es 0. Usando esto, podemos completar esta función en unos pocos pasos:

1 - Define la cabecera de la función para que acepte un parametro llamado num.
2 - Calcular el resto dividido por 10 (usar módulo %).
3 - Utiliza una sentencia if para comprobar si el resto % es igual 0. Si el resto es 0, devuelve True, en caso contrario, devuelve False

"""

def divisible_por_diez(num):
    if (num % 10 == 0):
        return True
    else:
        return False

print(divisible_por_diez(20))
print(divisible_por_diez(25))

# realizamos la operación módulo ( % )  dentro de la condición de la sentencia if. Probamos si el resultado es igual a 0 y si lo es, entonces devolvemos True (return True) de lo contrario devolvemos False (return False).


