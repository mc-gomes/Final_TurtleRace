import tkinter as tk
import turtle
from turtle import ScrolledCanvas, RawTurtle, TurtleScreen
from time import sleep
import random


CVWIDTH = 650
CVHEIGHT = 500

root = tk.Tk()
root.title('Turtle Race')
root.config(bg='#f2f0eb')


frameescolhas = tk.Frame(root, pady=20)
frameescolhas.grid(row=0, column=0, padx=10, pady=10)

tk.Label(frameescolhas, text="""Escolha entre as opções disponíveis, 
 em seguida inicie o jogo.""").pack(side="top", pady=15)

canvas = tk.Canvas(root, width=CVWIDTH, height=CVHEIGHT)
canvas.configure(bg='green')
canvas.grid(row=0, column=1, padx=10, pady=10)

screen = TurtleScreen(canvas).bgcolor('green')
t_linha_start = RawTurtle(canvas)
t_linha_div = RawTurtle(canvas)
t_linha_div.ht()

t_pontos = RawTurtle(canvas)
t_pontos.ht()

tartuga = RawTurtle(canvas)
tartuga.ht()
tartuga.color("blue")
tartuga.speed(1)


def gerar_linhas():
    t_linha_start.ht()
    t_linha_start.up()
    t_linha_start.setpos(-250, CVHEIGHT / 2)
    t_linha_start.right(90)
    sleep(0.3)
    t_linha_start.down()
    t_linha_start.forward(CVHEIGHT)

    t_linha_div.ht()
    t_linha_div.up()
    t_linha_div.setpos(-CVWIDTH / 2.0, 0)
    sleep(0.2)
    t_linha_div.down()
    t_linha_div.forward(CVWIDTH-65)

    gerar_linha_chegada()


def gerar_linha_chegada():
    espaco = 20
    t_linha_chegada = RawTurtle(canvas)
    t_linha_chegada.shape('square')
    t_linha_chegada.up()
    t_linha_chegada.speed(4)

    t_linha_chegada.color('black')
    for i in range(13):
        t_linha_chegada.goto(260, (240 - (i * espaco * 2)))
        t_linha_chegada.stamp()

    for i in range(13):
        t_linha_chegada.goto(260 + espaco, ((240 - espaco) - (i * espaco * 2)))
        t_linha_chegada.stamp()

    t_linha_chegada.color('#d4d2cf')
    for i in range(13):
        t_linha_chegada.goto(260, (220 - (i * espaco * 2)))
        t_linha_chegada.stamp()

    for i in range(13):
        t_linha_chegada.goto(260 + espaco, ((260 - espaco) - (i * espaco * 2)))
        t_linha_chegada.stamp()


def gerar_pontos(cor: str):
    t_pontos.ht()
    t_pontos.color(cor)
    t_pontos.speed(1)

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
    tartuga.speed(4)
    tartuga.setpos(-270, -125)
    tartuga.speed(1)


def inicializar():
    t_pontos.clear()
    tartuga.st()
    tartuga.clear()
    set_posicoes()


def valendo():
    inicializar()
    botao_iniciar.config(state='disabled')
    botao_reset.config(state='disabled')
    opt1.config(state='disabled')
    opt2.config(state='disabled')

    tartuga.down()

    coordenadas = gerar_pontos('red')

    sleep(0.5)
    for i in range(len(coordenadas)):
        tartuga.goto(coordenadas[i])
        sleep(0.7)

    while tartuga.xcor() <= 250:
        print(tartuga.xcor())
        tartuga.forward(10)
    botao_iniciar.config(state='normal')
    botao_reset.config(state='normal')
    opt1.config(state='normal')
    opt2.config(state='normal')


def ver_escolha():
    escolha_user = v.get()
    return escolha_user


v = tk.StringVar()
opcoes = ['Azul', 'Verde']
v.set(opcoes[0])


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


if __name__ == '__main__':
    gerar_linhas()
    inicializar()

    framebotao = tk.Frame(root, pady=20)
    framebotao.grid(row=0, column=2, padx=10, pady=10)

    botao_iniciar = tk.Button(framebotao, text="Iniciar trajeto", command=valendo,
                              state='normal')
    botao_iniciar.pack(pady=10)

    botao_reset = tk.Button(framebotao, text="Reiniciar", command=inicializar,
                            state='normal')
    botao_reset.pack(pady=5)

    root.mainloop()
