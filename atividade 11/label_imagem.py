from tkinter import *

janela = Tk()

info = "esse texto será\nexibido no rótulo\nem varias linhas."

rotulo = Label(janela, text=info, justify="left")
rotulo.grid(row=0, column=0)

logo = PhotoImage(file="logo.png")
rotulo2 = Label(janela, image = logo)
rotulo2.grid(row=0, column=1)

janela.mainloop()