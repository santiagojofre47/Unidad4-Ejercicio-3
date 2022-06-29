from tkinter import *
from tkinter import ttk,messagebox,font 
import requests

class Aplicacion():
    __ventana = None
    __dolares = None
    __pesos = None

    def __init__(self):
        self.__ventana = Tk()
        self.__ventana.geometry('245x117')
        self.__ventana.title('Conversor de moneda')

        mainframe=Frame(self.__ventana,padx=8,pady=8,bg='#68c3bf')
        mainframe.grid(column=0,row=0,sticky=(N,W,E,S))
        mainframe.columnconfigure(0,weight=0)
        mainframe.rowconfigure(0,weight=0)
        mainframe['borderwidth']=2
        mainframe['relief']='sunken'

        fuente=font.Font(weight='bold',size=9,family="Helvetica")

        self.__dolares=StringVar()
        self.__pesos=StringVar()

        self.__dolares.trace('w', self.convertir)
        self.dolaresEntry=Entry(mainframe,textvariable=self.__dolares,width=10)
        self.dolaresEntry.grid(column=1,row=0, sticky= W)
        self.equivaleLbl=Label(mainframe,text='es equivalente a',bg='#52afaa',font=fuente).grid(column=0,row=1)
        self.dolarLbl=Label(mainframe,text='dólares',bg='#52afaa',font=fuente).grid(column=2,row=0)
        self.pesosLbl=Label(mainframe,text='pesos',bg='#52afaa',font=fuente).grid(column=2,row=1)
        self.precioConvertidoLbl=Label(mainframe,textvariable=self.__pesos,bg='#52afaa',font=fuente).grid(column=1,row=1)
        self.botonSalir=Button(mainframe,text="Salir",command=self.__ventana.destroy,bg='#c7773e',font=fuente).grid(column=2,row=2)

        for child in mainframe.winfo_children():
            child.grid_configure(padx=5,pady=5)

        self.__ventana.mainloop()

    def convertir(self,*args):
        url = 'https://www.dolarsi.com/api/api.php?type=dolar'
        r1 = requests.get(url)
        r2 = r1.json()

        for i in range(len(r2)):
            if r2[i]['casa']['nombre'] == 'Oficial':
                precioVenta=r2[i]['casa']['venta']

        precioVenta=float(precioVenta.replace(',','.'))

        if self.dolaresEntry.get() != '':
            try:
                dolares = float(self.dolaresEntry.get())
                self.__pesos.set(precioVenta*dolares)
            except ValueError:
                messagebox.showerror(title = 'Error de tipo', message = 'Debe ingresar un valor numérico')
                self.__dolares.set('')
                self.dolaresEntry.focus()
        else:
            self.__pesos.set('')
    

