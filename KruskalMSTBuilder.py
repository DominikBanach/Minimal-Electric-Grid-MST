class KruskalMSTBuilder():


    def __init__(self, verticesNumber, sortedEdges):
        self.verticesNumber = verticesNumber
        self.sortedEdges = sortedEdges
        self.MST = []
        self.parent = []
        self.rank = []

        for i in range(verticesNumber):
            self.parent.append(i)
            self.rank.append(0)
        


    def find(self, x):
        while x != self.parent[x]:
            x = self.parent[x]
        return x


    def union(self, x, y):

        rx = self.find(x)
        ry = self.find(y)

        if rx != ry:

            if self.rank[rx] > self.rank[ry]: 
                self.parent[ry] = rx
                self.rank[rx] += 1
            else: 
                self.parent[rx] = ry

            if self.rank[rx] == self.rank[ry]: self.rank[ry] += 1

            return True

        return False


    def kruskalMST(self):

        for edge in self.sortedEdges:
            if self.union(edge[0], edge[1]): 
                self.MST.append(edge)

        return self.MST
