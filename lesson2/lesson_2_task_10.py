def bank(x, y):
    for n in range(1, y + 1):
        count = x +(x/10)
        x = count
    print(round(count, 3))
bank(6000, 5)