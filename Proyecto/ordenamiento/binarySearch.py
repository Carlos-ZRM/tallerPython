import random

def binarySort(list, element):
  pass
def binarySearch(list_a, element, left ,  right):
  print(left, " : ", right)
  # stop recirsion 
  if left == right or  right -1 == left or right < left :
    # check list[left] element
    if list_a[left] == element:
      return left
    else :
      return -1
  #check center element 
  center = (right - left)//2
  center = left + center
  # stop recursion if center = right

  if list_a[center] == element:
    return center
  elif  element < center:
    return binarySearch(list_a, element, left, center)
  else:
    return binarySearch(list_a, element, center, right)

lista = list(range(-15,15,3))
print(lista)

i = binarySearch(lista[::], 6 , 0 , len(lista)-1 )
print(i,"i")
