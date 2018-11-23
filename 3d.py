import pygame 
import numpy as np 


'''
coordenada = (x,y,z)
not used 
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
mi_estructura.addNode([0,0,40])
mi_estructura.addNode([0,40,0])
mi_estructura.addNode([40,0,0])
mi_estructura.addNode([0,40,40])
mi_estructura.addNode([40,40,40])
mi_estructura.addNode([40,0,40])
mi_estructura.addNode([40,40,0])

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

class Proyeccion():
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((width,height))
        pygame.display.set_caption('estructura mostrando .. ')
        self.background =  (10,10,50)
        self.wireframe = {}
        self.displayNodes = True
        self.displayEdges = True
        self.nodeColor = (255,255,255)
        self.edgeColor = (122,211,111)
        self.nodeRadius = 4
        pass 

    def run(self):
        running =  True 
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            #pygame.display.flip()
            self.screen.fill(self.background)
            self.display()
            pygame.display.flip()
        pass

    def addEstructura(self, name, estructura):
        self.wireframe[name] = estructura
        pass 
    
    def display(self):
        self.screen.fill(self.background)
        for wireframe in self.wireframe.values():
            if self.displayEdges:
                for edge in wireframe.aristas:
                    pygame.draw.aaline(self.screen, self.edgeColor, (edge[0], edge[0]) ,(edge[1], edge[1]),1)
                
            if self.displayNodes:
                for node in wireframe.puntos:
                    pygame.draw.circle(self.screen, self.nodeColor, (int(node[0]), int(node[1])), self.nodeRadius, 0)


'''
todo : A better way to make a cube structure, no loops
'''


#if __name__ == "__main__":
pv = Proyeccion(400, 300)
pv.addEstructura('tmr',mi_estructura)
pv.run()


