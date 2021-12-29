
def increment_node(n, node):
    # Builds the lexicographically next node after 'node' or signals that 'node'
    # is the last node via 'last_node' = True.
    last_node = True
    all_checked = False
    i = n - 1
    while last_node == True and all_checked == False:
        if node[i] < n - 1:
            last_node = False
            node[i] = node[i] + 1
            for j in range(n - 1, i, -1):
                node[j] = 0
        else:
            i = i - 1
            if i == -1:
                all_checked = True
    return last_node, node

def test_permutation(n, node):
    # Checks that the list 'node' is in the form of a permutation, i.e., all elements
    # are distinct and are in {0, 1, ...., n}.
    permutation = True
    i = 0
    while i < n - 1 and permutation == True:
        j = i + 1
        while j < n and permutation == True:
            if node[i] == node[j]:
                permutation = False
            j = j + 1
        i = i + 1
    return permutation

def alltoall_traffic(n):
    # Generates a list of source nodes 'list_of_sources' and a list of destination nodes
    # 'list_of_destinations', both lists of length (n!)^2, such that every pair of nodes
    # appears as a pair in 'list_of_sources[i]' x 'list_of_destinations[i]' (including
    # pairs of the form [node, node]).
    list_of_nodes = []
    node = []
    for i in range(0, n):
        node.append(i)
    list_of_nodes.append(node[:])
    last_node = False
    while last_node == False:
        last_node, node = increment_node(n, node)
        if last_node == False:
            if test_permutation(n, node):
                list_of_nodes.append(node[:])
    list_of_sources = []
    list_of_destinations = []
    for source in list_of_nodes:
        for target in list_of_nodes:
            list_of_sources.append(source[:])
            list_of_destinations.append(target[:])
    return list_of_sources, list_of_destinations

# here is a little test run for you to see what happens

# n = 3
# list_of_sources, list_of_destinations = alltoall_traffic(n)
# length = len(list_of_sources)
# for i in range (0, length):
#     print(list_of_sources[i], list_of_destinations[i])



