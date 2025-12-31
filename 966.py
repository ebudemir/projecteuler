from tqdm import tqdm
import numpy as np
import mpmath as mp
from decimal import Decimal, getcontext, ROUND_HALF_UP

mp.mp.dps = 100  # hassasiyet
ctx = getcontext()
ctx.prec = 100
ctx.rounding = ROUND_HALF_UP

PI = Decimal("3.14159265358979323846264338327950288419716939937510")


def Area(a, b, c):
    # semi-perimeter
    s = (a + b + c) / 2
    # area using Heron's formula
    area = (s * (s - a) * (s - b) * (s - c)).sqrt()
    return area


def get_radius(area):
    return (area / PI).sqrt()


def triangle_angles(a, b, c):
    A = mp.acos((b * b + c * c - a * a) / (2 * b * c))
    B = mp.acos((a * a + c * c - b * b) / (2 * a * c))
    C = mp.acos((a * a + b * b - c * c) / (2 * a * b))
    return A, B, C


def get_angle(side, chord, radius):
    other_side = (radius * radius - side * side).sqrt()
    big_angle = mp.atan(chord / side)
    small_angle = mp.atan(other_side / side)
    return big_angle - small_angle


def triangular_area(side, radius):
    other_side = (radius * radius - side * side).sqrt()
    return other_side * side


if __name__ == "__main__":
    aa, bb, cc = 3, 4, 6
    a = Decimal.from_float(aa)
    b = Decimal.from_float(bb)
    c = Decimal.from_float(cc)
    t_area = Area(a, b, c)
    r = get_radius(t_area)
    #print(r)
    A, B, C = triangle_angles(a, b, c)
    #print(mp.degrees(A), mp.degrees(B), mp.degrees(C))
    max_area = 0
    #for A_Hc in tqdm(np.arange(r - Decimal("0.3"), a + Decimal("2"), Decimal("0.005"))):
    for A_Hc in tqdm(np.arange(Decimal("3.3450"), Decimal("3.3550"), Decimal("0.00001"))):
        #for I_Hc in np.arange(Decimal("0.05"), r + Decimal("0.9"), Decimal("0.005")):
        for I_Hc in np.arange(Decimal("0.5110"), Decimal("0.5140"), Decimal("0.00001")):
            a_I_A_Hc = mp.atan(I_Hc / A_Hc)
            A_I = (A_Hc * A_Hc + I_Hc * I_Hc).sqrt()
            a_I_A_Hb = A - a_I_A_Hc
            I_Hb = A_I * Decimal(str(mp.sin(a_I_A_Hb)))
            A_Hb = A_I * Decimal(str(mp.cos(a_I_A_Hb)))
            C_Hb = b - A_Hb
            B_Hc = c - A_Hc
            a_I_B_Hc = mp.atan(I_Hc / B_Hc)
            B_I = (B_Hc * B_Hc + I_Hc * I_Hc).sqrt()
            a_I_B_Ha = B - a_I_B_Hc
            I_Ha = B_I * Decimal(str(mp.sin(a_I_B_Ha)))
            B_Ha = B_I * Decimal(str(mp.cos(a_I_B_Ha)))
            C_Ha = a - B_Ha
            I_C1 = (C_Ha * C_Ha + I_Ha * I_Ha).sqrt()
            I_C2 = (C_Hb * C_Hb + I_Hb * I_Hb).sqrt()
            I_C = (I_C1 + I_C2) / 2
            if C_Ha > 0 and C_Hb > 0:
                a_I_C_Ha = mp.atan(I_Ha / C_Ha)
                a_I_C_Hb = mp.atan(I_Hb / C_Hb)
                if 0 < I_Ha <= r and 0 < I_Hb <= r and 0 < I_Hc <= r:
                    area1 = triangular_area(I_Hc, r)
                    area2 = triangular_area(I_Hb, r)
                    area3 = triangular_area(I_Ha, r)
                    angle1 = get_angle(I_Hc, A_Hc, r)
                    angle2 = get_angle(I_Hc, B_Hc, r)
                    angle3 = get_angle(I_Hb, A_Hb, r)
                    angle4 = get_angle(I_Hb, C_Hb, r)
                    angle5 = get_angle(I_Ha, B_Ha, r)
                    angle6 = get_angle(I_Ha, C_Ha, r)
                    angle = angle1 + angle2 + angle3 + angle4 + angle5 + angle6
                    area = angle * r * r / 2
                    total_area = area + area1 + area2 + area3
                    tri_area = area1 + area2 + area3
                    #print(area)
                    #print("MAX AREA", max_area)
                    if total_area > max_area:
                        max_area = total_area
                        print("MAX AREA", max_area)
                        print("A_Hc", A_Hc)
                        print("I_Hc", I_Hc)
                        # print(I_C, I_C1, I_C2)
                        # print(mp.degrees(a_I_A_Hc), mp.degrees(a_I_A_Hb))
                        # print(mp.degrees(a_I_B_Hc), mp.degrees(a_I_B_Ha))
                        # print(mp.degrees(a_I_C_Ha), mp.degrees(a_I_C_Hb))
                        # print(I_Ha, I_Hb, I_Hc)
                        # print(C_Ha, B_Ha)
                        # print(C_Hb, A_Hb)
                        # print(A_Hc, B_Hc)
                        # print(angle)
                        # print(tri_area)
