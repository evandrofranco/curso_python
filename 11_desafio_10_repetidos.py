

def remove_repetidos(lista):
    clone = []
    for i in lista:
        if clone.count(i) < 1:
            clone.append(i)
    return sorted(clone)


print(remove_repetidos([2, 2, 5, 1, 1, 10, 9, 8, 7, 7, 0, 1, 2, 7]))

print(remove_repetidos([10, 8, 9, 2, 1, 7, 7, 6, 5,
                        3, 3, 4, 2, 1, 0, -10, -20, -10, 9, 8, 7]))
