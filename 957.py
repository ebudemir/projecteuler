def create_lines(red_dots, blue_dots, lines):
    count = 0
    for x in red_dots:
        for y in blue_dots:
            already_has_line = False
            for line in lines:
                if x in line and y in line:
                    already_has_line = True
                    break
            if not already_has_line:
                lines.append([x, y])
                count += 1
    return count


def create_blue_points(lines, blue_dots, count):
    for first_line in lines:
        for second_line in lines:
            if first_line != second_line:
                already_has_intersection = False
                for first_line_point in first_line:
                    for second_line_point in second_line:
                        if first_line_point == second_line_point:
                            already_has_intersection = True
                            break
                    if already_has_intersection:
                        break
                if not already_has_intersection:
                    point = str(count)
                    first_line.append(point)
                    second_line.append(point)
                    blue_dots.append(point)
                    count += 1


if __name__ == "__main__":
    red_dots = ["a", "b", "c"]
    blue_dots = ["1", "2"]
    lines = []
    count = 3
    for i in range(1, 17):
        create_lines(red_dots, blue_dots, lines)
        create_blue_points(lines, blue_dots, count)
        print(i, len(blue_dots))
