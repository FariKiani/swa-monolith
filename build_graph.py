from collections import defaultdict

from dijkstra import Graph, dijkstra

lookup = defaultdict(lambda: {})


def get_weight(mapping, a, b):
    w = 0
    try:
        w += mapping[a][b]
    except KeyError:
        pass
    try:
        w += mapping[b][a]
    except KeyError:
        pass
    return w


def get_distance(calls, changes, service_a, service_b):
    try:
        return lookup[service_a][service_b]
    except KeyError:
        distance = get_weight(changes, service_a, service_b) \
                   + get_weight(calls, service_a, service_b)
        lookup[service_a][service_b] = distance
        return distance


def get_distances(g, service, services):
    dijkstra(g, g.get_vertex(service), g.get_vertex('ALL'))
    row = {}
    for service_b in services:
        row[service_b] = round(g.get_vertex(service_b).distance, 4)
    return row


def build_graph(calls, changes, services):
    isolation_count = 0
    g = Graph()

    for service_a in services:
        g.add_vertex(service_a)

    for service_a in services:
        connection_count = 0
        for service_b in services:
            weight = get_distance(calls, changes, service_a, service_b)

            if weight > 0:
                connection_count += 1
                # print(service_a, service_b, weight)
                g.add_edge(service_a, service_b, weight)

    return g
