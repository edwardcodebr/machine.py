import numpy as np

# Definir os nós da treliça (coordenadas x, y)
nos = {
    1: (0, 0),
    2: (5, 0),
    3: (10, 0),
    4: (0, 5),
    5: (5, 5),
    6: (10, 5)
}

# Definir os membros da treliça (conectando nós)
membros = [
    (1, 4),
    (1, 5),
    (2, 5),
    (2, 6),
    (3, 6),
    (4, 5),
    (5, 6),
    (1, 2),
    (2, 3)
]

# Definir as forças aplicadas nos nós (força em x, força em y)
forcas = {
    1: (0, 0),
    2: (0, 0),
    3: (0, 0),
    4: (0, -10),  # Força aplicada no nó 4
    5: (0, 0),
    6: (0, 0)
}

# Função para calcular a matriz de rigidez de um membro
def calcular_rigidez_membro(n1, n2):
    x1, y1 = nos[n1]
    x2, y2 = nos[n2]
    L = np.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    c = (x2 - x1) / L
    s = (y2 - y1) / L
    k = np.array([
        [c*c, c*s, -c*c, -c*s],
        [c*s, s*s, -c*s, -s*s],
        [-c*c, -c*s, c*c, c*s],
        [-c*s, -s*s, c*s, s*s]
    ])
    return k / L

# Montar a matriz global de rigidez
n_nos = len(nos)
K = np.zeros((2*n_nos, 2*n_nos))
for n1, n2 in membros:
    k = calcular_rigidez_membro(n1, n2)
    indices = [
        2*(n1-1), 2*(n1-1)+1,
        2*(n2-1), 2*(n2-1)+1
    ]
    for i in range(4):
        for j in range(4):
            K[indices[i], indices[j]] += k[i, j]

# Aplicar as condições de contorno (apoios)
apoios = [1, 2, 3]
for a in apoios:
    idx = 2 * (a - 1)
    K[idx, :] = 0
    K[:, idx] = 0
    K[idx, idx] = 1
    K[idx + 1, :] = 0
    K[:, idx + 1] = 0
    K[idx + 1, idx + 1] = 1

# Montar o vetor de forças
F = np.zeros(2 * n_nos)
for n, (fx, fy) in forcas.items():
    F[2 * (n - 1)] = fx
    F[2 * (n - 1) + 1] = fy

# Resolver o sistema de equações para encontrar os deslocamentos
deslocamentos = np.linalg.solve(K, F)

# Calcular as forças nos membros
for n1, n2 in membros:
    x1, y1 = nos[n1]
    x2, y2 = nos[n2]
    L = np.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    c = (x2 - x1) / L
    s = (y2 - y1) / L
    indices = [
        2*(n1-1), 2*(n1-1)+1,
        2*(n2-1), 2*(n2-1)+1
    ]
    u = np.array([
        deslocamentos[indices[0]], deslocamentos[indices[1]],
        deslocamentos[indices[2]], deslocamentos[indices[3]]
    ])
    k = np.array([
        [c, s, -c, -s]
    ])
    f = (1 / L) * np.dot(k, u)
    print(f'Força no membro ({n1}, {n2}): {f[0]:.2f} N')

# Exibir os deslocamentos dos nós
for n in range(1, n_nos + 1):
    dx = deslocamentos[2 * (n - 1)]
    dy = deslocamentos[2 * (n - 1) + 1]
    print(f'Deslocamento no nó {n}: ({dx:.4f}, {dy:.4f}) m')
