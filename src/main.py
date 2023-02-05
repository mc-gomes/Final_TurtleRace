import tkinter as tk
import turtle
from turtle import ScrolledCanvas, RawTurtle, TurtleScreen
from time import sleep

root = tk.Tk()
root.config(bg='#f2f0eb')

v = tk.StringVar()

opcoes = ['Azul', 'Verde']
v.set(opcoes[0])

frameescolhas = tk.Frame(root, pady=20)
frameescolhas.grid(row=0, column=0, padx=10, pady=10)

tk.Label(frameescolhas, text="""Escolha entre as opções disponíveis, 
 em seguida inicie o jogo.""").pack(side="top", pady=15)


def ver_escolha():
    escolha_user = v.get()
    return escolha_user


opt1 = tk.Radiobutton(
    frameescolhas,
    text=opcoes[0],
    padx=20,
    variable=v,
    command=ver_escolha,
    value=opcoes[0])
opt1.pack(anchor=tk.W)

opt2 = tk.Radiobutton(
    frameescolhas,
    text=opcoes[1],
    padx=20,
    variable=v,
    command=ver_escolha,
    value=opcoes[1])
opt2.pack(anchor=tk.W)

canvas = tk.Canvas(root, width=600, height=400)
canvas.grid(row=0, column=1, padx=10, pady=10)

screen = TurtleScreen(canvas)
tartuga = RawTurtle(canvas)
tartuga.color("blue")
tartuga.speed(1)


def set_posicoes():
    tartuga.up()
    tartuga.setpos(-150, -150)


def reiniciar():
    tartuga.clear()
    set_posicoes()


def valendo():
    botao_iniciar.config(state='disabled')
    botao_reset.config(state='disabled')
    opt1.config(state='disabled')
    opt2.config(state='disabled')

    tartuga.down()

    xy = [(-50, 50), (-35, 60), (-20, -45), (20, 0)]
    sleep(0.5)
    for i in range(len(xy)):
        tartuga.goto(xy[i])
        sleep(0.8)

    tartuga.forward(150)
    botao_iniciar.config(state='normal')
    botao_reset.config(state='normal')
    opt1.config(state='normal')
    opt2.config(state='normal')


framebotao = tk.Frame(root, pady=20)
framebotao.grid(row=0, column=2, padx=10, pady=10)

botao_iniciar = tk.Button(framebotao, text="Iniciar trajeto", command=valendo,
                          state='normal')
botao_iniciar.pack(pady=10)

botao_reset = tk.Button(framebotao, text="Reiniciar", command=reiniciar,
                        state='normal')
botao_reset.pack(pady=5)

tartuga.down()

root.mainloop()

