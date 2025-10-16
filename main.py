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

frame_esquerda=Frame(janela, width=300, height=200, bg=co2, relief="flat")
frame_esquerda.grid(row=0, column=0, sticky=NSEW)

frame_direita=Frame(janela, width=200, height=250, bg=co2, relief="flat")
frame_direita.grid(row=0, column=1, sticky=NSEW)


# dividino o frame a esquerda em duas partes ###

frame_e_cima=Frame(frame_esquerda, width=300, height=50, bg=co2, relief="flat")
frame_e_cima.grid(row=0, column=0, sticky=NSEW)

frame_e_baixo=Frame(frame_esquerda, width=300, height=150, bg=co2, relief="flat")
frame_e_baixo.grid(row=1, column=0, sticky=NSEW)

# Criação de botões novo, remover e atualizar

b_novo = Button(frame_e_cima,text="Novo", width=10, height=1,bg=co3,fg="white", font=5,anchor="center", relief=RAISED)

b_novo.grid(row=0, column=0, sticky=NSEW,pady=1)

b_remover = Button(frame_e_cima,text="Remover", width=10, height=1,bg=co4,fg="white", font=5,anchor="center", relief=RAISED)

b_remover.grid(row=0, column=1, sticky=NSEW,pady=1)

b_atualizar = Button(frame_e_cima,text="Atualizar", width=10, height=1,bg=co5,fg="white", font=5,anchor="center", relief=RAISED)

b_atualizar.grid(row=0, column=2, sticky=NSEW,pady=1)

#### Adicionando Listbox e um label

label = Label(frame_direita,text="Tarefas",width=37,height=1,pady=7,padx=10,relief="flat",anchor=W,font=("Courier 14 bold"),fg=co0,bg=co2)

label.grid(row=0, column=0, sticky=NSEW,pady=1)

listbox = Listbox(frame_direita, font=("Courier 9 bold"), width=1)

listbox.grid(row=1, column=0, sticky=NSEW,pady=1)

#### Adicionando tarefas na listbox

tarefas = ["Pagar contas", "Realizar um site", "Fazer o curso de Back-End","Ir para a faculdade"]

for item in tarefas:
    listbox.insert(END,item)

janela.mainloop()
