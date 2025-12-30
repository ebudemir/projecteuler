import math

import numpy as np


def Area(a, b, c):
    # semi-perimeter
    s = (a + b + c) / 2
    # area using Heron's formula
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    return area

def get_radius(area):
    return math.sqrt(area / math.pi)


def triangle_angles(a, b, c):
    A = math.acos((b * b + c * c - a * a) / (2 * b * c))
    B = math.acos((a * a + c * c - b * b) / (2 * a * c))
    C = math.acos((a * a + b * b - c * c) / (2 * a * b))

    return A, B, C

def cross_half_angles(distance, half_angle, radius):
    tan = math.tan(half_angle)
    cos = math.cos(half_angle)
    val = distance * distance * tan * tan
    val = val + distance * math.sqrt(distance * distance - val)
    val = val * cos / (distance * radius)
    return math.acos(val)

def triangular_area(distance, half_angle, radius):
    tan = math.tan(half_angle)
    return distance * tan * math.sqrt(radius * radius - tan * tan * distance * distance)

if __name__ == "__main__":
    a, b, c = 3, 4, 5
    t_area = Area(a, b, c)
    r = get_radius(t_area)
    print(r)
    A, B, C = triangle_angles(a, b, c)
    print(A, B, C)
    max_area = 0
    for a_ha in np.arange(0.01, a, 0.01):
        for I_ha in np.arange(0.01, r, 0.01):
            sA = math.atan(I_ha / a_ha)
            lA = math.sqrt(a_ha * a_ha + I_ha * I_ha)
            I_hb = lA * math.sin(A - sA)
            b_ha = c - a_ha
            sB = math.atan(I_ha / b_ha)
            lB = math.sqrt(b_ha * b_ha + I_ha * I_ha)
            I_hc = lB * math.sin(B - sB)
            if I_ha < r and I_hb < r and I_hc < r:
                A1 = triangular_area(a_ha, A, r)
                B1 = triangular_area(c - a_ha, B, r)
                C1 = triangular_area(b - a_ha, C, r)
                ang1 = cross_half_angles(a_ha, A, r)
                ang2 = cross_half_angles(c - a_ha, B, r)
                ang3 = cross_half_angles(b - a_ha, C, r)
                ang = 2 * (ang1 + ang2 + ang3)
                area = A1 + B1 + C1 + r * r * ang
                if area > max_area:
                    max_area = area
                    print(r, a_ha, A, B, C, r, ang1, ang2, ang3)

