from util import Stack, Queue  # These may come in handy

def get_neighbors(vertex_id, ancestors):
    result = []
    for tup in ancestors:
        print(tup)
        if tup[1] == vertex_id:
            result.append(tup[0])
    return result

def earliest_ancestor(ancestors, starting_node):
    # Create an empty queue and enqueue the PATH TO starting_vertex
        no_parents = [10, 2, 4, 11]
        if starting_node in no_parents:
            return -1
        ancestor_path = []
        queue = Queue()
        queue.enqueue({
            'current_vertex': starting_node,
            'path': [starting_node]
        })
        # Create an empty set to track visited verticies
        visited = set()
        # while the queue is not empty:
        while queue.size() > 0: 
            # get current vertex PATH (dequeue from queue)
            obj = queue.dequeue()
            path = obj['path']
            vertex = obj['current_vertex']
            # set the current vertex to the LAST element of the PATH
            current = path[-1]
            # Check if the current vertex has not been visited:
            if current not in visited:
                # CHECK IF THE CURRENT VERTEX IS DESTINATION
                if get_neighbors(current, ancestors) == []:
                # IF IT IS, STOP AND RETURN
                    ancestor_path.append(path)
                # Mark the current vertex as visited
                visited.add(current)
                    
                for neighbor_vertex in get_neighbors(current, ancestors):
                    new_path = list(path)
                    new_path.append(neighbor_vertex)

                    queue.enqueue({
                        'current_vertex': neighbor_vertex,
                        'path': new_path
                    })
        print(ancestor_path)
        earliest = ancestor_path[0]
        for path in ancestor_path:
            if len(path) > len(earliest):
                earliest = path
            elif len(path) == len(earliest) and path[-1] < earliest[-1]:
                earliest = path
        return earliest[-1]

test_ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]
print(earliest_ancestor(test_ancestors, 6))