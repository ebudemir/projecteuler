import math
import numpy as np


def find_all_integer_points(radius_limit, list_of_radius):
    # n represents r^2. We go up to radius_limit**2
    max_n = radius_limit ** 2

    print(f"{'Radius':<10} | {'All Integer Points (x, y)':<20}")
    print("-" * 60)

    for n in range(1, max_n + 1):
        points = []
        # Check all possible x values for this specific r^2 (n)
        # x goes up to sqrt(n). If x^2 + y^2 = n, then x <= sqrt(n)
        for x in range(-int(math.sqrt(n)), int(math.sqrt(n)) + 1):
            y_sq = n - x ** 2
            y = math.isqrt(y_sq)

            # Check if y is a perfect square
            if y * y == y_sq:
                # Add (x, y)
                points.append(np.array([x, y]))
                # If y > 0, we must also add (x, -y) to get the bottom half
                if y > 0:
                    points.append(np.array([x, -y]))

        # If we found any points for this n
        if points:
            r = math.sqrt(n)
            if r > radius_limit:
                break

            # Formatting the radius for display
            #display_r = int(r) if r.is_integer() else round(r, 3)
            display_r = n
            # Sort points for a cleaner display: (x, y)
            #points.sort()
            print(f"{display_r:<10} | {points}")
            list_of_radius.append((n, np.array(points)))

def get_all_circles(radius_square, point1, point2, starting_center, list_of_integer_points):
    new_center = point1 + point2 - starting_center






# Warning: A limit of 1000 will result in a massive output.
# Starting with 10 to see the effect:
list_of_radius = []
find_all_integer_points(50, list_of_radius)
print(list_of_radius)

for n, integer_points in list_of_radius:
    length = len(integer_points)
    for i in range(length):
        for j in range(i+1, length):
            point1 = integer_points[i]
            point2 = integer_points[j]
            new_center = point1 + point2 - starting_center
            new_circle_points = integer_points.copy()

