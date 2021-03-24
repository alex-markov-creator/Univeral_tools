#-*- coding=utf-8 -*-
"""
dfs_while_vs_dfs_recursion.py - сравнение времени выполнения
алгоритма поиска в глубину через рекурсивную функцию с алгоритмом
dfs через инструкцию while.
"""
import unittest
import pytest
import time

def dfs_recursion(graph:dict, node:str or int, visited:list)->list:
    if node not in visited:
        visited.append(node)
        for k in graph[node]:
            dfs_recursion(graph, k, visited)
    return visited

def dfs_while(graph:dict, node:str)->list:
    visited = [node]
    stack = [node]
    while stack:
        node = stack[-1]
        if node not in visited:
            visited.extend(node)
        remove_from_stack = True
        for next in graph[node]:
            if next not in visited:
                stack.extend(next)
                remove_from_stack = False
                break
        if remove_from_stack:
            stack.pop()
    return visited


class TestDfs(unittest.TestCase):
        """[summary]
        Test for the file evclid.py

        Arguments:
            unittest {[type]} -- [description]
        """

        # visited = dfs(test_graph_1, 'A',[])
        #Output ['A','B','S','C','D','E','H','G','F']

        def test_dfs_recursion(self):
            test_graph_1 = {
                    'A': ['B','S'],
                    'B': ['A'],
                    'C': ['D','E', 'F', 'S'],
                    'D': ['C'],
                    'E': ['C','H'],
                    'F': ['C','G'],
                    'G': ['F','S'],
                    'H': ['E','G'],
                    'S': ['A','C','G']
            }
            test_graph_2 = {
                    'S': [1,6,8],
                    1: [2,3],
                    2: [11,10],
                    3: [12,4],
                    4: [3,13,5],
                    5: [4,6,9],
                    6: [5,7, 'S'],
                    7: [6,8],
                    8: [7, 'S', 14],
                    9: [5, 'T'],
                    10 : [],
                    11: [],
                    12: [],
                    13: [],
                    14: [],
                    'T': [9]
            }
            self.assertEqual(['A','B','S','C','D','E','H','G','F'], dfs_recursion(test_graph_1, 'A',[]))
            self.assertEqual(['S',1,2,11,10,3,12,4,13,5,6,7,8,14,9,'T'], dfs_recursion(test_graph_2, 'S',[]))

        def test_dfs_while(self):
            test_graph_1 = {
                    'A': ['B','S'],
                    'B': ['A'],
                    'C': ['D','E', 'F', 'S'],
                    'D': ['C'],
                    'E': ['C','H'],
                    'F': ['C','G'],
                    'G': ['F','S'],
                    'H': ['E','G'],
                    'S': ['A','C','G']
            }
            self.assertEqual(['A','B','S','C','D','E','H','G','F'], dfs_while(test_graph_1, 'A'))

        def test_time(self):
            test_graph_1 = {
                'A': ['B','S'],
                'B': ['A'],
                'C': ['D','E', 'F', 'S'],
                'D': ['C'],
                'E': ['C','H'],
                'F': ['C','G'],
                'G': ['F','S'],
                'H': ['E','G'],
                'S': ['A','C','G']
                }
            start = time.perf_counter_ns()
            dfs_while(test_graph_1, 'A')
            stop = time.perf_counter()
            print(f'Время dfs_while = {stop-start}')

            start = time.perf_counter_ns()
            visited = dfs_recursion(test_graph_1, 'A',[])
            stop = time.perf_counter()
            print(f'Время dfs_recursion = {stop-start}')

if __name__ == '__main__':
    unittest.main()

