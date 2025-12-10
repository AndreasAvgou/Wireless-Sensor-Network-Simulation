# experiments.py
import matplotlib.pyplot as plt
import random
import networkx as nx
from graph_logic import calc_transmissions, calc_loads_and_dists, build_graph

def run_part_1a(G, t_transmit):
    """
    Part 1a: Analyzes how Sink placement impacts total transmissions.
    Compares the 'Best' node (Max Neighbors) against random nodes.
    """
    print("\n--- Running Part 1a: Sink Placement Analysis ---")
    
    # Identify the node with the highest degree (most neighbors)
    degrees = dict(G.degree())
    best_node = max(degrees, key=degrees.get)
    
    # Select 19 random nodes + the best node for comparison
    candidates = random.sample([n for n in G.nodes() if n != best_node], 19)
    candidates.append(best_node)
    
    x_neigh = []
    y_tx = []
    
    for sink in candidates:
        tx = calc_transmissions(G, sink, t_transmit)
        x_neigh.append(G.degree[sink])
        y_tx.append(tx)
        
    # Plotting
    plt.figure(figsize=(8, 6))
    plt.scatter(x_neigh, y_tx, c='blue', alpha=0.6, label='Random Sinks')
    # Highlight the best node in red
    best_tx = calc_transmissions(G, best_node, t_transmit)
    plt.scatter([degrees[best_node]], [best_tx], c='red', s=100, label='Max Degree Node')
    
    plt.title('1a: Total Transmissions vs Sink Neighbors')
    plt.xlabel('Number of Neighbors')
    plt.ylabel('Total Transmissions (Rate)')
    plt.legend()
    plt.grid(True)
    plt.show()

def run_part_1b(pos_dict, t_transmit, start_rc):
    """
    Part 1b: Analyzes how increasing the communication radius (rc) 
    affects total transmissions.
    """
    print("\n--- Running Part 1b: Variable RC Analysis ---")
    rc_list = []
    tx_list = []
    curr_rc = start_rc
    
    # Iterate 10 times, increasing rc by 0.1 each step
    for _ in range(10):
        G_temp = build_graph(curr_rc, pos_dict)
        
        if nx.is_connected(G_temp):
            # Recalculate best sink for this new graph topology
            degs = dict(G_temp.degree())
            bsink = max(degs, key=degs.get)
            
            val = calc_transmissions(G_temp, bsink, t_transmit)
            
            rc_list.append(curr_rc)
            tx_list.append(val)
        
        curr_rc += 0.1
        
    # Plotting
    plt.figure(figsize=(8, 6))
    plt.plot(rc_list, tx_list, 'g-o')
    plt.title('1b: Total Transmissions vs Radius (rc)')
    plt.xlabel('Radius (rc)')
    plt.ylabel('Total Transmissions (Rate)')
    plt.grid(True)
    plt.show()

def run_part_2(G, t_transmit):
    """
    Part 2: 
    1. Plots Node Load vs Distance (Energy Hole Problem).
    2. Finds the optimal Sink for Minimum Energy and Maximum Lifetime.
    """
    print("\n--- Running Part 2: Load & Energy Analysis ---")
    
    # 2.1 Visualization: Load vs Distance (using Node 0 as arbitrary sink)
    sink = 0
    loads, dists = calc_loads_and_dists(G, sink, t_transmit)
    
    x_dist = [dists[n] for n in G.nodes() if n != sink]
    y_load = [loads[n] for n in G.nodes() if n != sink]
            
    plt.figure(figsize=(8, 6))
    plt.scatter(x_dist, y_load, c='purple', alpha=0.6)
    plt.title('2: Node Load vs Distance from Sink')
    plt.xlabel('Distance (Hops)')
    plt.ylabel('Load (Packets/sec)')
    plt.grid(True)
    plt.show()
    
    # 2.2 Optimization: Find the best sink
    print("Searching for optimal sink nodes...")
    
    min_total_energy = float('inf')
    best_energy_sink = -1
    
    min_max_load = float('inf') # Determines lifetime
    best_lifetime_sink = -1
    
    # Check every node as a potential sink
    for n in G.nodes():
        l, _ = calc_loads_and_dists(G, n, t_transmit)
        
        if not l: continue # Skip if calculation failed
        
        # Total Energy = Sum of all node loads (excluding sink)
        total_e = sum(l.values()) - l[n]
        
        # Max Load = The load of the most burdened node (excluding sink)
        loads_no_sink = [v for k,v in l.items() if k != n]
        max_l = max(loads_no_sink) if loads_no_sink else 0
        
        # Update Minimum Total Energy
        if total_e < min_total_energy:
            min_total_energy = total_e
            best_energy_sink = n
        
        # Update Min-Max Load (Lifetime)
        if max_l < min_max_load:
            min_max_load = max_l
            best_lifetime_sink = n
            
    print(f"-> Optimal Sink for Min Total Energy: Node {best_energy_sink} (Total Load: {min_total_energy:.2f})")
    print(f"-> Optimal Sink for Max Lifetime:     Node {best_lifetime_sink} (Max Node Load: {min_max_load:.2f})")