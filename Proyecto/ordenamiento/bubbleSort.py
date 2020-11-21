import random 
def bubbleSort(list_a):
  # set i and j 
  i = 0 
  j = 0 
  while i < len(list_a):
    j = i
    bubble = list_a[i]
    while j < len(list_a):
      n_bubble = list_a[j]
      # swap if n_bubble is lees than bubble
      if bubble > n_bubble:
        swap = n_bubble
        list_a[j] = bubble
        list_a[i] = swap
      j = j + 1
    i = i + 1


lista = [random.randint(-30,-1) for r in range(15) ]
print("lista", lista)
bubbleSort(lista)
print("lista_0", lista)
