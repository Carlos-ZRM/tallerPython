# librerias
from flask import Flask , send_file, request, Response , json
import random

# crear una aplicacion 
app = Flask(__name__)
# dic = bd(nombre_bd=nombre)
'''
    division (numerador, denominador):
        return numerador / denominador
    
    ... 
    res = division(10, 5 )
    res = division(denominador=10, numerador=5 )
'''
def db ():
    "JSON es un tipo de documento que define datos"
    '''
    {
     "name":"calabaza",
     "imagen":"ruta.png",
     "nombres":["Carlos","vianey"],
     "dic":{
             "nom_dic":"nombre"
             }
     }
    '''
    mole = {
        "nombre":"mole con pollo",
        "ingredientes":["pollo","mole","ingrediente"],
        "ruta": "mole.png"
        }
    caña = {
       "nombre":"caña",
       "ruta":"caña.png",
       "peso":5
        }
    li = {"mole":mole, "caña":caña }
    return li
# decoradores # netflix.com/pelicula300 
# se crea la ruta raiz netflix.com/
# AQUI SE RECIBE EL REQUEST O PETICION DEL CLIENTE WEB 
# 127.0.0.1:5000/
@app.route('/')
def hello_world():
    # diccionario
    #o = {"mandarina":"fruta", "caña":"fruta", "mole":"comida" }
    base_datos = db()
    # tipo de dato es lista 
    # list convirtio dictlist a list 
    llaves = list(base_datos.keys())
    # llaves = ['mandarina', 'caña', 'mole']
    # aleatorio es del tipo de dato entero 
    aleatorio = random.randint(0, len(llaves)-1 ) 
    # llave_ale es de tipo de dato string 
    #llave elegida
    llave_ale = llaves[aleatorio]
    # asi se accede a un diccionario 
    key = llave_ale
    value = base_datos[key]
    #filename="fruta.png"
    #return send_file(filename, mimetype='image/png')
    # RETURN (RESPUESTA ) 
    return 'Tu eres '+ str(value) + " \n"+key
# 127.0.0.1:5000/json
@app.route('/json')
def hello_json():
    # diccionario
    base_datos = db()
    # tipo de dato es lista 
    # list convirtio dictlist a list 
    llaves = list(base_datos.keys())
    # llaves = ['mandarina', 'caña', 'mole']
    # aleatorio es del tipo de dato entero 
    aleatorio = random.randint(0, len(llaves)-1 ) 
    # llave_ale es de tipo de dato string 
    #llave elegida
    llave_ale = llaves[aleatorio]
    # asi se accede a un diccionario 
    key = llave_ale
    value = base_datos[key]
    #filename="fruta.png"
    #return send_file(filename, mimetype='image/png')
    # RETURN (RESPUESTA ) 
    # crear archivos .json 
    # convertir diccionario a .json
    myjson = json.dumps(base_datos)
    # debemos crear una respuesta: datos, estatus, tipo de dato
    # response(datos) = Nuestro diccionario convertido en JSON
    # status ( estatus) = 200 correcto
    # mimetype ( tipo de dato) = application/json
    respuesta = Response(response=myjson,
                         status=200, 
                         mimetype='application/json'
                         )
    # retornar la respuesta creada 
    return respuesta


if __name__ == '__main__':
    app.run()