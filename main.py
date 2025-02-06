import tkinter as tk
from tkinter import ttk

# Create the main window
root = tk.Tk()
root.title("Pretty Table in GUI")
style = ttk.Style()

style.theme_use("default")

style.configure("Treeview",
                background="#2a2d2e",
                foreground="white",
                rowheight=25,
                fieldbackground="#343638",
                bordercolor="#343638",
                borderwidth=0)
style.map('Treeview', background=[('selected', '#22559b')])

style.configure("Treeview.Heading",
                background="#565b5e",
                foreground="white",
                relief="flat")
style.map("Treeview.Heading",background=[('active', '#3484F0')])

# Create a treeview (table) widget
tree = ttk.Treeview(root, columns=("Camera Name", "Latitude", "Longitude", "Altitude"), show="headings")

# Define the column headings
tree.heading("Camera Name", text="Camera Name")
tree.heading("Latitude", text="Latitude")
tree.heading("Longitude", text="Longitude")
tree.heading("Altitude", text="Altitude")

# Define the column widths
tree.column("Camera Name", width=150)
tree.column("Latitude", width=100)
tree.column("Longitude", width=100)
tree.column("Altitude", width=100)

# Add rows of data
tree.insert("", "end", values=("Camera A", 52.5200, 13.4050, 100))
tree.insert("", "end", values=("Camera B", 48.8566, 2.3522, 200))
tree.insert("", "end", values=("Camera C", 51.5074, -0.1278, 150))

# Add the treeview to the window
tree.pack(padx=10, pady=10)

# Start the Tkinter event loop
root.mainloop()


