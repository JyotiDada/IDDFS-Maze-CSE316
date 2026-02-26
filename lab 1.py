def iddfs(grid, start, target, max_depth):
    rows = len(grid)
    cols = len(grid[0])

    def dls(x, y, depth, visited, path):

        if (x, y) == target:
            path.append((x, y))
            return True

        if depth == 0:
            return False

        visited.add((x, y))
        path.append((x, y))

        directions = [(-1,0), (1,0), (0,-1), (0,1)]

        for dx, dy in directions:
            nx, ny = x + dx, y + dy

            if (0 <= nx < rows and
                0 <= ny < cols and
                grid[nx][ny] == 0 and
                (nx, ny) not in visited):

                if dls(nx, ny, depth - 1, visited, path):
                    return True

        path.pop()
        return False

    for depth in range(max_depth + 1):
        visited = set()
        path = []

        if dls(start[0], start[1], depth, visited, path):
            return depth, path

    return None, None

if __name__ == "__main__":
    rows, cols = map(int, input().split())

    grid = []
    for _ in range(rows):
        grid.append(list(map(int, input().split())))

    start_input = input()
    target_input = input()

    start = tuple(map(int, start_input.strip("Start: ()").split(",")))
    target = tuple(map(int, target_input.strip("Target: ()").split(",")))

    depth, path = iddfs(grid, start, target, 10)

    if path:
        print(f"Path found at depth {depth}")
        print("Traversal Order:", path)
    else:
        print("Path not found")