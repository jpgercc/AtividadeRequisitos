import tkinter as tk
from gui import TreinoNadadorGUI
from timerer import Timerer

if __name__ == "__main__":
    root = tk.Tk()
    timer = Timerer()
    app = TreinoNadadorGUI(root, timer)
    root.mainloop()
