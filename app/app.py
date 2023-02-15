from flask import Flask
from config import config
from flask_mysqldb import MySQL




app = Flask(__name__)
conexion = MySQL(app)


##Funcion para que detecte HTML
@app.route('/pokemons')
def lista_pokemon():
    try:
        cursor=conexion.connection.cursor()
        sql="SELECT Nombre_pokemon, Abilidad, Limite, FROM api_pokemon_prueba"
        cursor.execute(sql)
        datos=cursor.fetchall()
        print(datos)
    except Exception as ex:
        return 'Error'

def page_not_found(error):
    return "<h1>Oppppppps!!!!!!!!!!!</h1><h2>The page you were searching Doesn´t exist </h2>"
   


##Dato para abrir el servidor con el puerto
if __name__== '__main__':
    app.config.from_object(config['development'])
    app.register_error_handler(404, page_not_found)
    app.run()