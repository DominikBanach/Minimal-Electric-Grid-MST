class InputParser():

    def __init__(self):
        pass

    def loadEdges(self, path):
        # Ta funkcja będzie używana w mainie, pozostałe dwie to jej pomocnicze
        return self.sortEdges(self.parseInputFileIntoEdgesList(path)) 

    def sortEdges(self, edges):
        # TODO: zaimplementować własne sortowanie które będzie najbardziej pasowało do zadania???
        return sorted(edges, key=lambda edge: edge[2]) # sortuje według wag

    def parseInputFileIntoEdgesList(self, path):
        with open(path) as f:
            return [list(map(int, line.split())) for line in f.readlines()] 
            # przykładowy zwrot [wierzchołek1, wierzchołek2, waga]: [[1, 2, 1], [1, 3, 2], [2, 3, 5], [4, 5, 3], [3, 4, 3], [2, 5, 1]]

# PRZYKŁAD UŻYCIA
parser = InputParser()
print(parser.loadEdges("test.txt"))
