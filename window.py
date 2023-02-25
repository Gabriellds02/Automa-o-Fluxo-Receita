from tkinter import *
from tkinter import ttk
from Data_frame import BaseDados
from automatic_web import Bot
import tkinter as tk
from tkinter import messagebox
import pyautogui
import time


lista_anos = ['2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020', '2021', '2022']


def robo ():
    bot = Bot()
    verifica = cb_anos.get()
    if verifica == '2022':
        messagebox.showinfo(f"Msg", "Seu robô trabalhará em segundo plano, aguarde o encerramento para gerar o Dashboard")
        bot.rodar_bot()
        messagebox.showinfo(f"Msg", "Receitas do exercício financeiro de 2022 e oriundas do FNAS, foram atualizadas com sucesso")
    elif verifica == '2021':
        messagebox.showinfo(f"Msg", "Seu robô trabalhará em segundo plano, aguarde o encerramento para gerar o Dashboard")
        bot.rodar_bot_2021()
        messagebox.showinfo(f"Msg", "Receitas do exercício financeiro de 2021 e oriundas do FNAS, foram atualizadas com sucesso")
    elif verifica == '2020':
        messagebox.showinfo(f"Msg", "Seu robô trabalhará em segundo plano, aguarde o encerramento para gerar o Dashboard")
        bot.rodar_bot_2020()
        messagebox.showinfo(f"Msg", "Receitas do exercício financeiro de 2020 e oriundas do FNAS, foram atualizadas com sucesso")
    elif verifica == '2019':
        messagebox.showinfo(f"Msg", "Seu robô trabalhará em segundo plano, aguarde o encerramento para gerar o Dashboard")       
        bot.rodar_bot_2019()
        messagebox.showinfo(f"Msg", "Receitas do exercício financeiro de 2019 e oriundas do FNAS, foram atualizadas com sucesso")
    elif verifica == '2018':
        messagebox.showinfo(f"Msg", "Seu robô trabalhará em segundo plano, aguarde o encerramento para gerar o Dashboard")
        bot.rodar_bot_2018()
        messagebox.showinfo(f"Msg", "Receitas do exercício financeiro de 2018 e oriundas do FNAS, foram atualizadas com sucesso")
    elif verifica == '2017':
        messagebox.showinfo(f"Msg", "Seu robô trabalhará em segundo plano, aguarde o encerramento para gerar o Dashboard")
        bot.rodar_bot_2017()
        messagebox.showinfo(f"Msg", "Receitas do exercício financeiro de 2017 e oriundas do FNAS, foram atualizadas com sucesso")
    elif verifica == '2016':
        messagebox.showinfo(f"Msg", "Seu robô trabalhará em segundo plano, aguarde o encerramento para gerar o Dashboard")
        bot.rodar_bot_2016()
        messagebox.showinfo(f"Msg", "Receitas do exercício financeiro de 2016 e oriundas do FNAS, foram atualizadas com sucesso")
    elif verifica == '2015':
        messagebox.showinfo(f"Msg", "Seu robô trabalhará em segundo plano, aguarde o encerramento para gerar o Dashboard")
        bot.rodar_bot_2015()
        messagebox.showinfo(f"Msg", "Receitas do exercício financeiro de 2015 e oriundas do FNAS, foram atualizadas com sucesso")
    elif verifica == '2014':
        messagebox.showinfo(f"Msg", "Seu robô trabalhará em segundo plano, aguarde o encerramento para gerar o Dashboard")
        bot.rodar_bot_2014()
        messagebox.showinfo(f"Msg", "Receitas do exercício financeiro de 2014 e oriundas do FNAS, foram atualizadas com sucesso")
    elif verifica == '2013':
        messagebox.showinfo(f"Msg", "Seu robô trabalhará em segundo plano, aguarde o encerramento para gerar o Dashboard")
        bot.rodar_bot_2013()
        messagebox.showinfo(f"Msg", "Receitas do exercício financeiro de 2013 e oriundas do FNAS, foram atualizadas com sucesso")

def dados ():
    dados = BaseDados()
    dados.logica()
    pyautogui.alert('Não utilize o computador até o fim do uso do bot')
    pyautogui.press('Win')
    pyautogui.write('Data_Base.xlsm')
    pyautogui.press('Backspace')
    pyautogui.press('enter')
   

def btn_clicked():
    print("Button Clicked")

window = Tk()

window.geometry("1182x663")
window.configure(bg = "#202122")
canvas = Canvas(
    window,
    bg = "#202122",
    height = 663,
    width = 1182,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
canvas.place(x = 0, y = 0)

background_img = PhotoImage(file = f"background.png")
background = canvas.create_image(
    562.0, 311.0,
    image=background_img)

cb_anos = ttk.Combobox(window, values=lista_anos)
cb_anos.set('2022')
cb_anos.place(x = 889, y = 392,
        width = 106,
        height = 27)

img0 = PhotoImage(file = f"img0.png")
b0_bot = Button(
    image = img0,
    borderwidth = 0,
    highlightthickness = 0,
    command =lambda:[robo()],
    relief = "flat")

b0_bot.place(
    x = 660, y = 489,
    width = 170,
    height = 110)


img1 = PhotoImage(file = f"img1.png")
b1_dashboard = Button(
    image = img1,
    borderwidth = 0,
    highlightthickness = 0,
    command = lambda:[dados()],
    relief = "flat")

b1_dashboard.place(
    x = 933, y = 489,
    width = 170,
    height = 110)

img2 = PhotoImage(file = f"img2.png")
b2 = Button(
    image = img2,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b2.place(
    x = 2, y = 13,
    width = 45,
    height = 44)

img3 = PhotoImage(file = f"img3.png")
b3 = Button(
    image = img3,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b3.place(
    x = 0, y = 599,
    width = 50,
    height = 45)

window.resizable(False, False)
window.mainloop()





