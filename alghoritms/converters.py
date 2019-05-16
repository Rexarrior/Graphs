import numpy as np
import json


def graph_list_to_matrix(graph):
    n = len(graph)
    ret = np.zeros((n, n))
    for i in range(n):
        for j in graph[i]:
            ret[i, j] = 1
    return ret


def graph_matrix_to_list(graph):
    ret = []
    for i in range(graph.shape[0]):
        cols = np.where(graph[i] > 0)
        ret.append([cols[j] for j in range(len(cols))])
    return ret


def graph_to_not_orientied(graph_matrix):
    graph_matrix = graph_matrix.copy()
    n = graph_matrix.shape[0]
    for i in range(n):
        for j in range(n):
            if (graph_matrix[i, j] == 1):
                graph_matrix[j, i] = 1
    return graph_matrix


def get_subgraph(graph, target_vertexes, id_map):
    '''
    graph is adjaency list of graph
    target_vertexes is a list of int - labels\indexes of vertexes in graph
    '''
    new_graph = [graph[i] for i in target_vertexes]
    i_map = {target_vertexes[i]: i for i in range(len(target_vertexes))}

    for i in range(len(new_graph)):
        edge_list = new_graph[i]
        new_edge_list = []
        for end_vertex in edge_list:
            if (end_vertex in target_vertexes):
                new_edge_list.append(i_map[end_vertex])
        new_graph[i] = new_edge_list

    new_id_map = {}
    for old_id in i_map.keys():
        new_id_map[i_map[old_id]] = id_map[old_id]

    return new_graph, new_id_map
