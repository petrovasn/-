import networkx as nx

# кол-во вершин
n = 60
# вероятность появления случайного ребра
p = 0.45
# генерация графа
G = nx.erdos_renyi_graph(n, p)
# расчёт средней степени вершин графа
a = 0

for n in G.nodes():
    a = a + G.degree(n)
# средняя степень вершины фактическая
a_avr = float(a) / len(G.nodes())

# средняя степень вершины по формуле
calc_avr = (n-1)*p

# разница значений
div_a = calc_avr - a_avr

print("Средняя степень вершины фактическая: ", round(a_avr, 2))
print("Средняя степень вершины по формуле: ", round(calc_avr, 2))
print("Полученная разница значений: ", round(div_a, 2))



