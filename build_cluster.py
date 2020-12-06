from collections import defaultdict

import matplotlib.pyplot as plt
from scipy.cluster import hierarchy
from scipy.cluster.hierarchy import weighted, fcluster, linkage

from read_file import read_file


#READ INPUT

matrix_file = 'tmp/matrix.txt'
matrix = read_file(matrix_file, lambda x: x)
services = matrix.pop(0)
m = []
for row in matrix:
    row.pop(0)
    row = list(map(float, row))
    m.append(row)
length = len(m)

y = []
for i in range(1, length):
    for j in range(i + 1, length):
        y.append(m[i][j])

# LINKAGE

# Z = weighted(y)
Z = linkage(y, 'ward')
# Z = linkage(y, 'complete')

#FIGURE

plt.figure()
hierarchy.set_link_color_palette(
    [
        '#AF0000',
        '#00AF00',
        '#0000AF',
        '#AF0000',
        '#00AF00',
        '#0000AF',
        '#AF0000',
        '#00AF00',
        '#0000AF',
        '#AF0000',
        '#00AF00',
        '#0000AF',
        '#AF0000',
        '#00AF00',
        '#0000AF',
        '#AF0000',
        '#00AF00',
        '#0000AF',

    ])
dn = hierarchy.dendrogram(
    Z,
    orientation='left',
    color_threshold=22,
    leaf_label_func=lambda i: str(id) if i >= len(services) else services[i],
)
plt.show()

# CLUSTER

t = 22
clusters = fcluster(Z, t, criterion='distance')
tuples = list(zip(services, clusters))
tuples.sort(key=lambda x: x[1])
print(tuples)
cluster_map = defaultdict(lambda: [])
for tuple in tuples:
    cluster_map[tuple[1]].append(tuple[0])

print(t)
print(list(cluster_map.values()))
print(list(map(len, cluster_map.values())))
print(list(map(len, cluster_map.values())))
print(len(cluster_map.values()))
print()
