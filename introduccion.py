numero = 10

if numero > 11:
    print('Este numero es mayor que 11')

string = 'soy un string'
boolean_true = True
booelan_false = False
flotantes = 3.14
diccionarios = {
    'nombre': 'Michell'
}
listas = [1,2,3, 'string', 3.14]
tuplas = ("texto_1", "texto_2", "texto_3")

# print(type(booelan_false))

x = 5
x = 'cinco'
x = 'numero'
y = '5'
y = int(y)
y = str(y)
y = float(y)
# print(y)

# formas icorrectas de nombrar una variable
# numero-cinco = 5
# 5numero = 5
# numero cinco = 5

# formas correctas de nombrar variables
numero_cinco = 5
numeroCinco = 5
_numeroCinco = 5

# asignar multiples variables
a,b,c = 2,5,'string'
# print(b)

def myFuncion():
    variable_1 = "texto de ejemplo"
    print(variable_1)

# myFuncion()

# OPERADORES

# 5 == 5
# 4 != 5
# 1 > 0
# 0 < 1
# 5 >= 5
# 6 <= 6

# or
# and
# not

# CONDICIONALES

# if (5 > 4):
#   print('El número cinco es mayor que cuatro')
# else:
#   print('No se cumplió con la condición')

edad = 18

# if edad < 18:
#    print('Eres menor de edad')
# elif edad == 18:
#    print('Acabas de convertirte en mayor de edad')
# else:
#    print('Eres mayor de edad')

estado_civil = 'D'

# if estado_civil == 'C':
#    print('El usuario esta casado')
# elif estado_civil == 'V':
#    print('El usuario esta viudo')
# elif estado_civil == 'D':
#    print('El usuario esta divorciado')
# else:
#    print('El usuario esta soltero')

lista_nombres = ['Eduardo', 'Antonio', 'Luis', 'Mary', 'Paolo']

#for nombre in lista_nombres:
#    print(nombre)

lista_numeros = [23, 24, 25, 26, 27]

for num in lista_numeros:
    if num == 25:
        break  
    print(num)
    # 23
    # 24

for num in lista_numeros:
    if num == 25:
        continue  
    print(num)
    # 23
    # 24
    # 26
    # 27

#print(lista_numeros[2]) 