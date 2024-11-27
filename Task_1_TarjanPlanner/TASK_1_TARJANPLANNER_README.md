TarjanPlanner - README
Overview
TarjanPlanner is a Python-based route optimization tool that calculates the most efficient path for visiting multiple locations. Designed for flexibility and usability, the tool allows users to optimize routes based on:


Time
Cost
Distance
The application uses Dijkstra's Algorithm for route planning and dynamically adjusts transportation modes based on distance ranges:


Walking: 0–0.5 km
Biking: 0.5–2 km
Bus: 2–5 km
Train: > 5 km
The program also includes a graphical user interface (GUI) built with Tkinter for ease of interaction, route visualization with Matplotlib, and a detailed summary table with metrics.


Features
Dynamic Start Location:
Generates a random starting point within 5 km of a relative.
Optimization Criteria:
Optimize for time, cost, or distance.
Modes:
Visit One Relative: Calculate the best route to a specific relative.
Visit All Relatives: Plan the shortest route to visit all relatives starting from the random point.
Graph Visualization:
Displays the graph with the calculated route highlighted.

Summary Table:
Displays step-by-step distances, times, and costs with transport modes in a formatted table.
Performance Logging:
Logs the time taken for route calculations.
Project Structure



Task_1_TarjanPlanner/
│
├── main.py                  # Main entry point for the program
├── requirements.txt         # Python dependencies
├── setup.py                 # Optional setup for installation
│
├── TarjanPlanner/           # Core application modules
│   ├── __init__.py
│   ├── io_utils.py          # Handles file I/O and data loading
│   ├── graph_utils.py       # Graph creation and route optimization logic
│   ├── transport_utils.py   # Transport modes and related utilities
│   ├── display_utils.py     # Utilities for displaying route details
│
├── data/                    # Data folder
│   ├── relatives.csv        # Relatives data (names, coordinates)
│   ├── transport_modes.json # Transport modes with speed, cost, and transfer times
│
└── tests/                   # Test folder
    ├── test_io_utils.py     # Unit tests for io_utils
    ├── test_graph_utils.py  # Unit tests for graph_utils
    ├── test_transport_utils.py # Unit tests for transport_utils

Setup Instructions
1. Clone the Repository

git clone https://github.com/TerjeOtsa/4420Final_assigment_s351881

cd Task_1_TarjanPlanner

2. Install Dependencies
Use pip to install the required dependencies:


pip install -r requirements.txt

3. Verify Installation
Ensure all dependencies are installed:


python --version
pip list

How to Run

1. Run the Application
Start the application by running:

python main.py


2. GUI Workflow
Select Optimization Criterion:
Choose from Time, Cost, or Distance.

Select Mode:

Visit One Relative:
Enter the name or number of the relative you want to visit.

Visit All Relatives:
Calculates the shortest path to visit all relatives from the random start.


Result:
The GUI displays the results, including:
Optimal route

Metrics: time, cost, and distance
A graphical visualization of the path.
A detailed table of step-by-step metrics is printed in the terminal.


Testing
Run Unit Tests
To validate the core functionality:


pytest tests/
Test Descriptions
test_io_utils.py:
Validates file loading for relatives.csv and transport_modes.json.
Tests random start location generation.
test_graph_utils.py:
Ensures the graph has correct nodes and edges.
Validates Dijkstra's algorithm for pathfinding.
test_transport_utils.py:
Ensures proper mode selection based on distance ranges.
Data Files

1. relatives.csv
Contains information about relatives, including names, districts, and coordinates.

Sample:

csv
Name,Latitude,Longitude
Relative_1,37.4979,127.0276
Relative_2,37.4833,127.0322

2. transport_modes.json
Defines transport modes with speed, cost per kilometer, and transfer times.

Sample:

json

[
    {"mode": "Walking", "speed_kmh": 5, "cost_per_km": 0, "transfer_time_min": 0},
    {"mode": "Bicycle", "speed_kmh": 15, "cost_per_km": 0, "transfer_time_min": 1},
    {"mode": "Bus", "speed_kmh": 40, "cost_per_km": 2, "transfer_time_min": 5},
    {"mode": "Train", "speed_kmh": 80, "cost_per_km": 5, "transfer_time_min": 2}
]
Key Functions
1. generate_random_start()
Generates a random starting location within 5 km of one of the relatives.

2. build_graph()
Constructs a graph with nodes representing relatives and edges weighted by time, cost, or distance.

3. find_optimized_route()
Calculates the optimal path to a single destination using Dijkstra's algorithm.

4. find_shortest_path_to_all_relatives()
Uses Dijkstra's algorithm to calculate the shortest path to visit all relatives.

5. visualize_graph()
Displays a graphical representation of the graph, highlighting the optimal route.

6. display_route_table()
Prints a step-by-step table showing metrics (distance, time, cost) and transport modes.

Performance Logging
The program logs:

Route Calculation Time:
Logs the time taken to compute the optimal path.
Overall Execution Time:
Logs the total runtime of the application.
Example log:

[LOG] Time taken to calculate the route: 1.23 seconds
[LOG] Function 'find_shortest_path_to_all_relatives' executed in 2.45 seconds.