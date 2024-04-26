import math

def diff(a,b):
    return a - b

def multiply(a,b):
    return a * b

def add(a,b):
    return a + b

def my_map(func, points1, points2):
    if len(points1) != len(points2):
        raise ValueError("Les listes de points doivent avoir la même longueur")
    distances = [func(a, b) for a, b in zip(points1, points2)]
    return distances

a =[1,2,3,4,5]
b =[6,7,8,9,10]

resultMutiply = my_map(multiply,a,b)
resultAdd = my_map(add,a,b)
resultDiff = my_map(diff,a,b)
print(resultMutiply)
print(resultAdd)
print(resultDiff)