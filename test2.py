from itertools import permutations

list_of_list_of_numbers = dict()
list_of_counts7 = dict()
pairs = [11, 13, 15, 17, 19, 31, 33, 35, 37, 39, 51, 53, 55, 57, 59, 71, 73, 75, 77, 79, 91, 93, 95, 97, 99]
total_count = 0


def list_numbers_from_counts(digit_counts):
    """
    digit_counts: dict like {1:3, 3:1, 5:1}
    yields integers formed using exactly these digits
    """

    digits = sorted(digit_counts.keys())
    total_len = sum(digit_counts.values())
    current = []

    def backtrack():
        if len(current) == total_len:
            yield int("".join(current))
            return

        for d in digits:
            if digit_counts[d] > 0:
                digit_counts[d] -= 1
                current.append(str(d))
                yield from backtrack()
                current.pop()
                digit_counts[d] += 1

    yield from backtrack()


def odd_digit_counts(digits, total):
    """
    digits: list of digits, e.g. [1,3,5,7,9]
    total: total count (must be >= len(digits) and same parity)

    returns: list of dicts {digit: odd_count}
    """

    k = len(digits)

    # Feasibility check
    if total < k or (total - k) % 2 != 0:
        return []

    target = (total - k) // 2
    results = []

    def backtrack(i, remaining, xs):
        if i == k:
            if remaining == 0:
                counts = [2 * x + 1 for x in xs]
                results.append(dict(zip(digits, counts)))
            return

        for x in range(remaining + 1):
            backtrack(i + 1, remaining - x, xs + [x])

    backtrack(0, target, [])
    return results


def get_very_odd_numbers(digits):
    permutations = odd_digit_counts([1, 3, 5, 7, 9], digits)
    print("permutations calculated.")
    for perm in permutations:
        total = sum(k * v for k, v in perm.items())
        r3 = total % 3
        perm[5] = perm[5] - 1
        numbers = list_numbers_from_counts(perm)
        for number in list(numbers):
            num = str(number) + "5"
            r7 = int(num) % 7
            key = str(r3) + str(r7)
            if not key in list_of_lists:
                list_of_lists[key] = []
            rlist = list_of_lists[key]
            rlist.append(int(num))
    for ls in list_of_lists.values():
        ls.sort()


def get_very_odd_numberss(digits):
    for number in range(1000005, 9999999, 10):
        num = str(number)
        c0 = num.count("0")
        c2 = num.count("2")
        c4 = num.count("4")
        c6 = num.count("6")
        c8 = num.count("8")
        if c0 == 0 and c2 == 0 and c4 == 0 and c6 == 0 and c8 == 0:
            r3 = number % 3
            r7 = number % 7
            c1 = num.count("1") % 2
            c3 = num.count("3") % 2
            c5 = num.count("5") % 2
            c7 = num.count("7") % 2
            c9 = num.count("9") % 2
            key = str(r3) + str(r7) + str(c1) + str(c3) + str(c5) + str(c7) + str(c9)
            if not key in list_of_list_of_numbers:
                list_of_list_of_numbers[key] = []
            rlist = list_of_list_of_numbers[key]
            rlist.append(int(num))
    for k, v in list_of_list_of_numbers.items():
        v.sort()
        print(k, len(v), v)
        list_of_list_of_counts[k] = len(v)


def step_up_two_digits(digits):
    previous_digit_count = digits - 2
    new_list_of_lists = {}
    for pair in pairs:
        addition = pair * 10 ** previous_digit_count
        r3 = addition % 3
        r7 = addition % 7
        num = str(addition)
        c1 = num.count("1") % 2
        c3 = num.count("3") % 2
        c5 = num.count("5") % 2
        c7 = num.count("7") % 2
        c9 = num.count("9") % 2
        for k, v in list_of_list_of_counts.items():

        key = str(r3) + str(r7) + str(c1) + str(c3) + str(c5) + str(c7) + str(c9)
        ct = list_of_list_of_counts[key]
        new_key = str(pair) + key
        new_list_of_lists[new_key] = new_list_of_lists.get(new_key, 0) + ct
        r3 = (3 - r3) % 3
        r7 = (7 - r7) % 7
        c1 = ((num.count("1") % 2) + 1) % 2
        c3 = ((num.count("3") % 2) + 1) % 2
        c5 = ((num.count("5") % 2) + 1) % 2
        c7 = ((num.count("7") % 2) + 1) % 2
        c9 = ((num.count("9") % 2) + 1) % 2
    count = 0
    for k, v in new_list_of_lists.items():
        count += v
    print(count)


if __name__ == "__main__":
    total = 0
    get_very_odd_numberss(7)
    count = list_of_lists_counts["0011111"]
    total_count += count
    print("7", total_count, count)
    step_up_two_digits(9)

