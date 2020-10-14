# Tipos de datos 
"""
1- Tipos de datos
  - int (integer entero )
  - float (decimal)
  - boolean (boleano, logico )
    0 False 1 True
  - string (cadenas de texto)
  Operaciones : 
    suma +
    resta -
    multiplicacion *
    division /
    potencias a**2
    raices a**.5
2 Funciones
  def miFuncion():
    pasos de la fuuncion
    return variable


"""

def saludar(nombre, apellido):
  print("Hola "+nombre+apellido)

def division(numerador, denominador):
  # manejo errores 
  if denominador == 0:
    return "Error"
  # definicion de variables
  resultado = 0.0
  # desarrollo de la funcion 
  resultado = numerador / denominador
  # regresar o retornar el valor obtenido
  return resultado 

def divisionEntera(numerador, denominador):
  resultado = 0
  resultado = numerador // denominador 
  return resultado

def multiplicacion(numero1, numero2):
  resultado = 0
  resultado = numero1 * numero2
  return resultado

def potencia(numero, potencia):
  resultado = 0 
  resultado = numero ** potencia
  return resultado 

def distanciaPuntos( x1,y1,x2,y2):
  resultado = 0.0
  resultado = (x1-x2)**2 +(y1-y2)**2
  resultado = resultado**.5
  return resultado 

a = 4
b = .5

r = potencia( a, b )

print("Resultado "+ str(r) )

x1 = 0
y1= 0 
x2 = 5
y2= 0

r = distanciaPuntos(x1,y1,x2,y2)
print("distancia  "+ str(r) )

#saludar("Carlos ", "Reyes ")




#saludar( 5, 10.0 )