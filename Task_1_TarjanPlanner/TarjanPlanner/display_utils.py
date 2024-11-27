from prettytable import PrettyTable
from colorama import Fore, Style


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
