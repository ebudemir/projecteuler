# Number words
ones = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine",
        "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen",
        "seventeen", "eighteen", "nineteen"]

tens = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]


def number_to_words(n):
    if n == 1000:
        return "onethousand"
    words = ""
    if n >= 100:
        words += ones[n // 100] + "hundred"
        if n % 100 != 0:
            words += "and"
    n = n % 100
    if n >= 20:
        words += tens[n // 10]
        n = n % 10
    if n > 0:
        words += ones[n]
    return words


# Compute total letters
total_letters = sum(len(number_to_words(i)) for i in range(1, 1001))
print(total_letters)
