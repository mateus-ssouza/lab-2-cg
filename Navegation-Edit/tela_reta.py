import math
from tkinter import *
from reta import Reta
from tkinter import ttk 



class TelaReta:

    master = None
    screen_width = 1000
    screen_height = 1000

    canvasSizeX = 800
    canvasSizeY = 800
    img = None
    treev = None
    canvas = None

    def __init__(self,master):
        self.master = Toplevel(master)
        self.table()
        self.renderScreen()


    #Tamanho da tela padrao

    def renderScreen(self):
        screen_width = 1000
        screen_height = 1000

        canvasSizeX = 800
        canvasSizeY = 800

        self.master.title('Projeto 2')

        self.master.geometry("%dx%d+0+0" % (screen_width, screen_height))  # largura, altura, dist esquerda + dist topo
        self.master.wm_resizable(width=False, height=False)  # travando a tela na resolução definida

        # colocando a img de fundo e especificando a posição dela na tela

        canvas = Canvas(self.master, width=canvasSizeX, height=canvasSizeY, bg="white")
        canvas.pack(side="bottom")
        self.canvas= canvas

        # colocar o pixel como imagem
        self.img = PhotoImage(width=screen_width, height=screen_height)
        self.drawnScreen(canvas)

        reta = Reta()

        # Container para mostrar dados da reta
        dados_da_reta = Frame(self.master)
        dados_da_reta.place(bordermode=OUTSIDE, height=20, width=400, x=450)
        msg_reta = Label(dados_da_reta,text=f"Length: {reta.length} | Xinc: {0} | Yinc: {0}")
        msg_reta["font"] = ("Verdana", "10", "italic", "bold")
        msg_reta.pack()
        
        reta.mostrar_paramentros(self.master,self.img,self.treev)
        reta.combobox_algoritmos(self.master)

        btnDesenhar = Button(self.master, text='Desenhar', command=lambda:[reta.execute_algoritmo(msg_reta)])
        btnDesenhar["font"] = ("Verdana", "10", "italic", "bold")
        btnDesenhar.place(x=100, y=150)

        btnApagar = Button(self.master, text="Apagar", command=lambda: [self.drawnScreen(canvas)])
        btnApagar["font"] = ("Verdana", "10", "italic", "bold")
        btnApagar.place(x=800, y=150)
       
    def drawnScreen(self,canvas):
        # colocar o pixel como imagem

        linhas = self.treev.get_children()
        for item in linhas: 
            self.treev.item(item, text="blub", values=(0, 0, 0))

        self.img.blank()

        canvas.create_image((self.screen_width / 2, self.screen_height / 2), image=self.img, state="normal")

        # criando plano cartesiano

        # Linha Horizontal
        for i in range(self.canvasSizeX):
            self.img.put("black", (int(0 + i), int(self.canvasSizeY / 2)))

        # Linha vertical
        for i in range(self.canvasSizeY):
            self.img.put("black", (int(self.canvasSizeX / 2), int(0 + i)))


    def table(self):
        widgetTest = Frame(self.master)
        widgetTest.configure(bg="white")
        widgetTest.place(bordermode=OUTSIDE, height=100, width=500, x=350, y=40)

        self.treev = ttk.Treeview(widgetTest, selectmode ='browse') 
        self.treev.pack(side ='right') 


        verscrlbar = ttk.Scrollbar(widgetTest,  
                                orient ="vertical",  
                                command = self.treev.yview)
                                 
        verscrlbar.pack(side ='right', fill ='x') 
        self.treev.configure(xscrollcommand = verscrlbar.set) 
        self.treev["columns"] = ("1", "2","3") 
        self.treev['show'] = 'headings'
        self.treev.column("1", width = 90, anchor ='c') 
        self.treev.column("2", width = 90, anchor ='c') 
        self.treev.column("3", width = 90, anchor ='c') 
        self.treev.heading("1", text ="D") 
        self.treev.heading("2", text ="X")
        self.treev.heading("3", text ="Y")

        for i in range(401):
            self.treev.insert("", i, text =f"L{i+1}",values =("0","0","0")) 
        