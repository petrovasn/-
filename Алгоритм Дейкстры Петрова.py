import sys

def dijkstra(graph, start_vertex):
    num_vertices = len(graph)

    # Массив для хранения кратчайших расстояний до каждой вершины
    shortest_distances = [sys.maxsize] * num_vertices
    shortest_distances[start_vertex] = 0

    # Массив для отслеживания посещённых вершин
    visited = [False] * num_vertices

    # Массив для хранения предыдущих вершин на кратчайшем пути
    previous_vertices = [None] * num_vertices

    for _ in range(num_vertices):
        # Выбираем вершину с минимальным расстоянием
        min_distance = sys.maxsize
        min_vertex = -1

        for vertex in range(num_vertices):
            if shortest_distances[vertex] < min_distance and not visited[vertex]:
                min_distance = shortest_distances[vertex]
                min_vertex = vertex

        if min_vertex == -1:
            break  # Все доступные вершины посещены

        # Пометить найденную вершину как посещенную
        visited[min_vertex] = True

        # Обновить расстояния до соседних (смежных) вершин
        for neighbor in range(num_vertices):
            if graph[min_vertex][neighbor] > 0 and not visited[neighbor]:
                new_distance = shortest_distances[min_vertex] + graph[min_vertex][neighbor]
                if new_distance < shortest_distances[neighbor]:
                    shortest_distances[neighbor] = new_distance
                    previous_vertices[neighbor] = min_vertex  # Сохраняем путь

    return shortest_distances, previous_vertices

def get_shortest_path(previous_vertices, start_vertex, end_vertex):
    path = []
    current_vertex = end_vertex
    while current_vertex is not None:
        path.append(current_vertex)
        current_vertex = previous_vertices[current_vertex]
    path.reverse()  # Путь построен в обратном порядке
    return path

# Пример использования

# Матрица смежности
graph = [
    [0, 2, 1, 0, 0],
    [2, 0, 4, 7, 0],
    [1, 4, 0, 3, 5],
    [0, 7, 3, 0, 6],
    [0, 0, 5, 6, 0]
]
# Запуск алгоритма
start_vertex = 0
shortest_distances, previous_vertices = dijkstra(graph, start_vertex)

# Вывод результата
print("Кратчайшие расстояния от вершины", start_vertex, ":", shortest_distances)
for end_vertex in range(len(graph)):
    if end_vertex != start_vertex and shortest_distances[end_vertex] != sys.maxsize:
        path = get_shortest_path(previous_vertices, start_vertex, end_vertex)
        print(f"Кратчайший путь от вершины {start_vertex} до вершины {end_vertex}: {path}, расстояние: {shortest_distances[end_vertex]}")
