# Wireless Sensor Network (WSN) Simulation

This project is a simulation of a Wireless Sensor Network (WSN) implemented in **Python**. The  analyzes network topology, connectivity, transmission costs, and energy consumption (load) in a network consisting of 100 randomly distributed nodes.

## Project Structure

The code is organized into **5 separate files** for better management and modularity:

1.  **`main.py`**: The central execution file. It coordinates the program flow and calls the necessary functions.
2.  **`config.py`**: Contains global settings (e.g., Number of nodes, Seed, Field dimensions).
3.  **`topology.py`**: Responsible for data generation (random node positions, transmission rates).
4.  **`graph_logic.py`**: Contains graph algorithms (NetworkX) and mathematical calculations (calculation of `rc`, transmissions, node load).
5.  **`experiments.py`**: Contains the assignment scenarios (Part 1 & 2) and code for generating the plots (`matplotlib`).

## 🚀 Installation & Requirements

To run the simulation, you need Python 3 installed along with the following libraries:

* `networkx` (Graph Theory)
* `matplotlib` (Plotting/Charts)
* `numpy` (Mathematical operations)

You can install them by running the following command:

```bash
pip install networkx matplotlib numpy
```
## ▶️ How to Run

1. Ensure all 5 files (.py) are located in the same folder.

2. Open your terminal or command prompt in this folder.

3. Run the command:

```bash
python main.py
```

## 📊 Simulation Analysis
Executing the program generates results for the following questions:

* 1: Transmissions & Topology
  
* Sink Placement: Compares the number of total transmissions when the Sink node is chosen randomly versus when it is the node with the most neighbors.

   * Goal: To demonstrate that central nodes reduce routing costs (hops).

* Variable Radius (rc): Studies how increasing the communication range (rc) reduces total hops and transmission costs.

* 2: Load & Energy

* Load Distribution (Energy Hole): Calculates and visualizes the traffic load of each node in relation to its distance from the Sink.

   * Observation: Nodes closer to the Sink are disproportionately burdened (bottleneck effect).

* Sink Optimization: The algorithm iterates through all nodes to identify:

   1. The optimal node for Minimum Total Energy (Min Total Energy).

   2. The optimal node for Maximum Network Lifetime (Min-Max Load).

## 📝 Notes

* When a plot window appears, you must close it for the simulation to proceed to the next step.
