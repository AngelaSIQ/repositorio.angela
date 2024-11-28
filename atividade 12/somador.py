from tkinter import *

janela = Tk()
janela.tittle("Somador")
janela.geometry("200x100+100+100")

rotulo1 = Label(janela, text="Valor 1:")
rotulo1.grid(row=0, column=0)

campo1 = Entry(janela)
campo1.grid(row=0, column=1)

rotulo2 = Label(janela, text="Valor 2:")
rotulo2.grid(row=1, column=0)

campo2 = Entry(janela)
campo2.grid(row=1, column=1)

rotulo3 = Label(janela, text="SOMA =")
rotulo3.grid(row=3, column=0)

campo3 = Entry(janela)
campo3.grid(row=3, column=1)

def somar():
    v1 = int(campo1.get())
    v2 = int(campo2.get())
    soma = v1+v2
    campo3.delete(0,END)
    campo3.insert(0,soma)

botao = Button(janela)
botao.grid(row=2, column=1)
botao["width"] = 15
botao["text"] = "Somar"
botao["command"] = somar

janela.mainloop()

#1 - modifique o programa "somador para que o campo TOTAL nao possa ser apagado manualmente dica use a propriedade "state" no campo

#2 - transforme o somador numa calculadora de 4 operacoes com soma, subtração, multiplicação e divisão, crie um botao para cada operação

#3 - faça uma tela de login onde se digite 
#o usuario e a senha e um botão "entrar"
#o campo da senha nao de ve exibir os 
#caracteres ao digitar. 
#dica use a propriedade "show" do campo
#mostre as mensagens de acesso permitido ou acesso negado em uma caixa de mensagem

