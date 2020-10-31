import random
def insertionSort(list_a,element):
  flag  = False
  if len(list_a) == 0:
    list_a.insert(0 , element)
    return 
  i = 0
  
  while(i < len(list_a) ):
    if element <= list_a[i]:
      list_a.insert(i, element)
      flag = True
      break
    i = i + 1 
  if not flag :
    list_a.insert(len(list_a)  , element)

"""
lista_o = []
lista = [random.randint(-5,7) for r in range(15) ]
for i in lista:
  insertionSort(lista_o, i)
for i in range(25): 
  insertionSort(lista_o, i)

print("lista->",lista)
print("lista_oo->",lista_o)
"""