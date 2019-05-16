import matplotlib.pyplot as plt


def make_and_save_gistogram(data, path_to_save):
    '''
    data is 2-d array with x in first row and y in second
    '''
    ax = plt.gca()
    ax.bar(data[0], data[1], align='edge') 
    # ax.set_xticks(x)
    # ax.set_xticklabels(('first', 'second', 'third', 'fourth'))
    plt.savefig(path_to_save)
