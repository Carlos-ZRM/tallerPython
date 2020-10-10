from PIL import Image
def crearLista(matriz,tamanio):
  lista = []
  for i in range(tamanio[0]):
    for j in range(tamanio[1]):
      lista.append(matriz[i][j])
  return lista 
def crearMatriz(lista, tamanio):
  matriz = []
  k = 0
  for i in range(tamanio[0]):
    fila = []
    for j in range(tamanio[1]):
      fila.append(lista[k])
      k = k + 1
    matriz.append(fila)
  return matriz 

def promedio(matriz,matrizDestino, tamanio , cuadro ):
  for i in range(0 ,tamanio[0],cuadro):
    for j in range(0,tamanio[1], cuadro):
      sumaCuadro(matriz,matrizDestino,i,j,cuadro)

def compress(matriz, tamanio, comprimir):
  for i in range(0,tamanio[0],comprimir[0]):
    for j in range(tamanio[1],comprimir[1]):
      pass
def sumaCuadro (matriz, matrizDestino, x, y,  cuadro):
  sum_rojo = 0
  sum_verde = 0
  sum_azul = 0
  for i in range(x,cuadro+1):
    for j in range (y, cuadro+1):
      sum_rojo = sum_rojo + matriz[i][j][0]
      sum_verde = sum_verde + matriz[i][j][1]
      sum_azul = sum_azul + matriz[i][j][2]
  sum_rojo = sum_rojo//(cuadro*2)
  sum_verde = sum_verde//(cuadro*2)
  sum_azul = sum_azul // (cuadro*2)
  for i in range(x,cuadro+1):
    for j in range (y, cuadro+1):
      matrizDestino[i][j] = (sum_rojo, sum_verde, sum_azul,matriz[i][j][3])

img = Image.open("crash.png")
#width, height = img.size
tamanio = img.size
mode = img.mode 
data = img.getdata()
data = list(data)
img2 = Image.new(size=tamanio, mode=mode)

print(mode)
print(type(data),list(data)[4000])
datos2 = [(55,55,55,1)]*len(data)

matrizData = crearMatriz(data,tamanio)
matrizDestino = crearMatriz(datos2,tamanio)

promedio(matrizData,matrizDestino,tamanio,8)

lista = crearLista(matrizDestino,tamanio)
print(type(lista))


img2.putdata(lista)
img2.save("nuevo.png")
print(len(datos2))