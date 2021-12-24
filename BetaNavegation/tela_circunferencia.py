from tkinter import *
from circunferencia import Circunferencia
    

class TelaCircunferencia:

    master = None
    screen_width = 1000
    screen_height = 1000
    img = None

    canvasSizeX = 800
    canvasSizeY = 800

    def __init__(self,master):
        self.master = Toplevel(master)
        self.renderScreen()

    #Tamanho da tela padrao

    def renderScreen(self):


        self.master.title('Projeto 2')

        self.master.geometry("%dx%d+0+0" % (self.screen_width, self.screen_height))  # largura, altura, dist esquerda + dist topo
        self.master.wm_resizable(width=False, height=False)  # travando a tela na resolução definida

        # colocando a img de fundo e especificando a posição dela na tela
        canvas = Canvas(self.master, width=self.canvasSizeX, height=self.canvasSizeY, bg="white")
        canvas.pack(side="bottom")



        # colocar o pixel como imagem
        self.img = PhotoImage(width=self.screen_width, height=self.screen_height)

        self.drawnScreen(canvas)

        # criando a caixinha q mostra as coordenadas
        widget1 = Frame(self.master)
        widget1.place(bordermode=OUTSIDE, height=20, width=300, x=50)
        msg = Label(widget1, text=f"Coordenadas da tela X:{0} | Y: {0}")
        msg["font"] = ("Verdana", "10", "italic", "bold")
        msg.pack()

        # Container para mostrar todas as coordenadas do plano
        coordenadas_plano_cartesiano = Frame(self.master)
        coordenadas_plano_cartesiano.place(bordermode=OUTSIDE, height=20, width=400, x=450)
        msg_plano = Label(coordenadas_plano_cartesiano, text=f"Coordenadas do plano X:{0} | Y: {0}")
        msg_plano["font"] = ("Verdana", "10", "italic", "bold")
        msg_plano.pack()

        # Importando os metodos da classe circunferencia
        tela_circunferencia = Circunferencia()
        tela_circunferencia.mostrar_paramentros(self.master,self.img)

        #combobox com as opções de algoritmos
        tela_circunferencia.combobox_algoritmos(self.master)

        # Definindo qual algoritmo ira desenhar na teal
        btnDesenhar = Button(self.master, text='Desenhar', command=tela_circunferencia.execute_algoritmo)
        btnDesenhar["font"] = ("Verdana", "10", "italic", "bold")
        btnDesenhar.place(x=100, y=150)

        btnApagar = Button(self.master,text="Apagar",command=lambda:[self.drawnScreen(canvas)] )

        btnApagar["font"] = ("Verdana", "10", "italic", "bold")
        btnApagar.place(x=800, y=150)




    def drawnScreen(self,canvas):
        # colocar o pixel como imagem



        self.img.blank()

        canvas.create_image((self.screen_width / 2, self.screen_height / 2), image=self.img,
                            state="normal")


        # criando plano cartesiano

        # Linha Horizontal
        for i in range(self.canvasSizeX):
            self.img.put("black", (int(0 + i), int(self.canvasSizeY / 2)))

        # Linha vertical
        for i in range(self.canvasSizeY):
            self.img.put("black", (int(self.canvasSizeX / 2), int(0 + i)))





