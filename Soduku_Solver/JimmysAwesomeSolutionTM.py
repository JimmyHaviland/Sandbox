from test_board import print_board

def solve(puzzle):

    solution = []
    print("old puzzle:")
    print_board(puzzle)

    for i in puzzle:
        solution.append(i)

    for x in solution:
        for i,y in enumerate(x):
            #print(str(i) + "," + str(y))
            if y == 0:
                x[i] = "*"





    print("right now just a copy....")

    print("solution:")
    print_board(solution)
    return solution
