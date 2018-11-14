
# https://www.acmicpc.net/problem/1260
# DFS: Depth First Search
# BFS: Breadth First Search
# https://www.acmicpc.net/problem/1260
# DFS: Depth First Search
# BFS: Breadth First Search
# def ans_dfs(g,i):
#     s = [i]
#     visited = []
#     while s:
#         top = s.pop()
#         visited.append(top)
#         for x in [x for x in sorted(g[top], reverse=True) if x not in visited]:
#             if x in s:
#                 s.pop(s.index(x))
#             s.append(x)
#     return visited
# 
# 
# def ans_bfs(g,i):
#     def lock_(x, visited): visited.append(x); return x
#     q = [i]
#     visited = [i]
#     while (q):
#         top = q.pop(0)
#         q.extend([lock_(x, visited) for x in sorted(g[top]) if x not in visited])
#     return visited


def ans_dfs(g,i):
    node = [i if x else 0 for i, x in g.items()]
    s = [i]
    visited = []
    while s:
        top = s.pop()
        if node[top-1]:
            node[top-1] = 0
            visited.append(top) 
        s.extend([x for x in sorted(g[top], reverse=True) if node[x-1]])
        print(s)
    return visited


def ans_bfs(g,i):
    node = [i if x else 0 for i, x in g.items()]
    def lock_(x, node, visited): node[x-1] = 0; visited.append(x); return x
    q = [i]
    node[i-1] = 0
    visited = [i]
    while (q):
        top = q.pop(0)
        q.extend([lock_(x, node, visited) for x in sorted(g[top]) if node[x-1]])
    return visited

def dfs(graph, start):
    visited = []
    stack = [start]

    while stack:
        n = stack.pop()
        if n not in visited:
            visited.append(n)
            stack += sorted(graph[n] - set(visited), reverse=True)
        print(stack)
    return visited

def bfs(graph, start):
    visited = []
    queue = [start]

    while queue:
        n = queue.pop(0)
        if n not in visited:
            visited.append(n)
            queue += sorted(graph[n] - set(visited))
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
    print()
    print(*dfs(g,i))
    print(*bfs(g,i))
