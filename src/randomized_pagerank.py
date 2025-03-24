import networkx as nx
import random

def run_randomized_pagerank(iterations=100, damping=0.85):
    # Create a random directed graph
    G = nx.gnp_random_graph(n=10, p=0.5, directed=True)
    G.remove_nodes_from(list(nx.isolates(G)))

    nodes = list(G.nodes())
    N = len(nodes)
    
    pagerank = {node: 1/N for node in nodes}

    for i in range(iterations):
        new_pagerank = {}
        for node in nodes:
            rank_sum = 0
            for nbr in G.predecessors(node):
                weight = random.uniform(0.1, 1.0)  # Random weight
                out_degree = G.out_degree(nbr)
                if out_degree > 0:
                    rank_sum += pagerank[nbr] * weight / out_degree
            new_pagerank[node] = (1 - damping) / N + damping * rank_sum
        pagerank = new_pagerank

    print("Randomized PageRank scores:")
    for node, score in pagerank.items():
        print(f"Node {node}: {score:.4f}")

if __name__ == "__main__":
    run_randomized_pagerank()
