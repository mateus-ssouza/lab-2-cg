import math
from tkinter import Label, Entry, StringVar, OptionMenu, Button

class Reta:
    entradaX0 = None
    entradaY0 = None
    entradaX1 = None
    entradaY1 = None

    treev = None
    img = None
    canvas = None
    length = 0
    algoritmo = 'DDA'

    """ Função para exibir os parametros da reta """
    def mostrar_paramentros(self, master, img, treev):

        self.img = img
        self.treev = treev

        lb_x0 = Label(master, text="X0:")
        lb_x0.place(x=100, y=30)

        self.entradaX0 = Entry(master)
        self.entradaX0.place(x=130, y=30, width=50)

        lb_y0 = Label(master, text="Y0:")
        lb_y0.place(x=200, y=30)

        self.entradaY0 = Entry(master)
        self.entradaY0.place(x=230, y=30, width=50)

        lb_x1 = Label(master, text="X1:")
        lb_x1.place(x=100, y=70)

        self.entradaX1 = Entry(master)
        self.entradaX1.place(x=130, y=70, width=50)

        lb_y1 = Label(master, text="Y1:")
        lb_y1.place(x=200, y=70)

        self.entradaY1 = Entry(master)
        self.entradaY1.place(x=230, y=70, width=50)

    """ Função calcular o método DDA da reta """
    def calculoDDA(self, label):
        
        """ Dados na entrada do input """
        x0Aux = str(self.entradaX0.get())
        y0Aux = str(self.entradaY0.get())
        x1Aux = str(self.entradaX1.get())
        y1Aux = str(self.entradaY1.get())
        
        """ Ifs para tratar números negativos nos inputs """
        if(x0Aux.find("-") != -1):
            x0Aux = self.entradaX0.get().replace("-", "")
            x0Aux = int(x0Aux) * -1
            
        if(y0Aux.find("-") != -1):
            y0Aux = self.entradaY0.get().replace("-", "")
            y0Aux = int(y0Aux) * -1
        
        if(x1Aux.find("-") != -1):
            x1Aux = self.entradaX1.get().replace("-", "")
            x1Aux = int(x1Aux) * -1
            
        if(y1Aux.find("-") != -1):
            y1Aux = self.entradaY1.get().replace("-", "")
            y1Aux = int(y1Aux) * -1
        
        x0Aux = int(x0Aux)
        y0Aux = int(y0Aux)
        x1Aux = int(x1Aux)
        y1Aux = int(y1Aux)
        
        """ Determinando X, Y, DX e DY """
        dx = x1Aux - x0Aux
        dy = y1Aux - y0Aux
        x = x0Aux
        y = y0Aux
        
        """ Determinar os passos para os incrementos adiante """
        if(abs(dx) > abs(dy)):
            steps = abs(dx)
        else:
            steps = abs(dy)
        
        """ Determinar os incrementos de X e Y """
        xIncrement = float(dx) / float(steps)
        yIncrement = float(dy) / float(steps)

        """ Plot incial """
        self.img.put("black", (round(400 + x), round(400 - y)))
        
        """ Laço para variações dos dados """
        for k in range(steps+1):
            """ Inserção de dados na tabela """
            linha = self.treev.get_children()[k]
            self.treev.item(linha, text="blub", values=("-",round(x,2), round(y,2)))
            
            x = x + xIncrement
            y = y + yIncrement
            
            """ Gerar os pixels na tela """
            self.img.put("black", (round(400 + x), round(400 - y)))
            self.length += 1
        self.length -= 1
        
        label.config(text=f"Length: {self.length}  Xinc: {round(xIncrement,2)}  Yinc: {round(yIncrement,4)}")
        self.length = 0
        label.pack()

    """ Função calcular o método do ponto médio da reta """
    def calculoPontoMedio(self, label):
        
        """ Dados na entrada do input """
        x0Aux = str(self.entradaX0.get())
        y0Aux = str(self.entradaY0.get())
        x1Aux = str(self.entradaX1.get())
        y1Aux = str(self.entradaY1.get())
        
        """ Ifs para tratar números negativos nos inputs """
        if(x0Aux.find("-") != -1):
            x0Aux = self.entradaX0.get().replace("-", "")
            x0Aux = int(x0Aux) * -1
            
        if(y0Aux.find("-") != -1):
            y0Aux = self.entradaY0.get().replace("-", "")
            y0Aux = int(y0Aux) * -1
        
        if(x1Aux.find("-") != -1):
            x1Aux = self.entradaX1.get().replace("-", "")
            x1Aux = int(x1Aux) * -1
            
        if(y1Aux.find("-") != -1):
            y1Aux = self.entradaY1.get().replace("-", "")
            y1Aux = int(y1Aux) * -1
        
        x0Aux = int(x0Aux)
        y0Aux = int(y0Aux)
        x1Aux = int(x1Aux)
        y1Aux = int(y1Aux)
        
        """ Calculo DX e DY """
        dx = abs(x1Aux - x0Aux)
        dy = abs(y1Aux - y0Aux)
        
        """ Calculo D, incremento E e NE"""
        p = 2 * dy - dx
        incE = 2 * dy
        incNE = 2 * (dy - dx) 
          
        if(x0Aux > x1Aux):
            x = x1Aux
            y = y1Aux
            x1Aux = x0Aux
        else:
            x = x0Aux
            y = y0Aux
        
        """ Plot incial """
        self.img.put("black", (round(400 + x), round(400 - y)))

        """ Laço para variações dos dados """
        count = 0
        while(x < x1Aux):
            x = x + 1
            
            """ Escolha entre E ou NE """
            if(p < 0):
                p = p + incE
            else:
                y = y + 1
                p = p + incNE
            
            """ Inserção de dados na tabela """
            linha = self.treev.get_children()[count]
            self.treev.item(linha, text="blub", values=(round(p,2),round(x,2), round(y,2)))
            
            """ Gerar os pixels na tela """
            self.img.put("black", (round(400 + x), round(400 - y)))
            
            count += 1
            self.length+=1

        """ Label com dados da reta """
        label.config(text=f"Length: {self.length}  IncE: {incE}  IncNE: {incNE}  DX: {dx}  DY: {dy}")
        self.length=0
        label.pack()
        
        """ Tabela de variações da reta """
        linha = self.treev.get_children()[count]
        self.treev.item(linha, text="blub", values=(round(p,2),round(x,2), round(y,2)))

    """ Função para executar os algoritmos da reta """
    def execute_algoritmo(self, label):
        
        """ Dados na entrada do input """
        x0Aux = str(self.entradaX0.get())
        y0Aux = str(self.entradaY0.get())
        x1Aux = str(self.entradaX1.get())
        y1Aux = str(self.entradaY1.get())
        
        """ Ifs para tratar números negativos nos inputs """
        if(x0Aux.find("-") != -1):
            x0Aux = self.entradaX0.get().replace("-", "")
            x0Aux = int(x0Aux) * -1
            
        if(y0Aux.find("-") != -1):
            y0Aux = self.entradaY0.get().replace("-", "")
            y0Aux = int(y0Aux) * -1
        
        if(x1Aux.find("-") != -1):
            x1Aux = self.entradaX1.get().replace("-", "")
            x1Aux = int(x1Aux) * -1
            
        if(y1Aux.find("-") != -1):
            y1Aux = self.entradaY1.get().replace("-", "")
            y1Aux = int(y1Aux) * -1
        
        x0Aux = int(x0Aux)
        y0Aux = int(y0Aux)
        x1Aux = int(x1Aux)
        y1Aux = int(y1Aux)
        
        """ Ifs para execução dos algoritmos escolhido na tela """
        if int((x0Aux < 0 or y0Aux < 0 or x1Aux < 0 or y1Aux < 0) and self.algoritmo.get() == 'Ponto Médio'):
            print('Não é possível plota retas para paramentros negativos') 
        else:
            if self.algoritmo.get() == 'DDA':
                return self.calculoDDA(label)
            elif self.algoritmo.get() == 'Ponto Médio':
                return self.calculoPontoMedio(label)
            else:
                print('Opção inválida')

    def combobox_algoritmos(self,master):
        """ Método responsável por criar o combobox de algoritmos. """
        lista_algoritmos = ['DDA','Ponto Médio']

        self.algoritmo = StringVar()
        self.algoritmo.set(lista_algoritmos[0])

        option_algoritmo = OptionMenu(master,self.algoritmo, *lista_algoritmos)
        option_algoritmo.place(x=100, y=100)
        return self.algoritmo