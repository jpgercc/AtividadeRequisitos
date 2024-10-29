import tkinter as tk
from gui import GUI
from timerer import Timerer
#q: EXPLIQUE O NOME E O FORMADO DE "if __name__ == "__main__":"
#r: O nome da função é __main__ e o formato é um if statement que verifica se o módulo está sendo executado como um programa principal. Se o módulo for importado, o bloco de código dentro do if statement não será executado.
if __name__ == "__main__": 
    timer = Timerer()
    root = tk.Tk()
    app = GUI(root, timer)
    root.mainloop()
