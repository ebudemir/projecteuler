import math
import numpy as np
from itertools import combinations

from tqdm import tqdm


class Circle:
    is_origin_harmony_points_calculated = False
    list_of_harmony_points_at_origin = []
    list_of_circles = []

    def __init__(self, radius_sq, hp_1=np.array([0, 0]), hp_2=np.array([0, 0]), cross_circle=None):
        self.radius_sq = radius_sq
        if cross_circle is None:
            self.center = np.array([0, 0])
            self.neighbours = []
        else:
            self.center = hp_1 + hp_2 - cross_circle.center
            self.neighbours = [(cross_circle, hp_1, hp_2)]
            cross_circle.neighbours.append((self, hp_1, hp_2))
        self.find_all_harmony_points_of_circle_centered_at_origin()
        self.list_of_harmony_points = np.copy(Circle.list_of_harmony_points_at_origin) + self.center
        Circle.list_of_circles.append(self)

    def find_harmony_circles(self):
        lp_self = self.list_of_harmony_points
        for circle in self.list_of_circles:
            lp_other = circle.list_of_harmony_points
            #matches = (lp_self[:, :, np.newaxis] == lp_other[:, np.newaxis, :]).all(axis=2)
            lps = lp_self[:, np.newaxis, :]
            lpo = lp_other[np.newaxis, :, :]
            matches = (lps == lpo).all(axis=2)
            match_count = np.sum(matches)
            if (match_count == 2) and (circle not in self.neighbours) and (circle is not self):
                matching_values = lps[np.any(matches, axis=1)].squeeze()
                self.neighbours.append((circle, matching_values[0], matching_values[1]))
        return len(self.neighbours)

    def is_neighbour(self, circle):
        if any(circle is cc for cc, c1, c2 in self.neighbours):
            return True
        return False

    def find_all_harmony_points_of_circle_centered_at_origin(self):
        if not Circle.is_origin_harmony_points_calculated:
            Circle.is_origin_harmony_points_calculated = True
            for x in range(-int(math.sqrt(self.radius_sq)), int(math.sqrt(self.radius_sq)) + 1):
                y_sq = self.radius_sq - x ** 2
                y = math.isqrt(y_sq)
                # Check if y is a perfect square
                if y * y == y_sq:
                    # Add (x, y)
                    Circle.list_of_harmony_points_at_origin.append(np.array([x, y]))
                    # If y > 0, we must also add (x, -y) to get the bottom half
                    if y > 0:
                        Circle.list_of_harmony_points_at_origin.append(np.array([x, -y]))
            Circle.list_of_harmony_points_at_origin = np.array(Circle.list_of_harmony_points_at_origin)


def create_circles(radius_squared):
    origin = Circle(radius_squared)
    length = Circle.list_of_harmony_points_at_origin.shape[0]

    for i in range(length):
        for j in range(i + 1, length):
            point1 = Circle.list_of_harmony_points_at_origin[i]
            point2 = Circle.list_of_harmony_points_at_origin[j]
            new_center = point1 + point2
            if not any(np.array_equal(new_center, item.center) for item in Circle.list_of_circles):
                Circle(radius_squared, point1, point2, origin)


def find_harmony_circles():
    for circle in Circle.list_of_circles:
        neigs = circle.find_harmony_circles()


def find_combination(set_size):
    for combs in tqdm(combinations(Circle.list_of_circles, set_size)):
        neig = True
        for i in range(set_size):
            for j in range(i + 1, set_size):
                if not combs[i].is_neighbour(combs[j]):
                    neig = False
                    break
            if not neig:
                break
        if neig:
            return combs, True
    return None, False


def get_intersections_vec(c1, c2, r):
    """
    c1, c2: np.array([x, y])
    r: float radius
    Returns: (point1, point2) as np.arrays or None
    """
    # Vector from center 1 to center 2
    vec = c2 - c1
    d = np.linalg.norm(vec)

    # 1. Check if they intersect at exactly two points
    # (d < 2r for overlap, d > 0 to not be same circle)
    if d >= 2 * r or d == 0:
        return None

        # 2. Geometry of the intersection
    # Distance from c1 to the midpoint of the chord
    a = d / 2
    # Distance from midpoint of chord to intersection points
    h = np.sqrt(r ** 2 - a ** 2)

    # 3. Calculate the midpoint M
    M = (c1 + c2) / 2

    # 4. Find the unit perpendicular vector to 'vec'
    # For a vector [dx, dy], the perpendicular is [-dy, dx]
    # We normalize it and scale by h
    perpendicular_unit = np.array([-vec[1], vec[0]]) / d

    # 5. Offset from the midpoint to the two intersection points
    point1 = M + h * perpendicular_unit
    point2 = M - h * perpendicular_unit
    return point1, point2


def get_max_combination():
    i = 2
    prev = None
    while True:
        combs, res = find_combination(i)
        if not res:
            return prev, i - 1
        else:
            prev = combs
            i += 1


def consonant(circles):
    for circle1, circle2 in combinations(circles, 2):
        if not circle1.is_neighbour(circle2):
            return False
    return True


def print_circles():
    for circle in Circle.list_of_circles:
        ne = []
        for neig, c1, c2 in circle.neighbours:
            ne.append((circle.center, neig.center, c1, c2))
        print(circle.center, circle.list_of_harmony_points, np.array(ne))


radius_squared = 5
create_circles(radius_squared)
print(len(Circle.list_of_harmony_points_at_origin))
find_harmony_circles()
print_circles()
combs, result = get_max_combination()
print(radius_squared, result)
for cc in combs:
    for cc2 in combs:
        print(cc.center, cc2.center, get_intersections_vec(cc.center, cc2.center, math.sqrt(radius_squared)))
