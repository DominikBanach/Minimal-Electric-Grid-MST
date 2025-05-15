class InputParser():

    def loadNumberOfVerticesAndSortedEdgesList(self, path):
        # Ta funkcja będzie używana w mainie, pozostałe dwie to jej pomocnicze
        n,  allEdges = self.parseInputFileIntoNumberOfVerticesAndEdgesList(path)
        return n, self.sortEdges(allEdges) 

    def sortEdges(self, edges):
        # DO ZMIANY DLA KUBY
        # TODO: zaimplementować własne sortowanie które będzie najbardziej pasowało do zadania???
        return sorted(edges, key=lambda edge: edge[2]) # sortowanie musi być według wag według wag

    def parseInputFileIntoNumberOfVerticesAndEdgesList(self, path):
        with open(path) as f:

            nodes = set()
            allEdges = []

            for line in f.readlines():
                edge = list(map(int, line.split()))
                nodes.add(edge[0])
                nodes.add(edge[1])
                allEdges.append(edge)

            return len(nodes), allEdges
            # przykładowe allEdges ( [wierzchołek1, wierzchołek2, waga] ): [[1, 2, 13], [1, 3, 21], [2, 3, 54], [4, 5, 31], [3, 4, 32], [2, 5, 13]]
