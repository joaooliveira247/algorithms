# 🔵📈 Dijkstra's algorithm

- It's used to calculate the shortest path for a weighted graph.

- Graphs can't be negative weight, to negative weight use [Bellman-Ford algorithm](https://en.wikipedia.org/wiki/Bellman%E2%80%93Ford_algorithm).

- Dijkstra's algorithm has four steps:

  1. Find the cheapest node, This is the node you can get to in the least amount of "time".

  2. Check whether there's a cheaper path to the neighbors of this node. If so, update their costs

  3. Repeat until you've done this for every node in the graph

  4. Calculate the final path.

- Bidirectional nodes can increase your weight, in this case we do a circular path.

- Path is defined by sections.

- The table parent method can improve your solution.

  `ex:`

  ![book_graph](https://i.imgur.com/mGZzXU8.png)

  Using the piano case as example.

  | Parent |  Node  | Cost |
  | :----: | :----: | :--: |
  |  Book  |   LP   |  5   |
  |  Book  | Poster |  0   |
  |   LP   | Guitar |  20  |
  |   LP   | Drums  |  25  |
  | Guitar | Piano  |  40  |

  | Parent |  Node  | Cost |
  | :----: | :----: | :--: |
  |  Book  |   LP   |  5   |
  |  Book  | Poster |  0   |
  |   LP   | Guitar |  20  |
  |   LP   | Drums  |  25  |
  | Drums  | Piano  |  35  |

  Final trade

  `Book -> LP -> Drums -> Piano`

`Code examples:`

`1º example`

![graph_diagram](https://i.imgur.com/vFgewTk.png)

[<img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg" width="20px" />
Python](./python/main.py)