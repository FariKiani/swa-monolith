from numpy import Inf

from build_graph import build_graph, get_distances


def build_patches(call_edge_dict, change_edge_dict, services):
    patches = []

    def _build_patches(_services):
        g = build_graph(call_edge_dict, change_edge_dict, _services)
        if len(_services) > 0:
            first = _services[0]
            distance_map = get_distances(g, first, _services)
            reachable = []
            unreachable = []
            for service in _services:
                d = distance_map[service]
                if d == Inf:
                    unreachable.append(service)
                else:
                    reachable.append(service)

            patches.append(reachable)
            _build_patches(unreachable)

    _build_patches(services)
    return patches
