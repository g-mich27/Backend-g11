def suma(numero_1, numero_2):
    return numero_1 + numero_2

# resultado_suma = suma(1, 2)
# print(resultado_suma)

def resta(a, b):
    return a - b

# print(resta(2, 4))

def multiplicacion(a, b):
    return a * b

# print(multiplicacion(2, 4))

def division(a, b): 
    return a / b

# print(division(2, 4))

# opcion = input('Indicar operación matematica:')
# print('La operación que solicito es ' + opcion)

def calcularResultadoPorOperacion(operacion, valor_1, valor_2):
    if operacion == 'suma':
        return suma(valor_1, valor_2)
    elif operacion == 'resta':
        return resta(valor_1, valor_2)
    else:
        return 'La operacion no existe'

# operacion = input('Ingrese el tipo de operacion: ')
# valor_1 = int(input('Ingrese el primer numero: '))
# valor_2 = int(input('Ingrese el segundo numero: '))

# resultado = calcularResultadoPorOperacion(operacion, valor_1, valor_2)

# print(f'El resultado de la operacion es: {resultado}')

# nombre = input('Ingrese su nombre: ')
# edad = input('Ingrese su edad: ')
# print (f'Hola {nombre}, tu tienes {edad} años')
# print('Hola {}, tu tienes {} años'.format(nombre, edad))

def calcularResultadoPorOperacion(operacion, valor_1, valor_2):
    if operacion == 'suma':
        return f'El resultado de la {operacion} es: {suma(valor_1, valor_2)}'
    elif operacion == 'resta':
        return f'El resultado de la {operacion} es: {resta(valor_1, valor_2)}'
    else:
        return 'La operacion no existe'

operacion = input('Ingrese el tipo de operacion: ')
valor_1 = int(input('Ingrese el primer numero: '))
valor_2 = int(input('Ingrese el segundo numero: '))

resultado = calcularResultadoPorOperacion(operacion, valor_1, valor_2)

print(resultado)