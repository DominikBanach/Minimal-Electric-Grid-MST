class InputParser():

    def loadNumberOfVerticesAndSortedEdgesList(self, path):
        # Ta funkcja będzie używana w mainie, pozostałe dwie to jej pomocnicze
        n,  allEdges = self.parseInputFileIntoNumberOfVerticesAndEdgesList(path)
        return n, self.sortEdges(allEdges) 

    def sortEdges(self, edges):
        def merge_sort(arr):
            if len(arr) <= 1:
                return arr
            mid = len(arr) // 2
            left = merge_sort(arr[:mid])
            right = merge_sort(arr[mid:])

            merged = []
            i = j = 0

            while i < len(left) and j < len(right):
                if left[i][2] <= right[j][2]:
                    merged.append(left[i])
                    i += 1
                else:
                    merged.append(right[j])
                    j += 1

            merged.extend(left[i:])
            merged.extend(right[j:])
            return merged
        return merge_sort(edges)
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
