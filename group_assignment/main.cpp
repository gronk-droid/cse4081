#include <bits/stdc++.h>

using namespace std;

#define ve vector<Edge>

struct Edge {
   int arrow;
   int weight;
   int reverse;
};

class Graph {
private:
   int size;
   int *level;
   ve *edges;
public:

   Graph(int n) {
      size = n;
      level = new int[n];
      edges = new ve[n];
   }

   // Needs modification if back edge can have weight
   Edge *add_edge(int from, int to, int weight) {
      Edge e1{to, weight, (int) this->edges[to].size()};
      Edge e2{from, 0, (int) this->edges[from].size()};
      this->edges[from].push_back(e1);
      this->edges[to].push_back(e2);
      return &this->edges[from][(int) this->edges[from].size() - 1];
   }

   bool run_bfs(int s, int t) {
      for (int i = 0; i < this->size; i++)
         this->level[i] = -1;
      this->level[s] = 0;
      queue<int> q;
      q.push(s);
      while (!q.empty()) {
         int v = q.front();
         q.pop();
         if (v == t)
            return true;
         for (Edge e : edges[v]) {
            if (this->level[e.arrow] == -1 && e.weight > 0) {
               this->level[e.arrow] = this->level[v] + 1;
               q.push(e.arrow);
            }
         }
      }
      return false;
   }
   int run_flow(int s, int t, int flow, int start[]) {
      if (s == t)
         return flow;
      for (; start[s] < (int) this->edges[s].size(); start[s]++) {
         Edge &e = this->edges[s][start[s]];
         if (level[e.arrow] == level[s] + 1 && e.weight > 0) {
            int new_flow = min(flow, e.weight);
            new_flow = run_flow(e.arrow, t, new_flow, start);
            if (new_flow > 0) {
               e.weight -= new_flow;
               edges[e.arrow][e.reverse].weight += new_flow;
               return new_flow;
            }
         }
      }
      return 0;
   }
   int get_max_flow(int s, int t) {
      if (s == t)
         return -1;

      int total = 0;
      while (run_bfs(s, t)) {
         int start[this->size];
         for (int i = 0; i < this->size; i++)
            start[i] = 0;
         while (int flow = run_flow(s, t, INT_MAX, start))
            total += flow;
      }
      return total;
   }
};

int main() {
    Graph g(6);
    g.add_edge(0, 1, 16 );
    g.add_edge(0, 2, 13 );
    g.add_edge(1, 2, 10 );
    g.add_edge(1, 3, 12 );
    g.add_edge(2, 1, 4 );
    g.add_edge(2, 4, 14);
    g.add_edge(3, 2, 9 );
    g.add_edge(3, 5, 20 );
    g.add_edge(4, 3, 7 );
    g.add_edge(4, 5, 4);

    cout << "Maximum flow " << g.get_max_flow(0, 5);
    return 0;
}
