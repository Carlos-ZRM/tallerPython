dic_usuario = {}
num_ascii = 7

def cifrar(contrasenia):
  cifrada = ""
  '''
  1) Recorremos el string, obteniendo el asscii de cada letra. 
  2) Ciframos cada letra aumentando el valor de su ascii 
  3) regresamos la contrasenia cifrada
  ''' 
  for letra in contrasenia:
    ascii = ord(letra)
    ascii += num_ascii
    letra_ascii = chr(ascii)
    cifrada = cifrada + letra_ascii
  print(cifrada)
  return cifrada

def decifrar():
  pass

def agregarUsuario(usuario, contrasenia ):
  '''
  1. Verificar si el usuario ya existe 
     1.1 Si existe devuelve un error 
  2. Cifrar la contrasenia
  3. agrega el usuario 
  4. devuelve el mensaje de agregado correctamente. 
  '''
  # 1) verificr usuario 
  if  usuario in dic_usuario:
    # 1.1 el usuario ya existe 
    return "Error. El usuario ya existe"
  #2 )  cifrar contrasenia
  con_cifrada = cifrar(contrasenia)
  # 3 ) agregar usuario 
  dic_usuario[usuario]= con_cifrada
  # regresar el valor 
  return "Exito. Usuario "+usuario+" agregado"
  

def eliminarUsuario():
  pass
def modificarUsuario():
  pass
def validarContrasena(usuario, contrasenia):
  ''' 
  1) Verificamos si el usuario existe
    1.1) Si el usuario no existe regresamos mensaje de error
  2) Ciframos la contrasenia ingresada y comparamos con la contrasenia guardada 
  3) Si coinciden mandamos mensaje de Exito
  4) Si no regresamos mensjae de error  
  ''' 
  # 1) verificr usuario 
  if  usuario not in dic_usuario:
    # 1.1 el usuario ya existe 
    return "Error. El usuario no existe"
  con_ingresada = cifrar(contrasenia)
  # Imprimimos las contrasenias
  print(dic_usuario[usuario]+" : " + con_ingresada)
  if dic_usuario[usuario] == con_ingresada:
    return "Exito, las contraseñas coinciden"
  else :
    return "Contrasenia incorrecta"
    
# Creamos un usuario
print("Creamos un usuario")
mensaje = agregarUsuario("Carlos", "Carlos")
print(mensaje)
# Imprimimos los usarios totales 
print("Imprimimos los usarios totales ")
print(dic_usuario)

print(" Verificamos erroneamente un usuario")
mensaje = validarContrasena("Carlos","error")
print(mensaje)


print(" Verificamos correctamente un usuario")
mensaje = validarContrasena("Carlos","Carlos")
print(mensaje)