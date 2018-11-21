#import pygame 
import numpy as np 


'''
coordenada = (x,y,z)
'''
class coordenada():
    def __init__(self, x,y,z):
        self.x = x
        self.y = y
        self.z = z

'''
AKA: point, node
'''
class Punto():
    def __init__(self, coordenada):
        self.punto = np.array(coordenada)
'''
AKA: edge
'''
class Arista():
    def __init__(self, (inicio, fin)):
        self.arista = np.array([inicio,fin]) 
        pass
    pass

'''
AKA : wireframe
'''
class Estructura():
    def __init__(self):
        self.puntos = []
        self.aristas = []

    def addNode(self, node):
        #node = np.array(node)
        self.puntos.append(node)

    def addEdge(self, edge):
        self.aristas.append(edge)

    def getNodes(self):
        return self.puntos

    def getEdges(self):
        return self.aristas
    pass

mi_estructura = Estructura()
#mi_estructura.addNode([1,2,3])
mi_estructura.addNode([0,0,0])
mi_estructura.addNode([0,0,1])
mi_estructura.addNode([0,1,0])
mi_estructura.addNode([1,0,0])
mi_estructura.addNode([0,1,1])
mi_estructura.addNode([1,1,1])
mi_estructura.addNode([1,0,1])
mi_estructura.addNode([1,1,0])

#mi_estructura.addEdge([1,2])
#mi_estructura.addEdge([3,4])
for n in range(0,4):
    mi_estructura.addEdge([n,n+4])
    
m = 0
for n in range(0,4):
    mi_estructura.addEdge([m,m+1])
    m += 2

#np.set_printoptions(threshold='nan')
print ((mi_estructura.puntos)) 
print ((mi_estructura.aristas))