# hay dos formas de crear string commilas simples comilla sencilla
nombre = "francisco"
nombre2 = 'hazel' 
# cuando estamos haciendo una string es parecido a tener una lista inmutable
lista = ['c','a', 'r', 'l', '0']
# cuando se crea un caracter chr() se crea una lista con un solo elemento

# car =  ['a']

nombre = 'ana'
# funcion cifrar < - 25 >
llave = 25
# funcion decifrar < +25 >


 
palabra_cifrada = ""
palabra_descifrada = ""
print("//////////******************")

# letra = 'a'
# letra = 'n'
# letra = 'a'


# for elemento_i in <nombre_lista>:
for letra in nombre: 
  # valor numerico de la letra
  # <<ord>> transformar letra a ascii 
  # valor_ascii tipo entero
  # 'a' -> 97  
  valor_ascii = ord(letra)
  
  # para cifrarlo necesitamos una funcion suma/resta
  # valor_ascii = valor_ascii - llave 
  # valor_ascii = 97 + llave (1) -> 98
  valor_ascii += llave
  # funcion <<chr>> transforma ascii a letra (caracter)
  # chr recibira una variable tipo int y regresara una variable string
  letra_cifrada = chr(valor_ascii)
  #print("Letra cifrada",letra, valor_ascii,letra_cifrada )
  #print("*****")
  # concatenar palabras 'b',  -> 'bo' -> 'bob'  
  palabra_cifrada = palabra_cifrada + letra_cifrada


for letra in palabra_cifrada:
  # transformar letra cifrada en numero
  # valor_ascii es una variable de tipo int 
  valor_ascii = ord(letra)
  # b = 98
  #print("letra cifrada",valor_ascii, chr(valor_ascii) )
  #valor_ascii = ord ("b") -> 98

  # decifrar la letra. << suma cifrar mensaje>> 
  # valor_ascii = valor_ascii - llave -> 98-1=97 
  valor_ascii = valor_ascii - llave
  #print("letra cifrada",valor_ascii, chr(valor_ascii) )
  
  # valor entero a caracter/letra /texto 
  # funcion chr recibir variable int regresar una variable string
  letra_decifrada = chr(valor_ascii)
  #letra_decifrada = chr(97) -> 'a'
  # (98-1) -> a , (111-1) -> n , (98-1) -> a 
  palabra_descifrada = palabra_descifrada + letra_decifrada
  

print("palabra cifrada", palabra_cifrada)
print("palabra descifrada", palabra_descifrada)
