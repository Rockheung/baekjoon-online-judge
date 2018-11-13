
# https://www.acmicpc.net/problem/1260
# DFS: Depth First Search
# BFS: Breadth First Search
def ans_dfs(g,i):
    print(g)
    node = list(g.keys())
    s = [i]
    visited = []
    while (s):
        top = s.pop()
        node[top-1] = 0
        visited.append(str(top))
        s.extend([x for x in sorted(g[top], reverse=True) if node[x-1]])
        print(s)
    return visited


def ans_bfs(g,i):
    node = list(g.keys())
    def lock_(x, node, visited): node[x-1] = 0; visited.append(str(x)); return x
    q = [i]
    node[i-1] = 0
    visited = [str(i)]
    while (q):
        top = q.pop(0)
        q.extend([lock_(x, node, visited) for x in sorted(g[top]) if node[x-1]])
    return visited


if __name__ == '__main__':
    from sys import stdin
    n, m, i = [int(x) for x in input().split()]
    g = {x+1:set() for x in range(n)}
    for _ in range(m):
        k, v = tuple(int(x) for x in stdin.readline().rstrip().split())
        g[k].add(v)
        g[v].add(k)

    print(*ans_dfs(g,i))
    print(*ans_bfs(g,i))
