from flask import Flask, render_template, request, url_for, redirect, jsonify
from flask_mysqldb import MySQL

app = Flask(__name__)

# Datos necesarios para conectar a base de datos

##Funcion para que detecte HTML
@app.route('/')

def index():
    
    ##Lista de datos para probar impresion
    clases_escuela = ['Quimica','Espanol','Fisica', 'Ingles']
    
    #Datos a imprimir 
    data = {
        'titulo' : 'Prueba Server PAPA al cuadrado',
        'bienvenida' : 'Hello There!',
        'clases' : clases_escuela,
        'numero_clases' : len(clases_escuela)
        
    }
    
    return render_template('index.html', data=data)

@app.route('/contacto/<nombre>/<int:edad>')
def contacto(nombre, edad):
    data={
        'titulo':'Contacto',
        'nombre':nombre,
        'edad':edad

    }
    return render_template('contacto.html', data=data)

def query_string():
    print(request)
    print(request.args)
    print(request.args.get('param1'))
    print(request.args.get('param2'))
    return "Ok"

def pagina404(error):
    return render_template('404.html'), 404

##Dato para abrir el servidor con el puerto
if __name__== '__main__':
    app.add_url_rule('/query_string',view_func=query_string)
    app.register_error_handler(404,pagina404)
    app.run(debug=True, port=5000)