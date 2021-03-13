# Хэш таблица графа для демонстрации алгоритма Дейкстры
#######################################################
graph = {}
graph["start"] = {}
graph["start"]["a"] = 6
graph["start"]["b"] = 2
graph["a"] = {}
graph["a"]["fin"] = 1
graph["b"] = {}
graph["b"]["a"] = 3
graph["b"]["fin"] = 5
graph["fin"] = {}
print(graph)
# Создание стоимостей
######################
infinity = float("inf")
costs = {}
costs["a"] = 6
costs["b"] = 2
costs["fin"] = infinity
print(costs)
# Создание хэш-таблицы родителей
################################
parents = {}
parents["a"] = "start"
parents["b"] = "start"
parents["in"] = None
print(parents)
##############
processed = [] # массив для отслеживания всех уже обработанных узлов
print(processed)
# Алгоритм
##############

def find_lowest_cost_node(costs):
    lowest_cost = float("inf")
    lowest_cost_node = None
    for node in costs: # перебрать все узлы
        cost = costs[node]
        if cost < lowest_cost and node not in processed:
            # если это узел с наименьшей стоимостью из уже виденных и он еще не был обработан
            lowest_cost = cost # он назначается новым узлом с наименьшей стоимостью
            lowest_cost_node = node
    return lowest_cost_node

node = find_lowest_cost_node(costs) # найти узел с наименьшей стоимостью среди обработанных
while node is not None: # если обработаны все узлы, цикл while завершен
    cost = costs[node]
    neighbors = graph[node]
    for n in neighbors.keys(): # перебрать всех соседей текущего узла
        new_cost = cost + neighbors[n] # если к соседу можно быстрее добраться через текущий узел
        if costs[n] > new_cost:
            costs[n] = new_cost # обновить стоимость для этого узла
            parents[n] = node # этот узел становится новым родителем для соседа
    processed.append(node) # узел помечается как обработанный
    node = find_lowest_cost_node(costs) # найти следующий узел для обработки и повторить цикл

print("\n")
print(processed)
print("\n Стоимость кратчайшего пути")
print(costs)