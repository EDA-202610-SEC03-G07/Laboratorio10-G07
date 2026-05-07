from DataStructures.Map import map_linear_probing as mp
from DataStructures.Graph import vertex as v
def new_graph(order):
    new_graph = {"vertices": mp.new_map(order),
                 "num_edges": 0}
    return new_graph

def insert_vertex(my_graph, key_u, info_u):
    new_vertex = v.new_vertex(key_u, info_u)
    my_graph["vertices"] = mp.put(my_graph["vertices"], key_u, new_vertex)
    return my_graph