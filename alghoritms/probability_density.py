from alghoritms.degrees import *
import numpy as np


def get_degrees_probability_density(graph_matrix, is_orinted=False,
                                    compute_average=False):
    degrees = get_degrees(graph_matrix, is_orinted)
    unique_degrees, count = np.unique(degrees, return_counts=True)
    count = count / graph_matrix.shape[0]
    density = np.array(list(zip(unique_degrees, count)))
    density = density.ravel().reshape((2, density.shape[0]), order='F')
    if compute_average:
        average = np.sum(count)
        return density, average
    else:
        return density
