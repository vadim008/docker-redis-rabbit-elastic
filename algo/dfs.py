

from collections import defaultdict


class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def addEdge(self, x, y):
        self.graph[x].append(y)



    def DFS(self, v):

        visited = [False] * len(self.graph)

        self.runDFS(v, visited)

    def runDFS(self, v, visited):
        if  visited[v] is False:
            print (v, end = " ")
            visited[v] = True
            for kid in self.graph[v]:
                self.runDFS(kid, visited)


if __name__ == '__main__':



    g = Graph()
    g.addEdge(0, 1)
    g.addEdge(0, 2)
    g.addEdge(1, 2)
    g.addEdge(2, 0)
    g.addEdge(2, 3)
    g.addEdge(3, 3)
    #g.addEdge(4, 0)

    print ("Following is Deepth First Traversal"
           " (starting from vertex 2)")
    g.DFS(2)


