# Final_TurtleRace

**Número da Lista**: 31<br>
**Conteúdo da Disciplina**: Final<br>

## Alunos
|Matrícula | Aluno |
| -- | -- |
| 19/0090901  | Laura Pinos |
| 19/0093331 |  Matheus Costa |

## Sobre 
O projeto é uma corrida realizada automaticamente entre duas tartarugas, que são instâncias do objeto Turtle da biblioteca importada. O objetivo é que uma termine o trajeto antes da outra, passando por todos os pontos gerados antes de irem para a linha de chegada. Utilizamos dos conteúdos de Grafos (algoritmo de Prim) e Dividir e Conquistar (Par de pontos mais próximos) para auxiliar na lógica do jogo.

Após iniciado o jogo, serão plotados pontos aleatórios na tela para cada uma das tartarugas, e esses pontos formarão um grafo para cada. Com os grafos gerados, é aplicado o **algoritmo de Prim** em cada um para criar as respectivas Árvores Geradoras Mínimas (minimum spanning tree), e em seguida, como resultado do algoritmo, os pesos atribuídos a cada aresta são utilizados para se calcular uma média que irá determinar a velocidade inicial de cada tartaruga.

Em segundo plano, o algoritmo para calcular o **Par de Pontos mais próximos** é aplicado para encontrar qual é esse par em cada grafo, e assim que uma tartaruga passa pelos pontos que fazem parte desse par, sua velocidade é aumentada fazendo com que ela termine mais rápido o seu trajeto.

## Screenshots

![tela_de_inicio](https://user-images.githubusercontent.com/72279998/217545088-41a59a2d-3d0c-4711-8609-246a2cab608a.png)

![tela_pontos](https://user-images.githubusercontent.com/72279998/217545240-1b7b4c9e-95a5-47b0-9fe4-8e0c47ded405.png)

![tela_fim_corrida](https://user-images.githubusercontent.com/72279998/217545349-0f799536-9e80-43da-9c47-56eab18b0364.png)


## Instalação 
**Linguagem**: Python3 <br>
**Framework**: bibliotecas 'turtle' e 'tkinter' (padrão do python) <br>
Para rodar a aplicação é necessário ter no mínimo a versão Python3.8 instalada na máquina.

Garanta que possui a biblioteca `tkinter` instalada. Por padrão essa biblioteca geralmente vem incluída junto com o python, mas caso ocorra algum problema, realize a instalação pelos seguintes comandos no terminal:

Linux:

```sudo apt-get install python3-tk```

Windows:

```pip install tk```

Em seguida clone o repositório e entre na pasta src e digite o seguinte comando no terminal:
`python3 main.py`

## Uso 
Ao clicar no botão "Iniciar corrida" que aparecerá na tela, o jogo iniciará automaticamente e as tartarugas percorrerão o campo alcançando todos os pontos antes de irem para a linha de chegada.

