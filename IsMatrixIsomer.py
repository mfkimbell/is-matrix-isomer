import itertools


class Graph(object):
    

    # Initialize the matrix
    def __init__(self, size):
        self.adjMatrix = []
        self.connect = []
        self.perms=[]
        self.matrices=[]
        for i in range(size):
            self.adjMatrix.append([0 for i in range(size)])
        self.size = size

    # Add edges
    def add_edge(self, v1, v2):
        if v1 == v2:
            self.adjMatrix[v2][v1] += 1
            self.adjMatrix[v1][v2] = self.adjMatrix[v2][v1]
        else:
            self.adjMatrix[v2][v1] += 1
            self.adjMatrix[v1][v2] += 1
        self.connect.append([v1,v2])

    # Remove edges
    def remove_edge(self, v1, v2):
        if self.adjMatrix[v1][v2] == 0:
            #print("No edge between %d and %d" % (v1, v2))
            return
        self.adjMatrix[v1][v2] = 0
        self.adjMatrix[v2][v1] = 0

    def __len__(self):
        return self.size

    # Print the matrix
    def print_matrix(self):
        for row in self.adjMatrix:
            print(row)
    
    def print_matrix_list(self):
        for matrix in self.matrices:
            for row in matrix:
                print(row)
            print()
    
    def create_permutations(self,g):
        size=g.size
        vertices=[]
        for num in range(size):
            vertices.append(str(num))
        self.perms = list(itertools.permutations(vertices))
    
    def create_all_matrices(self):
        def add_edge(v1, v2,list):
            if v1 == v2:
                list[v2][v1] += 1
                list[v1][v2] = list[v2][v1]
            else:
                list[v1][v2] += 1
                list[v2][v1] += 1
            
        
        size=self.size
        for perm in self.perms:
            adjMatrix = []
            for i in range(size):
                adjMatrix.append([0 for i in range(size)])
            for x in range(len(self.connect)):
                add_edge(perm.index(str((self.connect[x][0]))),perm.index(str((self.connect[x][1]))),adjMatrix)
                
            self.matrices.append(adjMatrix)
        
    def compare_matrices(self,graph2):
        result=0
        for matrix in self.matrices:
            if matrix==graph2.adjMatrix:
                result+=1
        print(f"These two graphs have {result} isomers")
            

        
   





def main():
    #creating the empty matrix:
    #create graph by entering its size
    #size would be one of its dimensions(5x5 = Size 5)
    #therefore, you would write graph1 = Graph(5)
    graph1 = Graph(3) 
    
    #connecting vertices:
    #the vertices are named by numbers in order
    #a graph of size 5 would have vertices (0,1,2,3,4)
    #to connect two vertices, .add_egdge(vertice1,vertice2)
    graph1.add_edge(0, 2)
    graph1.add_edge(0, 2)
    graph1.add_edge(1,1)

    #this will create all permutations of vertices
    graph1.create_permutations(graph1)
    #this will create all matrices with those permuations
    graph1.create_all_matrices()
    #this will print those matrices (but i have it commented out)
    print("These are the adjacency matrix isomers of graph 1:")
    graph1.print_matrix_list()
    

    #create the second graph here
    #must be at least the same size as graph 1 for isomorphism
    graph2 = Graph(3)
    graph2.add_edge(0, 0)
    graph2.add_edge(1,2)
    graph2.add_edge(1,2)
    print("This is the adjacency matrix of graph2:")
    graph2.print_matrix()
    print()
    
    #this function will check if any graph1's isomers match graph2
    graph1.compare_matrices(graph2)
    print()
    
    

    
    


if __name__ == '__main__':
    main()