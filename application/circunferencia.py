import math
from tkinter import *
from tkinter import ttk 

class Circunferencia:
    entradaX = None
    entradaY = None
    raio = None
    img = None
    treev = None
    algoritmo = 'Explicita'
    master = None
    widget = None

    def mostrar_paramentros(self, master, img, treev):
        """ Método responsável por plota a tela com os paramentros da circunferencia. """
        self.img = img
        self.treev = treev
        self.master = master
        lb_x = Label(master, text="X:")
        lb_x.place(x=100, y=40)

        self.entradaX = Entry(master)
        self.entradaX.place(x=140, y=40, width=40)

        lb_y = Label(master, text="Y:")
        lb_y.place(x=100, y=60)

        self.entradaY = Entry(master)
        self.entradaY.place(x=140, y=60, width=40)

        lb_raio = Label(master, text="RAIO:")
        lb_raio.place(x=100, y=90)

        self.raio = Entry(master)
        self.raio.place(x=140, y=90, width=40)

    """ Método responsável por calcular a circunferencia no método polinomial/explicita e plotar os pixels. """
    def explicita(self):

        print('Explicita')
        xAux = str(self.entradaX.get())
        yAux = str(self.entradaY.get())
        
        """ Ifs para tratar números negativos nos inputs """
        if(xAux.find("-") != -1):
            xAux = self.entradaX.get().replace("-", "")
            xAux = int(xAux) * -1
            
        if(yAux.find("-") != -1):
            yAux = self.entradaY.get().replace("-", "")
            yAux = int(yAux) * -1
        
        """ Localizando o centro do plano """
        xCentro = 400 + int(xAux)
        yCentro = 400 - int(yAux)

        raio = int(str(self.raio.get()))
        
        """ Plot incial """
        self.img.put("black", (xCentro, yCentro))

        inc1 = 0
        
        """ Laço para variações dos dados """
        while(inc1 <= raio):
            
            yAux1 = int(math.sqrt((raio * raio) - (inc1 * inc1)))

            """ Gerar os pixels na tela """
            self.img.put("black", (xCentro - inc1, yCentro + yAux1))
            self.img.put("black", (xCentro + inc1, yCentro + yAux1))

            self.img.put("black", (xCentro + inc1, yCentro - yAux1))
            self.img.put("black", (xCentro - inc1, yCentro - yAux1))

            """ Inserção de dados na tabela """
            linha = self.treev.get_children()[inc1]
            self.treev.item(linha, text="blub", values=(xCentro - inc1-400, (xCentro - inc1-400) * -1,yCentro + yAux1 - 400,(yCentro + yAux1 - 400)*-1))
            inc1 += 1
    
    """ Método responsável por calcular a circunferencia no método do ponto médio e plotar os pixels. """
    def pontoMedio(self):
        print('Ponto medio')
        
        x = 0
        y = int(str(self.raio.get()))
        d = 5/4 - int(str(self.raio.get()))
        
        """ Dados na entrada do input """
        xAux = str(self.entradaX.get())
        yAux = str(self.entradaY.get())
        
        """ Ifs para tratar números negativos nos inputs """
        if(xAux.find("-") != -1):
            xAux = self.entradaX.get().replace("-", "")
            xAux = int(xAux) * -1
            
        if(yAux.find("-") != -1):
            yAux = self.entradaY.get().replace("-", "")
            yAux = int(yAux) * -1
        
        """ Localizando o centro do plano """
        xCentro = 400 + int(xAux)
        yCentro = 400 - int(yAux)
        
        """ Plot incial """
        self.img.put("black", (xCentro, yCentro))
        
        count = 0 
        """ Laço para variações dos dados """
        while(y > x):
            
            """ Inserção de dados na tabela """
            linha = self.treev.get_children()[count]
            self.treev.item(linha, text="blub", values=(d,xCentro + x-400, yCentro + y-400,xCentro + y-400,yCentro + x-400,xCentro + y-400,yCentro - x-400,xCentro + x-400,yCentro - y-400,xCentro - x-400,yCentro - y-400,xCentro - y-400,yCentro - x-400,xCentro - y-400, yCentro + x-400,xCentro - x-400,yCentro + y-400))
            count += 1
            
            """ Escolha entre E ou NE """
            if(d < 0): # ESCOLHE E
                d = d + 2 * x + 3 
            else: # ESCOLHE NE
                d = d + 2 * (x - y) + 5
                y = y - 1
            x = x + 1
            
            """ Gerar os pixels na tela """
            self.img.put("black", (xCentro - x, yCentro + y))
            self.img.put("black", (xCentro + x, yCentro + y))
            self.img.put("black", (xCentro + x, yCentro - y))
            self.img.put("black", (xCentro - x, yCentro - y))
        
            self.img.put("black", (xCentro - y, yCentro + x))
            self.img.put("black", (xCentro + y, yCentro + x))
            self.img.put("black", (xCentro + y, yCentro - x))
            self.img.put("black", (xCentro - y, yCentro - x))
             

    """ Método responsável por calcular a circunferencia no método trigonometrico e plotar os pixels. """
    def trigonometrica(self):

        print('trigonometrica!')
        
        """ Dados na entrada do input """
        xAux = str(self.entradaX.get())
        yAux = str(self.entradaY.get())
        
        """ Ifs para tratar números negativos nos inputs """
        if(xAux.find("-") != -1):
            xAux = self.entradaX.get().replace("-", "")
            xAux = int(xAux) * -1
            
        if(yAux.find("-") != -1):
            yAux = self.entradaY.get().replace("-", "")
            yAux = int(yAux) * -1
        
        """ Localizando o centro do plano """
        xCentro = 400 + int(xAux)
        yCentro = 400 - int(yAux)
        
        """ Plot incial """
        self.img.put("black", (xCentro, yCentro))

        raio = int(str(self.raio.get()))
        

        if(raio > 0):
            """ Laço para variações dos dados """
            for i in range(46):
                x = round(int(str(self.raio.get())) * math.cos(math.radians(i)))
                y = round(int(str(self.raio.get())) * math.sin(math.radians(i)))
            
                """ Gerar os pixels na tela """
                self.img.put("black", (xCentro - x, yCentro + y)) 
                self.img.put("black", (xCentro + x, yCentro + y)) 
                self.img.put("black", (xCentro + x, yCentro - y)) 
                self.img.put("black", (xCentro - x, yCentro - y)) 
        
                self.img.put("black", (xCentro - y, yCentro + x)) 
                self.img.put("black", (xCentro + y, yCentro + x)) 
                self.img.put("black", (xCentro + y, yCentro - x)) 
                self.img.put("black", (xCentro - y, yCentro - x)) 
            
                """ Inserção de dados na tabela """
                linha = self.treev.get_children()[i]
                self.treev.item(linha, text="blub", values=("-",xCentro + x - 400, (yCentro - y - 400)*-1, xCentro + y - 400, (yCentro - x - 400)*-1, xCentro + y - 400, 
                                (yCentro + x - 400)*-1, xCentro + x - 400, (yCentro - y - 400)*-1, xCentro - x - 400, (yCentro - y - 400)*-1, xCentro - y - 400, 
                                (yCentro + x - 400)*-1, xCentro - y - 400, (yCentro - x - 400)*-1, xCentro - x - 400, (yCentro - y - 400)*-1))
        else:
            print("Raio negativo! - O algoritmo não pode ser executado.")
    
    def combobox_algoritmos(self,master):
        """ Método responsável por criar o combobox de algoritmos. """
        
        lista_algoritmos = ['Explicita','Ponto Médio','Trigonométrica']

        self.algoritmo = StringVar()
        self.algoritmo.set(lista_algoritmos[0])

        option_algoritmo = OptionMenu(master,self.algoritmo, *lista_algoritmos)
        option_algoritmo.place(x=100, y=120)

        return self.algoritmo.get()

    """ Método responsável executar os tipos de algoritmos """
    def execute_algoritmo(self):
        if self.widget != None:
            self.widget.destroy()
            
        if self.algoritmo.get() == 'Explicita':
            self.table_explicita()
            return self.explicita()
        elif self.algoritmo.get() == 'Ponto Médio':
            self.table_pm_trig()
            return self.pontoMedio()
        elif self.algoritmo.get() == 'Trigonométrica':
            self.table_pm_trig()
            return self.trigonometrica()
        else:
            print('Opção inválida')
    
    """ Método responsável por mostrar as tabelas de dados do método explicíta """
    def table_explicita(self):
        self.widget = Frame(self.master)
        self.widget.configure(bg="white")
        self.widget.place(bordermode=OUTSIDE, height=100, width=400, x=340, y=40)

        self.treev = ttk.Treeview(self.widget, selectmode ='browse') 
        self.treev.pack(side ='right') 


        verscrlbar = ttk.Scrollbar(self.widget,  
                                orient ="vertical",  
                                command = self.treev.yview)
                                 
        verscrlbar.pack(side ='right', fill ='x') 
        self.treev.configure(xscrollcommand = verscrlbar.set) 
        self.treev["columns"] = ("1", "2","3","4") 
        self.treev['show'] = 'headings'
        self.treev.column("1", width = 60, anchor ='c') 
        self.treev.column("2", width = 60, anchor ='c') 
        self.treev.column("3", width = 60, anchor ='c') 
        self.treev.column("4", width = 60, anchor ='c') 
        self.treev.heading("1", text ="X0") 
        self.treev.heading("2", text ="Y0")
        self.treev.heading("3", text ="X1")
        self.treev.heading("4", text ="Y1")

        for i in range(401):
            self.treev.insert("", i, text =f"L{i+1}",values =("0","0","0","0"))
    
    """ Método responsável por mostrar as tabelas de dados do método trigonométrico e ponto médio  """
    def table_pm_trig(self):
        ## mudar a tabela de acordo com o algoritmo
        self.widget = Frame(self.master)
        self.widget.configure(bg="white")
        self.widget.place(bordermode=OUTSIDE, height=100, width=725, x=245, y=40)

        self.treev = ttk.Treeview(self.widget, selectmode ='browse') 
        self.treev.pack(side ='right') 


        verscrlbar = ttk.Scrollbar(self.widget,  
                                orient ="vertical",  
                                command = self.treev.yview)
                                 
        verscrlbar.pack(side ='right', fill ='x') 
        self.treev.configure(xscrollcommand = verscrlbar.set) 
        self.treev["columns"] = ("1", "2","3","4","5", "6","7","8","9","10","11","12","13", "14","15","16","17") 
        self.treev['show'] = 'headings'

        self.treev.column("1", width = 50, anchor ='c') 
        self.treev.column("2", width = 40, anchor ='c') 
        self.treev.column("3", width = 40, anchor ='c') 
        self.treev.column("4", width = 40, anchor ='c') 
        self.treev.column("5", width = 40, anchor ='c') 
        self.treev.column("6", width = 40, anchor ='c') 
        self.treev.column("7", width = 40, anchor ='c') 
        self.treev.column("8", width = 40, anchor ='c') 
        self.treev.column("9", width = 40, anchor ='c') 
        self.treev.column("10", width = 40, anchor ='c') 
        self.treev.column("11", width = 40, anchor ='c') 
        self.treev.column("12", width = 40, anchor ='c') 
        self.treev.column("13", width = 40, anchor ='c') 
        self.treev.column("14", width = 40, anchor ='c') 
        self.treev.column("15", width = 40, anchor ='c') 
        self.treev.column("16", width = 40, anchor ='c') 
        self.treev.column("17", width = 40, anchor ='c') 

        self.treev.heading("1", text ="D")
        self.treev.heading("2", text ="X0") 
        self.treev.heading("3", text ="Y0")
        self.treev.heading("4", text ="X1")
        self.treev.heading("5", text ="Y1")
        self.treev.heading("6", text ="X2") 
        self.treev.heading("7", text ="Y2")
        self.treev.heading("8", text ="X3")
        self.treev.heading("9", text ="Y3")
        self.treev.heading("10", text ="X4") 
        self.treev.heading("11", text ="Y4")
        self.treev.heading("12", text ="X5")
        self.treev.heading("13", text ="Y5")
        self.treev.heading("14", text ="X6") 
        self.treev.heading("15", text ="Y6")
        self.treev.heading("16", text ="X7")
        self.treev.heading("17", text ="Y7")
        
        """ Inicializando a tabela com valores padrões """
        for i in range(401):
            self.treev.insert("", i, text =f"L{i+1}",values =("0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0"))
        