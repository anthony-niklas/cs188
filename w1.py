from networkx import *

# Construct a graph

# h = { edge: h value }
# g = { edge: w }

G = Graph()

G.add_node('Odessa',    h=20)
G.add_node('Budapest',  h=12)
G.add_node('Munich',    h=3)
G.add_node('Rome',      h=0)
G.add_node('Warsaw',    h=30)
G.add_node('Venice',    h=3)

G.add_edge('Munich', 'Warsaw')
G.add_edge('Munich', 'Rome')
G.add_edge('Munich', 'Budapest')
G.add_edge('Munich', 'Venice')

G.add_edge('Warsaw', 'Odessa')
G.add_edge('Warsaw', 'Budapest')

G.add_edge('Odessa', 'Venice')

G.add_edge('Venice', 'Rome')


# Greedy, no edge weights in this graph
print 'Greedy: ', algorithms.shortest_paths.astar.astar_path(G, 'Warsaw', 'Rome', heuristic=lambda s, d: G.node[s]['h'])

G = Graph()

G.add_node('Odessa',    h=20)
G.add_node('Budapest',  h=12)
G.add_node('Munich',    h=3)
G.add_node('Rome',      h=0)
G.add_node('Warsaw',    h=30)
G.add_node('Venice',    h=3)

G.add_edge('Munich', 'Warsaw',      weight=15)
G.add_edge('Munich', 'Rome',        weight=15)
G.add_edge('Munich', 'Budapest',    weight=12)
G.add_edge('Munich', 'Venice',      weight=3)

G.add_edge('Warsaw', 'Odessa',      weight=6)
G.add_edge('Warsaw', 'Budapest',    weight=9)

G.add_edge('Odessa', 'Venice',      weight=14)

G.add_edge('Venice', 'Rome',        weight=6)

# A*, now using edge weights
print 'A*: ', algorithms.shortest_paths.astar.astar_path(G, 'Warsaw', 'Rome', heuristic=lambda s, d: G.node[s]['h'])

# UCS, h=0
print 'UCS: ', algorithms.shortest_paths.astar.astar_path(G, 'Warsaw', 'Rome', heuristic=lambda s, d: 0)
