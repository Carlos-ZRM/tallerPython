import numpy as np

todas_peliculas = {
    "v1": np.array([1, 2]),
    "v2": np.array([2, 1]),
    "v3": np.array([3, 3]),
}

def centroides_aleatorios(dic_espacio, k_clases):
    # obtener la lista de llaves ( el nombre de todas las peliculas)
    lista_llaves = dic_espacio.keys()
    # Aleatorio entre el nombre de todas las peliculas 
    #aleatorio1 = randint(0, len(lista_llaves) - 1)
    #0 1
    centroide1 = dic_espacio["v1"]
    centroide2 = dic_espacio["v2"]
    lista_clase  = [
      {"nombre":"Clase 1", "elementos":[], "centro":centroide1},
      {"nombre":"Clase 2", "elementos":[], "centro":centroide2}
    ]
    return lista_clase

    # 0, 1, 2
def clasificacion(lista_clase, todas_peliculas):
    #1 ) Calcula distancia a cada centroides
    #2 ) Elegir clase a partir de la distancias mas corta
    # regresa/actualiza las clases
    # funcion entre dos vectores
    pass

# centroide= [3.3, 5, 3] vector = [1,0,1] 
def distancia(centroide, vector):
  
  suma = 0.0
  for i in range( len(centroide) ):
      # i = 0 , i = 1, i= 2:
      # x1 = 3.3 x2 = 1
    x1 = centroide[i]
    x2 = vector[i]
    s = (x1 - x2)**2
    suma = suma + s
  suma = suma ** (1/2)
  return suma 

#def suma (va, vb):
#  suma = []
#  if len(va)== 0:
#    return vb
#  else: 

def calcular_centroide(clase):
    # definimos el promedio de las entradas de cada clase.
    # recorremos la lista de las clases
    elementos = clase['elementos']
    c = np.array()
    k = 0 
    for vector in elementos:
      # obtenemos el vector 
      v = todas_peliculas[vector]
      c = c + v
      k = k + 1
    c = c/k



