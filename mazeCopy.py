class Solution:
    def hasPath(self, maze: list[list[int]], start: list[int], destination: list[int]) -> bool:
        visited = set()
        directions = [(1, 0), (-1, 0), (0, -1), (0, 1)]
        stack = [start]
        while stack:
            row, col = stack.pop()
            # reach the destination
            if [row, col] == destination:
                return True
            # try all possible directions from the current position
            for dirx, diry in directions:
                r, c = row, col
                while 0 <= r + dirx < len(maze) and 0 <= c + diry < len(maze[0]) and not maze[r + dirx][c + diry]:
                    r = r + dirx
                    c = c + diry
                if (r, c) not in visited:
                    visited.add((r, c))
                    stack.append((r, c))
        return False  # if there is no path


# testcase1
maze = [[0, 0, 1, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 1, 0],
        [1, 1, 0, 1, 1], [0, 0, 0, 0, 0]]
start1 = [0, 4]
destination1 = [4, 4]
print(f"testcase1---> {Solution().hasPath(maze, start1, destination1)}")

# testcase2
start2 = [0, 4]
destination2 = [3, 2]
#print(f"testcase2---> {Solution().hasPath(maze, start2, destination2)}")

# testcase3
start3 = [4, 3]
destination3 = [0, 1]
#print(f"testcase3---> {Solution().hasPath(maze, start3, destination3)}")
