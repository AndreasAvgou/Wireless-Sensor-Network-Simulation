# topology.py
import numpy as np
import random
import config

def generate_data():
    """
    Generates random positions for nodes and assigns transmission intervals.
    
    Returns:
        pos_dict (dict): Dictionary mapping Node ID -> (x, y) coordinates.
        t_transmit (dict): Dictionary mapping Node ID -> transmission interval (seconds).
    """
    # Set seeds to ensure the same topology is generated every time
    np.random.seed(config.SEED)
    random.seed(config.SEED)

    # Generate random (x, y) coordinates within the AREA_SIZE
    positions = np.random.rand(config.NUM_NODES, 2) * config.AREA_SIZE
    pos_dict = {i: positions[i] for i in range(config.NUM_NODES)}
    
    # Assign a random transmission interval [1, 10] seconds to each node
    # Rate = 1 / t_transmit
    t_transmit = {i: random.randint(1, 10) for i in range(config.NUM_NODES)}
    
    return pos_dict, t_transmit