# main.py
from topology import generate_data
from graph_logic import find_min_rc, build_graph
from experiments import run_part_1a, run_part_1b, run_part_2
import config

def main():
    print(f"=== WSN SIMULATION STARTED (N={config.NUM_NODES}) ===")
    
    # Step 1: Generate Topology Data
    pos_dict, t_transmit = generate_data()
    
    # Step 2: Determine Minimum Connectivity Radius
    min_rc = find_min_rc(pos_dict)
    print(f"Minimum RC for connectivity found: {min_rc:.4f}")
    
    # Step 3: Build the Base Graph
    G_base = build_graph(min_rc, pos_dict)
    
    # Step 4: Execute Assignments
    run_part_1a(G_base, t_transmit)
    run_part_1b(pos_dict, t_transmit, min_rc)
    run_part_2(G_base, t_transmit)
    
    print("\n=== SIMULATION COMPLETED ===")

if __name__ == "__main__":
    main()