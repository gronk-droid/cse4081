INF = float("inf")

class Graph:
    def __init__(self, n):
        self.lvl = [0] * n
        self.ptr = [0] * n
        self.q = [0] * n
        self.adj = [[] for _ in range(n)]

    def add_edge(self, start, end, weight, residual_capacity=0):
        self.adj[start].append([end, len(self.adj[end]), weight, 0])
        self.adj[end].append([start, len(self.adj[start]) - 1, residual_capacity, 0])

    def dfs(self, vertex, sink, flow):
        if vertex == sink or not flow:
            return flow

        for i in range(self.ptr[vertex], len(self.adj[vertex])):
            e = self.adj[vertex][i]
            if self.lvl[e[0]] == self.lvl[vertex] + 1:
                p = self.dfs(e[0], sink, min(flow, e[2] - e[3]))
                if p:
                    self.adj[vertex][i][3] += p
                    self.adj[e[0]][e[1]][3] -= p
                    return p
            self.ptr[vertex] = self.ptr[vertex] + 1
        return 0

    def max_flow(self, source, sink):
        flow, self.q[0] = 0, source
        for l in range(31):
            while True:
                self.lvl, self.ptr = [0] * len(self.q), [0] * len(self.q)
                qi, qe, self.lvl[source] = 0, 1, 1
                while qi < qe and not self.lvl[sink]:
                    v = self.q[qi]
                    qi += 1
                    for e in self.adj[v]:
                        if not self.lvl[e[0]] and (e[2] - e[3]) >> (30 - l):
                            self.q[qe] = e[0]
                            qe += 1
                            self.lvl[e[0]] = self.lvl[v] + 1

                p = self.dfs(source, sink, INF)
                while p:
                    flow += p
                    p = self.dfs(source, sink, INF)

                if not self.lvl[sink]:
                    break

        return flow


def main():
    g = Graph(6)
    source = 0
    sink = 5

    g.add_edge(0, 1, 16)
    g.add_edge(0, 2, 13)
    g.add_edge(1, 2, 10)
    g.add_edge(1, 3, 12)
    g.add_edge(2, 1, 4)
    g.add_edge(2, 4, 14)
    g.add_edge(3, 2, 9)
    g.add_edge(3, 5, 20)
    g.add_edge(4, 3, 7)
    g.add_edge(4, 5, 4)

    print(f'Maximum Flow: {g.max_flow(source, sink)}')


main()
