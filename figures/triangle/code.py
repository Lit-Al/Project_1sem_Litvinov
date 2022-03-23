from math import sqrt
A = 7
B = 2
C = 8

def triangle_perimeter(ft=A, sd=B, td=C):
    return ft + sd + td

def triangle_area(ft=A, sd=B, td=C):
    p = (ft + sd + td)
    return sqrt(p * (p - ft) * (p - sd) * (p - td))