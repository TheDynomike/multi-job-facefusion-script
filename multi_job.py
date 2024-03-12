import tkinter as tk
import subprocess
import os
from tkinter import filedialog, Entry

def execute_command():
    image_file = entry_image_file.get("1.0", tk.END).strip().split('\n')
    video_file = entry_video_file.get("1.0", tk.END).strip().split('\n')
    images = "".join(f'--source {s} ' for s in image_file)

    venv_dir = os.path.join(os.path.dirname(__file__), "venv")
    python_executable = os.path.join(venv_dir, "Scripts", "python.exe")
    script_path = os.path.join(os.path.dirname(__file__), "run.py")
    
    for arg in video_file:
        if arg:
            try:
                command = f'{python_executable} {script_path} {images} --target "{arg}" --headless'
                print("Execute command:")
                print(command)
                subprocess.run(command, check=True, text=True, capture_output=True)
                print("Subprocess executed successfully for argument:", arg)
            except subprocess.CalledProcessError as e:
                print("Subprocess execution failed for argument:", arg, "Error:", e)

# Handle file explorers
def open_image_file_explorer():
    file_path = filedialog.askopenfilenames()
    entry_image_file.delete("1.0", tk.END)
    for x in file_path:
        print("Selected image(s):", x)
        entry_image_file.insert(tk.END,x)
        entry_image_file.insert(tk.END, "\n")

def open_video_file_explorer():
    file_path = filedialog.askopenfilenames()
    entry_video_file.delete("1.0", tk.END)
    for x in file_path:
        print("Selected video(s):", x)
        entry_video_file.insert(tk.END,x)
        entry_video_file.insert(tk.END, "\n")

# Create main window
root = tk.Tk()
root.title("CLI Command Executor")

# Image File Input
label_image_file = tk.Label(root, text=f"Image Files:")
label_image_file.grid(row=0, column=0, padx=5, pady=5)
entry_image_file = tk.Text(root, height=10, width=40)
entry_image_file.grid(row=0, column=1, padx=25, pady=5)


# Video File Input
label_video_file = tk.Label(root, text="Video Files:")
label_video_file.grid(row=1, column=0, padx=5, pady=5)
entry_video_file = tk.Text(root, height=10, width=40)
entry_video_file.grid(row=1, column=1, padx=25, pady=5)


# Create a button to open file explorer
open_img_button = tk.Button(root, text="Find Image Source(s)", command=open_image_file_explorer)
open_img_button.grid(row=3, column=0, columnspan=2, padx=25, pady=5)

# Create a button to open file explorer
open_vid_button = tk.Button(root, text="Find Video Target(s)", command=open_video_file_explorer)
open_vid_button.grid(row=4, column=0, columnspan=2, padx=25, pady=5)

# Execute Button
execute_button = tk.Button(root, text="Execute", command=execute_command)
execute_button.grid(row=5, column=0, columnspan=2, padx=25, pady=25)

root.mainloop()
