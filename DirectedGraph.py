
#Implement a directed graph using adjacency lists.
class DirectedGraph:
    def __init__(self):
        self.graph = {}

    def addNode(self, node):
        if node not in self.graph:
            self.graph[node] = []

    def addNodes(self, nodes):
        for node in nodes:
            self.addNode(node)

    def addEdge(self, node1, node2):
        if node1 in self.graph and node2 in self.graph:
            self.graph[node1].append(node2)

    def addEdges(self, edges):
        for edge in edges:
            self.addEdge(edge[0], edge[1])

    def removeNode(self, node):
        if node in self.graph:
            del self.graph[node]
            for key in self.graph:
                if node in self.graph[key]:
                    self.graph[key].remove(node)

    def removeEdge(self, node1, node2):
        if node1 in self.graph and node2 in self.graph:
            if node2 in self.graph[node1]:
                self.graph[node1].remove(node2)

    def hasNode(self, node):
        return node in self.graph

    def neighbors(self, node):
        if node in self.graph:
            return self.graph[node]
        return []

    def shortestPath(self, node1, node2):
        if node1 not in self.graph or node2 not in self.graph:
            return None
        if node1 == node2:
            return [node1]
        visited = [node1]
        queue = [[node1]]
        while queue:
            path = queue.pop(0)
            node = path[-1]
            for neighbor in self.graph[node]:
                if neighbor not in visited:
                    visited.append(neighbor)
                    newPath = list(path)
                    newPath.append(neighbor)
                    queue.append(newPath)
                    if neighbor == node2:
                        return newPath
        return None

    def __str__(self):
        return str(self.graph)

    def __repr__(self):
        return str(self.graph)
    


# Write a main function to test your code:
def main():
    # you can use this to test your DirectedGraph implementation
    g = DirectedGraph()
    g.addNodes([0,1,2,3,4,5,6])
    g.addEdges([(0,1),(0,2),(1,3),(1,4),(2,5),(2,6)])
    print(g)
    print(g.shortestPath(0,6))
    print(g.shortestPath(6,0))

    pass

if __name__ == "__main__":
    main()