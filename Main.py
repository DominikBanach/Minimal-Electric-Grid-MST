from InputParser import InputParser
from KruskalMSTBuilder import KruskalMSTBuilder
from Visualizer import Visualizer

PATHS = [f"inputExamples/inputExample{i}.txt" for i in range(8)]

if __name__ == "__main__":

    for PATH in PATHS:

        parser = InputParser()
        n, sortedEdges = parser.loadNumberOfVerticesAndSortedEdgesList(PATH)

        kruskalMSTBuilder = KruskalMSTBuilder(n, sortedEdges)

        visualizer = Visualizer(sortedEdges, kruskalMSTBuilder.kruskalMST(), n)
        visualizer.present()
