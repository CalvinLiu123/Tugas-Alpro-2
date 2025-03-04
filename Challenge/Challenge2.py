import networkx as nx


G = nx.Graph()


nodes = ['A', 'B', 'C', 'D', 'E', 'F']
G.add_nodes_from(nodes)


edges = [('A', 'D'), ('A', 'B'), ('B', 'E'), ('C', 'B'), ('C', 'F'),
         ('C', 'E'), ('D', 'E'), ('E', 'F')]
G.add_edges_from(edges)


def find_paths(graph, start, end):
    return list(nx.all_simple_paths(graph, start, end))


def find_cycles(graph, start):
    cycles = []
    for cycle in nx.simple_cycles(nx.DiGraph(graph)):  
        if start in cycle:
            cycles.append(cycle)
    return cycles


def find_eulerian_circuit(graph):
    if nx.is_eulerian(graph):
        return list(nx.eulerian_circuit(graph))
    return "Graf bukan Eulerian"

# Menjalankan fungsi
print("1. Semua kemungkinan Path dari A ke C:", find_paths(G, 'A', 'C'))
print("2. Semua kemungkinan Cycle jika C sebagai titik awal:", find_cycles(G, 'C'))
print("3. Semua kemungkinan Cycle jika B sebagai titik awal:", find_cycles(G, 'B'))
print("4. Circuit terpendek dan terpanjang dari A ke C:", find_eulerian_circuit(G))
