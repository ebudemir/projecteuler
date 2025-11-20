import datetime


def count_sundays_datetime(start_year=1901, end_year=2000):
    count = 0
    for year in range(start_year, end_year + 1):
        for month in range(1, 13):
            if datetime.date(year, month, 1).weekday() == 6:  # Monday=0 ... Sunday=6
                count += 1
    return count


if __name__ == "__main__":
    print(count_sundays_datetime())  # Expected: 171
