#texto com varias linhas

from tkinter import *

janela = Tk()

info = "esse texto será\nexibido no rótulo\nem varias linhas."

rotulo = Label(janela, text=info, justify="left")
rotulo.grid(row=0, column=0)

info2 = """assim também 
é possivel
ter varias linhas."""

rotulo2 = Label(janela, text=info2, justify="right")
rotulo2.grid(row=2, column=0)

janela.mainloop()
