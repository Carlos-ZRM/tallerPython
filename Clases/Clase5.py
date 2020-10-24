# una linea 
"""
- numerico 
  - enteros (int)
  - decimales (float)
  - bool (True, False ) (bool)
- string 

numero = 5
decimal = 10.0

print(numero, type(numero))
print(decimal, type(decimal))

variable1 = float(numero)
print(variable1, type(variable1))
# float() int()
# type()
cadena1 = '10'
cadena2 = "5.5"

v = float(cadena2)
print(v, type(v))

num = 13.333
palabra = str(num)
print(palabra, type(palabra))

# crear diccionario limpio 
dic_correos = {}
# crear diccionario con elementos
dic_correos = {"carloszrm90@gmail.com":"carlos" , "correo@mail.com":"Hazel"}

# obtener un elemento del diccionario 
usuario = dic_correos['carloszrm90@gmail.com']

# crear un nuevo elemento del diccionario
dic_correos['correo3@gmail.com'] = 'yess'
dic_correos['llave1'] = 25.25

# actualizar un elemento del diccionario 
dic_correos['carloszrm90@gmail.com'] = "Reyes"

print(dic_correos)


"""

dic_gpos = {}
# llenar datos grupo python
dic_dias = {"lunes":"10-11","miercoles":"10-11","sabado":"11-13"}
dic_links = {"sabado":"ksksksks.com"}
asistentes = ['Francisco', 'monserrat']

# crear diccionario del grupo 
python = {'dias':dic_dias, 'links':dic_links, 'asistentes':asistentes}

# agregamos el diccionario python a los grupos
dic_gpos['python']= python
print(dic_gpos)



