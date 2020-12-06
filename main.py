import json
import os

from build_graph import build_graph, get_distances
from call_graph import get_call_edge_dict, get_change_edge_dict
from patches import build_patches
from service_list import get_service_list

# READ INPUT

services = get_service_list()
call_edge_dict = get_call_edge_dict()
change_edge_dict = get_change_edge_dict()

length = len(services)


# BUILD PATCHES (subgraph)

patch_file = "tmp/patches.json"

f = open(patch_file, "r")
line = f.readline()
f.close()
patches = None
print('line', line)
if line:
    patches = json.loads(line)
print('patches', patches)
if patches is None:
    patches = build_patches(call_edge_dict, change_edge_dict, services)

    f = open(patch_file, "w")
    f.write(json.dumps(patches))
    f.close()
print('patches', patches)

systems = []

# CALC MATRIX
def get_sub_patches(service_list):
    print(patch)

    g = build_graph(call_edge_dict, change_edge_dict, service_list)
    distances = {}
    matrix_file = 'tmp/matrix.txt'
    file = open(matrix_file, "w")
    file.write(','.join(service_list) + os.linesep)
    c = 0
    for service in service_list:
        row = get_distances(g, service, service_list)
        g.reset()
        line = service + ',' + (','.join(map(str, row.values()))) + os.linesep
        print(line)
        c += 1
        print(c, '/', len(service_list))
        file.write(line)
        distances[service] = row
    file.close()


for patch in patches:
    if len(patch) > 50:
        get_sub_patches(patch)
    else:
        systems.append(patch)
