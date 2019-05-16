from serializers import *
import alghoritms.converters as conv
import alghoritms.dfs as dfs


def dfs_test():
    graph_list = load_json("data\\graph.json")
    graph_matrix = conv.graph_list_to_matrix(graph_list)
    components, order = dfs.dfs(graph_matrix)
    print(components)
    print("\n"*3)
    print(order)


def converters_test():
    with open('data\\graph.json', 'rt', encoding='utf8') as f:
        graph = json.loads(f.read())
    orinted_graph_matrix = conv.graph_list_to_matrix(graph)
    graph_matrix = conv.graph_to_not_orientied(orinted_graph_matrix)
    write_graph_matrix_to_csv(orinted_graph_matrix, 'data\\orinted_graph.csv')
    write_graph_matrix_to_csv(graph_matrix, 'data\\non_orinted_graph.csv')
    lst_graph = conv.graph_matrix_to_list(orinted_graph_matrix)
    print(lst_graph)
