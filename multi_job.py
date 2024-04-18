import tkinter as tk
import subprocess
import os
from tkinter import filedialog
import re

class MultiJobApp:
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(self.master)
        self.frame.pack()

        # Image File Input
        self.label_image_file = tk.Label(self.frame, text=f"(Source) Image Files:")
        self.label_image_file.grid(row=0, column=0, padx=5, pady=5)
        self.entry_image_file = tk.Text(self.frame, height=10, width=40)
        self.entry_image_file.grid(row=0, column=1, padx=25, pady=5)


        # Video File Input
        self.label_video_file = tk.Label(self.frame, text="(Target) Video Files:")
        self.label_video_file.grid(row=1, column=0, padx=5, pady=5)
        self.entry_video_file = tk.Text(self.frame, height=10, width=40)
        self.entry_video_file.grid(row=1, column=1, padx=25, pady=5)


        # Create a button to open file explorer
        self.open_img_button = tk.Button(self.frame, text="Find Image Source(s)", command=self.open_image_file_explorer)
        self.open_img_button.grid(row=3, column=0, columnspan=2, padx=25, pady=5)

        # Create a button to open file explorer
        self.open_vid_button = tk.Button(self.frame, text="Find Video Target(s)", command=self.open_video_file_explorer)
        self.open_vid_button.grid(row=4, column=0, columnspan=2, padx=25, pady=5)

        # Execute Button
        self.execute_button = tk.Button(self.frame, text="Execute", command=self.execute_command)
        self.execute_button.grid(row=5, column=0, columnspan=2, padx=5, pady=5)

    def execute_command(self):
        image_file = self.entry_image_file.get("1.0", tk.END).strip().split('\n')
        video_file = self.entry_video_file.get("1.0", tk.END).strip().split('\n')
        images = "".join(f"--source \"{s}\" " for s in image_file)
        videos = "".join(f"--target \"{s}\" " for s in video_file)
        videos = re.split(r'\s*(?=\-\-)', videos)
        videos = [item.strip() for item in videos]

        #venv_dir = os.path.join(os.path.dirname(__file__), "venv")
        #python_executable = os.path.join(venv_dir, "Scripts", "python.exe")
        script_path = os.path.join(os.path.dirname(__file__), "run.py")

        for arg in videos:
            if arg:
                try:
                    #command = f'{python_executable} {script_path} {images} --target "{arg}" --headless'
                    command = f"conda activate facefusion && python {script_path} {images}{arg} --headless"
                    print("Execute command:")
                    print(command)
                    subprocess.run(command, check=True, text=True, capture_output=True, shell=True)
                    print("Subprocess executed successfully for argument:", arg)
                except subprocess.CalledProcessError as e:
                    print("Subprocess execution failed for argument:", arg, "Error:", e)

    # Handle file explorers
    def open_image_file_explorer(self):
        file_path = filedialog.askopenfilenames()
        self.entry_image_file.delete("1.0", tk.END)
        for x in file_path:
            print("Selected image(s):", x)
            self.entry_image_file.insert(tk.END,x)
            self.entry_image_file.insert(tk.END, "\n")

    def open_video_file_explorer(self):
        file_path = filedialog.askopenfilenames()
        self.entry_video_file.delete("1.0", tk.END)
        for x in file_path:
            print("Selected video(s):", x)
            self.entry_video_file.insert(tk.END,x)
            self.entry_video_file.insert(tk.END, "\n")

    def start(self):
        self.master.mainloop()
