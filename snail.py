def snail(snail_map):
    print (snail_map)
    n = len(snail_map)
    fors = n + (n-1)
    cycles = 0
    newArr = []
    while fors > 0:
        for i in range( cycles, n - cycles ):
            if len(snail_map[cycles]) > 0:
                newArr.append(snail_map[cycles][i])
        fors = fors -1
        if fors > 1:
            for a in range( cycles + 1, n - cycles ):
                newArr.append(snail_map[a][n - (cycles +1)])
            fors = fors - 1
            for b in range( 1, n - (cycles * 2) ):
                newArr.append(snail_map[n - (cycles + 1)][n - (cycles + 1) - b]);
            fors = fors - 1
        if fors > 1:
            for c in range( n - cycles, 2 + cycles, -1 ):
                newArr.append(snail_map[c-2][cycles])
            fors = fors - 1
            cycles = cycles + 1
    return newArr

    pass