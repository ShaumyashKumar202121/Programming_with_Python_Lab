# Lab-8: Design a class for all the Graph traversal types (BFS, DFS)#
class Graph:
    def __init__(self,size) -> None:
        self.Nodesize = size # to track number of the nodes
        self.adjMatrix = [[0]*size for i in range(size)] 
    
    def getGraph(self):
        return self.adjMatrix
    
    def add_edge(self,edg1,edg2):
        if edg1 == edg2 :
            print(f"Same vertex {edg1} and {edg2}")
        self.adjMatrix[edg1][edg2] = 1  
        self.adjMatrix[edg2][edg1] = 1 

class Queue:
    def __init__(self,size = 5) -> None:  # default size of the queue is 5
        self.arr = [0] * size
        self.size = size
        self.front = 0
        self.rear = 0
        
    # utility functions :
    def isEmpty(self,queue):
        if queue.front == queue.rear :
            return 1
        return 0
    def isFull(self,queue):
        if queue.rear == queue.size - 1 :
            return 1
        return 0
    # member functions:
    def enqueue(self,queue,val):
        if self.isFull(queue) :
            print("Queue Overflow ! ")
        else :
            queue.rear = queue.rear + 1
            queue.arr[queue.rear] = val
    
    def dequeue(self,queue): 
        if self.isEmpty(queue) :
            print("No elements to Dequeue ")
            return -1
        else :
            queue.front = queue.front + 1
            return queue.arr[queue.front]


class graphTraversal(object):
    def __init__(self,graph) -> None: 
        self.graph = graph    # datamembers
        self.length = len(graph)
        self.visited = [False]*len(graph)
    def breadthFirstsearch(self):
        '''BFS implementation on a graph'''
        i = 0
        print(i,end=' ')
        visited = [False] * self.length
        visited[i] = True
        q = Queue(100)  # using queue data structure
        q.enqueue(q,i)
   
        while not q.isEmpty(q):
            node = q.dequeue(q)

            for j in range(0,self.length):
                if self.graph[node][j] == 1 and visited[j] == False :
                    print(j,end=' ')
                    visited[j] = True
                    q.enqueue(q,j)
        return
        
    def depthFirstsearch(self,start = 0):
        '''DFS implementation on a graph '''
        self.visited[start] = True
        print(start,end=' ')
        for i in range(self.length):
            if self.graph[start][i] == 1 and not self.visited[i] :
                self.depthFirstsearch(i)
    
        return
    
# insert values to check the bfs and dfs               
g = Graph(7) # graph creation
g.add_edge(0,5)                                           
g.add_edge(0,4)                                           
g.add_edge(1,3)                                           
g.add_edge(1,4)                                           
g.add_edge(2,2)                                           
g.add_edge(2,3)                                           
g.add_edge(3,1)                                           
g.add_edge(4,0)                                           
g.add_edge(4,3)                                           

trav = graphTraversal(g.getGraph()) # graph traversal
trav.depthFirstsearch()
print()
trav.breadthFirstsearch()