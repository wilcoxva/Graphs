from room import Room
from player import Player
from world import World

import random
from ast import literal_eval

###############################
class Queue():
    def __init__(self):
        self.queue = []
    def enqueue(self, value):
        self.queue.append(value)
    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None
    def size(self):
        return len(self.queue)

class Stack():
    def __init__(self):
        self.stack = []
    def push(self, value):
        self.stack.append(value)
    def pop(self):
        if self.size() > 0:
            return self.stack.pop()
        else:
            return None
    def size(self):
        return len(self.stack)
###################################

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
# map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = []

####################################################
# Decided to use DFS instead of DFT because it makes more sense with a path
def dfs(graph, starting_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        stack = Stack()
        visited_vertices = set()
        stack.push({ 
            'current_vertex': starting_vertex,
            'path': [starting_vertex]        
        })
        while stack.size() > 0:
            current_obj = stack.pop()
            current_path = current_obj['path']
            current_vertex = current_obj['current_vertex']
            if current_vertex not in visited_vertices:
                visited_vertices.add(current_vertex)
                for neighbor_vertex in self.get_neighbors(current_vertex):
                    new_path = list(current_path)
                    new_path.append(neighbor_vertex)
                    stack.push({
                        'current_vertex': neighbor_vertex,
                        'path': new_path
                    })
        return None

def bfs(graph, starting_vertex):
    queue = Queue()
    visited_vertices = set()
    queue.enqueue({ 
        'current_vertex': starting_vertex,
        'path': [starting_vertex]        
    })
    while queue.size() > 0:
        current_obj = queue.dequeue()
        current_path = current_obj['path']
        current_vertex = current_obj['current_vertex']
        if current_vertex not in visited_vertices:
            visited_vertices.add(current_vertex)
            for neighbor_vertex in self.get_neighbors(current_vertex):
                new_path = list(current_path)
                new_path.append(neighbor_vertex)
                queue.enqueue({
                    'current_vertex': neighbor_vertex,
                    'path': new_path
                })
    return None

def get_neighbors:
    pass

def find_room(graph, current_room):
    pass

def create_path:
    pass
########################################################

# TRAVERSAL TEST
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")



#######
# UNCOMMENT TO WALK AROUND
#######
player.current_room.print_room_description(player)
while True:
    cmds = input("-> ").lower().split(" ")
    if cmds[0] in ["n", "s", "e", "w"]:
        player.travel(cmds[0], True)
    elif cmds[0] == "q":
        break
    else:
        print("I did not understand that command.")
