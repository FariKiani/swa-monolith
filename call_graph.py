from collections import defaultdict
from math import log

from read_file import read_file


def get_call_edge_dict():
    filename = 'input/call_graph.csv'

    edges = read_file(filename, lambda row: [row[0], row[1], log(int(row[2]))])
    # cycles = find_cycles(edges)
    max_weight = max([edge[2] for edge in edges])
    print(max_weight)

    for edge in edges:
        edge.append(1 - edge[2] / max_weight)
        # print(edge)

    edge_dict = defaultdict(lambda: {})
    for edge in edges:
        edge_dict[edge[0]][edge[1]] = edge[3]

    return edge_dict


def get_change_edge_dict():
    filename = 'input/change_graph.csv'

    edges = read_file(filename, lambda row: [row[0], row[1], log(int(row[2]))])
    # cycles = find_cycles(edges)
    max_weight = max([edge[2] for edge in edges])
    print(max_weight)

    for edge in edges:
        edge.append(1 - edge[2] / max_weight)
        # print(edge)

    edge_dict = defaultdict(lambda: {})
    for edge in edges:
        edge_dict[edge[0]][edge[1]] = edge[3]

    return edge_dict
