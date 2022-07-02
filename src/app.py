# Importaciones para el manejo de metodos, consultas sql y formatos ligeros json
import json
from flask import Flask,jsonify,request
from flask_mysqldb import MySQL

from config import config
# Validaciones y declaración de base de datos
app = Flask(__name__)

conexion = MySQL(app)

# Con el app route ejecuto el codigo que esté por debajo, señalizandolo con methods para identificar su función
@app.route('/cursos', methods=['GET'])
def listarcursos():
    try:
        """"Declarando el cursor de la conexión para navegar dentro de la base de datos
        Arguments:
            sql: Variable utilizada para realizar las consultas requeridas según el metodo
            cursor: Variable utilizada para ejecutar la consulta, recolectando el valor de la variable sql
            datos: Variable con una función fetch utilizada para tomar en este caso fetchall todos los datos
            cursos: Variable declarada como lista para ingresar los valores con un ciclo
            curso: Diccionario utilizado para identificar en donde se encuentra el valor de cada columna dentro de la tabla
            cursos.append(curso): Los valores del diccionaro curso pasan a la lista cursos
            return: Utilizados para al finalizar la consulta, impriminan en dado caso los resultados y un mensaje satisfactorio
            o por el contrario impriman un error
        
        """
        cursor=conexion.connection.cursor()
        sql = "SELECT codigo, nombre, creditos FROM curso"
        cursor.execute(sql)
        datos = cursor.fetchall()
        cursos = []
        for fila in datos:
            curso = {'codigo': fila[0], 'nombre': fila[1], 'creditos': fila[2]}
            cursos.append(curso)
        return jsonify({'cursos': cursos, 'mensaje': "Cursos Listados."})
    except Exception as ex:
        return jsonify({'mensaje': "Error"})

@app.route('/cursos/<codigo>', methods=['GET'])
def leer_curso(codigo):
    try:
        cursor=conexion.connection.cursor()
        sql = "SELECT codigo, nombre, creditos FROM curso WHERE codigo = '{0}'".format(codigo)
        cursor.execute(sql)
        datos = cursor.fetchone()
        if datos != None:
            curso = {'codigo': datos[0], 'nombre': datos[1], 'creditos': datos[2]}
            return jsonify({'curso': curso, 'mensaje': "Cursos encontrados."})
        else:
            return jsonify({'mensaje': "Curso no encontrado"})
    except Exception as ex:
        return jsonify({'mensaje': "Error"})

@app.route('/cursos', methods=['POST'])
def registrar_curso():
    # print(request.json)
    try:
        cursor=conexion.connection.cursor()
        sql= """INSERT INTO curso (codigo, nombre, creditos) 
        VALUES ('{0}','{1}', {2})""".format(request.json['codigo'],request.json['nombre'],request.json['creditos'])
        cursor.execute(sql)
        conexion.connection.commit() #Confirma la acción que se va realizar
        return jsonify({'mensaje': "Curso Registrado"})
    except Exception as ex:
        return jsonify({'mensaje': "Error"})

@app.route('/cursos/<codigo>', methods=['PUT'])
def actualizar_curso(codigo):
    try:
        cursor=conexion.connection.cursor()
        sql = """UPDATE curso SET nombre = '{0}', creditos = '{1}' 
        WHERE codigo = '{2}'""".format(request.json['nombre'], request.json['creditos'], codigo)
        cursor.execute(sql)
        conexion.connection.commit() #Confirma la acción que se va realizar
        return jsonify({'mensaje': "Curso Actualizado"})
    except Exception as ex:
        return jsonify({'mensaje': "Error"})


@app.route('/cursos/<codigo>', methods=['DELETE'])
def eliminar_curso(codigo):
    try:
        cursor=conexion.connection.cursor()
        sql= "DELETE FROM curso WHERE codigo = '{0}'".format(codigo)
        cursor.execute(sql)
        conexion.connection.commit() #Confirma la acción que se va realizar
        return jsonify({'mensaje': "Curso Eliminado"})
    except Exception as ex:
        return jsonify({'mensaje': "Error"})


# Función utilizada para identificar que, efectivamente, no existe una pagina
def pagina_no_encontrada(error):
    return "<h1>La página que intentas buscar no existe</h1>", 404
# Condición, que efectua en complemento con config.py, la validación de las credenciales de la BD y en dado caso, un error 404
if __name__ == '__main__':
    app.config.from_object(config['development'])
    app.register_error_handler(404, pagina_no_encontrada)
    app.run()
        
    