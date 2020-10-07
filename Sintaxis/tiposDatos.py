# Comentario una linea
''' 
  Comentario multi linea 
  <3 
''' 

'''
Tipos de datos :
  1- Integer, int enteros
  2- Float, decimal
  3- boolean binario
  4- Character, char , caracter 
  5- String 
'''

print(" Int Entero ")

# 1 Integer int

num1 = 5
num2 = -2

# suma

num3 = num1 + num2 
print(str(num1)+"+"+str(num2)+"="+str(num3))

# Resta 

num3 = num1 - num2 
print(str(num1)+"-"+str(num2)+"="+str(num3))

# Multiplicacion 
num3 = num1 * num2 
print(str(num1)+"*"+str(num2)+"="+str(num3))

# Division 
num3 = num1 / num2 
print(str(num1)+"/"+str(num2)+"="+str(num3))

# Division entera  
num3 = num1 // num2 
print(str(num1)+"//"+str(num2)+"="+str(num3))

# Potencia 
num3 = num1**3
print(str(num1)+"**3 ="+str(num3))

# Raiz 
num3 = num1**.5
print(str(num1)+"**.5 ="+str(num3))


print("Float")
# 2 Float decimal

dec1 = 10.0
dec2 = .5

# Multiplicacion

dec3 = dec1*dec2

print(str(dec1)+"*"+str(dec2)+"="+str(dec3))

# Binario 

verdadero = True
falso = False 

print("Verdadero",verdadero)

print("Falso",falso)

# 4 Caracter

print("Char")

chr = 'a'
print(type(chr))

print("String")

str1 = 'primer'
str2 = """
      hola
      mundo
      """

'''
  Operaciones String
  1) concatenacion c=ab
  3) repeticion c = aaa
  4) longitud
  5) Obtener caracter
   
'''

str3 = str1+str2

print("Concatenacion", str3)


str3 = str1*2

print("repeticion", str3)

l = len(str1)
print(l)


str3 = str1[0]
print("Indice 0",str3)


# convertir tipos de datos
# obtener tipo de delato
print("tipo de dato "+str(type(num1)))
# Float a int 
num3 = int(dec1)
print("float a int "+str(num3))

# bool a int

num3 = int(verdadero)
print("bool a int "+str(num3))

num3 = verdadero+verdadero
print("verdadero "+str(num3))

num3 = int('55')
print("string a int "+ str(num3))







