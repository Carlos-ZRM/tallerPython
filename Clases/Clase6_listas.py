import random

# lista vacia 
lista = []

# crear lista con elementos
lista = [10, 0.0, 'str1', "str2"]

# Primer elemento de mi lista
primero = lista[0]
## len(lista) -> numero de elementos de la lista 
# ultimo elemento de la lista
ultimo = lista[len(lista)-1]
# imprimir elementos 
#print("ultimo : ", ultimo, "primero-> \n", primero)
#print(lista)

# recorrer listas 
#  recorrer lista en C++ o Java 
## for ( int i = 0 ; i<= lista.length()-1 ; i++ )
for elemento in lista : 
  
  print('elemento',elemento)
#print("elemento fuera del for ")

# range normal 
rango = range(10)
#print(list(rango))
rango2 = range(0,20,2)
#print(list(rango2))
rango3 =range(25,-5, -5)
print(list(rango3))
## diccionarios 
# Diccionario { llave: valor }



aleatorios = []
# diccionario {llave(numero):numero de apariciones}
# {1:10, 5:3}
histograma = {}

# lista = range(100) -> [0,1,2...99]
for i in range(10):
  # para agregar elementos a una lista 
  # append( nuevo_elemento)
  aleatorios.append(random.randint(0, 3) )

print(aleatorios)

for numero in aleatorios: 
  # 1) verificar si el numero esta en el diccionario 
  if numero in histograma:
    # 1.1 acceder al elemento 
    # diccionario[<llave>] -> d[0]
    nuevo = histograma[numero] + 1
    # 1.2 asignarle el nuevo valor 
    histograma[numero] = nuevo
  else: 
    histograma[numero] = 1

print(histograma)



