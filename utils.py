import matplotlib.pyplot as plt
import numpy as np


# ALGEBRA UTILS ========================================================================

def simplify(lst_coefficients):
    m = max(lst_coefficients)
    return (e / m if e != m else 1 for e in lst_coefficients)


def extract_slope_coefficients(line):
    xa, ya = line[1]
    xb, yb = line[0]
    a = ya - yb
    b = xb - xa
    c = (xa - xb) * ya + (yb - ya) * xa
    a, b, c = simplify((a, b, c))
    return a, b, c


# GEOMETRY UTILS =======================================================================

def area_of(polygon):
    x, y = list(zip(*polygon))
    return 0.5 * np.abs(np.dot(x, np.roll(y, 1)) - np.dot(y, np.roll(x, 1)))


def is_point_on_segment(segment, point_to_check):
    a, b = segment
    cross_product = (point_to_check[1] - a[1]) * (b[0] - a[0]) - (
            point_to_check[0] - a[0]) * (
                            b[1] - a[1])
    dotproduct = (point_to_check[0] - a[0]) * (b[0] - a[0]) + (point_to_check[1] - a[1]) * (b[1] - a[1])
    squaredlengthba = (b[0] - a[0]) * (b[0] - a[0]) + (b[1] - a[1]) * (b[1] - a[1])
    return not (abs(cross_product) > 0.0000001 or dotproduct < 0 or dotproduct > squaredlengthba)


def subtract_from(from_poly, second_poly):
    magic_point = second_poly[-1]
    designated_vertex = from_poly[0]
    result = [designated_vertex, magic_point] + [from_poly[i] for i in range(len(from_poly)) if
                                                 i >= len(second_poly) or from_poly[i] != second_poly[i]]
    return result


# DISPLAY UTILS ========================================================================

def display_polygons(polygons):
    for poly in polygons:
        draw_polygon(poly, 'black')
    plt.axis('equal')
    plt.show()


def draw_polygon(poly_vertices, color):
    next_point = []
    for i in range(len(poly_vertices) - 1):
        point = poly_vertices[i]
        next_point = poly_vertices[i + 1]
        plt.plot((point[0], next_point[0]), (-point[1], -next_point[1]), color=color)
    plt.plot((next_point[0], poly_vertices[0][0]), (-next_point[1], -poly_vertices[0][1]),
             color=color)
