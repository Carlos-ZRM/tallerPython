arbol = {
  0:["Volar", [1,2] ],
  1:["Marmota", [] ] ,
  2:["Pelikano",[] ],
  }
arbol =  {0: ['Volar', [1, 2]], 1: ['ladrar ', [7, 8]], 2: ['comer mamiferos ', [3, 4]], 3: ['Marmota', []], 4: ['raton', []], 5: ['halcon', []], 6: ['aguila', []], 7: ['es un reptil', [9, 10]], 8: ['perro', []], 9: ['maulla ', [11, 12]], 10: ['cocodrilo', []], 11: ['ruge ', [13, 14]], 12: ['gato', []], 13: ['es terrestre', [3, 4]], 14: ['leon', []]}

numero_max = 2
def agregar(numero_nodo, animal, caracteristica ):
  nodo_raiz = arbol[numero_nodo]
  animal_original = nodo_raiz[0]
  # crear nodo izquierdo 
  global numero_max 
  # 2 +1 
  numero_max = numero_max + 1
  # numero_nodo_I = 3 
  numero_nodo_I = numero_max
  nodo_izq = [ animal_original , [] ]
  # agregar nodo al arbol
  arbol[numero_nodo_I] = nodo_izq
  # crear nodo derecho 
  nodo_der = [ animal , [] ]
  # numero_max = 3 +1 
  numero_max = numero_max + 1
  #numero_nodo_D = 4 
  numero_nodo_D = numero_max
  #Agregar nodo 4 al arbol 

  arbol[numero_nodo_D] = nodo_der

  # nuevo_nodo = [ "es mamifero", [3,4] ]
  nuevo_nodo = [ caracteristica , [ numero_nodo_I, numero_nodo_D  ]  ]
  # sobre escribiendo el nodo 2 
  arbol[numero_nodo] = nuevo_nodo


def jugar ():
  
  numero_nodo = 0 
  while True:
    continuar = True
    numero_nodo = 0 
    # Evaluamos siempre un nodo
    while continuar:
      # 1 obtener informacion
      nodo = arbol[numero_nodo]
      frase = nodo[0]
      hijos = nodo[1]
      # 2 Verificar si es nodo u hoja
      if len(hijos) > 0 :
        #3.1 Imprimer pregunta
        print("¿ Su animal puede "+ frase+ " ?" ) 
        #print("")
        res = input('n) no \n s) si\n')
        
        if res == "n":
          numero_nodo = hijos[0]
        else:
          numero_nodo = hijos[1]
      else:

        print("El animal que penso es : \n" , frase )
        print('n) no \n s) Si')
        res = input()
        if res == 's':
          print("Fin del juego")
          
        else:
          print("¿Que animal pensaste?")
          animal = input()
          print('Agregue una caracteristica que su animal SI  tenga y que el '+ frase + 'NO tenga ')
          caracteristica = input()
          agregar(numero_nodo, animal, caracteristica )

        print("arbol", arbol )
        continuar = False


jugar()