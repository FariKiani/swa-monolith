# SWA - Compute Architcture

## Run
`python3.8 main.py` then `python3.8 build_cluster.py`

main takes some hours

## Results
`system.json` `system.png`

## Prepare
save as csv

## Procedure

- parse csv files

- build graph
    - services are nodes
    - edges
        - Calls
        - changes 
    - edge weights from file
        - used ```1/log(calls) + 1/log(changes)```
        - [not implemented] better ```1/(log(calls) + log(changes))```
            - noticed too late: no time to recompute
    - [not implemented] ignore cyclic dependencies (no time)
        - constraint: cyclic deps must be in one system same system

- create connected subgraphs
    - union–find [algorithm]
    - 84 small subgraphs (< 20 nodes)
        - could maybe merge some
    - 1 huge graph (~ 2900 nodes)

- calc distance matrix (for huge graph)
    - 2900 x 2900
    - calc with Dikstra [algorithm]
    - ~10h
    
- build clusters
    - ``scipy.cluster.hierarchy.linkage``
        - param: method: ``ward``
    -  ``scipy.cluster.hierarchy.fcluster``
        - param: threshold: ``22``
    - 27 cluster
    
- total - 111 systems
    - 84 small (maybe merge some? no semantic)
    - 27 in huge (divide big systems with recursion)
    

## links        
### clustering
- https://docs.scipy.org/doc/scipy/reference/cluster.hierarchy.html
- https://docs.scipy.org/doc/scipy/reference/generated/scipy.cluster.hierarchy.linkage.html#scipy.cluster.hierarchy.linkage
- https://en.wikipedia.org/wiki/Ward%27s_method
- https://docs.scipy.org/doc/scipy/reference/generated/scipy.cluster.hierarchy.fcluster.html


### graph
- https://www.bogotobogo.com/python/python_Dijkstras_Shortest_Path_Algorithm.php
- https://en.wikipedia.org/wiki/Connectivity_(graph_theory)
- https://en.wikipedia.org/wiki/Disjoint-set_data_structure
