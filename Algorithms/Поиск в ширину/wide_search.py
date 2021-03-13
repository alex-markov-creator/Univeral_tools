# Алгоритм поиска в ширину
######################################################## 
from collections import deque

# Построение условного графа в виде словарей
########################################################
graph = {}
graph["you"] = ["alice", "bob", "claire"]
graph["bob"] = ["anuj", "peggy"]
graph["alice"] = ["peggy"]
graph["claire"] = ["thom","jonny"]
graph["anuj"] = []
graph["peggy"] = []
graph["thom"] = []
graph["jonny"] = []
# Создание двусторонней очереди
#########################################################

def person_is_seller(name):
    return name[-1] == 'm'

def search(name):
    search_queue = deque()
    search_queue += graph[name]
    searched = [] # список проверенных элементов
    while search_queue: # пока очередь не пуста
        person = search_queue.popleft() # из очереди извлекается первый элемент
        if not person in searched: # проверка на дублирование
            if person_is_seller(person): # проверка на выполнение условия
                print (person.upper() + " is a mango seller!")
                return True
            else:
                search_queue += graph[person] # добавление в очередь второго уровня 
                searched.append(person) # добавление в список проверенных
    return False

search("you")


