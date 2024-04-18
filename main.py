import tkinter as tk
from tkinter import ttk
from video_trimmer import VideoTrimmerApp
from multi_job import MultiJobApp

class MainApp:
    def __init__(self, master):
        self.master = master
        self.master.title("FF Tools")
        
        self.notebook = ttk.Notebook(self.master)

        self.tab1 = tk.Frame(self.notebook)
        self.tab2 = tk.Frame(self.notebook)

        self.notebook.add(self.tab1, text='Multi Job Queue')
        self.notebook.add(self.tab2, text='Video Trimmer')
        self.notebook.pack(expand=1, fill='both')

        self.app1 = MultiJobApp(self.tab1)
        self.app2 = VideoTrimmerApp(self.tab2)

        # Start each app
        self.app1.start()
        self.app2.start()

def main():
    root = tk.Tk()
    app = MainApp(root)
    root.mainloop()

if __name__ == '__main__':
    main()
