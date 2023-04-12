from networkx import adjacency_matrix
from scipy.sparse import identity
import networkx as nx

def is_irreducible(G: nx.Graph) -> bool:
    adj_mat = adjacency_matrix(G)  # adjacency matrix
    n_nodes = adj_mat.shape[0]     # number of nodes
    taylor_sum = identity(n_nodes) # initialize taylor sum
    add = adj_mat.copy()           # initialize adj_mat^1
    for _ in range(1, n_nodes):
        taylor_sum += add
        add *= adj_mat

    return taylor_sum.min() > 0

from networkx import laplacian_matrix
from scipy.sparse.linalg import eigs

def lapplacian_is_connected(G: nx.Graph) -> bool:
    lap_mat = laplacian_matrix(G).asfptype()
    eigvals = eigs(lap_mat, # Laplacian matrix
                   k=2, which='SR', # 2 smallest real eigenvalues
                   return_eigenvectors=False) # only eigenvalues
    # print(f'Is this value close to zero? {sorted(eigvals)[1].real}')
    return np.isclose(sorted(eigvals)[1].real, 0) == False



def bfs_is_connected(G: nx.Graph) -> bool:
    root = 0 # start at node 0
    visited = np.zeros(G.number_of_nodes(), dtype=bool) # array to keep track of visited nodes
    queue = [root] # queue to keep track of nodes to visit
    while queue:
        node = queue.pop(0) # pop the first node
        if not visited[node]: # if node has not been visited
            visited[node] = True # mark node as visited
            queue.extend([n for n in G.neighbors(node) if not visited[n]]) # add neighbors to queue
    
    # Is all True?
    return visited.all()