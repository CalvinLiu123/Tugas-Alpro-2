import networkx as nx

# Membuat graf tidak berarah
G = nx.Graph()

# Menambahkan simpul (node)
nodes = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K']
G.add_nodes_from(nodes)

# Menambahkan sisi (edges) berdasarkan gambar
edges = [('A', 'C'), ('A', 'B'), ('A', 'D'), ('B', 'E'), ('C', 'E'),
         ('C', 'F'), ('D', 'F'), ('E', 'G'), ('E', 'K'), ('F', 'K'),
         ('F', 'I'), ('G', 'H'), ('H', 'K'), ('I', 'K'), ('J', 'K')]

G.add_edges_from(edges)

# Fungsi untuk mencari semua path antara dua simpul
def find_paths(graph, start, end):
    return list(nx.all_simple_paths(graph, start, end))

# Fungsi untuk mencari semua cycle dengan titik awal tertentu
def find_cycles(graph, start):
    cycles = []
    for cycle in nx.simple_cycles(nx.DiGraph(graph)):  # Konversi ke DiGraph untuk mendukung cycle detection
        if start in cycle:
            cycles.append(cycle)
    return cycles

# Fungsi untuk mencari circuit terpendek dan terpanjang
def find_eulerian_circuit(graph):
    if nx.is_eulerian(graph):
        return list(nx.eulerian_circuit(graph))
    return "Graf bukan Eulerian"

# Menjalankan fungsi
print("1. Semua kemungkinan Path dari A ke K:", find_paths(G, 'A', 'K'))
print("2. Semua kemungkinan Path dari G ke J:", find_paths(G, 'G', 'J'))
print("3. Semua kemungkinan Path dari E ke F:", find_paths(G, 'E', 'F'))
print("4. Semua kemungkinan Cycle jika A sebagai titik awal:", find_cycles(G, 'A'))
print("5. Semua kemungkinan Cycle jika K sebagai titik awal:", find_cycles(G, 'K'))
print("6. Circuit terpendek dan terpanjang dari A ke K:", find_eulerian_circuit(G))
print("7. Circuit terpendek dan terpanjang dari G ke J:", find_eulerian_circuit(G))
print("8. Circuit terpendek dan terpanjang dari E ke F:", find_eulerian_circuit(G))
