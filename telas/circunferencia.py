import math
from tkinter import Label, Entry, StringVar, OptionMenu, Button

class Circunferencia:
    entradaX = None
    entradaY = None
    raio = None
    img = None
    algoritmo = 'Explicita'

    def mostrar_paramentros(self, master, img):
        """ Método responsável por plota a tela com os paramentros da circunferencia. """

        self.img = img
        lb_x = Label(master, text="X:")
        lb_x.place(x=100, y=30)

        self.entradaX = Entry(master)
        self.entradaX.place(x=140, y=30, width=50)

        lb_y = Label(master, text="Y:")
        lb_y.place(x=100, y=60)

        self.entradaY = Entry(master)
        self.entradaY.place(x=140, y=60, width=50)

        lb_raio = Label(master, text="RAIO:")
        lb_raio.place(x=100, y=90)

        self.raio = Entry(master)
        self.raio.place(x=140, y=90, width=50)


    def explicita(self):
        """ Método responsável por calcular a circunferencia e plotar os pixels. """
        print('Explicita')
        xAux = str(self.entradaX.get())
        yAux = str(self.entradaY.get())
        
        if(xAux.find("-") != -1):
            xAux = self.entradaX.get().replace("-", "")
            xAux = int(xAux) * -1
            
        if(yAux.find("-") != -1):
            yAux = self.entradaY.get().replace("-", "")
            yAux = int(yAux) * -1
        
        xCentro = 400 + int(xAux)
        yCentro = 400 - int(yAux)

        passosD = 0
        passosU = 0
        raio = int(str(self.raio.get()))
        
        if(raio % 2 == 0):
            passosD = raio + 1 // 2
            passosU = int((raio + 1) / 2) + int((raio + 1) % 2)
        else:
            passosD = raio // 2
            passosU = int(raio / 2) + int(raio % 2)
        
        inc1 = 0
        inc2 = passosU
        
        self.img.put("black", (xCentro, yCentro))
        
        while(inc1 < passosD):
            #print((raio * raio) - (inc2 * inc2))
            yAux1 = int(math.sqrt((raio * raio) - (inc1 * inc1)))
            yAux2 = int(math.sqrt((raio * raio) - (inc2 * inc2)))
        
            self.img.put("black", (xCentro - inc1, yCentro + yAux1))
            self.img.put("black", (xCentro + inc1, yCentro + yAux1))
            self.img.put("black", (xCentro + inc1, yCentro - yAux1))
            self.img.put("black", (xCentro - inc1, yCentro - yAux1))
        
            self.img.put("black", (xCentro - yAux1, yCentro + inc1))
            self.img.put("black", (xCentro + yAux1, yCentro + inc1))
            self.img.put("black", (xCentro + yAux1, yCentro - inc1))
            self.img.put("black", (xCentro - yAux1, yCentro - inc1))
            
            self.img.put("black", (xCentro + inc2, yCentro + yAux2))
            self.img.put("black", (xCentro - inc2, yCentro + yAux2))
            self.img.put("black", (xCentro + inc2, yCentro - yAux2))
            self.img.put("black", (xCentro - inc2, yCentro - yAux2))
            
            inc1 += 1
            inc2 += 1
    

    def pontoMedio(self):
        print('Ponto medio')
        x = 0
        y = int(str(self.raio.get()))
        d = 5/4 - int(str(self.raio.get()))
        
        xAux = str(self.entradaX.get())
        yAux = str(self.entradaY.get())
        
        if(xAux.find("-") != -1):
            xAux = self.entradaX.get().replace("-", "")
            xAux = int(xAux) * -1
            
        if(yAux.find("-") != -1):
            yAux = self.entradaY.get().replace("-", "")
            yAux = int(yAux) * -1
        
        xCentro = 400 + int(xAux)
        yCentro = 400 - int(yAux)
        
        #pontoCirculo(x, y, valor)
        self.img.put("black", (xCentro, yCentro))
        
        while(y > x):
            if(d < 0): #ESCOLHE E
                d = d + 2 * x + 3 
            else: #ESCOLHE NE
                d = d + 2 * (x - y) + 5
                y = y - 1
            x = x + 1
            #pontoCirculo(x, y, valor) 
            self.img.put("black", (xCentro - x, yCentro + y))
            self.img.put("black", (xCentro + x, yCentro + y))
            self.img.put("black", (xCentro + x, yCentro - y))
            self.img.put("black", (xCentro - x, yCentro - y))
        
            self.img.put("black", (xCentro - y, yCentro + x))
            self.img.put("black", (xCentro + y, yCentro + x))
            self.img.put("black", (xCentro + y, yCentro - x))
            self.img.put("black", (xCentro - y, yCentro - x))
        

    def trigonometrica(self):

        print('trigonometrica!')
        xAux = str(self.entradaX.get())
        yAux = str(self.entradaY.get())
        
        if(xAux.find("-") != -1):
            xAux = self.entradaX.get().replace("-", "")
            xAux = int(xAux) * -1
            
        if(yAux.find("-") != -1):
            yAux = self.entradaY.get().replace("-", "")
            yAux = int(yAux) * -1
        
        xCentro = 400 + int(xAux)
        yCentro = 400 - int(yAux)
        
        #pontoCirculo(x, y, valor)
        self.img.put("black", (xCentro, yCentro))
        
        for i in range(46):
            x = round(int(str(self.raio.get())) * math.cos(math.radians(i)))
            y = round(int(str(self.raio.get())) * math.sin(math.radians(i)))
            
            self.img.put("black", (xCentro - x, yCentro + y))
            self.img.put("black", (xCentro + x, yCentro + y))
            self.img.put("black", (xCentro + x, yCentro - y))
            self.img.put("black", (xCentro - x, yCentro - y))
        
            self.img.put("black", (xCentro - y, yCentro + x))
            self.img.put("black", (xCentro + y, yCentro + x))
            self.img.put("black", (xCentro + y, yCentro - x))
            self.img.put("black", (xCentro - y, yCentro - x))


    def combobox_algoritmos(self,master):
        """ Método responsável por criar o combobox de algoritmos. """
        lista_algoritmos = ['Explicita','Ponto Médio','Trigonométrica']

        self.algoritmo = StringVar()
        self.algoritmo.set(lista_algoritmos[0])

        option_algoritmo = OptionMenu(master,self.algoritmo, *lista_algoritmos)
        option_algoritmo.place(x=100, y=120)
        return self.algoritmo


    def execute_algoritmo(self):
        if self.algoritmo.get() == 'Explicita':
            return self.explicita()
        elif self.algoritmo.get() == 'Ponto Médio':
            return self.pontoMedio()
        elif self.algoritmo.get() == 'Trigonométrica':
            return self.trigonometrica()
        else:
            print('Opção inválida')