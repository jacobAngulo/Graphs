import sys
sys.path.append('../graph')
from util import Queue

def earliest_ancestor(rel_graph, target):
    paths = []
    q = Queue()
    q.enqueue([target])
    while len(q.queue) > 0:
        v = q.dequeue()
        for rel in rel_graph:
            if rel[1] == v[-1]:
                path_copy = list(v)
                path_copy.append(rel[0])
                q.enqueue(path_copy)
        if len(v) > 1:
            paths.append(v)
    possible_solutions = []
    if len(paths) == 0:
        return -1
    else:
        for path in paths:
            if len(path) == len(paths[-1]):
                possible_solutions.append(path)
        for i in range(len(possible_solutions)):
            possible_solutions[i] = possible_solutions[i][-1]
        solution = possible_solutions[0]
        for possible_solution in possible_solutions:
            if possible_solution < solution:
                solution = possible_solution
        return solution


print(earliest_ancestor([(1, 3), (2, 3), (3, 6), (5, 6),
                         (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)], 6))
