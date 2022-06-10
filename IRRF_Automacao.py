#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests
from tkinter import *

def calcula_irrf():
    
    salario = 0
    desconto = 0
    
    salario = entry1.get()
    
    if salario == "":
        salario = 0
    else: salario = salario
    
    if float(salario) <= 1903.98:
        desconto = 0
        
    elif float(salario) >= 1903.99 and float(salario) <= 2826.65:
        desconto = 142.80
        
    elif float(salario) >= 2826.66 and float(salario) <= 3751.05:
        desconto = 354.80
        
    elif float(salario) >= 3751.06 and float(salario) <= 4664.68:
        desconto = 636.13
        
    else:
        desconto = 869.36  
    
    texto_resposta['text'] = f'''
    Salario Bruto: {salario}
    Desconto IRRF 2022: {desconto}
    Salarío Líquido: {float(salario) - desconto}
    '''

#Instancia o frame
janela = Tk()
#Tamanho do Frame
janela.geometry('450x350')


#titulo
janela.title("Calculo desconto IRRF")

#Botao calcular + posição
texto = Label(janela, text="Digite seu salário base: ")
texto.grid(column=0, row=0, padx=10, pady=10)


botao = Button(janela, text="Calcular IRRF 2022", command=calcula_irrf)
botao.grid(column=1, row=1, padx=10, pady=10)

entry1 = Entry (janela)
entry1.grid(column=1, row=0, padx=10, pady=10)

texto_resposta = Label(janela, text="")
texto_resposta.grid(column=1, row=3, padx=10, pady=10)


janela.mainloop()


# In[ ]:




