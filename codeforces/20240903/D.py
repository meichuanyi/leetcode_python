

def count_right_triangles(points):
    point_set = set(points)  # 使用集合来存储点以便快速查找
    count = 0

    for A in points:
        # 统计 A 在同一横坐标和纵坐标的点
        vertical_points = [p for p in points if p[0] == A[0] and p != A]
        horizontal_points = [p for p in points if p[1] == A[1] and p != A]

        # 形成直角三角形
        for B in vertical_points:
            for C in horizontal_points:
                # 检查点 B 和 C 是否是有效的三角形顶点
                if (B[0], C[1]) in point_set:  # 检查是否存在交点
                    count += 1

    return count

T = int(input())
for _ in range(T):
    n = int(input())
    points = []
    for _ in range(n):
        x, y = list(map(int, input().split()))
        points.append((x, y))

    print(count_right_triangles(points))