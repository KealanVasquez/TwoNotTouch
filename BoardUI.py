with open("STAR_R2_10x10_v1.txt", "r") as file:
    collection = file.readlines()

print(collection[1])
print(type(collection[1]))

print(collection[1][9:109]+"\n")

puzzle = collection[300][9:109]
solution = collection[300][112:212]


blank = " "*100
print(blank)

def board(puzzle,solution):
    output = "┏━━━┳━━━┳━━━┳━━━┳━━━┳━━━┳━━━┳━━━┳━━━┳━━━┓\n┃                                       ┃\n┣   ╋   ╋   ╋   ╋   ╋   ╋   ╋   ╋   ╋   ┫\n┃                                       ┃\n┣   ╋   ╋   ╋   ╋   ╋   ╋   ╋   ╋   ╋   ┫\n┃                                       ┃\n┣   ╋   ╋   ╋   ╋   ╋   ╋   ╋   ╋   ╋   ┫\n┃                                       ┃\n┣   ╋   ╋   ╋   ╋   ╋   ╋   ╋   ╋   ╋   ┫\n┃                                       ┃\n┣   ╋   ╋   ╋   ╋   ╋   ╋   ╋   ╋   ╋   ┫\n┃                                       ┃\n┣   ╋   ╋   ╋   ╋   ╋   ╋   ╋   ╋   ╋   ┫\n┃                                       ┃\n┣   ╋   ╋   ╋   ╋   ╋   ╋   ╋   ╋   ╋   ┫\n┃                                       ┃\n┣   ╋   ╋   ╋   ╋   ╋   ╋   ╋   ╋   ╋   ┫\n┃                                       ┃\n┣   ╋   ╋   ╋   ╋   ╋   ╋   ╋   ╋   ╋   ┫\n┃                                       ┃\n┗━━━┻━━━┻━━━┻━━━┻━━━┻━━━┻━━━┻━━━┻━━━┻━━━┛"
    puzzlelist = []
    for i in range(10):
        puzzlelist.append(puzzle[10*i:10*i+10])
    print(puzzlelist)
    for row in range(10):
        for column in range(9):
            if puzzlelist[row][column] != puzzlelist[row][column+1]:
                output = output[:84*row+4*column+46] + "┃" + output[84*row+4*column+47:]
    zipped = tuple(zip(puzzlelist[0],puzzlelist[1],puzzlelist[2],puzzlelist[3],puzzlelist[4],puzzlelist[5],puzzlelist[6],puzzlelist[7],puzzlelist[8],puzzlelist[9]))
    print(zipped)
    for column in range(10):
        for row in range(9):
            if puzzlelist[row][column] != puzzlelist[row+1][column]:
                output = output[:84*row+4*column+85]+"━━━"+output[84*row+4*column+88:]
    for row in range(10):
        for column in range(10):
            if solution[10*row+column] == "1":
                output = output[:84*row+4*column+43]+"❲★❳"+output[84*row+4*column+46:]
            elif solution[10*row+column] == "0":
                output = output[:84*row+4*column+43]+" · "+output[84*row+4*column+46:]
    print(output)

board(puzzle,blank)

board(puzzle,solution)


