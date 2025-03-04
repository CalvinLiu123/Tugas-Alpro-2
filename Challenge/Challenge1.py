import networkx as nx


G = nx.Graph()


nodes = ['A', 'B', 'C', 'D']
G.add_nodes_from(nodes)


edges = [('A', 'B'), ('B', 'D'), ('B', 'C'), ('A', 'C'), ('C', 'D')]
G.add_edges_from(edges)


def find_trails(graph, start, end):
    return list(nx.all_simple_edge_paths(graph, start, end))


def find_paths(graph, start, end):
    return list(nx.all_simple_paths(graph, start, end))


def find_cycles(graph, start):
    cycles = []
    for cycle in nx.simple_cycles(nx.DiGraph(graph)):  
        if start in cycle:
            cycles.append(cycle)
    return cycles


print("Trail dari A ke D:", find_trails(G, 'A', 'D'))
print("Semua kemungkinan Path dari A ke D:", find_paths(G, 'A', 'D'))
print("Semua kemungkinan Cycle jika A sebagai titik awal:", find_cycles(G, 'A'))
