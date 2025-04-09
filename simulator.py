import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import random

# Este código demonstra a relação direta entre Álgebra Linear e Fractais.
# Em particular, veremos como as transformações afins – representadas por uma matriz
# 2x2 (parte linear) e um vetor de translação (parte afim) – podem ser iteradas para 
# gerar padrões extremamente complexos e belos, como a Samambaia de Barnsley.
# Representação geral de uma transformação afim:

#           [ x' ]   =   [ a   b ]   [ x ]   +   [ e ]
#           [ y' ]       [ c   d ]   [ y ]       [ f ]

# Cada uma das quatro transformações utilizadas possui uma probabilidade associada,
# determinando com que frequência ela é aplicada durante as iterações. A soma das
# probabilidades é igual a 1.

# Definição das transformações para a Samambaia de Barnsley.
# Dicionários que representam as transformações:
# • 'matrix': a matriz 2x2 que representa a transformação linear.
# • 'offset': o vetor de translação (representa a parte afim da transformação).
# • 'prob': a probabilidade de escolha dessa transformação.

transformations = [
    {
        'matrix': np.array([[0.0, 0.0],
                            [0.0, 0.16]]),
        'offset': np.array([0.0, 0.0]),
        'prob': 0.01   # 1% de probabilidade
    },
    {
        'matrix': np.array([[0.85, 0.04],
                            [-0.04, 0.85]]),
        'offset': np.array([0.0, 1.6]),
        'prob': 0.85   # 85% de probabilidade
    },
    {
        'matrix': np.array([[0.2, -0.26],
                            [0.23, 0.22]]),
        'offset': np.array([0.0, 1.6]),
        'prob': 0.07   # 7% de probabilidade
    },
    {
        'matrix': np.array([[-0.15, 0.28],
                            [0.26, 0.24]]),
        'offset': np.array([0.0, 0.44]),
        'prob': 0.07   # 7% de probabilidade
    }
]

# Apply_transformation, esta função aplica uma transformação afim a um ponto.
# • point: array [x, y] representando o ponto atual.
# • transformation: dicionário.
#
# Utilizando np.dot, a função realiza a multiplicação da matriz pelo ponto e soma o vetor
# de translação, retornando o novo ponto transformado.

def apply_transformation(point, transformation):
    new_point = transformation['matrix'].dot(point) + transformation['offset']
    return new_point

# choose_transformation seleciona aleatoriamente uma das transformações com base na probabilidade acumulada.
# Gera um número aleatório entre 0 e 1 e, percorrendo as transformações, soma as
# probabilidades até encontrar aquela em que o número gerado é menor ou igual à soma acumulada.

def choose_transformation(transformations):
    r = random.random()  # Número aleatório entre 0 e 1
    cumulative_prob = 0.0
    for t in transformations:
        cumulative_prob += t['prob']
        if r <= cumulative_prob:
            return t
    # Caso raro, retorna a última transformação:
    return transformations[-1]

# ----------------------------------
# Montamos a função que anima a Samambaia
# ----------------------------------

def animate_barnsley():
    num_points = 200000  # Número total de pontos a serem gerados
    points = np.zeros((num_points, 2))  # Vetor para armazenar os pontos (cada linha é [x, y])
    
    # Define o ponto inicial como (0, 0)
    current_point = np.array([0.0, 0.0])
    points[0] = current_point
    
    # Itera para gerar os pontos aplicando transformações afins escolhidas aleatoriamente
    for i in range(1, num_points):
        trans = choose_transformation(transformations)
        current_point = apply_transformation(current_point, trans)
        points[i] = current_point
    
    fig, ax = plt.subplots(figsize=(6, 10))
    scat = ax.scatter([], [], s=0.1, c='#5dbb63')
    ax.set_title("Evolução da Samambaia de Barnsley")
    ax.axis("off")
    
    # Ajusta limites para garantir que o fractal apareça
    ax.set_xlim(-3, 3)
    ax.set_ylim(0, 10)
    
    def init():
        scat.set_offsets(np.empty((0, 2)))
        return scat,
    
    def update(frame):
        total_frames = 200
        max_index = min(num_points, int((frame / total_frames) * num_points))
        scat.set_offsets(points[:max_index])
        # Redefine limites (se quiser atualizar dinamicamente)
        ax.relim()
        ax.autoscale_view()
        return scat,
    
    ani = animation.FuncAnimation(
        fig, 
        update, 
        frames=500,    # quantos frames de animação
        init_func=init, 
        interval=400,  # intervalo em ms entre cada frame (mais alto => mais lento)
        blit=False, 
        repeat=False
    )
    
    plt.show()



#                          FRACTAL 2: CURVA DE KOCH


def koch_curve_points(p1, p2, depth):
    """
    Retorna a lista de pontos da curva de Koch para duas extremidades p1 e p2
    e uma profundidade (depth).
    """
    if depth == 0:
        return [p1, p2]
    else:
        # p1 e p2 são arrays np: ex.: [x1, y1], [x2, y2]
        p1 = np.array(p1)
        p2 = np.array(p2)
        # Vetor base
        base = p2 - p1
        # Pontos de divisão (1/3 e 2/3 ao longo do segmento)
        pA = p1 + base / 3
        pB = p1 + 2 * base / 3
        # Ponto do "triângulo" que fica "para fora" - rotacionando o vetor base 60 graus
        # O vetor base/3 girado 60 graus: (x, y) -> (x*cos60 - y*sin60, x*sin60 + y*cos60)
        # cos60=0.5, sin60=√3/2
        rot = np.array([[0.5, -np.sqrt(3)/2],
                        [np.sqrt(3)/2, 0.5]])
        peak = pA + rot.dot(base/3)
        
        # Chama recursivamente para cada um dos 4 segmentos
        curve = []
        curve += koch_curve_points(p1, pA, depth - 1)[:-1]  # evita duplicar o final
        curve += koch_curve_points(pA, peak, depth - 1)[:-1]
        curve += koch_curve_points(peak, pB, depth - 1)[:-1]
        curve += koch_curve_points(pB, p2, depth - 1)
        return curve

def animate_koch():
    """
    Anima a construção iterativa da curva de Koch.
    """
    # Número de iterações (profundidade)
    max_depth = 5
    # Pontos iniciais (vértices de um segmento grande)
    p1 = np.array([-1.5, 0])  
    p2 = np.array([1.5, 0])   
    # Vamos gerar uma lista de listas de pontos:
    # Ex.: all_levels[0] = curva de profundidade 0 (linha reta)
    #      all_levels[1] = curva de profundidade 1 ...
    all_levels = []
    for depth in range(max_depth + 1):
        pts = koch_curve_points(p1, p2, depth)
        all_levels.append(np.array(pts))
    
    # Agora animamos esses níveis de detalhe
    fig, ax = plt.subplots()
    ax.set_title("Curva de Koch")
    ax.set_aspect('equal', 'box')
    ax.axis("off")
    
    line, = ax.plot([], [], lw=1, c='blue')  # linha vazia inicial
    
    # Para manter o mesmo enquadramento em todos os frames
    ax.set_xlim(-1.7, 1.7)
    ax.set_ylim(-1, 1)
    
    def init():
        line.set_data([], [])
        return line,
    
    def update(frame):
        # frame = índice da iteração (0 até max_depth)
        pts = all_levels[frame]
        x, y = pts[:, 0], pts[:, 1]
        line.set_data(x, y)
        return line,
    
    ani = animation.FuncAnimation(
        fig,
        update,
        frames=len(all_levels),  # = max_depth+1
        init_func=init,
        interval=800,           # ms de pausa entre frames
        blit=False,
        repeat=False
    )
    
    plt.show()



#                          FRACTAL 3: TRIÂNGULO DE SIERPINSKI

def animate_sierpinski():
    """
    Gera e anima o Triângulo de Sierpinski usando IFS (método do ponto médio).
    """
    # Vértices do triângulo principal
    # Podem ser alterados para mudar o tamanho/posição
    A = np.array([0, 0])
    B = np.array([2, 4])
    C = np.array([4, 0])
    
    # Iniciamos com um ponto qualquer (ex., A)
    current = A.copy()
    
    # Quantos pontos gerar
    total_points = 30000
    points_sier = np.zeros((total_points, 2))
    points_sier[0] = current
    
    # Gera os pontos: cada vez, escolhe-se randomicamente um vértice e
    # move-se o ponto atual para o ponto médio entre ele e o vértice escolhido.
    vertices = [A, B, C]
    for i in range(1, total_points):
        chosen = random.choice(vertices)
        current = (current + chosen) / 2.0
        points_sier[i] = current
    
    # Agora faremos uma animação que mostra o surgimento desses pontos
    fig, ax = plt.subplots()
    ax.set_title("Triângulo de Sierpinski (IFS)")
    scat = ax.scatter([], [], s=0.5, c='red')
    ax.set_aspect('equal', 'box')
    ax.axis("off")
    
    # Definir limites do triângulo
    ax.set_xlim(-1, 5)
    ax.set_ylim(-1, 5)
    
    def init():
        scat.set_offsets(np.empty((0,2)))
        return scat,
    
    def update(frame):
        # frame vai de 0 até, digamos, 100
        # definimos quantos frames queremos
        total_frames = 100
        max_index = min(total_points, int((frame / total_frames) * total_points))
        scat.set_offsets(points_sier[:max_index])
        return scat,
    
    ani = animation.FuncAnimation(
        fig,
        update,
        frames=100,   # quantos "passos" de animação
        init_func=init,
        interval=100, # ms entre frames
        blit=False,
        repeat=False
    )
    
    plt.show()

# 1) Samambaia de Barnsley
animate_barnsley()

# 2) Curva de Koch
animate_koch()

# 3) Triângulo de Sierpinski
animate_sierpinski()
