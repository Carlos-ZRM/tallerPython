from PIL import Image

def imprimirImg(data, tamanio):
  k = 0 
  file = open("ascii.txt","w+")
  for i in range(tamanio[0]):
    linea = ""
    for j in range(tamanio[0]):
      ascii = chr(data[k][0]+32)
      linea = linea+ascii
      k = k + 1 
    file.write(linea)


img = Image.open('crash.png').convert('LA')
img = img.resize((100,100)) 

data = img.getdata()
data = list(data)
#print(data)
imprimirImg(data, img.size)
img.save('greyscale.png')