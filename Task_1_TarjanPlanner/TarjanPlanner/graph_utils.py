import itertools
import networkx as nx
import time
import networkx as nx
from geopy.distance import geodesic
import matplotlib.pyplot as plt
import itertools
import random

def generate_random_start(relatives, max_distance=5):
    """Generate a random starting location within a given distance from at least one relative."""
    # Select a random relative as the anchor point
    anchor = random.choice(relatives)
    lat, lon = anchor["coords"]

    while True:
        delta_lat = random.uniform(-0.05, 0.05)  # Approx. 5 km latitude range
        delta_lon = random.uniform(-0.05, 0.05)  # Approx. 5 km longitude range
        random_point = (lat + delta_lat, lon + delta_lon)

        # Check if the random point is within the max_distance of at least one relative
        for relative in relatives:
            if geodesic(random_point, relative["coords"]).km <= max_distance:
                return {"name": "Random_Start", "coords": random_point}



def calculate_distance(coord1, coord2):
    """Calculate geodesic distance between two coordinates."""
    return geodesic(coord1, coord2).km


import networkx as nx
from geopy.distance import geodesic


def calculate_distance(coord1, coord2):
    """Calculate geodesic distance between two coordinates."""
    return geodesic(coord1, coord2).km

from geopy.distance import geodesic

def calculate_cartesian_positions(relatives, reference_point):
    """Convert geographic coordinates to Cartesian distances."""
    positions = {}
    for name, coords in relatives.items():
        x_distance = geodesic((reference_point[0], coords[1]), reference_point).km
        y_distance = geodesic((coords[0], reference_point[1]), reference_point).km

        # Adjust for direction (negative for left/down)
        x_distance *= -1 if coords[1] < reference_point[1] else 1
        y_distance *= -1 if coords[0] < reference_point[0] else 1
        positions[name] = (x_distance, y_distance)
    return positions



def normalize_positions(positions):
    """Normalize positions for visualization scaling."""
    x_values = [pos[0] for pos in positions.values()]
    y_values = [pos[1] for pos in positions.values()]
    min_x, max_x = min(x_values), max(x_values)
    min_y, max_y = min(y_values), max(y_values)

    normalized_positions = {
        name: (
            (pos[0] - min_x) / (max_x - min_x), 
            (pos[1] - min_y) / (max_y - min_y)
        )
        for name, pos in positions.items()
    }
    return normalized_positions


def build_graph(relatives, transport_modes, criterion="time"):
    """Build a graph from relatives and transport modes, optimizing for time, cost, or distance."""
    graph = nx.Graph()

    # Add random start point
    random_start = generate_random_start(relatives)
    relatives_dict = {relative["name"]: relative["coords"] for relative in relatives}
    relatives_dict["Random_Start"] = random_start["coords"]

    for name1, coords1 in relatives_dict.items():
        for name2, coords2 in relatives_dict.items():
            if name1 != name2:
                distance = calculate_distance(coords1, coords2)

                # Choose mode based on distance range
                if distance <= 0.5:
                    preferred_mode = "Walking"
                elif 0.5 < distance <= 2:
                    preferred_mode = "Bicycle"
                elif 2 < distance <= 5:
                    preferred_mode = "Bus"
                else:
                    preferred_mode = "Train"

                mode = next((m for m in transport_modes if m["mode"] == preferred_mode), None)
                if not mode:
                    continue

                transfer_time = mode["transfer_time_min"] / 60
                time = distance / mode["speed_kmh"] + transfer_time
                cost = distance * mode["cost_per_km"]

                graph.add_edge(
                    name1, name2,
                    weight={"time": time, "cost": cost, "distance": distance}[criterion],
                    time=time, cost=cost, distance=distance, mode=mode["mode"]
                )
    return graph







def find_optimized_route(graph, start, end, criterion):
    """Find the shortest path based on the given criterion."""
    print(f"Finding route with criterion: {criterion}")
    if start not in graph:
        raise ValueError(f"Start node '{start}' is not in the graph.")
    if end not in graph:
        raise ValueError(f"End node '{end}' is not in the graph.")
    
    if criterion == "time":
        path = nx.shortest_path(graph, source=start, target=end, weight="weight")
        total_time = sum(graph[path[i]][path[i + 1]]["weight"] for i in range(len(path) - 1))
        total_cost = sum(graph[path[i]][path[i + 1]]["cost"] for i in range(len(path) - 1))
    elif criterion == "cost":
        path = nx.shortest_path(graph, source=start, target=end, weight="cost")
        total_time = sum(graph[path[i]][path[i + 1]]["weight"] for i in range(len(path) - 1))
        total_cost = sum(graph[path[i]][path[i + 1]]["cost"] for i in range(len(path) - 1))
    else:
        raise ValueError("Invalid criterion. Choose 'time' or 'cost'.")
    
    return path, total_cost, total_time


import matplotlib.pyplot as plt
import networkx as nx


def visualize_graph(graph, path=None, relatives=None):
    """Visualize the graph using Matplotlib with accurate relative positions."""
    if not relatives:
        raise ValueError("Relatives dictionary with coordinates is required for accurate positions.")

    # Generate positions using latitude and longitude for all nodes
    pos = {node: (relatives[node][1], relatives[node][0]) for node in graph.nodes if node in relatives}

    # Add position for the Random_Start node if it exists
    if 'Random_Start' in graph.nodes and 'Random_Start' not in pos:
        random_start_coords = relatives.get('Random_Start')
        if random_start_coords:
            pos['Random_Start'] = (random_start_coords[1], random_start_coords[0])
        else:
            raise ValueError("Random_Start does not have valid coordinates in the relatives dictionary.")

    plt.figure(figsize=(12, 8))

    # Draw nodes and edges
    nx.draw(
        graph,
        pos,
        with_labels=True,
        node_color="skyblue",
        edge_color="gray",
        node_size=2500,
        font_size=10,
        font_weight="bold",
    )

    # Highlight path if provided
    if path:
        path_edges = list(zip(path, path[1:]))
        nx.draw_networkx_edges(
            graph,
            pos,
            edgelist=path_edges,
            edge_color="red",
            width=3,
            alpha=0.8,
        )
        nx.draw_networkx_nodes(
            graph,
            pos,
            nodelist=path,
            node_color="orange",
            node_size=3000,
        )

    # Add edge labels
    edge_labels = nx.get_edge_attributes(graph, "weight")  # Use weight as the label
    nx.draw_networkx_edge_labels(
        graph, pos, edge_labels={k: f"{v:.2f}" for k, v in edge_labels.items()}
    )

    # Add grid and explanations
    plt.grid(visible=True, which="both", color="lightgray", linestyle="--", alpha=0.7)
    plt.title("TarjanPlanner Graph Visualization", fontsize=16, fontweight="bold")
    plt.xlabel("Longitude", fontsize=12)
    plt.ylabel("Latitude", fontsize=12)

    # Add legend
    legend_elements = [
        plt.Line2D([0], [0], color="gray", lw=2, label="All Routes"),
        plt.Line2D([0], [0], color="red", lw=2, label="Optimal Route"),
        plt.Line2D(
            [0], [0], marker="o", color="w", markerfacecolor="skyblue", markersize=10, label="Relatives"
        ),
        plt.Line2D(
            [0], [0], marker="o", color="w", markerfacecolor="orange", markersize=10, label="Optimal Path Nodes"
        ),
    ]
    plt.legend(handles=legend_elements, loc="upper left", fontsize=10)

    plt.show()




def find_shortest_path_to_all_relatives(graph, start, criterion="time"):
    """Find the shortest path to visit all relatives based on the given criterion."""
    if start not in graph:
        raise ValueError(f"Start node '{start}' is not in the graph.")

    print(f"Starting point: {start}")
    nodes = list(graph.nodes)
    nodes.remove(start)
    print(f"Remaining nodes to visit: {nodes}")

    # Start timing
    start_time = time.time()

    shortest_path = None
    shortest_metric = float("inf")

    for perm in itertools.permutations(nodes):
        path = [start] + list(perm)  # Build the path
        total_metric = 0

        for i in range(len(path) - 1):
            from_node = path[i]
            to_node = path[i + 1]
            total_metric += graph[from_node][to_node][criterion]

        if total_metric < shortest_metric:
            shortest_metric = total_metric
            shortest_path = path

    # End timing
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"\n[LOG] Time taken to calculate the route: {elapsed_time:.2f} seconds")

    return shortest_path, shortest_metric