import numpy as np
import alghoritms.distances as dist
import alghoritms.similarity as sim


def compute_degree_centrality(graph, x_ind):
    neighbours = sim.get_neighbours(graph, x_ind)
    return neighbours.shape[0] / graph.shape[0]


def _compute_closeness_centrality(graph, x_ind, distances_matrix):
    n = graph.shape[0]
    sum_distances = np.sum(distances_matrix[x_ind])
    measure = (n-1) / sum_distances


def compute_closeness_centrality(graph, x_ind):
    distances = dist.get_distances_matrix(graph)
    return _compute_closeness_centrality(graph, distances)


def _compute_betweenness_centrality(graph, )