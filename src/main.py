import tkinter as tk
import turtle
from turtle import ScrolledCanvas, RawTurtle, TurtleScreen
from time import sleep
import random


CVWIDTH = 650
CVHEIGHT = 500

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

canvas = tk.Canvas(root, width=CVWIDTH, height=CVHEIGHT)
canvas.grid(row=0, column=1, padx=10, pady=10)

screen = TurtleScreen(canvas)
t_linha_div = RawTurtle(canvas)
t_linha_div.ht()
t_linha_div.up()
t_linha_div.setpos(-CVWIDTH/2.0, 0)
sleep(0.5)
t_linha_div.down()
t_linha_div.forward(CVWIDTH)

t_pontos = RawTurtle(canvas)
t_pontos.color('red')
t_pontos.ht()

tartuga = RawTurtle(canvas)
tartuga.color("blue")
tartuga.speed(1)


def gerar_pontos():
    coord = []

    for _ in range(10):
        x = random.randint(-200, 200)
        y = random.randint(-200, -50)
        coord.append((x, y))
        t_pontos.up()
        t_pontos.setpos(x, y)
        t_pontos.down()
        t_pontos.dot(10)

    return coord


def set_posicoes():
    tartuga.up()
    tartuga.setpos(-270, -125)


def inicializar():
    tartuga.clear()
    set_posicoes()
    t_pontos.clear()


def valendo():
    inicializar()
    botao_iniciar.config(state='disabled')
    botao_reset.config(state='disabled')
    opt1.config(state='disabled')
    opt2.config(state='disabled')

    tartuga.down()

    coordenadas = gerar_pontos()

    sleep(0.5)
    for i in range(len(coordenadas)):
        tartuga.goto(coordenadas[i])
        sleep(0.8)

    tartuga.forward(150)
    botao_iniciar.config(state='normal')
    botao_reset.config(state='normal')
    opt1.config(state='normal')
    opt2.config(state='normal')


inicializar()

size = 10
t_pontos.speed(1)

framebotao = tk.Frame(root, pady=20)
framebotao.grid(row=0, column=2, padx=10, pady=10)

botao_iniciar = tk.Button(framebotao, text="Iniciar trajeto", command=valendo,
                          state='normal')
botao_iniciar.pack(pady=10)

botao_reset = tk.Button(framebotao, text="Reiniciar", command=inicializar,
                        state='normal')
botao_reset.pack(pady=5)

tartuga.down()

root.mainloop()
