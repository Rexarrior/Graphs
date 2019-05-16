import json


def write_graph_matrix_to_csv(matrix, path):
    with open(path, 'wt', encoding='utf8') as f:
        n = matrix.shape[0]
        for i in range(n):
            f.write(f'{i};')
        for i in range(n):
            for j in range(n):
                f.write(f'{graph[i,j]};')
            f.write('\n')


def load_json(path):
    with open(path, 'rt', encoding='utf-8') as f:
        return json.load(f)


def save_json(path, target):
    with open(path, 'wt', encoding='utf-8') as f: 
        json.dump(target, f)


def write_matrixes_to_csv(matrixes, description, path):
    # we think that all matrixes is equal-sized and square
    with open(path, 'wt', encoding='utf-8') as f:
        n = matrixes[0].shape[0]
        for i in range(len(matrixes)):
            matrix = matrixes[i]
            f.write(description[i])
            f.write('\n')
            f.write(' ;')
            for k in range(matrix.shape[1]):
                    f.write(f'{k};')
            f.write('\n')
            for j in range(matrix.shape[0]):
                f.write(f'{j};')
                for k in range(matrix.shape[1]):
                    f.write(f'{matrix[j, k]};')
                f.write('\n')
            f.write('\n'*3)
                