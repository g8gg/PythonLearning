# Merry Christmas

def christmas_trees(level=3, bigger=3):
    for number in range(level, 0, -1):
        for item in range(number * bigger, 0, -1):
            print('*', end='')
        print()


christmas_trees()
