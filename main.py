from serializers import *
import alghoritms.converters as conv
import alghoritms.dfs as dfs
import alghoritms.degrees as deg
import alghoritms.probability_density as dens
import visualization.histogram as hist
import alghoritms.distances as dist
import alghoritms.similarity as sim


def compute_graph_connectivity(graph, properties):
    components, order = dfs.dfs(graph)
    properties['is graph strongly connected'] = len(components) == 1
    properties['strong connectivity components count'] = \
        len(components)
    component_lengths = [len(component) for component in components]
    component_lengths = sorted(component_lengths)
    properties['lengths of strong connectivity components'] = component_lengths
    not_oriented_graph = conv.graph_to_not_orientied(graph)
    components, order = dfs.dfs(not_oriented_graph)
    properties['is graph weakly connected'] = len(components) == 1
    properties['weak connectivity components count'] = \
        len(components)
    component_lengths = [len(component) for component in components]
    component_lengths = sorted(component_lengths)
    properties['lengths of weak connectivity components'] = component_lengths
    persent = component_lengths[-1] / graph.shape[0]
    properties['persent of vertexes of' +
               ' max weak connectivity component'] = persent
    return components


def get_graph_max_component(graph, components, id_map):
    lengths = [len(component) for component in components]
    max_lengths = max(lengths)
    i = lengths.index(max_lengths)
    component = list(components[i])
    subgraph, new_id_map = conv.get_subgraph(graph, component, id_map)
    return subgraph, new_id_map


def degrees(graph, properties):
    density, average_degree = dens.\
        get_degrees_probability_density(graph, compute_average=True)
    properties["vertexes degree probability density"] = density.tolist()
    properties["average vertex degree"] = average_degree
    hist.make_and_save_gistogram(density, "report\\density_histogram.png")
    eccentricity = dist.get_eccentricity_matrix(graph)
    distances = dist.get_distances_matrix(graph)
    diameter = dist.get_diameter(eccentricity)
    properties["diameter of graph"] = diameter
    radius = dist.get_radius(eccentricity)
    properties["radius of graph"] = radius
    properties["average way length"] = dist.get_average_distance(distances)
    periphery_vertexes = dist.get_periphery_vertexes(eccentricity, diameter)
    central_vertexes = dist.get_central_vertexes(eccentricity, radius)
    properties["central vertexes of graph"] = central_vertexes.tolist()
    properties["periphery vertexes of graph"] = periphery_vertexes.tolist()


def similarity(graph, properties):
    matrixes = list(sim.compute_all_similarity_measures(graph))
    descriptions = ['Common Neighbors', 'Jaccard’s Coefficient',
                    'Adamic/Adar', 'Preferential Attachment']
    write_matrixes_to_csv(matrixes, descriptions, 'report\\similarity.csv')


def main():
    properties = dict()
    graph = load_json("data\\graph.json")
    id_map = load_json("data\\id_map.json")
    id_map = {int(key): id_map[key] for key in id_map.keys()}
    graph_matrix = conv.graph_list_to_matrix(graph)
    components = compute_graph_connectivity(graph_matrix, properties)
    graph, id_map = get_graph_max_component(graph, components, id_map)
    graph_matrix = conv.graph_list_to_matrix(graph)
    graph_matrix = conv.graph_to_not_orientied(graph_matrix)
    degrees(graph_matrix, properties)
    similarity(graph_matrix, properties)
    save_json("report\\properties.json", properties)
