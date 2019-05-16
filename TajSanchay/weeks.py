import datetime


def week_list():
    i = 1
    while i < 6:
        print(i)
        i += 1

    return i


d = datetime.date(2018, 8, 17)

print(week_list)
