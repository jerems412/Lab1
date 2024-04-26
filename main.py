import math

def calc_distance(point1, point2):
    x1, y1, z1 = point1
    x2, y2, z2 = point2
    distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2 + (z2 - z1) ** 2)
    return distance


def my_map(func, points1, points2):
    if len(points1) != len(points2):
        raise ValueError("Les listes de points doivent avoir la même longueur")
    distances = [func(point1, point2) for point1, point2 in zip(points1, points2)]
    return distances

points1 = [(1.0,1.0,1.0),(2.0,2.0,2.0),(3.0,3.0,3.0)]
points2 = [(4.0,4.0,4.0),(5.0,5.0,5.0),(6.0,6.0,6.0)]

distances = my_map(calc_distance, points1, points2)
print(distances)