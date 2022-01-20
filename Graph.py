from MyQueue import Queue
from enum import Enum
from typing import Any, Optional, Dict, List, Callable
import networkx as nx
import matplotlib.pyplot as plt


def visit(vertex: Any) -> None:
    print(f'v{vertex.index}')


class EdgeType(Enum):
    directed = 1
    undirected = 2


class Vertex:
    data: Any
    index: int

    base: int = 0

    def __init__(self, data: Any) -> None:
        self.data = data
        self.index = Vertex.base
        Vertex.base += 1

    def __ne__(self, other: 'Vertex') -> bool:
        return False if(self.index != other.index) else True

    def __str__(self):
        return self.data


class Edge:
    source: Vertex
    destination: Vertex
    weight: Optional[float]

    def __init__(self, source: Vertex, destination: Vertex, weight: Optional[float] = None) -> None:
        self.source = source
        self.destination = destination
        self.weight = weight


class Graph:
    adjacencies: Dict[Vertex, List[Edge]]

    def getVertex(self, value: Any) -> Vertex:
        for vertex in self.adjacencies.keys():
            if vertex.data == value:
                return vertex

    def __init__(self):
        self.adjacencies = {}

    def create_vertex(self, data: Any) -> None:
        self.adjacencies[Vertex(data)] = []

    def add_directed_edge(self, source: Vertex, destination: Vertex, weight: Optional[float] = None) -> None:
        self.add(EdgeType(1), source, destination, weight)

    def add_undirected_edge(self, source: Vertex, destination: Vertex, weight: Optional[float] = None) -> None:
        self.add(EdgeType(2), source, destination, weight)

    def add(self, edge: EdgeType, source: Vertex, destination: Vertex, weight: Optional[float] = None) -> None:
        if edge == 1:
            self.adjacencies[source].append(Edge(source, destination, weight))
        else:
            self.adjacencies[source].append(Edge(source, destination, weight))
            self.adjacencies[destination].append(Edge(destination, source, weight))

    def traverse_breadth_first(self, visit: Callable[[Any], None]) -> None:
        queue = Queue()
        queue.enqueue(next(iter(self.adjacencies)))
        visited = Queue()
        visited.enqueue(next(iter(self.adjacencies)))
        while len(queue):
            current: Vertex = queue.dequeue()
            visit(current)
            for edge in self.adjacencies[current]:
                destination = edge.destination
                condition: bool = True
                for element in visited:
                    if element.index == destination.index:
                        condition = False
                if condition:
                    visited.enqueue(destination)
                    queue.enqueue(destination)

    def traverse_depth_first(self, visit: Callable[[Any], None]) -> None:
        self.dfs(next(iter(self.adjacencies)), list(), visit)

    def dfs(self, v: Vertex, visited: List[Vertex], visit: Callable[[Any], None]) -> None:
        visit(v)
        visited.append(v)
        for neighbour in self.adjacencies[v]:
            if neighbour.destination not in visited:
                self.dfs(neighbour.destination, visited, visit)

    def show(self):
        G = nx.Graph()
        G.add_weighted_edges_from(self.get())
        labels = nx.get_edge_attributes(G, 'weight')
        pos = nx.circular_layout(G)
        nx.draw_networkx_nodes(G, pos, node_size=500)
        nx.draw_networkx_edges(G, pos, edgelist=G.edges())
        nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
        nx.draw_networkx_labels(G, pos)
        plt.show()

    def get(self):
        result = list()
        A = list(self.adjacencies.values())
        for i in A:
            for edge in i:
                temp = list()
                temp.append(edge.source.data)
                temp.append(edge.destination.data)
                temp.append(edge.weight)
                result.append(temp)
        return result
