from InputParser import InputParser
from KruskalMSTBuilder import KruskalMSTBuilder
from Visualizer import Visualizer

PATH = "input.txt"

if __name__ == "__main__":

    parser = InputParser()
    n, sortedEdges = parser.loadNumberOfVerticesAndSortedEdgesList(PATH)

    kruskalMSTBuilder = KruskalMSTBuilder(n, sortedEdges)

    visualizer = Visualizer(sortedEdges, kruskalMSTBuilder.kruskalMST(), n)
    visualizer.present()
