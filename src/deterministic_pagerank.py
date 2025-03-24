# deterministic_pagerank.py
import networkx as nx

def run_deterministic_pagerank():
    # Create a random directed graph
    G = nx.gnp_random_graph(n=10, p=0.5, directed=True)
    
    # Remove isolated nodes to avoid divide-by-zero issues
    G.remove_nodes_from(list(nx.isolates(G)))

    # Run NetworkX built-in PageRank
    pr = nx.pagerank(G, alpha=0.85)

    print("Deterministic PageRank scores:")
    for node, score in pr.items():
        print(f"Node {node}: {score:.4f}")

if __name__ == "__main__":
    run_deterministic_pagerank()
