# Graph from Exercise 1 (S, A, B, C, D, E, G)
graph = {'S':['A','D'], 'A':['B','C'], 'B':['C','D','E'], 'C':['G'], 'D':['B','E'], 'E':['G'], 'G':[]}

# Depth Limited Search (DLS)
def dls(node, goal, limit, path, depth=0):
    path.append(node)
    
    if node == goal:
        return path
        
    if depth < limit:
        for neighbour in graph[node]:
            if neighbour not in path:  # avoid revisiting (reached check)
                result = dls(neighbour, goal, limit, path.copy(), depth + 1)
                if result is not None:
                    return result
                    
    return None

# Iterative Deepening Search (IDS)
def ids(start, goal, max_depth=10):
    for limit in range(max_depth):
        print(f"Trying with depth limit = {limit}")
        result = dls(start, goal, limit, [])
        if result is not None:
            return result
    return None

# Driver code
print("Following is the Iterative Deepening Search")
solution = ids('S', 'G')

if solution:
    print("\nPath found:", " -> ".join(solution))
else:
    print("\nNo path found")