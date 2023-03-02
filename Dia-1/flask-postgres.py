from flask import Flask, request
from psycopg2 import connect

app = Flask(__name__)

@app.route('/', methods= ['GET'])
def inicial():
    return {
        'message': 'Bienvenido a mi API'
    }
@app.route('/alumnos', methods= ['GET', 'POST'])
def alumnos():
    if request.method == 'GET':
        # Me conecto a la red
        conexion = connect(host='localhost', database='pruebas', user='postgres', password='sql2023')
        
        # Creo un cursor que es el responsable de hacer lecturas y escrituras a al bd
        cursor = conexion.cursor()

        # Extraigo la informacion de la ejecución de la query
        cursor.execute('SELECT * FROM alumnos;')

        resultados = cursor.fetchall()

        print(resultados)
        return {
            'message': 'Yo soy el GET'
        }
    elif request.method == 'POST':
        return {
            'message': 'Yo soy el POST'
        }

if __name__ == '__main__':
    # debug > indica que cada vez que guardemos un archivo del proyecyo el servidor se reinicie automaticamente
    app.run(debug=True)