from tkinter import *

co0 = "#000000"  # preta
co1 = "#59656F"
co2 = "#feffff"  # branca
co3 = "#0074eb"  # azul
co4 = "#f04141"  # vermelho
co5 = "#59b356"  # verde
co6 = "#cdd1cd"  # cinza

janela = Tk()
janela.resizable(width=FALSE, height=FALSE)
janela.geometry('500x225')
janela.title('Lista de Tarefas')
janela.configure(background=co0)  # corrigido

# dividindo a janela em duas partes

frame_esquerda=Frame(janela, width=300, height=200, bg=co2)

janela.mainloop()
