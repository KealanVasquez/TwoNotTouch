with open("STAR_R2_10x10_v1.txt", "r") as file:
    collection = file.readlines()


level = 600

#print(collection[level])


solution = collection[level][112:212]

#print(puzzle)


for level in [1,600,1200,1800,2400]:
    puzzle = collection[level][9:109]
    print("LEVEL : " + str(level) +"\n")
    input = ""
    for region in ["A","B","C","D","E","F","G","H","I","J"]:
        for cell in range(0, 100):
            if puzzle[cell] == region:
                input += "x"
                if cell <10:
                    input += "0"
                input += str(cell)+" + "
        input = input[0:-3] + " = 2\n"
    print(input)