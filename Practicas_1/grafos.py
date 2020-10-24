import networkx as nx
import matplotlib.pyplot as plt
from networkx.drawing.nx_agraph import write_dot, graphviz_layout



#Vanilla call= 1
#vanilla put = 2
#call digital= 3
#put digital = 4
import math




def subyacente(S0, u=1.1, d=0.5, n=1):
  grafo = {}
  # variable auxiliar para contar nodos

  nodo = 1
  # agregamos el primer elemento
  grafo[0]=[S0,[1,2],0]
  # primer for recorrera N los niveles
  # N_i -> i 
  for i in range (1,n+1):
    # variable para las derivadas 
    for j in range (0,i+1):
      valor = S0*u**(j)*d**(i-j)
      # calcular grafo 
      inf = nodo + i + 1 
      sup = nodo + i +2 
      grafo[nodo]=[valor, [inf,sup],i]
      # aumneta el contador de nodos
      nodo = nodo + 1

  return grafo

def derivado(grafo,opcion,k=0,p=0,t=0,r =1, n=1, u =1, d=.5):
  grafo_eval = {}
  # recorremos el grafo 
  for indice in grafo:
    # obtenemos el nodo / elemento de un diccionario 
    #  nodo = [valor, [sup, inf] ]

    nodo = grafo[indice]
    
    # verificamos si es hoja.
    # es hoja si su produccion no esta en el diccionario 
    # produccion 
    # accedemmos a superior
    prod = nodo[1][0]
    # accedemos al inferio 
    #   prod = nodo[1][1]
    # acceder al valor 
    # prod =nodo[0]

    # vara verificar si un elemento esta en el k, pdiccionario

    if prod in grafo:
      # si esta la produccion en el diccionario es nodo
      #valor = funcion_nodo(nodo,grafo, u, d, r , t, n)
      valor = 0 
    else :
      valor = funcion_hoja(nodo, opcion, k, p )
    # copia del nodo ( copiar listas)
    nodo_eval = nodo[:] 
    # actualizamos los valores en el grafo evaluado 
    nodo_eval[0]=valor
    # agregamos el nodo (lista) al grafo evaluado 
    grafo_eval[indice]=nodo_eval
  
  for nivel in range( n-1,-1,-1):
    # recorrer todo el grafo
    for indice in grafo_eval:
      nodo_eval = grafo_eval[indice]
      # si el nodo es del nivel visitado 
      #print(nodo_eval[2], nivel)
      if nodo_eval[2]==nivel:
        valor = funcion_nodo(nodo_eval,grafo_eval, u, d, r , t, n)
        nodo_eval[0]=valor
        grafo_eval[indice]=nodo_eval



      

  return grafo_eval
  
def alpha(subyacente, derivado,n):
  grafo_alpha = {}
  for indice in subyacente: 
    # recorremos subyacente para guiarnos
    nodo_sub = subyacente[indice]
    # verifico si el nivel no es el ultimo (hojas)
    if nodo_sub[2] < n:

      nodo_alpha = nodo_sub[:]
      # obtener produciones de nodo_alpha
      llave_inf = nodo_alpha[1][0]
      llave_sup = nodo_alpha[1][1]
      #print(nodo_sub, llave_inf, llave_sup )

      # buscamos der_inf con la llave
      der_inf = derivado[llave_inf][0]
      der_sup =  derivado[llave_sup][0]
      subya_inf= subyacente[llave_inf][0]
      subya_sup = subyacente[llave_sup][0]
      valor = (der_sup - der_inf)/(subya_sup - subya_inf)
      nodo_alpha[0]=valor
      grafo_alpha[indice] = nodo_alpha
  
  return grafo_alpha
def beta(subyacente,derivado,alpha, r=1, t=1, n=1):
  
  a = math.e 
  z= t/n
  b = a**((-1)*r*z)
  grafo_beta = {}
  for indice in subyacente: 
    # recorremos subyacente para guiarnos
    nodo_sub = subyacente[indice]
    # verifico si el nivel no es el ultimo (hojas)
    if nodo_sub[2] < n:
      nodo_beta = nodo_sub[:]
      # obtener produciones de nodo_alpha
      llave_inf = nodo_beta[1][0]
      llave_sup = nodo_beta[1][1]

      der_inf = derivado[llave_inf][0]
      der_sup =  derivado[llave_sup][0]
      subya_inf= subyacente[llave_inf][0]
      subya_sup = subyacente[llave_sup][0]
      #alpha_inf = alpha[llave_inf][0]
      #alpha_sup = alpha[llave_sup[0]]
      valor =b*(der_sup-(subya_sup)*((der_sup - der_inf)/(subya_sup - subya_inf)))
      nodo_beta[2] = valor
      grafo_beta[indice] = nodo_beta
  
  return grafo_beta


def funcion_nodo(nodo,grafo, u=1.1, d=.8, r =.045, t=2, n=5):

  llave_inf = nodo[1][0]
  x_inf = grafo[llave_inf][0]
  llave_sup = nodo[1][1]
  x_sup = grafo[llave_sup][0]
  a = math.e 
  z= t/n
  b =a**((-1)*r*z)
  #print(a)
  q = ((b**(-1))-d)/(u-d)
  #print("type",type(b), type(a), type(q), type(x_inf), type(x_sup))
  resultado = b
  resultado =  b*(q*x_sup + (1-q)*x_inf)
  return resultado 
def funcion_hoja(hoja, opcion, k =0, p=0 ):
  resultado = 0.0
  
  if opcion == 1:
    resultado = max(hoja[0]-k,0)

  elif opcion== 2 :
    resultado = max(k-hoja[0],0)
  
  elif opcion == 3:
    if hoja[0]>k:
      resultado = p
    else:
      resultado = 0
  elif opcion == 4:
    if k>hoja[0] :
      resultado = 0
    else :
      resultado = p
   

  return resultado

def plot_grafo(grafo, nombre='grafo.png', color='red'):
  G = nx.Graph()
  for nodo in grafo:
    val = round(grafo[nodo][0],2)
    val = str(nodo)+"="+str(val)
    G.add_node(str(nodo),val=val )  
  
    # crear un grafo
  for indice in grafo:
    hijos = grafo[indice][1]
    # inf 
    inf = hijos[0]
    sup = hijos[1]

    # si el inf esta en el arbo
    if inf in grafo:
      G.add_edge(str(indice),str(inf))
    """  
    else :
      G.add_node(str(inf))
      G.add_edge(str(indice),str(inf))
    """ 
    if sup in grafo:
      G.add_edge(str(indice),str(sup))
  
  #pos = graphviz_layout(G, prog="circo")  
  labels = nx.get_node_attributes(G, 'val') 
  pos = graphviz_layout(G, prog="twopi", args="")

  nx.draw(G, pos=pos, labels=labels, node_color=color, with_labels = True, node_size=600)
  
  nx.draw(G, labels=labels, node_color=color, with_labels = True, node_size=600)
  
  plt.savefig(nombre)

  #plt.show()



opcion = 1
S0 = 100
u = 1.2
d = 0.8
t = 2
n= 5
r = 0.045
k = 100

grafo_subya = subyacente(S0,u = u, d=d, n=n)
#print(x)
grafo_deri = derivado(grafo_subya, opcion, k = k, t=t, r = r, n=n , u=u, d=d )

grafo_alpha = alpha(grafo_subya,grafo_deri, n=n)
grafo_beta = beta(grafo_subya, grafo_deri,grafo_alpha ,r=r,t=t,n=n)

plot_subya = plot_grafo(grafo_subya,nombre="subyacente.png")
plot_deri = plot_grafo(grafo_deri,nombre="deri.png")
plot_alpha = plot_grafo(grafo_alpha,nombre="alpha.png")
plot_beta = plot_grafo(grafo_beta, nombre="beta.png")

print("++****+\n\n ")


print("grafo_subya",grafo_subya)
print()
print("grafo_deri",grafo_deri)
print()
print("grafp_alpha",grafo_alpha)
print()
print("grafp_beta",grafo_beta)

