import sys


def dijkstra(graph, start_vertex):
    num_vertices = len(graph)

    # Массив для хранения кратчайших расстояний до каждой вершины
    shortest_distances = [sys.maxsize] * num_vertices
    shortest_distances[start_vertex] = 0

    # Массив для отслеживания посещённых вершин
    visited = [False] * num_vertices

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

    return shortest_distances


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
shortest_paths = dijkstra(graph, start_vertex)

# Вывод результата
print("Кратчайшие расстояния от вершины", start_vertex, ":", shortest_paths)