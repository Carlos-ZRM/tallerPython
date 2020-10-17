nombre = "francisco"
# funcion cifrar < - 25 >
llave = 25
# funcion decifrar < +25 >


# for <elementos> in <nombre_lista>: 
palabra_cifrada = ""
palabra_descifrada = ""
print("//////////******************")
for letra in nombre: 
  # valor numerico de la letra
  # <<ord>> transformar letra a ascii 
  valor_ascii = ord(letra)
  #print("Letra sin cifrar", letra, valor_ascii)
  # funcion suma/resta
  # valor_ascii = valor_ascii - llave 
  valor_ascii -= llave
  # funcion <<chr>> transforma ascii a letra (caracter)
  letra_cifrada = chr(valor_ascii)
  #print("Letra cifrada",letra, valor_ascii,letra_cifrada )
  #print("*****")
  palabra_cifrada = palabra_cifrada + letra_cifrada


for letra in palabra_cifrada:
  # transformar letra cifrada en numero
  # int 
  
  valor_ascii = ord(letra)
  print("letra cifrada",valor_ascii, chr(valor_ascii) )
  #valor_ascii = ord ("b") -> 98

  # decifrar la letra. << suma cifrar mensaje>> 
  # valor_ascii = valor_ascii - llave -> 98-1=97 
  valor_ascii = valor_ascii + llave
  print("letra cifrada",valor_ascii, chr(valor_ascii) )
  
  # valor entero a caracter/letra /texto 
  letra_decifrada = chr(valor_ascii)
  #letra_decifrada = chr(97) -> a
  palabra_descifrada = palabra_descifrada + letra_decifrada
  

print("palabra cifrada", palabra_cifrada)
print("palabra descifrada", palabra_descifrada)
