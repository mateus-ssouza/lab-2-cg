import math
from tkinter import Label, Entry, StringVar, OptionMenu, Button

class Reta:
    entradaX0 = None
    entradaY0 = None
    entradaX1 = None
    entradaY1 = None
    img = None
    algoritmo = 'DDA'

    def mostrar_paramentros(self, master, img):

        self.img = img
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


    def calculoDDA(self):
        x0Aux = str(self.entradaX0.get())
        y0Aux = str(self.entradaY0.get())
        x1Aux = str(self.entradaX1.get())
        y1Aux = str(self.entradaY1.get())
        
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
        
        dx = x1Aux - x0Aux
        dy = y1Aux - y0Aux
        x = x0Aux
        y = y0Aux
        
        if(abs(dx) > abs(dy)):
            steps = abs(dx)
        else:
            steps = abs(dy)
        
        xIncrement = float(dx) / float(steps)
        yIncrement = float(dy) / float(steps)
        
        # Colocar um setPixel aqui. Colocando um print pra ver as coordenadas.
        self.img.put("black", (round(400 + x), round(400 - y)))
        for k in range(steps):
            x = x + xIncrement
            y = y + yIncrement
        # Colocar um setPixel aqui. Colocando um print pra ver as coordenadas.
            self.img.put("black", (round(400 + x), round(400 - y)))
    

    def calculoPontoMedio(self):
        x0Aux = str(self.entradaX0.get())
        y0Aux = str(self.entradaY0.get())
        x1Aux = str(self.entradaX1.get())
        y1Aux = str(self.entradaY1.get())
        
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
        
        dx = abs(x1Aux - x0Aux)
        dy = abs(y1Aux - y0Aux)
        
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
        
        self.img.put("black", (round(400 + x), round(400 - y)))
        
        while(x < x1Aux):
            x = x + 1
            if(p < 0):
                print(f'P={p} X={x} Y={y}')
                p = p + incE
            else:
                y = y + 1
                print(f'P={p} X={x} Y={y}')
                p = p + incNE
            self.img.put("black", (round(400 + x), round(400 - y)))
    

    def execute_algoritmo(self):
        if int(self.entradaX0.get()) < 0 or int(self.entradaX1.get()) < 0 or int(self.entradaY0.get()) < 0 or int(self.entradaY1.get()) < 0:
            print('Não é possível plota retas para paramentros negativos') # colocar um aviso 
        else:
            if self.algoritmo.get() == 'DDA':
                return self.calculoDDA()
            elif self.algoritmo.get() == 'Ponto Médio':
                return self.calculoPontoMedio()
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