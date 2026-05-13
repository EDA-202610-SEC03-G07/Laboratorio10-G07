from DataStructures.Map import map_linear_probing as mp
from DataStructures.Graph import digraph as dg
from DataStructures.Graph import vertex as v

def dfs(my_graph, source):
    order = dg.order(my_graph)
    visited_map = mp.new_map(order)
    mp.put(visited_map, source, {"marked": True, "edge_from": None})
    dfs_vertex(my_graph, source, visited_map)  
    return visited_map
def dfs_vertex(my_graph, vertex, visited_map):
    pass