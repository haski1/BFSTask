import sys


class Graph:
    def __init__(self, size, adjacency_list):
        self.nodes = set(range(1, size + 1))
        self.adjacency_list = dict()
        for i in range(1, size + 1):
            self.adjacency_list[i] = adjacency_list[i - 1]
        self.components = []

    def BFS(self, queue, visited):
        node = queue.pop(0)
        visited.add(node)
        not_visited = self.adjacency_list[node] - visited
        for node in not_visited:
            queue.append(node)
        if queue:
            self.BFS(queue, visited)
        return visited

    def get_components(self):
        visited = set()
        not_visited = self.nodes - visited
        while not_visited:
            component = self.BFS([not_visited.pop()], set())
            self.components.append(component)
            visited = visited | component
            not_visited = self.nodes - visited
        return self.components


size = 0
adjacency_list = []

with open(sys.argv[1], mode='r', encoding='UTF-8') as file:
    size = int(file.readline())
    for i in range(size):
        numbers = set(map(int, file.readline().split(' ')[0:-1]))
        adjacency_list.append(numbers)

graph = Graph(size, adjacency_list)
components = graph.get_components()

with open(sys.argv[2], mode='w', encoding='UTF-8') as file:
    for component in components:
        line = ""
        for node in component:
            line += str(node) + ' '
        line += '0\n'
        file.write(line)
