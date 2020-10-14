def palindromo(palabra):
  # indice inicial e indice final
  i = 0 
  # len devuelve el numero de letras de la palabra
  # restamos -1 porque las letras se empiezan a contar desde 0

  j = len(palabra) - 1

  # la palabra es palindroma al menos que encontremos un caso que no lo sea. 
  resultado  = True 
  # recorremos siempre que los indices sean diferentes
  while i < j :

    if palabra[i] != palabra[j] and resultado :
      # No es palindromo 
      resultado = False
    i = i + 1
    j = j - 1 
  
  return resultado 

palabra ="anna"
res = palindromo(palabra)
if res: 
  print("es palindromo")
else: 
  print("no es palindromo")