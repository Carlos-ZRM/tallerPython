- 0 Comentario multilinea 
Tipos de datos :
- 1 Integer, int enteros
- 2 Float, decimal
-  3 boolean binario
-  4 Character, char , caracter 
-  5 String 
 
# 0. Comentario una linea
``` Python
''' 
  Comentario multi linea 
  <3 
'''
# Comenario una linea 
```
 
# 1 Integer int
``` Python

num1 = 5
num2 = -2
```


## suma
``` Python

num3 = num1 + num2 
print(str(num1)+"+"+str(num2)+"="+str(num3))
```

## Resta 

``` Python
num3 = num1 - num2 
print(str(num1)+"-"+str(num2)+"="+str(num3))
```

## Multiplicacion 
``` Python
num3 = num1 * num2 
print(str(num1)+"*"+str(num2)+"="+str(num3))
```

## Division 
``` Python
num3 = num1 / num2 
print(str(num1)+"/"+str(num2)+"="+str(num3))
```

## Division entera  
``` Python
num3 = num1 // num2 
print(str(num1)+"//"+str(num2)+"="+str(num3))
```

## Potencia 
``` Python
num3 = num1**3
print(str(num1)+"**3 ="+str(num3))
```

## Raiz 
``` Python
num3 = num1**.5
print(str(num1)+"**.5 ="+str(num3))
```


# 2 Float decimal
``` Python
dec1 = 9.0
dec2 = .55
```

## Multiplicacion
``` Python

dec3 = dec1*dec2

print(str(dec1)+"*"+str(dec2)+"="+str(dec3))
```

## redondear 
``` Python

round(dec3, 2)
```

# 3  Binario 
``` Python

verdadero = True
falso = False 

print("Verdadero",verdadero)

print("Falso",falso)
```

# 4 Caracter
``` Python

print("Char")

chr = 'a'
print(type(chr))
```

# 5 String palabra 

``` Python

str1 = 'primer'
str2 = """
      hola
      mundo
      """
```

#  Operaciones String
  - 1) concatenacion c=ab
  - 3) repeticion c = aaa
  4) longitud
  5) Obtener caracter
   

## Concatenar
``` Python

str3 = str1+str2

print("Concatenacion", str3)
```

## repeticion 
``` Python

str3 = str1*2

print("repeticion", str3)
## tamaño palabra 
l = len(str1)
print(l)
```

## elegir una letra
``` Python

str3 = str1[0]
print("Indice 0",str3)
```


# 6 convertir tipos de datos
## obtener tipo de delato
``` Python

print("tipo de dato "+str(type(num1)))
```

## Float a int 
``` Python

num3 = int(dec1)
print("float a int "+str(num3))
```

## bool a int
``` Python

num3 = int(verdadero)
print("bool a int "+str(num3))

num3 = verdadero+verdadero
print("verdadero "+str(num3))
```

## string a int 
``` Python
num3 = int('55')
print("string a int "+ str(num3))


```





