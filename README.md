# Discrete Maths Summative Assignment
#### Graph and Euler circuits, December 17 2021
#### By Group 12
* Ghea Sandrine Mawen
* Natley Nyamukondiwa
* Marie Ishimwe
* Maikem Victorine
* Emile Kamana
## Description
In this assignment, we were tasked to write a python program that randomly generates simple undirected graphs with 10 vertices.The program again should determine if the graph is connected and if it contains an Euler circuit. If the graph contains an Euler circuit then your program should output the Euler circuit.
## Setup/Installation Requirements
* Internet connection
* access to a browser
* clone {https://github.com/emilekamana/CS_C3_DM_Summative_Code_PeerGroup12}
* install libraries: random, collections, networkx, matplotlib
## Getting Started With The App
After installing:
* Run the main.py file

For quick generation of a euler circuit:
* Open main.py
* Scroll down
* Uncomment this

```python
# iterations = 1
# while not is_eulerian(G):
#     iterations += 1
#     G = nx.generators.erdos_renyi_graph(10, 0.5)
```
* Run main.py