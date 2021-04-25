# Depth-first search
def dfs(node, explored):
    if node not in explored:
        explored.append(node)
        for n in node.neighbors:
            dfs(n, explored)
    return explored

# Breadth-first search
def bfs(start, goal):
    # begin = time()
    explored = []
    paths = [[start]]

    while len(paths) > 0:
        path1 = paths.pop(0)
        lastnode = path1[-1]
        if lastnode not in explored:
            for n in lastnode.neighbors:
                newpath = list(path1)
                newpath.append(n)
                paths.append(newpath)
                if n == goal:
                    # print(time() - begin)
                    return newpath
            explored.append(lastnode)
    # pass
