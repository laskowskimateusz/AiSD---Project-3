from Graph import Graph, Edge, Vertex
from typing import Any, Dict, List, Tuple
import math


def print_all_weighted_shortest_paths(d: Dict[Any, List[Edge]], start: Any):
    for key in d.keys():
        print(f'{start} - {key}: ', end='')
        for edge in d[key]:
            print(f'{edge.source} - {edge.destination}, ', end='')
        print()


def all_weighted_shortest_paths(g: Graph, start: Any) -> Dict[Any, List[Edge]]:
    list_of_vertex = list(g.adjacencies.keys())
    list_of_vertex.remove(start)
    vertices: Dict[Vertex, List[Vertex]] = {}
    edges: Dict[Vertex, List[Edge]] = {}
    for vertex in list_of_vertex:
        vertices[vertex] = dijkstra(g, start, vertex)
        vertices[vertex].insert(0, vertex)
    for vertex in vertices.keys():
        edges[vertex] = []
    for vertex in vertices.keys():
        temp: List = vertices[vertex]
        for i in range(len(temp) - 1):
            lowest: Edge = None
            for edge in g.adjacencies[temp[i]]:
                if lowest is None:
                    if edge.destination == temp[i + 1]:
                        lowest = edge
                    else:
                        continue
                else:
                    if edge.weight < lowest.weight and edge.destination == temp[i + 1]:
                        lowest = edge
            edges[vertex].append(lowest)
    return edges


def dijkstra(g: Graph, start: Vertex, end: Vertex) -> List[Vertex]:
    costs: Dict[Vertex, int] = dict()
    parents: Dict[Vertex, Vertex] = dict()
    visited: list[Vertex] = []
    costs[end] = math.inf

    for edge in g.adjacencies[start]:
        costs[edge.destination] = edge.weight
    for vertex in list(costs.keys()):
        if costs[vertex] is math.inf:
            parents[vertex] = None
        else:
            parents[vertex] = start
    visited.append(start)

    v: Tuple = cheapest_NewVertex(costs, visited)
    while v[0]:
        for edge in g.adjacencies[v[0]]:
            nc: int = v[1] + edge.weight
            if edge.destination in costs.keys():
                if costs[edge.destination] > nc:
                    costs[edge.destination] = nc
                    parents[edge.destination] = v[0]
            else:
                costs[edge.destination] = nc
                parents[edge.destination] = v[0]
        visited.append(v[0])
        v = cheapest_NewVertex(costs, visited)

    parent: Vertex = parents[end]
    path: List = []
    while parent is not start:
        path.append(parent)
        parent = parents[parent]
    path.append(start)
    return path


def cheapest_NewVertex(costs: Dict[Vertex, int], visited: List[Vertex]) -> Tuple[Vertex, int]:
    result: Vertex = None
    for vertex in costs.keys():
        if vertex not in visited:
            result = vertex

    if result is None:
        return None, None

    lc: int = costs[result]

    for v in costs.keys():
        if v not in visited:
            if costs[v] < lc:
                lc = costs[v]
                result = v
    return result, lc


graph1: Graph = Graph()
graph2: Graph = Graph()
graph3: Graph = Graph()

graph1.create_vertex("A")
graph1.create_vertex("B")
graph1.create_vertex("C")
graph1.create_vertex("D")
graph1.create_vertex("E")
graph1.create_vertex("F")
graph1.create_vertex("G")
graph1.create_vertex("H")
graph1.create_vertex("I")

graph2.create_vertex("A")
graph2.create_vertex("B")
graph2.create_vertex("C")
graph2.create_vertex("D")
graph2.create_vertex("E")
graph2.create_vertex("F")
graph2.create_vertex("G")

graph3.create_vertex("A")
graph3.create_vertex("B")
graph3.create_vertex("C")
graph3.create_vertex("D")
graph3.create_vertex("E")
graph3.create_vertex("F")


graph1.add_undirected_edge(graph1.getVertex("A"), graph1.getVertex("B"), 2)
graph1.add_undirected_edge(graph1.getVertex("B"), graph1.getVertex("C"), 6)
graph1.add_undirected_edge(graph1.getVertex("A"), graph1.getVertex("D"), 3)
graph1.add_undirected_edge(graph1.getVertex("A"), graph1.getVertex("E"), 4)
graph1.add_undirected_edge(graph1.getVertex("C"), graph1.getVertex("E"), 7)
graph1.add_undirected_edge(graph1.getVertex("C"), graph1.getVertex("F"), 15)
graph1.add_undirected_edge(graph1.getVertex("F"), graph1.getVertex("I"), 3)
graph1.add_undirected_edge(graph1.getVertex("I"), graph1.getVertex("H"), 11)
graph1.add_undirected_edge(graph1.getVertex("H"), graph1.getVertex("E"), 20)
graph1.add_undirected_edge(graph1.getVertex("G"), graph1.getVertex("H"), 4)
graph1.add_undirected_edge(graph1.getVertex("G"), graph1.getVertex("E"), 10)
graph1.add_undirected_edge(graph1.getVertex("G"), graph1.getVertex("D"), 5)
graph1.add_undirected_edge(graph1.getVertex("E"), graph1.getVertex("I"), 2)

graph2.add_undirected_edge(graph2.getVertex("A"), graph2.getVertex("D"), 11)
graph2.add_undirected_edge(graph2.getVertex("D"), graph2.getVertex("B"), 8)
graph2.add_undirected_edge(graph2.getVertex("B"), graph2.getVertex("A"), 4)
graph2.add_undirected_edge(graph2.getVertex("C"), graph2.getVertex("B"), 2)
graph2.add_undirected_edge(graph2.getVertex("D"), graph2.getVertex("C"), 5)
graph2.add_undirected_edge(graph2.getVertex("A"), graph2.getVertex("E"), 9)
graph2.add_undirected_edge(graph2.getVertex("F"), graph2.getVertex("G"), 7)
graph2.add_undirected_edge(graph2.getVertex("G"), graph2.getVertex("E"), 3)

graph3.add_undirected_edge(graph3.getVertex("A"), graph3.getVertex("F"), 5)
graph3.add_undirected_edge(graph3.getVertex("C"), graph3.getVertex("F"), 2)
graph3.add_undirected_edge(graph3.getVertex("F"), graph3.getVertex("B"), 7)
graph3.add_undirected_edge(graph3.getVertex("C"), graph3.getVertex("D"), 8)
graph3.add_undirected_edge(graph3.getVertex("D"), graph3.getVertex("F"), 3)
graph3.add_undirected_edge(graph3.getVertex("E"), graph3.getVertex("F"), 4)
graph3.add_undirected_edge(graph3.getVertex("A"), graph3.getVertex("E"), 11)

print("Przykład 1: ")
g1 = all_weighted_shortest_paths(graph1, graph1.getVertex("C"))
print_all_weighted_shortest_paths(g1, graph1.getVertex("C"))

print("Przyklad 2: ")

g2 = all_weighted_shortest_paths(graph2, graph2.getVertex("G"))
print_all_weighted_shortest_paths(g2, graph2.getVertex("G"))

print("Przykład 3: ")

g3 = all_weighted_shortest_paths(graph3, graph3.getVertex("D"))
print_all_weighted_shortest_paths(g3, graph3.getVertex("D"))

graph1.show()
graph2.show()
graph3.show()
