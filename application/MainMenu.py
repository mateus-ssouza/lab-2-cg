from tkinter import *

from tela_circunferencia import *
from tela_reta import *


def renderReta():
    tr = TelaReta(master)



def renderCircunferencia():
    tr = TelaCircunferencia(master)


master = Tk()
master.configure(bg="white")

screen_width = 600
screen_height = 200

master.geometry("%dx%d+0+0" % (screen_width, screen_height))  # largura, altura, dist esquerda + dist topo
master.wm_resizable(width=False, height=False)  # travando a tela na resolução definida

widget1 = Frame(master)
widget1.configure(bg="white")
widget1.place(bordermode=OUTSIDE, height=100, width=500, x=50)
label = Label(widget1,text="Desenho de Primitivas Gráficas", bg="white")
label["font"] = ("Verdana", "20", "italic", "bold")
label.pack()

btnReta= Button(master,text="Retas",command=renderReta,bg="#3D86FC",fg="white",width=13)
btnReta.place(x=100,y=100)
btnReta["font"] = ("Verdana", "10", "italic", "bold")

btnCircunferencia = Button(master,text="Circunferencias",command=renderCircunferencia,bg="#3D86FC",fg="white",width=13)
btnCircunferencia.place(x=350,y=100)
btnCircunferencia["font"] = ("Verdana", "10", "italic", "bold")


if __name__ == "__main__":

    master.mainloop()

