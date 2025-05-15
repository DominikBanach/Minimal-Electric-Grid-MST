import matplotlib.pyplot as plt
import networkx as nx

class Visualizer():
    def __init__(self, allEdges, MST, n):

        self.allEdges = allEdges
        self.MST = MST
        self.nodes = list(range(n))


    def present(self):

        G = nx.Graph()

        G.add_nodes_from(self.nodes)
        
        for u, v, weight in self.allEdges:
            G.add_edge(u, v, weight=weight)

        pos = nx.spring_layout(G, k=2.2, iterations=30, seed=40) 

        plt.figure(figsize=(16, 7))

        mst_edge_set = set()
        for u, v, _ in self.MST:
            mst_edge_set.add(tuple(sorted((u, v))))

        edges_in_mst_to_draw = []
        edges_not_in_mst_to_draw = []
        edge_labels = {}

        for u, v, weight in self.allEdges:
            edge_tuple = tuple(sorted((u, v)))
            if edge_tuple in mst_edge_set:
                edges_in_mst_to_draw.append((u,v))
            else:
                edges_not_in_mst_to_draw.append((u,v))
            edge_labels[(u,v)] = weight
        
        nx.draw_networkx_edges(
            G, pos,
            edgelist=edges_not_in_mst_to_draw,
            edge_color='gray',
            style='dashed',
            alpha=0.3,
            width=1
        )

        nx.draw_networkx_edges(
            G, pos,
            edgelist=edges_in_mst_to_draw,
            edge_color='yellow',
            width=3
        )

        for node_id in G.nodes():
            x, y = pos[node_id]
            plt.text(
                x, y, '\U0001F3E0',
                fontsize=20,
                ha='center',
                va='center',
                fontname='Segoe UI Symbol',
                bbox=dict(facecolor='skyblue', alpha=0.3, boxstyle='circle,pad=0.3', edgecolor='none')
            )


        nx.draw_networkx_edge_labels(
            G, pos,
            edge_labels=edge_labels,
            font_size=12,
            font_color='black',
            bbox=dict(facecolor='white', alpha=0.8, edgecolor='none', pad=0.1)
        )
        
        plt.title("Proponowana struktura sieci elektrycznej w podanej miejscowości na podstawie drzewa MST", fontsize=16)
        plt.axis('off') 
        plt.tight_layout()
        plt.show()
