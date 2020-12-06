from collections import defaultdict
from typing import List

from unioinfind.unionfind import UnionFind


def find_cycles(edges):
    def _find_cycles(adjacent_dict):
        cycles = []

        def extract_cycle(node, stack):

            cycle = []
            for el in reversed(stack):
                cycle.append(el)
                if (el == node):
                    break
            return cycle

        def rec(pos, stack: List):
            if (pos in stack):
                cycle = extract_cycle(pos, stack)
                cycles.append(cycle)
                return
            next_edges = adjacent_dict[pos];
            if (len(next_edges) == 0):
                return

            stack.append(pos)
            for next in adjacent_dict[pos]:
                rec(next, stack)
            stack.pop()

        keys = list(adjacent_dict.keys())
        for start_node in keys:
            rec(start_node, [])

        return cycles

    edge_dict = defaultdict(lambda: [])
    for edge in edges:
        edge_dict[edge[0]].append(edge[1])

    cycles = _find_cycles(edge_dict)
    s = set()
    for cycle in cycles:
        for service in cycle:
            s.add(service)

    uf = UnionFind(list(s))

    for cycle in cycles:
        a = cycle.pop()
        for service in cycle:
            uf.union(a, service)

    return uf.component_mapping();
