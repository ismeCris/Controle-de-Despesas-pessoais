from tkinter import *
from tkinter import ttk,Tk

################# cores ###############
co0 = "#2e2d2b"  # Preta
co1 = "#feffff"  # branca
co2 = "#4fa882"  # verde
co3 = "#38576b"  # valor
co4 = "#403d3d"   # letra
co5 = "#e06636"   # - profit
co6 = "#038cfc"   # azul
co7 = "#3fbfb9"   # verde
co8 = "#263238"   # + verde
co9 = "#e9edf5"   # + verde

colors = ['#5588bb', '#66bbbb','#99bb55', '#ee9944', '#444466', '#bb5555']

#Criando janela
janela = Tk()
janela.title("Controle Financeiro")
janela.geometry('900x650')
janela.configure(background=co9)
janela.resizable(width=FALSE, height=FALSE)


style = ttk.Style(janela)
style.theme_use("clam")


#criando frames
frame_cima = Frame(janela, width=1043, height=50, bg=co1, relief="flat")
frame_cima.grid(row=0, column=0, sticky=NSEW)

frame_meio = Frame(janela, width=1043, height=361, bg=co1, padx=20, relief="raised")
frame_meio.grid(row=1,column=0, pady=1, padx=0, sticky=NSEW)

frame_baixo = Frame(janela, width=1043, height=300, bg=co1, relief="flat")
frame_baixo.grid(row=2, column=0, pady=1, padx=10, sticky=NSEW)

janela.mainloop()


