import numpy as np


def get_indegree(graph_matrix, ind):
    return np.sum(graph_matrix[ind])


def get_outdegree(graph_matrix, ind):
    return np.sum(graph_matrix[:, ind])


def get_indegrees(graph_matrix):
    return np.sum(graph_matrix, axis=1)


def get_outdegrees(graph_matrix):
    return np.sum(graph_matrix, axis=0)


def get_degrees(graph_matrix, is_orinted=False):
    if is_orinted:
        return get_indegrees(graph_matrix) + get_outdegrees(graph_matrix)
    else:
        return get_indegrees(graph_matrix)
