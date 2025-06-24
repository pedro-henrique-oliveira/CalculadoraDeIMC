from tkinter import *
from tkinter import Tk, ttk
from tkinter import messagebox

#cores
co0 =  '#ffffff'
co1 =  '#1c1c1c'
co2 = '#4065a1'
co3 = '#4f4f4f'

janela = Tk()
janela.title('')
janela.geometry('295x230')
janela.configure(bg=co0)

frame_cima = Frame(janela, width=295, height=60, bg=co0, pady=1, padx=0, relief="flat")
frame_cima.grid(row=0, column=0, sticky=NSEW)

frame_baixo = Frame(janela, width=400, height=230, bg=co0, pady=1, padx=0, relief="flat")
frame_baixo.grid(row=1, column=0, sticky=NSEW)

# configurando frame_cima
app_nome = Label(frame_cima, text='Calculadora de IMC', width=23, height=1, padx=0, relief='flat', anchor='center', font=('Ivy 16'), bg=co0, fg=co1)
app_nome.place(x=0, y=0)

app_nome = Label(frame_cima, text='', width=400, height=1, padx=0, relief='flat', anchor='center', font=('Ivy 1'), bg=co2, fg=co1)
app_nome.place(x=0, y=35)

def calcular():
    peso = float(e_peso.get())
    altura = float(e_altura.get())

    imc = peso / altura**2

    resultado = imc

    if resultado < 18.5:
        l_resultado_texto['text'] = "Abaixo do peso"
    elif resultado >= 18.5 and resultado < 25:
        l_resultado_texto['text'] = "Peso normal"
    elif resultado >= 25 and resultado < 29.9:
        l_resultado_texto['text'] = "Sobrepeso"
    elif resultado >= 30 and resultado < 34.9:
        l_resultado_texto['text'] = "Obesidade grau 1"
    elif resultado >= 35 and resultado < 39.9:
        l_resultado_texto['text'] = "Obesidade grau 2"
    else:
        l_resultado_texto['text'] = "Obesidade (Mórbida)"

    l_resultado['text'] = "{:.{}f}".format(resultado, 2)


l_peso = Label(frame_baixo, text='Insira seu peso', height=1, padx=0, relief='flat', anchor='center', font=('Ivy 10 bold'), bg=co0, fg=co1)
l_peso.grid(row=0, column=0, sticky=NSEW, pady=10, padx=3)

e_peso = Entry(frame_baixo,width=5 ,relief='solid', font=('Ivy 10 bold '), justify='center')
e_peso.grid(row=0, column=1, sticky=NSEW, pady=10, padx=3)


l_altura = Label(frame_baixo, text='Insira sua altura', height=1, padx=0, relief='flat', anchor='center', font=('Ivy 10 bold'), bg=co0, fg=co1)
l_altura.grid(row=1, column=0, sticky=NSEW, pady=10, padx=3)

e_altura = Entry(frame_baixo,width=5 ,relief='solid', font=('Ivy 10 bold '), justify='center')
e_altura.grid(row=1, column=1, sticky=NSEW, pady=10, padx=3)

l_resultado = Label(frame_baixo, text='---', width=5 ,height=1, padx=6, pady=12, relief='flat', anchor='center', font=('Ivy 24 bold'), bg=co2, fg=co0)
l_resultado.place(x=170, y=10)

l_resultado_texto = Label(frame_baixo, text='', width=37 ,height=1, padx=0, pady=0, relief='flat', anchor='center', font=('Ivy 10 bold'), bg=co0, fg=co1)
l_resultado_texto.place(x=0, y=90)

b_calcular = Button(frame_baixo,command=calcular, text='Calcular', width=34 ,height=1,overrelief=SOLID, relief='raised', anchor='center', font=('Ivy 10 bold'), bg=co2, fg=co0)
b_calcular.grid(row=4, column=0, sticky=NSEW, pady=50, padx=5, columnspan=30)



janela.mainloop()
