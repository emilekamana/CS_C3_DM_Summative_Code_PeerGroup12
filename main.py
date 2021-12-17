# A python program to randomly generate simple undirected graphs with 10 vertices.
# The program again should determine if the graph is connected and if it contains an Euler circuit.
# If the graph contains an Euler circuit then your program should output the Euler circuit.

import random
from collections import deque

import networkx as nx
import matplotlib.pyplot as plt


# A function to display the randomly generated graph
def generate_graph(graph):
   # No. of vertices

   print(f"Edges: {graph.edges()}")
   print(f"Vertices: {graph.nodes()}")

   pos = nx.spring_layout(graph)
   nx.draw_networkx_nodes(graph, pos)
   nx.draw_networkx_edges(graph, pos)
   nx.draw_networkx_labels(graph, pos)

   plt.show()


# Depth First Search function to avoid visiting a node more than once
def dfs(graph, init):
   seen = set()
   next_level = {init: {}}
   while next_level:
       this_level = next_level
       next_level = set()
       for v in this_level:
           if v not in seen:
               seen.add(v)
               next_level.update(graph[v])
   return seen


# A function to check if all degrees of a graph are even
def all_degrees_even(graph):
   return all(d % 2 == 0 for v, d in graph.degree())


# A function to check if a graph is connected
def is_connected(graph):
   return len(set(dfs(graph, random.choice(list(G.nodes))))) == len(graph.nodes)


# A function to check if a graph is Eulerian
def is_eulerian(graph):
   return is_connected(graph) and all_degrees_even(graph)


# A function to generate the path of an Euler circuit
def circuit(graph):
   if is_eulerian(graph):
       path = deque()
       H = graph.copy()
       curr_node = random.choice(list(graph.nodes))
       while H.number_of_edges() > 0:
           if H.degree(curr_node) > 0:
               next_node = next(H.neighbors(curr_node))
               path.append(next_node)
               H.remove_edge(curr_node, next_node)
               curr_node = next_node
           else:
               curr_node = path.popleft()
               path.append(curr_node)

       path.append(path[0])
       return list(path)


G = nx.generators.erdos_renyi_graph(10, 0.5)
# # Using while loop to iterate through is_eulerian function until the random graph is an euler circuit
# iterations = 1
# while not is_eulerian(G):
#     iterations += 1
#     G = nx.generators.erdos_renyi_graph(10, 0.5)


print(f"Is the graph connected? {is_connected(G)}")
print(f"Is the graph an Euler circuit? {is_eulerian(G)}")
print(f"The Euler circuit path: {circuit(G)}")
# print(f"iterations:{iterations}")
print(f"Degree of each node: {G.degree}")
generate_graph(G)

