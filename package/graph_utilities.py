import networkx as nx
import numpy as np

def arg_n_smallest(dc : dict, n : int) -> dict:
    '''Returns the n smallest keys in a dictionary based on values'''
    values = list(dc.values())
    n_small = np.argpartition(values, n)[:n]
    keys = np.array(list(dc.keys()))[n_small]
    return {k:v for k,v in dc.items() if k in keys}

def select_nodes(g: nx.Graph, **attrs) -> set:
    '''Selects all nodes in a graph which have certain attributes'''
    return {k for k,data in g.nodes(data=True) if all(attr in data and data[attr] == val for attr,val in attrs.items())}

def leaves(G: nx.Graph) -> list:
    '''Returns the leaves in an undirected graph'''
    leaves = [x for x in G.nodes() if G.degree(x)==1]
    return leaves

def n_closest(g: nx.Graph, n: int, src: int, targets: set) -> list :
    '''Returns the n closest nodes to a certain src and their distances'''
    sp = nx.single_source_shortest_path_length(g, src)
    del sp[src]
    sp_servers = {k:sp[k] for k in sp.keys() & targets}
    
    return arg_n_smallest(sp_servers, n)

def count_closest(h: dict, N : int) -> dict:
    r = {}
    for h,n in sorted(h.items(), key=lambda x: x[0]):
        n_0 = min(n, N)
        N -= n_0
        r[h] = n_0
        if N == 0:
            break
        
    return r