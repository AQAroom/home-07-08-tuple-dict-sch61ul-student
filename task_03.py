x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())

point1 = (x1, y1)
point2 = (x2, y2)
distance = ((point2[0] - point1[0]) ** 2 + (point2[1] - point1[1]) ** 2) ** 0.5
print(f"{distance:.2f}")