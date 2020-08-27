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
# He said to start out with DFT and end up using BFS:
def dft(self, starting_vertex):
    stack = Stack()
    stack.push(starting_vertex)
    visited = set()
    while stack.size() > 0:
        current = stack.pop()
        if current not in visited:
            print(current)
            visited.add(current)
            for neighbor in self.get_neighbors(current):
                stack.push(neighbor)
# I was thinking of using world.starting_room as starting_vertex but that doesn't seem to work
# I was thinking of replacing visited with traversal_path but that didn't work 
def bfs(self, starting_vertex, destination_vertex):
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
            if current_vertex == destination_vertex:
                return current_path
            visited_vertices.add(current_vertex)
            for neighbor_vertex in self.get_neighbors(current_vertex):
                new_path = list(current_path)
                new_path.append(neighbor_vertex)
                queue.enqueue({
                    'current_vertex': neighbor_vertex,
                    'path': new_path
                })
    return None
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
