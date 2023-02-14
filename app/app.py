from flask import Flask, render_template, request, url_for, redirect, jsonify
from config import config
from flask_mysqldb import MySQL


app = Flask(__name__)
conexion = MySQL(app)


##Funcion para que detecte HTML
@app.route('/pokemons')
def lista_pokemon():
    try:
        return 'ok'
    except Exception as ex:
        return 'Error'



def index():
    return "Evola"
   


##Dato para abrir el servidor con el puerto
if __name__== '__main__':
    app.config.from_object(config['development'])
    app.run()