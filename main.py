import tkinter as tk
import pandas as pd

# Global variables
current_index = 0
data = None
output_file = 'modified_gpass.csv'

def load_data():
    global data
    data = pd.read_csv('gpass.csv')

def update_labels():
    global current_index, data

    if current_index >= len(data):
        # All entries processed
        name_label.config(text="End of entries")
        url_label.config(text="")
        username_label.config(text="")
        password_label.config(text="")
    else:
        row = data.iloc[current_index]
        name_label.config(text="Name: " + str(row['name']))
        url_label.config(text="URL: " + str(row['url']))
        username_label.config(text="Username: " + str(row['username']))
        password_label.config(text="Password: " + str(row['password']))

def delete_entry():
    global current_index, data

    if current_index < len(data):
        data.drop(current_index, inplace=True)
        data.reset_index(drop=True, inplace=True)

    current_index += 1
    update_labels()

def keep_entry():
    global current_index

    current_index += 1
    update_labels()

def save_data():
    global data, output_file

    data.to_csv(output_file, index=False)
    print("Data saved to", output_file)

# Create the GUI window
window = tk.Tk()
window.title("Delete Unused Credentials")
window.geometry("400x200")  # Set the window size (width x height)

# Load the data
load_data()

# Create labels
name_label = tk.Label(window, text="Name:")
name_label.pack()
url_label = tk.Label(window, text="URL:")
url_label.pack()
username_label = tk.Label(window, text="Username:")
username_label.pack()
password_label = tk.Label(window, text="Password:")
password_label.pack()

# Create buttons
delete_button = tk.Button(window, text="Delete", command=delete_entry)
delete_button.pack(side=tk.LEFT, padx=10, pady=10)
keep_button = tk.Button(window, text="Keep", command=keep_entry)
keep_button.pack(side=tk.RIGHT, padx=10, pady=10)

# Save button
save_button = tk.Button(window, text="Save", command=save_data)
save_button.pack(pady=10)

# Update the labels with the first entry
update_labels()

# Start the GUI event loop
window.mainloop()
