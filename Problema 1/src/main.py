import tkinter as tk
from gui import GUI
from timerer import timerer

if __name__ == "__main__": 
    timer = Timerer()
    root = tk.Tk()
    app = GUI(root, timer)
    root.mainloop()
