def saludar(nombre):
    saludo = 'Hola {}'.format(nombre)
    print(saludo)

saludar('Michell')

def saludar_varios(*args):
    # cuando nosotros colocamos en un parametro el '*' significa que no 
    # hay limite de ese parametro, este parametro debe de ir al ultimo
    # en un tupla
    # Nota: la tuplas, a diferencia de los arreglos, no se pueden modificar
    # osea una vez creadas sus valores no pueden cambiar
    print(args)
    for nombre in args:
        saludo = 'Hola {}'.format(nombre)
        print(saludo)

saludar_varios('Roxana', 'Juana', 'Martin', 'Roberto')
saludar_varios('Pedro', 'Luis')
saludar_varios()
saludar_varios('Michell', 20, True, 10.5)

def informacion_usuario(**kwargs):
    # kwargs > keyboard argumentso se le pasan parametros por llaves
    print(kwargs)
    # .get('llave') > devolver el valor si es que existe la llave, sino existe entonces devolvera none o el segundo parametro que le colocaremos (opcional)
    print(kwargs.get('estatura', 'NO HAAAAAAAAY'))
    try:
        print(kwargs['estatura'])
    except:
        print('No existe la llave estatura')

informacion_usuario(nombre='Michell', edad=30, estado_civil='soltero', estatura=1.88)
informacion_usuario(nombre='Pamela', apellido='Juarez', nacionalidad='Colombiana',
fecha_nacimiento='31/06/1999')
print('ADIOOOOOOOS')

# Recibir 2 valores y hacer la division (dividendo / divisor) y retornamos el resultado
def dividir(dividendo, divisor):
    # Si la division da error entonces retornar un mensaje que diga 'Division incorrecta'
    try:
        resultado = dividendo / divisor
        return resultado
    except ZeroDivisionError:
        # aqui ingresara cuando la division sea entre 0
        return 'No puede haber division entre 0'
    except TypeError:
        # ingresara cuando la division tienes algun caracter
        return 'Las divisiones solamente pueden ser entre dos numeros'
    except:
        # ingresara si no es ninguna de los dos errores enteriores
        return 'Error desconocido'

valor = dividir(10,5)
print(valor)

valor = dividir(10,0)
print(valor)

valor = dividir('a', 'h')
print(valor)

try: 
    valor = dividir(5,)
    print(valor)
except TypeError:
    print('Estubo mal llamar asi la funcion')