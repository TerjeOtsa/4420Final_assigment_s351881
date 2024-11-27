import tkinter as tk
from tkinter import messagebox
from TarjanPlanner.io_utils import load_data, generate_random_start
from TarjanPlanner.graph_utils import (
    build_graph,
    find_optimized_route,
    visualize_graph,
    find_shortest_path_to_all_relatives,
)
from TarjanPlanner.transport_utils import load_transport_modes
from TarjanPlanner.display_utils import display_route_table


def run_optimizer():
    """Handle the optimization based on user input."""
    criterion = optimization_criteria.get()
    mode = mode_selection.get()

    if criterion not in ["time", "cost", "distance"]:
        messagebox.showerror("Error", "Please select a valid optimization criterion.")
        return

    try:
        # Load relatives and transport modes
        relatives = load_data("data/relatives.csv")
        transport_modes = load_transport_modes("data/transport_modes.json")
        graph = build_graph(relatives, transport_modes, criterion=criterion)

        # Generate a random starting point
        random_start = generate_random_start(relatives, max_distance=5)
        start_location = random_start["coords"]

        if mode == "1":
            # Visit one relative from the generated start point
            end = end_input.get().strip()
            if not end:
                messagebox.showerror("Error", "Please enter an end relative.")
                return

            route, cost, time, distance = find_optimized_route(graph, random_start["name"], end, criterion)
            result_display.delete(1.0, tk.END)  # Clear previous results
            result_display.insert(
                tk.END,
                f"Generated Start Location: {random_start['name']} (Lat: {start_location[0]:.4f}, "
                f"Long: {start_location[1]:.4f})\n"
                f"Optimal Route: {route}\n"
                f"Total Cost: {cost:.2f} units\n"
                f"Total Time: {time:.2f} hours\n"
                f"Total Distance: {distance:.2f} km\n"
            )
            display_route_table(graph, route)
            visualize_graph(graph, path=route)

        elif mode == "2":
            # Visit all relatives from the generated start point
            path, metric = find_shortest_path_to_all_relatives(graph, random_start["name"], criterion)
            result_display.delete(1.0, tk.END)  # Clear previous results
            result_display.insert(
                tk.END,
                f"Generated Start Location: {random_start['name']} (Lat: {start_location[0]:.4f}, "
                f"Long: {start_location[1]:.4f})\n"
                f"Shortest Path to Visit All Relatives: {path}\n"
                f"Total {criterion.capitalize()}: {metric:.2f}\n"
            )
            display_route_table(graph, path)
            visualize_graph(graph, path=path)

        else:
            messagebox.showerror("Error", "Please select a valid mode.")

    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")


# Create the main window
window = tk.Tk()
window.title("TarjanPlanner")
window.geometry("600x400")

# Optimization Criteria
tk.Label(window, text="Optimization Criterion:").pack(pady=5)
optimization_criteria = tk.StringVar(value="time")
tk.Radiobutton(window, text="Time", variable=optimization_criteria, value="time").pack()
tk.Radiobutton(window, text="Cost", variable=optimization_criteria, value="cost").pack()
tk.Radiobutton(window, text="Distance", variable=optimization_criteria, value="distance").pack()

# Mode Selection
tk.Label(window, text="Mode Selection:").pack(pady=5)
mode_selection = tk.StringVar(value="1")
tk.Radiobutton(window, text="Visit One Relative", variable=mode_selection, value="1").pack()
tk.Radiobutton(window, text="Visit All Relatives", variable=mode_selection, value="2").pack()

# End Input (for "Visit One Relative" mode only)
tk.Label(window, text="End Relative (Number or Name, only for 'Visit One Relative'):").pack(pady=5)
end_input = tk.Entry(window)
end_input.pack()

# Run Button
tk.Button(window, text="Run", command=run_optimizer).pack(pady=20)

# Result Display (Scrollable Text Widget for Wrapping)
result_display_frame = tk.Frame(window)
result_display_frame.pack(fill="both", expand=True, padx=10, pady=10)

scrollbar = tk.Scrollbar(result_display_frame)
scrollbar.pack(side="right", fill="y")

result_display = tk.Text(result_display_frame, wrap="word", yscrollcommand=scrollbar.set, height=10, width=60)
result_display.pack(side="left", fill="both", expand=True)
scrollbar.config(command=result_display.yview)

# Start the GUI loop
window.mainloop()
