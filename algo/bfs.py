

from collections import defaultdict


class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def addEdge(self, x, y):
        self.graph[x].append(y)


    def BFS(self, s):
        visited = [False] * len(self.graph)

        queue = []
        queue.append(s)

        while queue:
            v = queue.pop(0)
            if not visited[v]:
                print(v, end = " ")
                for kid in self.graph[v]:
                    queue.append(kid)


if __name__ == '__main__':



    g = Graph()
    g.addEdge(0, 1)
    g.addEdge(0, 2)
    g.addEdge(1, 2)
    g.addEdge(2, 0)
    g.addEdge(2, 3)
    g.addEdge(3, 3)

    print ("Following is Breadth First Traversal"
           " (starting from vertex 2)")
    g.BFS(2)


