import networkx as nx
import itertools as permutations



def cycle_length(g, cycle):
    assert len(cycle) == g.number_of_nodes()
    weight=0
    for x in range(len(cycle)):
        if x!=len(cycle)-1:
            weight+=g[cycle[x]][cycle[x+1]]['weight']
        else:
            weight+=g[cycle[x]][cycle[0]]['weight']
    return weight

def cycle_length_average(g, cycle):
    assert len(cycle) == g.number_of_nodes()
    weight=0
    count=0
    for x in range(len(cycle)):
        if x!=len(cycle)-1:
            weight+=g[cycle[x]][cycle[x+1]]['weight']
            count+=1
        else:
            weight+=g[cycle[x]][cycle[0]]['weight']
            count+=1
    return weight/count
    
def all_permutations(g):
    n = g.number_of_nodes()
    weight=float("inf")
    for cycle in permutations(range(n)):
        cycle_weight=cycle_length(g,cycle)
        if weight>cycle_weight:
            weight=cycle_weight
    return weight

def average(g):
    # n is the number of vertices.
    n = g.number_of_nodes()

    # Sum of weights of all n*(n-1)/2 edges.
    sum_of_weights = sum(g[i][j]['weight'] for i in range(n) for j in range(i))

    # Write your code here.
    return 2*sum_of_weights/(n-1)

def nearest_neighbors(g):
    current_node = 0
    path = [current_node]
    n = g.number_of_nodes()

    # We'll repeat the same routine (n-1) times
    for _ in range(n - 1):
        next_node = None
        # The distance to the closest vertex. Initialized with infinity.
        min_edge = float("inf")
        for v in g.nodes():
            if v in path:
                continue
            if min_edge>g[current_node][v]['weight']:
                min_edge=g[current_node][v]['weight']
                next_node=v

        assert next_node is not None
        path.append(next_node)
        current_node = next_node

    weight = sum(g[path[i]][path[i + 1]]['weight'] for i in range(g.number_of_nodes() - 1))
    weight += g[path[-1]][path[0]]['weight']
    return weight


g = nx.Graph()
# Now we will add 6 edges between 4 vertices
g.add_edge(0, 1, weight = 2)
# We work with undirected graphs, so once we add an edge from 0 to 1, it automatically creates an edge of the same weight from 1 to 0.
g.add_edge(1, 2, weight = 2)
g.add_edge(2, 3, weight = 2)
g.add_edge(3, 0, weight = 2)
g.add_edge(0, 2, weight = 1)
g.add_edge(1, 3, weight = 1)

# Now we want to compute the lengths of two cycles:
cycle1 = [0, 1, 2, 3]
cycle2 = [0, 2, 1, 3]

print(cycle_length(g,cycle1))
