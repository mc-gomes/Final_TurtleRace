import tkinter as tk
from turtle import RawTurtle
from time import sleep
from random import randint


CVWIDTH = 650
CVHEIGHT = 500

# JANELA PRINCIPAL
root = tk.Tk()
root.title('Turtle Race')
root.config(bg='#f2f0eb')

# Frame com a mensagem para a escolha do palpite
frameescolhas = tk.Frame(root, pady=20)
frameescolhas.grid(row=0, column=0, padx=10, pady=10)

tk.Label(frameescolhas, text="""Quem você acha que vai ganhar?
 Dê o seu palpite entre as opções disponíveis, 
 em seguida inicie o jogo.""").pack(side="top", pady=15)

# Tela da área da corrida
canvas = tk.Canvas(root, width=CVWIDTH, height=CVHEIGHT)
canvas.configure(bg='green')
canvas.grid(row=0, column=1, padx=10, pady=10)

# INICIALIZAÇÃO DOS OBJETOS TURTLE

# Turtle para marcar a linha de partida
t_linha_start = RawTurtle(canvas)
t_linha_div = RawTurtle(canvas)
t_linha_div.ht()

# Turtle para gerar os pontos no mapa
t_pontos = RawTurtle(canvas)
t_pontos.ht()

# Turtle de corrida 1
t1 = RawTurtle(canvas)
t1.shape('turtle')
t1.ht()
t1.color("orange")
t1.speed(1)

# Turtle de corrida 2
t2 = RawTurtle(canvas)
t2.shape('turtle')
t2.ht()
t2.color("blue")
t2.speed(1)


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
    t_linha_chegada.ht()
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


def gerar_pontos(cor: str, y):
    t_pontos.ht()
    t_pontos.color(cor)
    t_pontos.speed(2)

    coord = []

    if y == 1:
        for _ in range(10):
            x = randint(-200, 200)
            y = randint(50, 220)
            coord.append((x, y))
            t_pontos.up()
            t_pontos.setpos(x, y)
            t_pontos.down()
            t_pontos.dot(10)

    if y == 2:
        for _ in range(10):
            x = randint(-200, 200)
            y = randint(-220, -50)
            coord.append((x, y))
            t_pontos.up()
            t_pontos.setpos(x, y)
            t_pontos.down()
            t_pontos.dot(10)

    return coord


def set_posicoes():
    t1.up()
    t1.speed(4)
    t1.setpos(-270, 125)
    t1.speed(1)

    t2.up()
    t2.speed(4)
    t2.setpos(-270, -125)
    t2.speed(1)


def inicializar():
    t_pontos.clear()
    t1.st()
    t1.clear()
    t2.st()
    t2.clear()
    set_posicoes()


def valendo():
    inicializar()
    botao_iniciar.config(state='disabled')
    botao_reset.config(state='disabled')
    opt1.config(state='disabled')
    opt2.config(state='disabled')

    t1.down()
    t2.down()

    coordenadas1 = gerar_pontos('red', 1)
    coordenadas2 = gerar_pontos('purple', 2)

    sleep(0.5)
    for i in range(len(coordenadas1)):
        t1.speed(randint(1, 4))
        t2.speed(randint(1, 4))
        t1.goto(coordenadas1[i])
        t2.goto(coordenadas2[i])

    while t1.xcor() <= 250 and t2.xcor() <= 250:
        t1.forward(randint(6, 10))
        t2.forward(randint(6, 10))

    vencedor()

    botao_iniciar.config(state='normal')
    botao_reset.config(state='normal')
    opt1.config(state='normal')
    opt2.config(state='normal')


def vencedor():

    FONT = ("Courier", 18, "bold")

    if t1.xcor() > t2.xcor():
        t1.write('Laranja venceu!', font=FONT, align='right')
    else:
        t2.write('Azul venceu!', font=FONT, align='right')


if __name__ == '__main__':
    opcoes = {'Laranja': 'orange', 'Azul': 'blue'}
    v = tk.StringVar(None, opcoes['Laranja'])

    opt1 = tk.Radiobutton(
        frameescolhas,
        text=list(opcoes.keys())[0],
        padx=20,
        variable=v,
        value=opcoes['Laranja'])
    opt1.pack(anchor=tk.W)

    opt2 = tk.Radiobutton(
        frameescolhas,
        text=list(opcoes.keys())[1],
        padx=20,
        variable=v,
        value=opcoes['Azul'])
    opt2.pack(anchor=tk.W)

    gerar_linhas()
    inicializar()

    framebotao = tk.Frame(root, pady=20)
    framebotao.grid(row=0, column=2, padx=10, pady=10)

    botao_iniciar = tk.Button(framebotao, text="Iniciar corrida", command=valendo,
                              state='normal')
    botao_iniciar.pack(pady=10)

    botao_reset = tk.Button(framebotao, text="Reiniciar", command=inicializar,
                            state='normal')
    botao_reset.pack(pady=5)

    root.mainloop()
