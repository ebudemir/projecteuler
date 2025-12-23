odddigits = "13579"
five = list("5")


def odd_digits_occur_odd_times(s):
    ss = str(s)
    for d in odddigits:
        if ss.count(d) % 2 == 0:
            return False
    return True


def divisible_by_105(s):
    sss = "".join(s)
    val = int(sss)
    if val % 3 == 0:
        if val % 5 == 0:
            if val % 7 == 0: return True
    return False


def increment_with5(s):
    first = s[:len(s) - 1]
    theta = first
    while True:
        theta = increment(theta)
        sw5 = theta + five
        if odd_digits_occur_odd_times(sw5) and divisible_by_105(sw5):
            return sw5


def increment_with9(s):
    for index in range(len(s)):
        if s[len(s) - index - 1] == "9":
            s[len(s) - index - 1] = "1"
        else:
            if s[len(s) - index - 1] == "1":
                s[len(s) - index - 1] = "3"
            elif s[len(s) - index - 1] == "3":
                s[len(s) - index - 1] = "5"
            elif s[len(s) - index - 1] == "5":
                s[len(s) - index - 1] = "7"
            elif s[len(s) - index - 1] == "7":
                s[len(s) - index - 1] = "9"
            return s
    return list("1") + s


def increment(s):
    digit = s[-1]
    if digit == "1":
        s[-1] = "3"
    elif digit == "3":
        s[-1] = "5"
    elif digit == "5":
        s[-1] = "7"
    elif digit == "7":
        s[-1] = "9"
    elif digit == "9":
        s = increment_with9(s)
    return s


if __name__ == "__main__":
    start = "1117935"
    print("1", start)
    theta = start
    for i in range(10**16):
        val = i + 2
        theta = increment_with5(list(theta))
        theta_val = "".join(theta)
        print(val, theta_val)
