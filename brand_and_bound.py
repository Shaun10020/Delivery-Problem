import networkx as nx



def lower_bound(g, sub_cycle):
    current_weight = sum([g[sub_cycle[i]][sub_cycle[i + 1]]['weight'] for i in range(len(sub_cycle) - 1)])
    unused = [v for v in g.nodes() if v not in sub_cycle]
    h = g.subgraph(unused)
    t = list(nx.minimum_spanning_edges(h))
    mst_weight = sum([h.get_edge_data(e[0], e[1])['weight'] for e in t])
    if len(sub_cycle) == 0 or len(sub_cycle) == g.number_of_nodes():
        return mst_weight + current_weight
    s = sub_cycle[0]
    t = sub_cycle[-1]
    min_to_s_weight = min([g[v][s]['weight'] for v in g.nodes() if v not in sub_cycle])
    min_from_t_weight = min([g[t][v]['weight'] for v in g.nodes() if v not in sub_cycle])
    return current_weight + min_from_t_weight + mst_weight + min_to_s_weight


def branch_and_bound(g, sub_cycle=None, current_min=float("inf")):
    if sub_cycle is None:
        sub_cycle = [0]
    if len(sub_cycle) == g.number_of_nodes():
        weight = sum([g[sub_cycle[i]][sub_cycle[i + 1]]['weight'] for i in range(len(sub_cycle) - 1)])
        weight = weight + g[sub_cycle[-1]][sub_cycle[0]]['weight']
        return weight
    unused_nodes = list()
    for v in g.nodes():
        if v not in sub_cycle:
            unused_nodes.append((g[sub_cycle[-1]][v]['weight'], v))
    unused_nodes = sorted(unused_nodes)
    for (d, v) in unused_nodes:
        assert v not in sub_cycle
        extended_subcycle = list(sub_cycle)
        extended_subcycle.append(v)
        if lower_bound(g, extended_subcycle) < current_min:
            now=branch_and_bound(g,extended_subcycle,current_min)
            if now<current_min:
                current_min=now

    return current_min
