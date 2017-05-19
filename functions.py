def sum_list(lister):
    sum = 0
    for x in lister:
        sum += x

    return sum

list = [2, 12, 8, 28, 35, 9, 22, 40]
sum = sum_list(list)
print(sum)
