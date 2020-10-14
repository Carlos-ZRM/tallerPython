# Definir listas
Las listas pueden tener cualquier tipo de dato 

lista = [1, "lista",[0], 10.0]

## acceder a elementos de una lista 
Los elementos de la lista son numerados desde el cero. 

# primer elemento
print(lista[0])
# segundo elemento
print(lista[0])
# Ultimo elemento 
print(lista[-1])

# Obtener longitud de la lista

lon = len(lista)


# podemos hacer lista a partir de numeros consecutos desde el cero. 

# lista desde el cero hasta el 9 
lista = list(range(9))

print(lista)




Tambien podemos obtener un segmento de la lista. Debemos indicar el primer elemento , el ultimo elemento

sublista = lista[2:5]

# sublista desde el primer elemento hasta un elemento 
## lista desde el cero hasta el indice 5
sublista = lista[:5]
print(sublista)
# sublista desde un elemento hasta el ultimo elemento 
## lista desde el cinco hasta el ultimo
sublista = lista[5:]
print(sublista)

## obtener lista cada dos elementos 
sublista = lista[::2]

## obtener la lista invertida 

sublista = lista[::-1]


