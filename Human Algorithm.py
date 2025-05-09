import time

#from fontTools.subset import intersect

with open("STAR_R2_10x10_v1.txt", "r") as file:
    collection = file.readlines()

times = []
acc = []
for i in [368]:
    level = i

    puzzle = collection[level][9:109]
    solution = collection[level][112:212]

    print("puzzle "+str(level))
    #print(puzzle)


    blank = " "*100

    def board(puzzle,solution):
        output = "┏━━━┳━━━┳━━━┳━━━┳━━━┳━━━┳━━━┳━━━┳━━━┳━━━┓\n┃                                       ┃\n┣   ╋   ╋   ╋   ╋   ╋   ╋   ╋   ╋   ╋   ┫\n┃                                       ┃\n┣   ╋   ╋   ╋   ╋   ╋   ╋   ╋   ╋   ╋   ┫\n┃                                       ┃\n┣   ╋   ╋   ╋   ╋   ╋   ╋   ╋   ╋   ╋   ┫\n┃                                       ┃\n┣   ╋   ╋   ╋   ╋   ╋   ╋   ╋   ╋   ╋   ┫\n┃                                       ┃\n┣   ╋   ╋   ╋   ╋   ╋   ╋   ╋   ╋   ╋   ┫\n┃                                       ┃\n┣   ╋   ╋   ╋   ╋   ╋   ╋   ╋   ╋   ╋   ┫\n┃                                       ┃\n┣   ╋   ╋   ╋   ╋   ╋   ╋   ╋   ╋   ╋   ┫\n┃                                       ┃\n┣   ╋   ╋   ╋   ╋   ╋   ╋   ╋   ╋   ╋   ┫\n┃                                       ┃\n┣   ╋   ╋   ╋   ╋   ╋   ╋   ╋   ╋   ╋   ┫\n┃                                       ┃\n┗━━━┻━━━┻━━━┻━━━┻━━━┻━━━┻━━━┻━━━┻━━━┻━━━┛"
        puzzlelist = []
        for i in range(10):
            puzzlelist.append(puzzle[10*i:10*i+10])
        for row in range(10):
            for column in range(9):
                if puzzlelist[row][column] != puzzlelist[row][column+1]:
                    output = output[:84*row+4*column+46] + "┃" + output[84*row+4*column+47:]
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

    #board(puzzle,blank)

    #board(puzzle,solution)


    squares = set()
    for i in range(9):
        for j in range(9):
            squares.add(frozenset({10*i+j,10*i+j+1,10*i++j+10,10*i+j+11}))


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

    regions = {frozenset(A),frozenset(B),frozenset(C),frozenset(D),frozenset(E),frozenset(F),frozenset(G),frozenset(H),frozenset(I),frozenset(J)}

    #print(regions)

    columns = set()
    for i in range(10):
        column = set()
        for j in range(10):
            column.add(10*j+i)
        columns.add(frozenset(column))
    #print(columns)

    rows = set()
    for j in range(10):
        row = set()
        for i in range(10):
            row.add(10*j+i)
        rows.add(frozenset(row))
    #print(rows)

    #NOT WORKING AS INTENDED?
    X = set()
    for region in regions:
        temp1 = set()
        temp2 = set()
        for cell in region:
            temp1.add(cell//10)
            temp2.add(cell%10)
            if len(temp1) == 2:
                doublerow = set()
                for row in rows:
                    if row & region != set():
                        doublerow |= row
                X.add(frozenset(doublerow-region))
            if len(temp2) == 2:
                doublecolumn = set()
                for column in columns:
                    if column & region != set():
                        doublecolumn |= column
                X.add(frozenset(doublecolumn-region))
    #print(X)





    two_star_containers = rows | columns | regions


    def clean(set_collection):
        cleaned = set(set_collection)
        for set1 in set_collection:
            for set2 in set_collection:
                if set1 < set2 and set1 != set2:
                    cleaned.discard(set2)
        return cleaned


    #update containers to remove x's and stars
    def update(set_collection,blank):
        new_set_collection = set()
        for member_set in set_collection:
            new = set()
            for cell in member_set:
                if blank[cell] != "0":
                    new.add(cell)
            new_set_collection.add(frozenset(new))
        return new_set_collection


    def accuracy(attempt):
        percent = 0
        for i in range(100):
            if attempt[i] == solution[i]:
                percent += 1
        return percent


    def solve(puzzle):
        blank = " " * 100
        two_star_containers = rows | columns | regions
        xcells = {1}
        while xcells != set():
            two_star_containers = update(two_star_containers,blank)
            #print("two-star containers",two_star_containers)
            # find one-plus star containers
            one_plus_star_containers = set()
            for square in squares:
                for container in two_star_containers:
                    difference = container - square
                    if difference != {}:
                        one_plus_star_containers.add(difference)
            one_plus_star_containers = clean(one_plus_star_containers)
            # place x's in cells adjacent to one-plus star containers
            xcells = set()
            for i in range(100):
                if blank[i] != "0":
                    neighborhood = {i - 11, i - 10, i - 9, i - 1, i + 1, i + 9, i + 10, i + 11}
                    if i // 10 == 0:
                        neighborhood.discard(i - 11)
                        neighborhood.discard(i - 10)
                        neighborhood.discard(i - 9)
                    if i // 10 == 9:
                        neighborhood.discard(i + 9)
                        neighborhood.discard(i + 10)
                        neighborhood.discard(i + 11)
                    if i % 10 == 0:
                        neighborhood.discard(i - 11)
                        neighborhood.discard(i - 1)
                        neighborhood.discard(i + 9)
                    if i % 10 == 9:
                        neighborhood.discard(i - 9)
                        neighborhood.discard(i + 1)
                        neighborhood.discard(i + 11)
                    for container in one_plus_star_containers:
                        if container.issubset(neighborhood):
                            xcells.add(i)
            for cell in xcells: #simplify this by making it the consequent of the above line?
                        blank = blank[:cell] + "0" + blank[cell + 1:]
            # adding stars to grid
            for container in one_plus_star_containers:
                if len(container) == 1:
                    for cell in container:
                        blank = blank[:cell] + "1" + blank[cell + 1:]
            # implementing row and column and region logic
            #NEW: Iterating more to find "chains" of one-plus, one-minus container logic
            #NOTE: no change observed in number of solved puzzles when changing number of iterations from 2 to 3
            for count in range(0,2):
                # finding one-minus star containers
                one_minus_star_containers = set()
                for Y in two_star_containers:
                    for X in one_plus_star_containers:
                        if X.issubset(Y):
                            one_minus_star_containers.add(Y - X)
                #NEW: finding more one plus star containers
                for Y in two_star_containers:
                    for X in one_minus_star_containers:
                        if X.issubset(Y):
                            one_plus_star_containers.add(Y - X)
            # finding zero-star containers
            zero_star_containers = set()
            for Z in one_minus_star_containers:
                for X in one_plus_star_containers:
                    if X.issubset(Z):
                        zero_star_containers.add(Z - X)
            #NEW: MORE ZERO-STAR CONTAINERS
            for container1 in two_star_containers:
                for container2 in two_star_containers:
                    if container1 < container2:
                        zero_star_containers.add(container2-container1)
            #NEW: ADDING CELLS IN ZERO-STAR CONTAINERS TO XCELLS SO SOLVER DOES NOT STOP EARLY IF NO ADJACENCY XCELLS FOUND
            for container in zero_star_containers:
                for cell in container:
                    xcells.add(cell)

                #NEW: FINDING MORE ZERO- AND TWO- STAR CONTAINERS BY SUBTRACTING REGIONS FROM LARGE SECTIONS
            if 1:
                uregions = update(regions,blank)
                for i in range(1,10):
                    Y = set()
                    for j in range(0,100):
                        if j//10 < i and blank[j] != 0:
                            Y.add(j)
                    intersect_region_union = set()
                    intersect_count = 0
                    subset_region_union = set()
                    subset_count = 0
                    for region in uregions:
                        if region & Y != set():
                            intersect_count += 1
                            intersect_region_union |= region
                    if intersect_count == i:
                        zero_star_containers.add(frozenset(intersect_region_union - Y))
                    if intersect_count == i+1:
                        two_star_containers.add(frozenset(intersect_region_union - Y))
                    for region in uregions:
                        if region < Y:
                            subset_count += 1
                            subset_region_union |= region
                    if subset_count == i:
                        zero_star_containers.add(frozenset(Y - subset_region_union))
                    if subset_count == i-1:
                        #print("TWO STAR CONTAINER: ",Y-subset_region_union)
                        two_star_containers.add(frozenset(Y - subset_region_union))

            if 1:
                uregions = update(regions,blank)
                for i in range(1,10):
                    Y = set()
                    for j in range(0,100):
                        if j%10 < i and blank[j] != 0:
                            Y.add(j)
                    intersect_region_union = set()
                    intersect_count = 0
                    subset_region_union = set()
                    subset_count = 0
                    for region in uregions:
                        if region & Y != set():
                            intersect_count += 1
                            intersect_region_union |= region
                    if intersect_count == i:
                        zero_star_containers.add(frozenset(intersect_region_union - Y))
                    if intersect_count == i+1:
                        two_star_containers.add(frozenset(intersect_region_union - Y))
                    for region in uregions:
                        if region < Y:
                            subset_count += 1
                            subset_region_union |= region
                    if subset_count == i:
                        zero_star_containers.add(frozenset(Y - subset_region_union))
                    if subset_count == i-1:
                        #print("TWO STAR CONTAINER: ",Y-subset_region_union)
                        two_star_containers.add(frozenset(Y - subset_region_union))


            # filling zero star containers with x's
            for container in zero_star_containers:
                for cell in container:
                    blank = blank[:cell] + "0" + blank[cell + 1:]

        board(puzzle,blank)
        acc.append(accuracy(blank))
        #print(accuracy(blank))
        if accuracy(blank) != 100:
            #print(level)
            pass



    start = time.time()
    solve(puzzle)
    finish = time.time()

    times.append(finish-start)
    print("\nsolved in "+str(finish-start)+" seconds")
#print(times)
#print(acc)

num_solved = 0
for j in acc:
    if j == 100:
        num_solved += 1
print(num_solved)

results = list(zip(times,acc))
print(results)
time_sum = 0
for entry in results:
    if entry[1] == 100:
        time_sum += entry[0]
average_time = time_sum/len(results)
print(average_time)
