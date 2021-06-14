from tkinter import *
from tkinter import ttk,messagebox,font 
import requests
import json
from datetime import datetime


class Aplicacion:
    __ventana = None
    __dolarOf=None
    __dolarBlue=None
    __dolarLiqui=None
    __dolarBolsa=None

    def __init__(self):
        self.__ventana = Tk()
        self.__ventana.geometry('290x150')
        self.__ventana.title('Conversor de moneda')
        self.__ventana.resizable(1,0)
        self.__dolarCompra = StringVar()
        self.__dolarVenta = StringVar()
        self.__dolarBlueCompra = StringVar()
        self.__dolarBlueVenta = StringVar()
        self.__dolarLiquiCompra = StringVar()
        self.__dolarLiquiVenta = StringVar()
        self.__dolarBolsaCompra = StringVar()
        self.__dolarBolsaVenta = StringVar()
        self.__fechaActual = StringVar()
        self.__dolarCompra.set('')
        self.__dolarVenta.set('')
        self.__dolarBlueCompra.set('')
        self.__dolarBlueVenta.set('')
        self.__dolarBolsaCompra.set('')
        self.__dolarBolsaVenta.set('')
        self.__fechaActual.set('')
        frame1=Frame(self.__ventana,padx=8,pady=8,bg='#86dc51')
        frame1.grid(column=0,row=0,sticky=(N,W,E,S))
        frame1.columnconfigure(1,weight=0)
        frame1.rowconfigure(1,weight=0)
        frame2 = Frame(self.__ventana,padx=8,pady=8,bg='#a2a050')
        frame2.grid(column=0,row=1,sticky=(N,W,E,S))
        frame2.columnconfigure(0,weight=0)
        frame2.rowconfigure(0,weight=0)
        fuente1=font.Font(weight='bold')
        self.monedaLbl=Label(frame1,text='Moneda',fg='white',bg='#86dc51').grid(column = 0, row = 0, sticky = W)
        self.tabLbl=Label(frame1,text='\t\t',fg='white',bg='#86dc51').grid(column = 1, row = 0, sticky = W)
        self.tab2Lbl=Label(frame2,text='\t\t', fg='#797979',bg='#a2a050').grid(column = 1, row = 4, sticky = W)
        self.compraLbl=Label(frame1,text='Compra',fg='white',bg='#86dc51').grid(column = 2, row = 0, sticky = W)
        self.ventaLbl=Label(frame1,text='Venta',fg='white',bg='#86dc51').grid(column = 3, row = 0, sticky = W)
        self.dolarLbl=Label(frame2,text='Dólar',fg='#797979',bg='#a2a050').grid(column = 0, row = 0, sticky = W)
        self.dolarBlueLbl=Label(frame2,text='Blue',fg='#797979',bg='#a2a050').grid(column = 0, row = 1, sticky = W)
        self.dolarLiquiLbl=Label(frame2,text='Liqui',fg='#797979',bg='#a2a050').grid(column = 0, row = 2, sticky = W)
        self.dolarBolsaLbl=Label(frame2,text='Bolsa',fg='#797979',bg='#a2a050').grid(column = 0, row = 3, sticky = W)
        self.dolarCompraLbl=Label(frame2,textvariable=self.__dolarCompra,fg='#797979',bg='#a2a050').grid(column = 2, row = 0, sticky = W)
        self.dolarventaLbl=Label(frame2,textvariable=self.__dolarVenta,fg='#797979',bg='#a2a050').grid(column = 3, row = 0, sticky = W)
        self.dolarBlueCompraLbl=Label(frame2,textvariable=self.__dolarBlueCompra,fg='#797979',bg='#a2a050').grid(column = 2, row = 1, sticky = W)
        self.dolarBlueventaLbl=Label(frame2,textvariable=self.__dolarBlueVenta,fg='#797979',bg='#a2a050').grid(column = 3, row = 1, sticky = W)
        self.liquiCompraLbl=Label(frame2,textvariable=self.__dolarLiquiCompra,fg='#797979',bg='#a2a050').grid(column = 2, row = 2, sticky = W)
        self.liquiventaLbl=Label(frame2,textvariable=self.__dolarLiquiVenta,fg='#797979',bg='#a2a050').grid(column = 3, row = 2, sticky = W)
        self.BolsaCompraLbl=Label(frame2,textvariable=self.__dolarBolsaCompra,fg='#797979',bg='#a2a050').grid(column = 2, row = 3, sticky = W)
        self.BolsaventaLbl=Label(frame2,textvariable=self.__dolarBolsaVenta,fg='#797979',bg='#a2a050').grid(column = 3, row = 3, sticky = W)
        self.actualizarBtn=Button(frame2,text='ACTUALIZAR',fg='white',bg='green', command = self.actualizar).grid(column=0,row=4,sticky=W)
        self.dolarBolsaLbl=Label(frame2,text='Actualizado',fg='#797979',bg='#a2a050').grid(column=2,row=4,sticky=W)
        self.actualizadoLbl = Label(frame2, textvariable=self.__fechaActual, fg='#797979',bg='#a2a050').grid(column=3,row=4,sticky=W) 
        self.__ventana.mainloop()

    def actualizar(self):
        url = 'https://www.dolarsi.com/api/api.php?type=valoresprincipales'
        r1 = requests.get(url)
        r2 = r1.json()

        for i in range(len(r2)):
            if r2[i]['casa']['nombre'] == 'Dolar Oficial':
                precioCompra=r2[i]['casa']['compra']
                precioCompra=precioCompra[:len(precioCompra)-1]
                self.__dolarCompra.set(f'${precioCompra}')
                precioVenta=r2[i]['casa']['venta']
                precioVenta=precioVenta[:len(precioVenta)-1]
                self.__dolarVenta.set(f'${precioVenta}')
            elif r2[i]['casa']['nombre'] == 'Dolar Blue':
                precioCompra=r2[i]['casa']['compra']
                precioCompra=precioCompra[:len(precioCompra)-1]
                self.__dolarBlueCompra.set(f'${precioCompra}')
                precioVenta=r2[i]['casa']['venta']
                precioVenta=precioVenta[:len(precioVenta)-1]
                self.__dolarBlueVenta.set(f'${precioVenta}')
            elif r2[i]['casa']['nombre'] == 'Dolar Contado con Liqui':
                precioCompra=r2[i]['casa']['compra']
                precioCompra=precioCompra[:len(precioCompra)-1]
                self.__dolarLiquiCompra.set(f'${precioCompra}')
                precioVenta=r2[i]['casa']['venta']
                precioVenta=precioVenta[:len(precioVenta)-1]
                self.__dolarLiquiVenta.set(f'${precioVenta}')
            elif r2[i]['casa']['nombre'] == 'Dolar Bolsa':
                precioCompra=r2[i]['casa']['compra']
                precioCompra=precioCompra[:len(precioCompra)-1]
                self.__dolarBolsaCompra.set(f'${precioCompra}')
                precioVenta=r2[i]['casa']['venta']
                precioVenta=precioVenta[:len(precioVenta)-1]
                self.__dolarBolsaVenta.set(f'${precioVenta}')
            fecha=datetime.now()
        self.__fechaActual.set('{}/{}/{} {}:{}'.format(fecha.day,fecha.month,fecha.year,fecha.hour,fecha.minute))    
    

