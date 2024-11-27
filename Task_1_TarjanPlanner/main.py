import time
from colorama import Fore, Style
from prettytable import PrettyTable
from TarjanPlanner.io_utils import load_data, get_user_input, map_number_to_relative
from TarjanPlanner.graph_utils import (
    build_graph,
    find_optimized_route,
    visualize_graph,
    find_shortest_path_to_all_relatives,
    generate_random_start
)
from TarjanPlanner.transport_utils import load_transport_modes


def log_runtime(func):
    """Decorator to log runtime of a function."""
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        runtime = end_time - start_time
        print(f"\n[LOG] Function '{func.__name__}' executed in {runtime:.2f} seconds.\n")
        return result, runtime
    return wrapper


@log_runtime
def process_single_relative(graph, relatives):
    """Process visiting one relative."""
    start, end, criterion = get_user_input(relatives)
    print(f"Processing route from {start} to {end} with criterion: {criterion}.")
    route, cost, travel_time = find_optimized_route(graph, start, end, criterion)
    print(f"Optimal Route: {route}")
    print(f"Total Cost: {cost:.2f} units")
    print(f"Total Time: {travel_time:.2f} hours")
    visualize_graph(graph, path=route)
    return route, cost, travel_time


@log_runtime
@log_runtime
def process_all_relatives(graph, start, criterion):
    """Process visiting all relatives."""
    print(f"Processing shortest path to visit all relatives starting from {start}.")
    path, total_metric = find_shortest_path_to_all_relatives(graph, start, criterion)
    if criterion == "time":
        print(f"Shortest Path: {path}, Total Time: {total_metric:.2f} hours.")
    else:
        print(f"Shortest Path: {path}, Total Cost: {total_metric:.2f} units.")

    # Ensure path is passed correctly
    display_route_table(graph, path)
    visualize_graph(graph, path=path)
    return path, total_metric



def get_mode_color(mode):
    """Assign colors to different modes of transportation."""
    colors = {
        "Bus": Fore.RED,
        "Train": Fore.BLUE,
        "Bicycle": Fore.GREEN,
        "Walking": Fore.YELLOW,
    }
    return colors.get(mode, Fore.WHITE) + mode + Style.RESET_ALL


def display_route_table(graph, path):
    """Display a table of distances, times, and costs with modes of transportation."""
    if not isinstance(path, (list, tuple)):
        raise ValueError("Path must be a list or tuple of node identifiers.")

    table = PrettyTable()
    table.field_names = ["Step", "From", "To", "Mode", "Distance (km)", "Time (hours)", "Cost (units)"]
    total_distance = total_time = total_cost = 0

    for i in range(len(path) - 1):
        from_node = path[i]
        to_node = path[i + 1]
        edge_data = graph[from_node][to_node]
        mode = edge_data.get("mode", "Unknown")
        distance = edge_data.get("distance", 0)
        time = edge_data.get("time", 0)
        cost = edge_data.get("cost", 0)

        total_distance += distance
        total_time += time
        total_cost += cost

        table.add_row(
            [i + 1, from_node, to_node, get_mode_color(mode), f"{distance:.2f}", f"{time:.2f}", f"{cost:.2f}"]
        )

    table.add_row(
        ["Total", "-", "-", "-", f"{total_distance:.2f}", f"{total_time:.2f}", f"{total_cost:.2f}"]
    )
    print("\nRoute Details:")
    print(table)



def main():
    print("Starting TarjanPlanner...\n")

    # Load relatives and transport modes
    try:
        relatives = load_data("data/relatives.csv")
        print(f"Loaded {len(relatives)} relatives.")
        transport_modes = load_transport_modes("data/transport_modes.json")
        print(f"Loaded {len(transport_modes)} transport modes.")
    except FileNotFoundError as e:
        print(f"Error loading data: {e}")
        return

    # Generate random start location
    random_start = generate_random_start(relatives)
    print(f"Generated random start location at: {random_start['coords']}.\n")

    # Prompt user to choose optimization criterion
    criterion = input("Optimize for time, cost, or distance? (time/cost/distance): ").strip().lower()
    if criterion not in ["time", "cost", "distance"]:
        print("Invalid criterion. Please choose 'time', 'cost', or 'distance'.")
        return

    # Build the graph with the chosen optimization criterion
    graph = build_graph(relatives, transport_modes, criterion=criterion)
    print(f"Graph built: {len(graph.nodes)} nodes, {len(graph.edges)} edges.\n")

    # Prompt user for mode of operation
    mode = input("Choose mode: 1 (Visit one relative) or 2 (Visit all relatives): ").strip()

    if mode == "1":
        # Visit one relative
        try:
            start = "Random_Start"
            end, _ = get_user_input(relatives)
            route, cost, time, distance = find_optimized_route(graph, start, end, criterion)
            print(f"Optimal Route: {route}")
            print(f"Total Distance: {distance:.2f} km")
            print(f"Total Cost: {cost:.2f} units")
            print(f"Total Time: {time:.2f} hours")
            visualize_graph(graph, path=route)
        except Exception as e:
            print(f"Error in single relative processing: {e}")

    elif mode == "2":
        # Visit all relatives
        try:
            start = "Random_Start"
            path, total_metric = find_shortest_path_to_all_relatives(graph, start, criterion)
            print(f"Shortest Path: {path}")
            if criterion == "time":
                print(f"Total Time: {total_metric:.2f} hours")
            elif criterion == "cost":
                print(f"Total Cost: {total_metric:.2f} units")
            else:
                print(f"Total Distance: {total_metric:.2f} km")
            display_route_table(graph, path)
            visualize_graph(graph, path=path)
        except Exception as e:
            print(f"Error in all relatives processing: {e}")
    else:
        print("Invalid mode selected. Please choose 1 or 2.")


if __name__ == "__main__":
    main()
