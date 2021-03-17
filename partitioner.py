from utils import display_polygons, area_of, is_point_on_segment, subtract_from, \
    extract_slope_coefficients


def reversed_shoelace(target_area, line, v_i, v_ip1, sign):
    a, b, c = extract_slope_coefficients(line)
    x1, y1 = v_i
    x2, y2 = v_ip1
    if b == 0:
        x = (-c / a).as_integer_ratio()
        y = ((-2 * sign * target_area - y1 * (a * x2 + c) + y2 * (a * x1 + c)) / (
                a * (x1 - x2))).as_integer_ratio()
    else:
        x = ((2 * target_area * sign * b + x2 * (b * y1 + c) - x1 * (b * y2 + c)) / (
                a * x1 - a * x2 + b * (y1 - y2))).as_integer_ratio()
        y = ((-2 * sign * target_area * a - y1 * (a * x2 + c) + y2 * (a * x1 + c)) / (
                a * x1 - a * x2 + b * (y1 - y2))).as_integer_ratio()
    return x[0] / x[1], y[0] / y[1]


def find_magic_point(target_area, v_ip1, v_ip2):
    """
    Finds the magic point point Φ located on the edge (v_ip1, v_ip2) such that
    such that the polygon [designatedVertex - v_ip1 - Φ] has targetArea
    :param target_area: Area of desired partition
    :param v_ip1: First point of edge opposite to the designated vertex
    :param v_ip2: Second point of edge opposite to the designated vertex
    :return:
    """
    magic_point = reversed_shoelace(target_area, (v_ip1, v_ip2), DESIGNATED_VERTEX,
                                    v_ip1,
                                    -1)
    point2 = reversed_shoelace(target_area, (v_ip1, v_ip2), DESIGNATED_VERTEX,
                               v_ip1, 1)
    if not (is_point_on_segment((v_ip1, v_ip2), magic_point)):
        magic_point = point2
    return magic_point


def cut(polygon_vertices, target_area, i=0):
    """
    Performs the cut of ONE partition from the given polygon
    :param polygon_vertices: List of vertices of the polygon to partition
    :param target_area: Current target area
    :param i: Index of current triangle
    :return: Partition and remaining polygon
    """
    v_ip1, v_ip2 = polygon_vertices[i + 1], polygon_vertices[i + 2]
    current_triangle = [DESIGNATED_VERTEX, v_ip1, v_ip2]
    area_current_triangle = area_of(current_triangle)
    if area_current_triangle == target_area:
        return current_triangle, subtract_from(polygon_vertices, current_triangle)
    elif area_current_triangle > target_area:
        magic_point = find_magic_point(target_area, v_ip1, v_ip2)
        sub_poly = polygon_vertices[:i + 2] + [magic_point]
        return sub_poly, subtract_from(polygon_vertices, sub_poly)
    else:
        remaining_area = target_area - area_current_triangle
        return cut(polygon_vertices, remaining_area, i + 1)


def compute_partitions(polygon_vertices, n_partitions, target_area):
    if n_partitions == 1:
        return [polygon_vertices]
    else:
        current_partition, remaining_polygon = cut(polygon_vertices, target_area)
        return [current_partition] + compute_partitions(remaining_polygon, n_partitions - 1, target_area)


def compute_partitions_of(polygon_vertices, n_partitions):
    sub_polygons = []
    target_area = area_of(polygon_vertices) / n_partitions
    remaining_polygon = polygon_vertices
    while n_partitions > 1:
        current_partition, remaining_polygon = cut(remaining_polygon, target_area)
        sub_polygons.append(current_partition)
        n_partitions -= 1
    sub_polygons.append(remaining_polygon)
    return sub_polygons


if __name__ == "__main__":
    original_region = [(98, 136), (179, 323), (321, 313), (493, 142), (506, 23), (98, 58)]
    DESIGNATED_VERTEX = original_region[0]
    n_partitions = 3
    target_area = area_of(original_region) / n_partitions

    partitions = compute_partitions(original_region, n_partitions, target_area)
    display_polygons(partitions)
