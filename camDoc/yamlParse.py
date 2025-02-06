import tkinter as tk
from tkinter import ttk
import yaml
import csv 


### this will retrieve the information from the .ibt file, put em into a table to display, and export data into a excel
##copy paste the ony the data you want into a txt cause i was bored to to make it ignore and find the right thing since this was only a short side quest 





with open("cameras.txt", "r") as file:
    yaml_data = file.read()


# Parse the YAML data
data = yaml.safe_load(yaml_data)

# Function to process the groups and cameras data
def get_table_data(groups):
    table_data = []
    for group in groups:
        group_num = group['GroupNum']
        group_name = group['GroupName']
        is_scenic = group.get('IsScenic', False)
        cameras = group['Cameras']

        for camera in cameras:
            camera_num = camera['CameraNum']
            camera_name = camera['CameraName']
            table_data.append([group_num, group_name, camera_num, camera_name, is_scenic])
    
    return table_data

# Extract the table data
table_data = get_table_data(data['Groups'])

# Create the main window
root = tk.Tk()
root.title("Camera Groups Table")




# Create a treeview (table) widget
tree = ttk.Treeview(root, columns=("GroupNum", "GroupName", "CameraNum", "CameraName", "IsScenic"), show="headings")

# Define the column headings
tree.heading("GroupNum", text="GroupNum")
tree.heading("GroupName", text="GroupName")
tree.heading("CameraNum", text="CameraNum")
tree.heading("CameraName", text="CameraName")
tree.heading("IsScenic", text="IsScenic")

# Define the column widths
tree.column("GroupNum", width=100)
tree.column("GroupName", width=150)
tree.column("CameraNum", width=100)
tree.column("CameraName", width=150)
tree.column("IsScenic", width=100)

# Insert the data rows
for row in table_data:
    tree.insert("", "end", values=row)

# Add the treeview to the window
tree.pack(padx=10, pady=10)

# Function to export data to CSV
def export_to_csv():
    with open("camera_groups.csv", mode="w", newline="") as file:
        writer = csv.writer(file)
        # Write the header
        writer.writerow(["GroupNum", "GroupName", "CameraNum", "CameraName", "IsScenic"])
        # Write the data rows
        writer.writerows(table_data)
    print("Data exported to camera_groups.csv")



# Button to export the table to CSV
export_button = tk.Button(root, text="Export to CSV", command=export_to_csv)
export_button.pack(pady=10)

# Start the Tkinter event loop
root.mainloop()



