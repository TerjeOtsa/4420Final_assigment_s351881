import os
import logging
import tkinter as tk
from tkinter import filedialog, messagebox
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib import pyplot as plt
from file_sorter import organize_files
from logger import setup_logging
from charts import get_file_counts, show_chart
from config import FILE_TYPES


class FileOrganizerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("File Organizer")
        self.root.geometry("600x400")
        
        # Configure grid layout
        self.root.grid_columnconfigure(0, weight=1)
        self.root.grid_rowconfigure(0, weight=1)

        # Create GUI elements
        self.label = tk.Label(root, text="Welcome to the File Organizer!", font=("Arial", 16))
        self.label.grid(row=0, column=0, pady=10, padx=10)

        self.choose_button = tk.Button(root, text="Choose Folder", command=self.choose_directory, font=("Arial", 12), bg="lightblue")
        self.choose_button.grid(row=1, column=0, pady=10)

        self.organize_button = tk.Button(root, text="Organize Files", command=self.organize_files, font=("Arial", 12), bg="green", fg="white", state=tk.DISABLED)
        self.organize_button.grid(row=2, column=0, pady=10)

        self.exit_button = tk.Button(root, text="Exit", command=root.quit, font=("Arial", 12), bg="red", fg="white")
        self.exit_button.grid(row=3, column=0, pady=10)

        self.status_label = tk.Label(root, text="", font=("Arial", 10), fg="green")
        self.status_label.grid(row=4, column=0, pady=10)

        self.directory = ""

    def choose_directory(self):
        """Prompt the user to choose a directory."""
        self.directory = filedialog.askdirectory(title="Select Folder to Organize")
        if self.directory:
            self.status_label.config(text=f"Selected Directory: {self.directory}", fg="blue")
            self.organize_button.config(state=tk.NORMAL)
        else:
            self.status_label.config(text="No directory selected.", fg="red")
            self.organize_button.config(state=tk.DISABLED)

    def organize_files(self):
        """Organize the files and display the chart."""
        if not os.path.exists(self.directory):
            messagebox.showerror("Error", "The selected directory does not exist.")
            self.status_label.config(text="Error: Directory does not exist.", fg="red")
            return

        try:
            # Organize files
            logging.info(f"Starting file organization for directory: {self.directory}")
            organize_files(self.directory)
            logging.info("File organization completed successfully.")

            # Count files in each category
            file_counts = get_file_counts(self.directory, FILE_TYPES)
            total_files = sum(file_counts.values())

            # Display success message and chart
            self.status_label.config(text=f"Organized {total_files} files successfully!", fg="green")
            show_chart(file_counts, self.root)
        except Exception as e:
            logging.error(f"An error occurred: {str(e)}")
            messagebox.showerror("Error", f"An error occurred: {str(e)}")
            self.status_label.config(text="Error during file organization.", fg="red")


def main():
    setup_logging()
    root = tk.Tk()
    app = FileOrganizerApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
