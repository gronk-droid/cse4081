"""Macro for infinity floating point representation."""
INF = float("inf")


class Graph:
    """
    Graph implementation for Dinic's algorithm.

    Dinic's algorithm looks to accomplish the problem of maximum flow as such:
    Guide paths from the source node to the sink using a level graph.
    A level graph is made from BFS. All edges that go from L to L + 1 are good,
    and any that do not are removed from consideration.
    The steps to the algorithm include:
    1. Construct level graph by using BFS from source to label all levels of
        the flow graph.
    2. If the sink was never reached, stop and return the max flow.
    3. Use valid edges in the level graph to find multiple DFS's from source to
    sink until blocking flow is reached, and then sum over the bottleneck
    values to calculate maximum flow.
    These are repeated until a maximum flow is found for the graph.

    ##### Attributes
    level
        array of the level of each node in the graph
    capacity
        array of the capacity of each
    queue
        a queue of length n
    adj
        adjacency matrix of the graph
    """

    def __init__(self, size):
        """
        Initialize graph object.

        ##### Arguments
        size
            the size of the graph
        """
        self.level = [0] * size
        self.ptr = [0] * size
        self.queue = [0] * size
        self.adj = [[] for _ in range(size)]

    def add_edge(self, start, end, cap, res_cap=0):
        """
        Add an edge between two nodes with a capacity.

        ##### Arguments
        start
            the node the edge starts from
        end
            the ending node of the edge
        cap
            capacity of the edge
        res_cap
            used capacity of the edge (default of 0)
        """
        self.adj[start].append([end, len(self.adj[end]), cap, 0])
        self.adj[end].append([start, len(self.adj[start]) - 1, res_cap, 0])

    def dfs(self, vertex, sink, flow):
        """
        Depth first search of the flow graph.

        ##### Arguments
        vertex
            starting node of the dfs
        sink
            end node of the dfs
        flow
            the flow through the resultant path
        """
        if vertex == sink or not flow:
            return flow  # return if the vertex is the sink or if the flow is 0

        for i in range(self.ptr[vertex], len(self.adj[vertex])):
            edge = self.adj[vertex][i]
            if self.level[edge[0]] == self.level[vertex] + 1:
                path = self.dfs(edge[0], sink, min(flow, edge[2] - edge[3]))
                if path:
                    self.adj[vertex][i][3] += path
                    self.adj[edge[0]][edge[1]][3] -= path
                    return path
            self.ptr[vertex] = self.ptr[vertex] + 1
        return 0

    def max_flow(self, source, sink):
        """
        Find the maximum flow of the graph. Includes a BFS.

        ##### Arguments
        source
            the starting node to find the flow from
        sink
            the ending node to find the flow to
        """
        flow = 0
        self.queue[0] = source
        for l in range(31):
            while True:
                self.level = [0] * len(self.queue)  # set lvl to size of queue
                self.ptr = [0] * len(self.queue)  # set ptr to size of queue
                initial = 0
                end = 1
                self.level[source] = 1
                while initial < end and not self.level[sink]:  # basically BFS
                    vertex = self.queue[initial]
                    initial += 1
                    for edges in self.adj[vertex]:
                        if not self.level[edges[0]] and (edges[2] - edges[3]) >> (30 - l):
                            self.queue[end] = edges[0]
                            end += 1
                            self.level[edges[0]] = self.level[vertex] + 1

                path_flow = self.dfs(source, sink, INF)
                while path_flow:  # runs until flow is 0
                    flow += path_flow
                    path_flow = self.dfs(source, sink, INF)

                if not self.level[sink]:
                    break

        return flow


def main():
    """Driver function."""
    # print(not float("inf"))
    # print(not float(0))
    example = Graph(6)
    source = 0
    sink = 5

    example.add_edge(0, 1, 16)
    example.add_edge(0, 2, 13)
    example.add_edge(1, 2, 10)
    example.add_edge(1, 3, 12)
    example.add_edge(2, 1, 4)
    example.add_edge(2, 4, 14)
    example.add_edge(3, 2, 9)
    example.add_edge(3, 5, 20)
    example.add_edge(4, 3, 7)
    example.add_edge(4, 5, 4)

    print(f'Maximum Flow: {example.max_flow(source, sink)}')


main()
