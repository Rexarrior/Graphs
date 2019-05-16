import random

import numpy as np


def choice_vertex(vertexes, priority):
    if priority is None:
        current_vertex = random.choice(list(vertexes))
        # first_v = list(leftover)[0]
    else:
        hight = 0
        for vertex in vertexes:
            if hight < priority[vertex]:
                hight = priority[vertex]
                current_vertex = vertex
    return current_vertex


def component_deep_search(graph_matrix, start_vertex, visited,
                          order, counter):
    stack = list()
    current_component = set()
    stack.append(start_vertex)
    stack.append(start_vertex)
    while len(stack):
        v = stack.pop()
        if v not in visited:
            visited.add(v)
            current_component.add(v)
            for vertex, flug in enumerate(graph_matrix[v]):
                if (flug and vertex not in visited):
                    stack.append(vertex)
                    stack.append(vertex)
        else:
            if v not in order:
                counter += 1
                order[v] = counter
    return current_component


def dfs(graph_matrix, priority=None):
    order = dict()
    counter = 0
    visited = set()
    remaining = set(range(graph_matrix.shape[0]))
    components = list()
    while len(visited) != graph_matrix.shape[0]:
        current_vertex = choice_vertex(remaining, priority)
        current_component = component_deep_search(graph_matrix,
                                                  current_vertex,
                                                  visited, order,
                                                  counter)
        remaining = remaining - visited
        components.append(current_component)
    return (components, order)
  