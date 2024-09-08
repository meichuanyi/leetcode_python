from collections import Counter
b =[]
c = Counter(b)
T = int(input())
for _ in range(T):
    a, b = list(map(int, input().split()))
    print(b - a)
a, b, c = list(map(int, input().split()))

from collections import deque


def bfs_shortest_path(matrix, start, end):
    if not matrix or not matrix[0]:
        return -1  # 矩阵为空

    rows, cols = len(matrix), len(matrix[0])
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # 上、下、左、右
    queue = deque([start])  # BFS 队列
    visited = set()  # 记录已访问的节点
    visited.add(start)
    distance = 0  # 路径长度

    while queue:
        for _ in range(len(queue)):
            x, y = queue.popleft()
            # 检查是否到达终点
            if (x, y) in end:
                return distance

            # 遍历四个方向
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if (0 <= nx < rows and 0 <= ny < cols and
                        matrix[nx][ny] == 0 and (nx, ny) not in visited):
                    visited.add((nx, ny))
                    queue.append((nx, ny))

        distance += 1  # 增加路径长度

    return -1  # 如果没有路径


# 示例
matrix = [
    [0, 0, 1, 0],
    [0, 0, 0, 0],
    [0, 1, 1, 0],
    [0, 0, 0, 0]
]
start = (0, 0)  # 起点
end = (3, 3)  # 终点

shortest_path_length = bfs_shortest_path(matrix, start, end)
print("最短路径长度:", shortest_path_length)
ends = []
d1, (a1, b1) = bfs_shortest_path(matrix, (a, b), ends)