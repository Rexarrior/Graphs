import numpy as np


def Dijkstra(graph, start_vertex):
    '''
    graph - adjaency matrix of graph
    return row of weights of minimal distance between
    start_vertex and other vertexes
    '''
    n = graph.shape[0]
    is_not_visited = np.array([True] * n)
    weight = np.array([float('inf')] * n)
    weight[start_vertex] = 0
    for i in range(n):
        weights_not_visited = weight[is_not_visited]
        min_weight = np.min(weights_not_visited)
        accepted = is_not_visited * (weight == min_weight)
        min_id = np.where(accepted)[0][0]
        
        for j in range(n):
            if is_not_visited[j] and graph[min_id, j] != 0:
                new_weight = graph[min_id, j] + weight[min_id]
                if new_weight < weight[j]:
                    weight[j] = new_weight
        is_not_visited[min_id] = False
    return weight


def get_distances_matrix(graph):
    '''
    graph is adjaency matrix of graph
    return matrix of distances between vertexes
    '''
    distances = np.empty(graph.shape, dtype='float')
    for i in range(distances.shape[0]):
        distances[i] = Dijkstra(graph, i)
    return distances


def get_eccentricity_matrix(graph):
    '''
    graph is adjaency matrix of graph
    returns row of eccentricity of vertexes:
    '''
    distances = get_distances_matrix(graph)
    eccentricity = np.max(distances, axis=0)
    return eccentricity


def get_diameter(eccentricity):
    '''
    eccentricity - row of eccentricity of graph
    returns diameter of graph
    '''
    return np.max(eccentricity)


def get_radius(eccentricity):
    '''
    eccentricity - row of eccentricity of graph
    returns radius of graph
    '''
    return np.min(eccentricity)


def get_periphery_vertexes(eccentricity, diameter):
    '''
    eccentricity - row of eccentricity of graph
    returns periphery vertexes of graph
    '''
    return np.where(eccentricity == diameter)[0]


def get_central_vertexes(eccentricity, radius):
    '''
    eccentricity - row of eccentricity of graph
    returns central vertexes of graph
    '''
    return np.where(eccentricity == radius)[0]


def get_average_distance(distances):
    '''
    distances is a matrix of all distances between vertexes in graph
    returns average distance in graph
    '''
    return np.average(distances)
