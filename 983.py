import math
import numpy as np

def find_all_grid_points_of_circle_centered_at_origin(radius_squared):
    points = []
    for x in range(-int(math.sqrt(radius_squared)), int(math.sqrt(radius_squared)) + 1):
        y_sq = radius_squared - x ** 2
        y = math.isqrt(y_sq)
        # Check if y is a perfect square
        if y * y == y_sq:
            # Add (x, y)
            points.append(np.array([x, y]))
            # If y > 0, we must also add (x, -y) to get the bottom half
            if y > 0:
                points.append(np.array([x, -y]))
    return np.array(points)

def get_all_harmonise_circles_with_origin(grid_points):
    length = grid_points.shape[0]
    result = [(np.array([0, 0]), grid_points.copy())]
    for i in range(length):
        for j in range(i + 1, length):
            point1 = grid_points[i]
            point2 = grid_points[j]
            new_center = point1 + point2
            if not any(np.array_equal(new_center, item[0]) for item in result):
                new_circle_points = grid_points.copy()
                new_circle_points = new_circle_points - new_center
                result.append((new_center, new_circle_points))
    return result

def get_consonant_sets(circles):



grid_points = find_all_grid_points_of_circle_centered_at_origin(1)
print(grid_points)
circles = get_all_harmonise_circles_with_origin(grid_points)


