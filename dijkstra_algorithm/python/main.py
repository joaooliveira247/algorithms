def find_lowest_cost_node(costs: dict, processed: list) -> dict:
    lowest_cost = float("inf")
    lowest_cost_node = None
    # Go through each node.
    for node in costs:
        cost = costs[node]
        # If it's the lowest cost so far and hasn't been processed yet...
        if cost < lowest_cost and node not in processed:
            # ... set it as the new lowest-cost node.
            lowest_cost = cost
            lowest_cost_node = node
    return lowest_cost_node


def main() -> None:
    # The graph start
    graph = {}
    # The node start
    graph["start"] = {}
    graph["start"]["a"] = 6
    graph["start"]["b"] = 2

    # The node A
    graph["a"] = {}
    graph["a"]["fin"] = 1

    # The node B
    graph["b"] = {}
    graph["b"]["fin"] = 5
    # That code represents the connection between A and B
    graph["b"]["a"] = 3

    # The end node can't has any connection
    graph["fin"] = {}

    # the costs table
    infinity = float("inf")
    costs = {}
    costs["a"] = 6
    costs["b"] = 2
    costs["fin"] = infinity

    # the parents table
    parents = {}
    parents["a"] = "start"
    parents["b"] = "start"
    parents["fin"] = None

    processed = []

    # Find the lowest-cost node that you haven't processed yet.
    node = find_lowest_cost_node(costs, processed)
    # If you've processed all the nodes, this while loop is done.
    while node is not None:
        cost = costs[node]
        # Go through all the neighbors of this node.
        neighbors = graph[node]
        for n in neighbors.keys():
            new_cost = cost + neighbors[n]
            # If it's cheaper to get to this neighbor by going through this node...
            if costs[n] > new_cost:
                # ... update the cost for this node.
                costs[n] = new_cost
                # This node becomes the new parent for this neighbor.
                parents[n] = node
        # Mark the node as processed.
        processed.append(node)
        # Find the next node to process, and loop.
        node = find_lowest_cost_node(costs, processed)

    print("Cost from the start to each node:")
    print(costs)


if __name__ == "__main__":
    main()
