import os
from matplotlib import pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from tkinter import Toplevel

def get_file_counts(directory, file_types):
    """
    Counts the number of files in each categorized folder.

    Parameters:
        directory (str): The directory to analyze.
        file_types (dict): Mapping of file extensions to categories.

    Returns:
        dict: A dictionary with category names as keys and file counts as values.
    """
    counts = {folder: 0 for folder in set(file_types.values())}
    counts["Others"] = 0  # Add "Others" folder for unknown types

    # Traverse the directory to count files in categorized folders
    for folder, count in counts.items():
        folder_path = os.path.join(directory, folder)
        if os.path.exists(folder_path):
            counts[folder] = len(os.listdir(folder_path))
    return counts


from tkinter import Toplevel
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


def show_chart(file_counts, parent):
    """
    Displays a bar chart of file counts for each category.

    Parameters:
        file_counts (dict): Dictionary with file categories and their counts.
        parent (tkinter.Tk or tkinter.Toplevel): Parent window for the chart.
    """
    categories = list(file_counts.keys())
    counts = list(file_counts.values())

    # Create a new chart window
    chart_window = Toplevel(parent)
    chart_window.title("File Organization Summary")
    chart_window.geometry("800x600")

    # Create the figure and bar chart
    fig = Figure(figsize=(8, 6), dpi=100)
    ax = fig.add_subplot(111)
    bars = ax.bar(categories, counts, color="skyblue", edgecolor="black")
    ax.set_title("File Organization Summary", fontsize=16)
    ax.set_xlabel("File Categories", fontsize=14)
    ax.set_ylabel("Number of Files", fontsize=14)
    ax.tick_params(axis="x", rotation=45)
    ax.grid(axis="y", linestyle="--", alpha=0.7)

    # Annotate bars with counts
    for bar, count in zip(bars, counts):
        ax.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 0.5, str(count), ha="center", fontsize=10)

    # Embed the chart in the Tkinter window
    canvas = FigureCanvasTkAgg(fig, master=chart_window)
    canvas.draw()
    canvas.get_tk_widget().pack(fill="both", expand=True)

