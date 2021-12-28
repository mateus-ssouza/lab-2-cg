from tkinter import *
from circunferencia import Circunferencia
    

class TelaCircunferencia:

    master = None
    screen_width = 1000
    screen_height = 1000
    img = None
    treev = None
    tela_circunferencia = None
    canvasSizeX = 800
    canvasSizeY = 800

    def __init__(self,master):
        self.master = Toplevel(master)
        self.renderScreen()

    """ Função responsável por redenrizar a tela de circunferência """
    def renderScreen(self):
        self.master.title('Circunferências')

        self.master.geometry("%dx%d+0+0" % (self.screen_width, self.screen_height))  # largura, altura, dist esquerda + dist topo
        self.master.wm_resizable(width=False, height=False)  # travando a tela na resolução definida

        # colocando a img de fundo e especificando a posição dela na tela
        canvas = Canvas(self.master, width=self.canvasSizeX, height=self.canvasSizeY, bg="white")
        canvas.pack(side="bottom")

        # colocar o pixel como imagem
        self.img = PhotoImage(width=self.screen_width, height=self.screen_height)
        
        # Container para mostrar onde irá fica os parâmetros
        widget1 = Frame(self.master)
        widget1.place(bordermode=OUTSIDE, height=20, width=300, x=20)
        msg = Label(widget1, text="Parâmetros")
        msg["font"] = ("Verdana", "10", "italic", "bold")
        msg.pack()

        # Container para mostrar onde irá fica a tabela
        label_titulo = Frame(self.master)
        label_titulo.place(bordermode=OUTSIDE, height=20, width=400, x=380)
        msg_tabela = Label(label_titulo, text=f"Tabela de variação")
        msg_tabela["font"] = ("Verdana", "10", "italic", "bold")
        msg_tabela.pack()

        # Importando os metodos da classe circunferencia
        self.tela_circunferencia = Circunferencia()
        self.tela_circunferencia.mostrar_paramentros(self.master,self.img,self.treev)

        #combobox com as opções de algoritmos
        self.tela_circunferencia.combobox_algoritmos(self.master)
        
        self.drawnScreen(canvas)
        
        # Botão para executar o desenho
        btnDesenhar = Button(self.master, text='Desenhar', command=self.tela_circunferencia.execute_algoritmo)
        btnDesenhar["font"] = ("Verdana", "10", "italic", "bold")
        btnDesenhar.place(x=100, y=150)

        # Botão para executar a limpeza de dos dados e da tela
        btnApagar = Button(self.master,text="Apagar",command=lambda:[self.drawnScreen(canvas)] )
        btnApagar["font"] = ("Verdana", "10", "italic", "bold")
        btnApagar.place(x=800, y=150)




    def drawnScreen(self,canvas):
        """ Limpa se existe uma tabela e desenha o plano novamente apos usar o metodo self.img.blank(). """

        if self.tela_circunferencia.algoritmo.get() != "Explicita":
            linhas = self.tela_circunferencia.treev.get_children()
            for item in linhas: 
                self.tela_circunferencia.treev.item(item, text="blub", values=("-", "-", "-","-", "-", "-","-", "-","-","-", "-", "-","-", "-", "-","-", "-","-","-"))
        elif self.tela_circunferencia.treev != None:
            linhas = self.tela_circunferencia.treev.get_children()
            for item in linhas: 
                self.tela_circunferencia.treev.item(item, text="blub", values=("-", "-", "-","-"))

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
