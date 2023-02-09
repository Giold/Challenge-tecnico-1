from flask import Flask, render_template

app = Flask(__name__)
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

@app.route('/contacto/<nombre>')
def contacto(nombre):
    data={
        'titulo':'Contacto',
        'nombre':nombre
    }
    return render_template('contacto.html', data=data)

##Dato para abrir el servidor con el puerto
if __name__== '__main__':
    app.run(debug=True, port=5000)