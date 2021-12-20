from tkinter import *
import math

def trigonometrica():
    
    xAux = str(entradaX.get())
    yAux = str(entradaY.get())
    
    if(xAux.find("-") != -1):
        xAux = entradaX.get().replace("-", "")
        xAux = int(xAux) * -1
        
    if(yAux.find("-") != -1):
        yAux = entradaY.get().replace("-", "")
        yAux = int(yAux) * -1
    
    xCentro = 400 + int(xAux)
    yCentro = 400 - int(yAux)
    
    #pontoCirculo(x, y, valor)
    img.put("black", (xCentro, yCentro))
    
    for i in range(46):
        x = round(int(str(raioEntrada.get())) * math.cos(math.radians(i)))
        y = round(int(str(raioEntrada.get())) * math.sin(math.radians(i)))
        
        img.put("black", (xCentro - x, yCentro + y))
        img.put("black", (xCentro + x, yCentro + y))
        img.put("black", (xCentro + x, yCentro - y))
        img.put("black", (xCentro - x, yCentro - y))
    
        img.put("black", (xCentro - y, yCentro + x))
        img.put("black", (xCentro + y, yCentro + x))
        img.put("black", (xCentro + y, yCentro - x))
        img.put("black", (xCentro - y, yCentro - x))
        
 
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

lb_x = Label(master, text="X:")
lb_x.place(x=100, y=30)

entradaX = Entry(master)
entradaX.place(x=130, y=30, width=50)

lb_y = Label(master, text="Y:")
lb_y.place(x=100, y=60)

entradaY = Entry(master)
entradaY.place(x=130, y=60, width=50)

lb_raio = Label(master, text="RAIO:")
lb_raio.place(x=100, y=90)

raioEntrada = Entry(master)
raioEntrada.place(x=140, y=90, width=50)

btnDesenhar = Button(master, text='Desenhar', command=trigonometrica)
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