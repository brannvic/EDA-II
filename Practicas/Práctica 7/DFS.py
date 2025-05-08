class Vertice: 
    def __init__(self, n): 
        self.nombre = n 
        self.vecinos = list() 
        
        self.d = 0 
        self.f = 0 
        self.color = 'white' 
        self.pred = -1 
    
    def agregarVecino(self, v): 
        if v not in self.vecinos: 
            self.vecinos.append(v) 
            self.vecinos.sort() 
            
class Grafo: 
    vertices = {} 
    tiempo = 0 
    
    def agregarVertice(self, vertice): 
        if isinstance(vertice, Vertice) and vertice.nombre not in self.vertices: 
            self.vertices[vertice.nombre] = vertice 
            return True 
        else: 
            return False 
            
    def agregarArista(self, u, v): 
        if u in self.vertices and v in self.vertices:
             for key, value in self.vertices.items(): 
                if key == u: 
                    value.agregarVecino(v) 
                if key == v: 
                    value.agregarVecino(u) 
            return True 
        else: 
            return False 
    
    def imprimeGrafo(self): 
        print("- RECORRIDO BFS: GRAFO 8 -\n") 
        for key in sorted(list(self.vertices.keys())): 
            print("\nVertice: " + key) 
            print("Descubrimiento/Termino: " + str(self.vertices[key].d)+"/"+str(self.vertices[key].f)) 
            
    def dfs(self, vert): 
        global tiempo 
        tiempo = 0 
        for u in sorted(list(self.vertices.keys())): 
            if self.vertices[u].color == 'white': 
                self.dfsVisitar(self.vertices[u]) 
                
    def dfsVisitar(self, vert): 
        global tiempo 
        tiempo = tiempo+1 
        vert.d = tiempo 
        vert.color = 'gris' 
        for v in vert.vecinos: 
            if self.vertices[v].color == 'white': 
                self.vertices[v].pred = vert 
                self.dfsVisitar(self.vertices[v]) 
            vert.color='black' 
            tiempo = tiempo+1 
            vert.f = tiempo 
            
class Controladora: 
    def main(self): 
        g = Grafo() a = Vertice('A') 
        g.agregarVertice(a) 
        for i in range(ord('A'), ord('L') + 1): 
            g.agregarVertice(Vertice(chr(i))) 
            edges = ['AB', 'AD', 'BC', 'BD', 'CD'] 
            for edge in edges: 
                g.agregarArista(edge[:1], edge[1:]) 
            for i in range(ord('A'), ord('L') + 1): 
                g.dfs(Vertice(chr(i))) 
                g.imprimeGrafo() 
                
obj = Controladora() 
obj.main()