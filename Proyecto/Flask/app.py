# librerias
from flask import Flask
import random

# crear una aplicacion 
app = Flask(__name__)

# decoradores # netflix.com/pelicula300 
# se crea la ruta raiz netflix.com/
@app.route('/')
def hello_world():
    # diccionario
    o = {"mandarina":"fruta", "caña":"fruta", "mole":"comida" }
    # tipo de dato es lista 
    # list convirtio dictlist a list 
    llaves = list(o.keys())
    # llaves = ['mandarina', 'caña', 'mole']
    # aleatorio es del tipo de dato entero 
    aleatorio = random.randint(0, len(llaves)-1 ) 
    # llave_ale es de tipo de dato string 
    llave_ale = llaves[aleatorio]
    # asi se accede a un diccionario 
    key = llave_ale
    value = o[key]
    
    return 'Tu eres '+ value + " \n"+key


if __name__ == '__main__':
    app.run()