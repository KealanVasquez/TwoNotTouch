import matplotlib.pyplot as plt
import time
with open("STAR_R2_10x10_v1.txt", "r") as file:
    collection = file.readlines()

x=range(1200,1201)
y=[]
for index in range(1200,1201):
    level = index

    #So far the solver works only on puzzles whose last cell is a star -- FIXED!

    #print(collection[level])

    puzzle = collection[level][9:109]
    solution = collection[level][112:212]

    print("puzzle "+str(level))
    print(puzzle)


    A = set()
    B = set()
    C = set()
    D = set()
    E = set()
    F = set()
    G = set()
    H = set()
    I = set()
    J = set()

    for i in range(100):
        if puzzle[i] == "A":
            A.add(i)
        if puzzle[i] == "B":
            B.add(i)
        if puzzle[i] == "C":
            C.add(i)
        if puzzle[i] == "C":
            C.add(i)
        if puzzle[i] == "D":
            D.add(i)
        if puzzle[i] == "E":
            E.add(i)
        if puzzle[i] == "F":
            F.add(i)
        if puzzle[i] == "G":
            G.add(i)
        if puzzle[i] == "H":
            H.add(i)
        if puzzle[i] == "I":
            I.add(i)
        if puzzle[i] == "J":
            J.add(i)

    endpoints = {max(A):A,max(B):B,max(C):C,max(D):D,max(E):E,max(F):F,max(G):G,max(H):H,max(I):I,max(J):J}

    #print(endpoints)

    blank = [0]*100

    def region_check(cell):
        #print("reg",cell)
        if cell%10 == 9:
            #print(sum(blank[i-9:i+1]),"star(s) in row")
            if sum(blank[cell-9:cell+1]) == 2:
                pass
            else:
                #print("failed row")
                return False
        if cell >= 90:
            column = cell%10
            column_sum = 0
            for row in range(10):
                column_sum += blank[10*row+column]
            if column_sum == 2:
                pass
            else:
                #print("failed column")
                return False
        if cell in endpoints:
            region_sum = 0
            for j in endpoints[cell]:
                region_sum += blank[j]
            if region_sum == 2:
                pass
            else:
                #print("failed region")
                return False
        return True

    def adjacency_check(cell):
        #print("adj",i)
        star = False
        top_border = False
        left_border = False
        right_border = False
        if blank[cell] == 1:
            star = True
        if cell<10:
            top_border = True
        if cell%10 == 0:
            left_border = True
        if cell%10 == 9:
            right_border = True
        if star:
            if top_border:
                if left_border:
                    return True
                else:
                    if blank[cell - 1] + blank[cell] <= 1:
                        pass
                    else:
                        #print("fail adj: top border")
                        return False
            else:
                if left_border:
                    if blank[cell - 10] + blank[cell-9] + blank[cell] <= 1:
                        pass
                    else:
                        #print("fail adj: left border")
                        return False
                else:
                    if right_border:
                        if blank[cell - 10] + blank[cell-11] + blank[cell - 1] + blank[cell] <= 1:
                            pass
                        else:
                            #print("fail adj: right border")
                            return False
                    else:
                        if blank[cell - 1] + blank[cell - 11] + blank[cell - 10] + blank[cell - 9] + blank[cell] <= 1:
                            #print(i,"pass adj: interior")
                            pass
                        else:
                            #print(i,"fail adj: interior",blank[i - 1],blank[i - 11],blank[i - 10],blank[i - 9],blank[i])
                            return False
        return  True


    def test(cell):
        #print(blank)
        blank[cell] = 1
        #print("cell",cell,"=",blank[cell])
        if cell == 99:
            blank[cell] = 1
            if adjacency_check(cell) and region_check(cell):
                return True
            blank[cell] = 0
            if region_check(cell):
                return True
            else:
                return  False

        blank[cell] = 1
        if adjacency_check(cell) and region_check(cell):
            if test(cell+1):
                return True

        blank[cell] = 0
        if region_check(cell):
            if test(cell+1):
                return True
        else:
            #print(cell,"failed X, did we backtrack?")
            return False

    start = time.time()
    test(0)
    finish = time.time()
    attempt = ""
    for entry in blank:
        attempt += str(entry)

    print("solution found by algorithm:")
    print(attempt)
    print("solution from solution key provided:")
    print(solution)
    print("computation completed in "+str(finish-start)+" seconds")

    y.append(finish-start)

plt.yscale("log")
plt.plot(x,y,'o')
plt.show()