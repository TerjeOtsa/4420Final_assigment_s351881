# **TarjanPlanner**

## **Overview**
TarjanPlanner is a Python-based program designed to compute the most efficient way to visit relatives in a city using various modes of transport. The program utilizes **Dijkstra's algorithm** to determine optimal routes based on time, cost, or distance, incorporating a heuristic that prioritizes different transportation modes for specific distance ranges. The starting location is randomly generated within a 5 km radius of at least one relative.

---

## **Features**
- **Dynamic Graph Construction**: Build a graph with nodes and edges representing relatives and their connectivity.
- **Mode Heuristics**:
  - Walking: 0–0.5 km
  - Biking: 0.5–2 km
  - Bus: 2–5 km
  - Train: >5 km
- **Optimization Criteria**:
  - Time
  - Cost
  - Distance
- **Visualization**: Display the graph and highlight optimal paths.
- **Testing**: Use `pytest` for validating core functionalities.

---

## **Folder Structure**

```plaintext
Task_1_TarjanPlanner/
├── main.py                # Entry point of the program
├── requirements.txt       # Dependencies for the project
├── setup.py               # Package setup for installation
├── data/                  # Data folder containing relatives and transport modes
│   ├── relatives.csv
│   └── transport_modes.json
├── TarjanPlanner/         # Core application logic
│   ├── __init__.py
│   ├── io_utils.py
│   ├── graph_utils.py
│   ├── transport_utils.py
        input_vaildation.py
        error_handler.py
├── tests/                 # Testing folder
│   ├── test_io_utils.py
│   ├── test_graph_utils.py
│   ├── test_transport_modes.py

## **Setup Instructions**

### **1. Clone the Repository**
```bash
git clone https://github.com/your-repo-url/Task_1_TarjanPlanner.git
cd Task_1_TarjanPlanner
2. Install Dependencies
Use pip to install required packages:

bash
Copy code
pip install -r requirements.txt
3. Verify Installation
Ensure pytest and all dependencies are installed:

bash
Copy code
pytest --version
Usage
Running the Program
To execute the program:

bash
Copy code
python main.py
Program Flow
Choose Optimization Criterion:
time
cost
distance
Select Mode:
1: Visit one relative.
2: Visit all relatives.
Random Starting Location:
A random location is generated within a 5 km radius of one relative.
Optimal Path Calculation:
The program calculates and displays the optimal path, cost, time, and distance.
Graph Visualization:
A graphical representation of the route is shown.
Testing
Running Tests
To validate the core functionality:

bash
Copy code
pytest tests/
Test Descriptions
test_io_utils.py:
Tests data loading from relatives.csv and transport_modes.json.
Validates random starting point generation.
test_graph_utils.py:
Tests graph construction for correct nodes and edges.
Validates Dijkstra's algorithm for pathfinding.
test_transport_modes.py:
Ensures proper mode selection based on distance ranges.
Data Files
1. relatives.csv
Details of relatives, including their names, districts, and geographical coordinates.

Sample:

csv
Copy code
Name,Latitude,Longitude
Relative_1,37.4979,127.0276
Relative_2,37.4833,127.0322
...
2. transport_modes.json
Defines the transport modes with their respective speeds, costs, and transfer times.

Sample:

json
Copy code
[
    {"mode": "Walking", "speed_kmh": 5, "cost_per_km": 0, "transfer_time_min": 0},
    {"mode": "Bicycle", "speed_kmh": 15, "cost_per_km": 0, "transfer_time_min": 1},
    {"mode": "Bus", "speed_kmh": 40, "cost_per_km": 2, "transfer_time_min": 5},
    {"mode": "Train", "speed_kmh": 80, "cost_per_km": 5, "transfer_time_min": 2}
]
Key Functions
1. generate_random_start()
Generates a random starting point within a 5 km radius of one relative.

2. build_graph()
Constructs the graph using the relatives and transport modes. Optimizes for:

Time
Cost
Distance
3. find_optimized_route()
Calculates the shortest path using Dijkstra's algorithm.

4. visualize_graph()
Displays the graph with the optimal path highlighted.

Limitations
Assumes data integrity for relatives.csv and transport_modes.json.
The heuristic for mode selection may not perfectly align with real-world scenarios.
Random starting point generation assumes uniform distribution.