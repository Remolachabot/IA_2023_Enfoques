import networkx as nx
import matplotlib.pyplot as plt
import random

# Generar grafo aleatorio
def generar_grafo_aleatorio(num_nodos, probabilidad_conexion):
    grafo = nx.erdos_renyi_graph(num_nodos, probabilidad_conexion)
    return grafo

# Agente activo
def agente_activo(estado_actual, grafo):
    # El agente activo toma una acción aleatoria
    acciones_posibles = list(grafo.neighbors(estado_actual))
    accion_elegida = random.choice(acciones_posibles)
    return accion_elegida

# Agente pasivo
def agente_pasivo(grafo):
    # Inicializar la tabla de recompensas
    tabla_recompensas = {}

    # Crear el gráfico
    plt.figure()
    pos = nx.spring_layout(grafo)
    nx.draw(grafo, pos, with_labels=True, node_color='lightblue', node_size=500, font_size=12, font_weight='bold')
    plt.title("Proceso de Aprendizaje por Refuerzo Pasivo")

    # Repetir el proceso de aprendizaje varias veces
    for i in range(1, 101):
        estado_actual = random.choice(list(grafo.nodes()))  # Estado inicial aleatorio
        ruta = [estado_actual]  # Ruta seguida por el agente pasivo

        while True:
            if len(list(grafo.neighbors(estado_actual))) == 1:
                break

            accion_elegida = agente_activo(estado_actual, grafo)  # Observar la acción tomada por el agente activo
            estado_siguiente = accion_elegida  # El siguiente estado es la acción tomada
            ruta.append(estado_siguiente)  # Actualizar la ruta
            estado_actual = estado_siguiente  # Actualizar el estado actual

        # Asignar una recompensa al estado final de la ruta
        estado_final = ruta[-1]
        if estado_final not in tabla_recompensas:
            tabla_recompensas[estado_final] = 0
        tabla_recompensas[estado_final] += 1

        # Dibujar el grafo con la ruta actual
        plt.figure()
        plt.title(f"Iteración {i}")
        nx.draw(grafo, pos, with_labels=True, node_color='lightblue', node_size=500, font_size=12, font_weight='bold')
        nx.draw_networkx_nodes(grafo, pos, nodelist=ruta, node_color='orange', node_size=500)
        nx.draw_networkx_edges(grafo, pos)
        plt.pause(0.5)

    # Imprimir la tabla de recompensas
    print("Tabla de recompensas:")
    for estado, recompensa in tabla_recompensas.items():
        print(f"Estado: {estado}, Recompensa: {recompensa}")

    # Mostrar todos los gráficos
    plt.show()

# Generar el grafo aleatorio
grafo_aleatorio = generar_grafo_aleatorio(10, 0.2)

# Ejecutar el agente pasivo
agente_pasivo(grafo_aleatorio)
