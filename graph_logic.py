# graph_logic.py
import networkx as nx
import numpy as np

def build_graph(rc, pos_dict):
    """
    Constructs a NetworkX graph based on the communication radius (rc).
    Two nodes are connected if their Euclidean distance is <= rc.
    """
    G = nx.Graph()
    G.add_nodes_from(pos_dict.keys())
    nodes = list(pos_dict.keys())
    coords = list(pos_dict.values())
    
    # Check distance between every pair of nodes
    for i in range(len(nodes)):
        for j in range(i + 1, len(nodes)):
            dist = np.linalg.norm(coords[i] - coords[j])
            if dist <= rc:
                G.add_edge(nodes[i], nodes[j])
    return G

def find_min_rc(pos_dict):
    """
    Iteratively finds the minimum radius (rc) required for the network 
    to be fully connected (path exists between all pairs).
    """
    rc = 0.01
    while rc < 2.0: # 2.0 is roughly the max diagonal distance
        G = build_graph(rc, pos_dict)
        if nx.is_connected(G):
            return rc
        rc += 0.01
    return rc

def calc_transmissions(G, sink_node, t_transmit):
    """
    Calculates the Total Network Transmission Rate.
    Formula: Sum(Hops_to_Sink * Packet_Rate) for all nodes.
    """
    try:
        # Calculate shortest path (hops) from sink to all nodes
        path_lengths = nx.single_source_shortest_path_length(G, sink_node)
    except nx.NetworkXNoPath:
        return float('inf') # Return infinity if graph is disconnected

    total_tx = 0
    for node in G.nodes():
        if node != sink_node:
            hops = path_lengths.get(node, 0)
            rate = 1.0 / t_transmit[node] # Packets per second
            total_tx += hops * rate
            
    return total_tx

def calc_loads_and_dists(G, sink_node, t_transmit):
    """
    Calculates the traffic load for every node and their distance from the sink.
    
    Logic:
    - Load of a node = Own generated traffic + Traffic forwarded from children.
    - We use a BFS tree to determine the parent-child relationship.
    - Calculation creates a bottom-up accumulation (leaves -> root).
    """
    try:
        # Get distances (hops)
        dists = nx.single_source_shortest_path_length(G, sink_node)
        # Get the tree structure (predecessors map child -> parent)
        predecessors = dict(nx.bfs_predecessors(G, sink_node))
    except:
        return {}, {} # Handle errors/disconnection

    # Initialize load with the node's own traffic generation rate
    loads = {n: 1.0 / t_transmit[n] for n in G.nodes()}
    
    # Sort nodes by distance in descending order (process furthest nodes first)
    sorted_nodes = sorted(dists, key=dists.get, reverse=True)
    
    for node in sorted_nodes:
        if node == sink_node:
            continue
        
        # Pass current node's total load to its parent
        parent = predecessors.get(node)
        if parent is not None:
            loads[parent] += loads[node]
            
    return loads, dists