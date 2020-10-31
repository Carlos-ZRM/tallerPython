from insertionSort import insertionSort
import random 

def create_bucket(list_a, buckets=2 ):
  dict = {}
  sort_l = []
  min_v = min(list_a)
  max_v = max(list_a)
  #if buckets > max_v :
  #  buckets = max_v
  scale = (max_v - min_v)//buckets
  if scale == 0:
    scale = 1
  for element in list_a:
    # get bucket
    i_bucket = element // scale

    if i_bucket not in dict :
      dict[i_bucket] = [element]
    else :
      insertionSort(dict[i_bucket], element)
  print("dict :: ",dict)

  for key in range(min_v // scale, (max_v //scale)+1):

    if key in dict:
      list_b = dict[key]
      sort_l = sort_l + (list_b)
  

  
  return sort_l 

lista = [random.randint(-60,0) for r in range(15) ]
s_l = create_bucket(lista, 7 )

print("sorted", s_l)
