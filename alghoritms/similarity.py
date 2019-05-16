import numpy as np


def get_neighbours(graph, ind):
    '''
    graph is adjaency matrix of graph
    ind is index of vertex
    return row of indexes of neighbours of ind-vertex
    '''
    return np.where(graph[ind] > 0)[0]


def _compute_common_neighbors(first, second):
    '''
    first and second - neighbours of vertexes
    '''
    intersection = np.intersect1d(first, second)
    return intersection.shape[0]


def compute_common_neighbors(graph, x_ind, y_ind):
    '''
    graph is adjaency matrix of graph
    x_ind - index of first vertex
    y_ind - index of second vertex
    returns value of common neighbours similarity measure
    '''
    first = get_neighbours(graph, x_ind)
    second = get_neighbours(graph, y_ind)
    return _compute_common_neighbors(first, second)


def _compute_jaccard_coeff(first, second):
    '''
    first and second - neighbours of vertexes
    '''
    intersection = np.intersect1d(first, second)
    union = np.union1d(first, second)
    coeff = intersection.shape[0] / union.shape[0]
    return coeff


def compute_jaccard_coeff(graph, x_ind, y_ind):
    '''
    graph is adjaency matrix of graph
    x_ind - index of first vertex
    y_ind - index of second vertex
    returns value of jaccard coefficient
    '''
    first = get_neighbours(graph, x_ind)
    second = get_neighbours(graph, y_ind)
    return _compute_jaccard_coeff(first, second)


def _compute_adamic_adar_coeff(graph, first, second, lengthes):
    '''
    graph is adjaency matrix of graph
    first and second are rows of neighbours of vertexes
    lengthes - map index of vertex to len of its neighbours
    returns value of adamic_adar_coefficient
    '''
    union = np.union1d(first, second)
    terms = np.empty(union.shape[0])
    for i in range(union.shape[0]):
        if (union[i] not in lengthes.keys()):
            lengthes[union[i]] = get_neighbours(graph, union[i]).shape[0]
        terms[i] = lengthes[union[i]]
    terms = np.log(terms)
    coeff = np.sum(terms)
    return coeff


def compute_adamic_adar_coeff(graph, x_ind, y_ind):
    '''
    graph is adjaency matrix of graph
    x_ind - index of first vertex
    y_ind - index of second vertex
    returns value of adamic_adar_coefficient
    '''
    first = get_neighbours(graph, x_ind)
    second = get_neighbours(graph, y_ind)
    lengthes = dict()
    return _compute_adamic_adar_coeff(graph, first, second, lengthes)


def _compute_preferential_attachment(first, second):
    '''
    graph is adjaency matrix of graph
    first, second are rows of neighbours of vertexes
    '''
    coeff = first.shape[0] * second.shape[0]
    return coeff


def compute_preferential_attachment(graph, x_ind, y_ind):
    '''
    graph is adjaency matrix of graph
    x_ind - index of first vertex
    y_ind - index of second vertex
    returns value of preferential attachment coeff
    '''
    first = get_neighbours(graph, x_ind)
    second = get_neighbours(graph, y_ind)
    return _compute_preferential_attachment(first, second)


def _complete_upper_triangular_matrix(matrix):
    for i in range(matrix.shape[0]):
        for j in range(i):
            matrix[i, j] = matrix[j, i]
    return matrix


def compute_neighbours_map(graph):
    ret = dict()
    for i in range(graph.shape[0]):
        ret[i] = get_neighbours(graph, i)
    return ret


def _compute_common_neighbours_matrix(graph, neighbours_map):
    '''
    graph is adjaency matrix of graph
    returns matrix of similarity by common neighbours measure
    '''
    ret_matrix = np.empty(graph.shape)
    for i in range(graph.shape[0]):
        for j in range(i, graph.shape[1]):
            ret_matrix[i, j] =\
                 _compute_common_neighbors(neighbours_map[i],
                                           neighbours_map[j])
    ret_matrix = _complete_upper_triangular_matrix(ret_matrix)
    return ret_matrix


def compute_common_neighbours_matrix(graph):
    '''
    graph is adjaency matrix of graph
    returns matrix of common neighbours similarity measure
    '''
    neighbours_map = compute_neighbours_map(graph)
    return _compute_common_neighbours_matrix(graph, neighbours_map)


def _compute_jaccard_coeff_matrix(graph, neighbours_map):
    ret_matrix = np.empty(graph.shape)
    for i in range(graph.shape[0]):
        for j in range(i, graph.shape[1]):
            ret_matrix[i, j] =\
                _compute_jaccard_coeff(neighbours_map[i],
                                       neighbours_map[j])
    ret_matrix = _complete_upper_triangular_matrix(ret_matrix)
    return ret_matrix


def compute_jaccard_coeff_matrix(graph):
    '''
    graph is adjaency matrix of graph
    returns matrix of jaccard similarity measure
    '''
    neighbours_map = compute_neighbours_map(graph)
    return _compute_jaccard_coeff_matrix(graph, neighbours_map)


def _compute_adamic_adar_matrix(graph, neighbours_map, lengthes):
    ret_matrix = np.empty(graph.shape)
    for i in range(graph.shape[0]):
        for j in range(i, graph.shape[1]):
            ret_matrix[i, j] =\
                _compute_adamic_adar_coeff(graph, neighbours_map[i],
                                           neighbours_map[j], lengthes)
    ret_matrix = _complete_upper_triangular_matrix(ret_matrix)
    return ret_matrix


def compute_jaccard_coeff_matrix(graph):
    '''
    graph is adjaency matrix of graph
    returns matrix of adamic\\adar similarity measure
    '''
    neighbours_map = compute_neighbours_map(graph)
    lengthes = dict()
    return _compute_adamic_adar_matrix(graph, neighbours_map, lengthes)


def _compute_preferential_attachment_matrix(graph, neighbours_map):
    ret_matrix = np.empty(graph.shape)
    for i in range(graph.shape[0]):
        for j in range(i, graph.shape[1]):
            ret_matrix[i, j] =\
                _compute_preferential_attachment(neighbours_map[i],
                                                 neighbours_map[j])
    ret_matrix = _complete_upper_triangular_matrix(ret_matrix)
    return ret_matrix


def compute_preferential_attachment_matrix(graph):
    '''
    graph is adjaency matrix of graph
    returns matrix of preferential_attachment similarity measure
    '''
    neighbours_map = compute_neighbours_map(graph)
    return _compute_preferential_attachment_matrix(graph, neighbours_map)


def compute_all_similarity_measures(graph):
    '''
    graph is adjaency matrix of graph
    returns matrixes of all similarity measures in next order:
    common, jaccard, adamic\\adar, preferential_attachment
    '''
    neighbours_map = compute_neighbours_map(graph)
    lengthes = dict()
    common = _compute_common_neighbours_matrix(graph, neighbours_map)
    jaccard = _compute_jaccard_coeff_matrix(graph, neighbours_map)
    adamic_adar = _compute_adamic_adar_matrix(graph, neighbours_map, lengthes)
    preferential_attachment =\
        _compute_preferential_attachment_matrix(graph, neighbours_map)
    return common, jaccard, adamic_adar, preferential_attachment
