from networkx import *
import sys, math


def max_v(L):
	return math.ceil((L-1)**0.5) + 1
	
def run(n):
	return ['L:%s | V:%s' % (L, max_v(L)) for L in range(1, n)]
	
for r in run(20):
	print r
	
	
sys.exit(0)

G = Graph()

G.add_node('Odessa',    h=20)
G.add_node('Budapest',  h=12)
G.add_node('Munich',    h=3)
G.add_node('Rome',      h=0)
G.add_node('Warsaw',    h=30)
G.add_node('Venice',    h=3)

G.add_edge('Munich', 'Warsaw',      weight=0)
G.add_edge('Munich', 'Rome',        weight=0)
G.add_edge('Munich', 'Budapest',    weight=0)
G.add_edge('Munich', 'Venice',      weight=0)

G.add_edge('Warsaw', 'Odessa',      weight=0)
G.add_edge('Warsaw', 'Budapest',    weight=0)

G.add_edge('Odessa', 'Venice',      weight=0)

G.add_edge('Venice', 'Rome',        weight=0)

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

# A*, g>=0
print 'A*: ', algorithms.shortest_paths.astar.astar_path(G, 'Warsaw', 'Rome', heuristic=lambda s, d: G.node[s]['h'])

# UCS, h=0
print 'UCS: ', algorithms.shortest_paths.astar.astar_path(G, 'Warsaw', 'Rome', heuristic=lambda s, d: 0)



G = Graph()

G.add_node('Odessa',    h=20)
G.add_node('Budapest',  h=12)
G.add_node('Munich',    h=3)
G.add_node('Rome',      h=0)
G.add_node('Warsaw',    h=30)
G.add_node('Venice',    h=3)

G.add_edge('Munich', 'Warsaw',      weight=0)
G.add_edge('Munich', 'Rome',        weight=0)
G.add_edge('Munich', 'Budapest',    weight=0)
G.add_edge('Munich', 'Venice',      weight=0)

G.add_edge('Warsaw', 'Odessa',      weight=0)
G.add_edge('Warsaw', 'Budapest',    weight=0)

G.add_edge('Odessa', 'Venice',      weight=0)

G.add_edge('Venice', 'Rome',        weight=0)
import pdb; pdb.set_trace()
print 'DFS: ', networkx.algorithms.traversal.depth_first_search.dfs_tree(G, source='Warsaw').edges()
print 'BFS: ', networkx.algorithms.traversal.breadth_first_search.bfs_tree(G, source='Warsaw').edges()