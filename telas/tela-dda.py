from tkinter import *
import math

def calculoDDA():
    
    x0Aux = str(entradaX0.get())
    y0Aux = str(entradaY0.get())
    x1Aux = str(entradaX1.get())
    y1Aux = str(entradaY1.get())
    
    if(x0Aux.find("-") != -1):
        x0Aux = entradaX0.get().replace("-", "")
        x0Aux = int(x0Aux) * -1
        
    if(y0Aux.find("-") != -1):
        y0Aux = entradaY0.get().replace("-", "")
        y0Aux = int(y0Aux) * -1
    
    if(x1Aux.find("-") != -1):
        x1Aux = entradaX1.get().replace("-", "")
        x1Aux = int(x1Aux) * -1
        
    if(y1Aux.find("-") != -1):
        y1Aux = entradaY1.get().replace("-", "")
        y1Aux = int(y1Aux) * -1
    
    x0Aux = int(x0Aux)
    y0Aux = int(y0Aux)
    x1Aux = int(x1Aux)
    y1Aux = int(y1Aux)
    
    dx = x1Aux - x0Aux
    dy = y1Aux - y0Aux
    x = y0Aux
    y = y0Aux
    
    if(abs(dx) > abs(dy)):
        steps = abs(dx)
    else:
        steps = abs(dy)
    
    xIncrement = dx / steps
    yIncrement = dy / steps
    
    # Colocar um setPixel aqui. Colocando um print pra ver as coordenadas.
    img.put("black", (round(400 + x), round(400 - y)))
    
    for k in range(steps):
        x = x + xIncrement
        y = y + yIncrement
    # Colocar um setPixel aqui. Colocando um print pra ver as coordenadas.
        img.put("black", (round(400 + x), round(400 - y)))
    
master = Tk()

#Tamanho da tela padrao
screen_width = 1000
screen_height = 1000

canvasSizeX = 800
canvasSizeY = 800

master.title('Projeto 2')

master.geometry("%dx%d+0+0" % (screen_width, screen_height))  # largura, altura, dist esquerda + dist topo
master.wm_resizable(width=False, height=False)  # travando a tela na resolução definida

# colocando a img de fundo e especificando a posição dela na tela
canvas = Canvas(master, width=canvasSizeX, height=canvasSizeY, bg="white")
canvas.pack(side="bottom")

# colocar o pixel como imagem
img = PhotoImage(width=screen_width, height=screen_height)
canvas.create_image((screen_width / 2, screen_height / 2), image=img, state="normal")  # normal, disabled or hidden

# criando plano cartesiano

#Linha Horizontal
for i in range(canvasSizeX):
    img.put("black", (int(0 + i), int(canvasSizeY/2)))

#Linha vertical
for i in range(canvasSizeY):
    img.put("black", (int(canvasSizeX/2), int(0+i)))


# criando a caixinha q mostra as coordenadas
widget1 = Frame(master)
widget1.place(bordermode=OUTSIDE, height=20, width=300, x=50)
msg = Label(widget1, text=f"Coordenadas da tela X:{0} | Y: {0}")
msg["font"] = ("Verdana", "10", "italic", "bold")
msg.pack()

# Container para mostrar todas as coordenadas do plano
coordenadas_plano_cartesiano = Frame(master)
coordenadas_plano_cartesiano.place(bordermode=OUTSIDE, height=20, width=400, x=450)
msg_plano = Label(coordenadas_plano_cartesiano, text=f"Coordenadas do plano X:{0} | Y: {0}")
msg_plano["font"] = ("Verdana", "10", "italic", "bold")
msg_plano.pack()

lb_x0 = Label(master, text="X0:")
lb_x0.place(x=100, y=30)

entradaX0 = Entry(master)
entradaX0.place(x=130, y=30, width=50)

lb_y0 = Label(master, text="Y0:")
lb_y0.place(x=100, y=60)

entradaY0 = Entry(master)
entradaY0.place(x=130, y=60, width=50)

lb_x1 = Label(master, text="X1:")
lb_x1.place(x=100, y=90)

entradaX1 = Entry(master)
entradaX1.place(x=130, y=90, width=50)

lb_y1 = Label(master, text="Y1:")
lb_y1.place(x=100, y=120)

entradaY1 = Entry(master)
entradaY1.place(x=130, y=120, width=50)

btnDesenhar = Button(master, text='Desenhar', command=calculoDDA)
btnDesenhar["font"] = ("Verdana", "10", "italic", "bold")
btnDesenhar.place(x=100, y=150)

def button(event):
    """ Função responsável por mostrar as coordenadas e marca o pixel selecionado.Além de mostrar todos
        as transformoções em containers separados """

    x = event.x
    y = event.y
    
    x_plano = round(x - (canvasSizeX / 2) - 1) + 1
    y_plano = (round(((y - canvasSizeY / 2) - 1)) * -1) - 1
    
    msg.configure(text=f'Coordenadas da tela X:{x} | Y: {y}')
    msg_plano.configure(
        text=f'Coordenadas do plano X:{x_plano} | Y: {y_plano}')

if __name__ == "__main__":
    canvas.bind('<Button>', button)
    master.mainloop()