with open('deepest_fear.txt') as original:
    with open('sample.txt', 'w') as copy:
        for line in original:
            copy.write(line)
