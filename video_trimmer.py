import tkinter as tk
from tkinter import filedialog, messagebox
import subprocess
import os
import cv2

class VideoTrimmerApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Video Trimmer")

        self.frame = tk.Frame(self.master)
        self.frame.pack()

        self.input_label = tk.Label(self.frame, text="Input Video:")
        self.input_label.grid(row=0, column=0)

        self.input_entry = tk.Entry(self.frame, width=50)
        self.input_entry.grid(row=0, column=1)

        self.browse_button = tk.Button(self.frame, text="Browse", command=self.browse_video)
        self.browse_button.grid(row=0, column=2)

        self.output_label = tk.Label(self.frame, text="Output Video:")
        self.output_label.grid(row=1, column=0)

        self.output_entry = tk.Entry(self.frame, width=50)
        self.output_entry.grid(row=1, column=1)

        self.open_folder_button = tk.Button(self.frame, text="Open Folder", command=self.open_output_folder)
        self.open_folder_button.grid(row=1, column=2)

        self.start_label = tk.Label(self.frame, text="Start Time:")
        self.start_label.grid(row=2, column=0)

        self.start_slider = tk.Scale(self.frame, from_=0, to=100, orient=tk.HORIZONTAL, command=self.update_start_time)
        self.start_slider.grid(row=2, column=1, sticky="ew")

        self.end_label = tk.Label(self.frame, text="End Time:")
        self.end_label.grid(row=3, column=0)

        self.end_slider = tk.Scale(self.frame, from_=0, to=100, orient=tk.HORIZONTAL, command=self.update_end_time)
        self.end_slider.grid(row=3, column=1, sticky="ew")

        self.trim_button = tk.Button(self.frame, text="Trim Video", command=self.trim_video)
        self.trim_button.grid(row=4, column=1)

        self.video_duration = 0

    def browse_video(self):
        filename = filedialog.askopenfilename(filetypes=[("Video files", "*.mp4 *.avi *.mkv")])
        self.input_entry.delete(0, tk.END)
        self.input_entry.insert(0, filename)
        output_file = os.path.splitext(filename)[0] + "_trimmed" + os.path.splitext(filename)[1]
        self.output_entry.delete(0, tk.END)
        self.output_entry.insert(0, output_file)
        self.update_sliders()

    def open_output_folder(self):
        output_file = self.output_entry.get()
        output_folder = os.path.dirname(output_file)
        output_folder = output_folder.replace('/', os.path.sep)  # Replace forward slashes with correct separator
        if os.path.exists(output_folder):
            subprocess.Popen(['explorer', output_folder])
        else:
            messagebox.showerror("Error", f"Output folder does not exist: {output_folder}")


    def update_sliders(self):
        input_file = self.input_entry.get()
        cap = cv2.VideoCapture(input_file)
        self.video_duration = int(cap.get(cv2.CAP_PROP_FRAME_COUNT) / cap.get(cv2.CAP_PROP_FPS))
        cap.release()

        self.start_slider.config(to=self.video_duration)
        self.end_slider.config(to=self.video_duration)
        self.start_slider.set(0)
        self.end_slider.set(self.video_duration)

    def update_start_time(self, value):
        start_time = int(value)
        end_time = int(self.end_slider.get())
        if start_time >= end_time:
            self.start_slider.set(end_time - 1)

    def update_end_time(self, value):
        end_time = int(value)
        start_time = int(self.start_slider.get())
        if end_time <= start_time:
            self.end_slider.set(start_time + 1)

    def trim_video(self):
        input_file = self.input_entry.get()
        output_file = self.output_entry.get()
        start_time = self.start_slider.get()
        end_time = self.end_slider.get()

        command = ['ffmpeg', '-i', input_file, '-ss', str(start_time), '-to', str(end_time), '-c', 'copy', output_file]

        try:
            subprocess.run(command, check=True)
            messagebox.showinfo("Success", "Video trimmed and saved successfully!")
        except subprocess.CalledProcessError as e:
            messagebox.showerror("Error", f"Error occurred: {e}")

def main():
    root = tk.Tk()
    app = VideoTrimmerApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
