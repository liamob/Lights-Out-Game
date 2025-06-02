from numpy import *
from appJar import gui


def get_ai_solution(bmat):
    amat = [[1,1,0,1,0,0,0,0,0], [1,1,1,0,1,0,0,0,0], [0,1,1,0,0,1,0,0,0], [1,0,0,1,1,0,1,0,0], [0,1,0,1,1,1,0,1,0], [0,0,1,0,1,1,0,0,1],[0,0,0,1,0,0,1,1,0],[0,0,0,0,1,0,1,1,1], [0,0,0,0,0,1,0,1,1]]
    ainv = [[1,0,1,0,0,1,1,1,0], [0,0,0,0,1,0,1,1,1], [1,0,1,1,0,0,0,1,1], [0,0,1,0,1,1,0,0,1], [0,1,0,1,1,1,0,1,0], [1,0,0,1,1,0,1,0,0], [1,1,0,0,0,1,1,0,1], [1,1,1,0,1,0,0,0,0], [0,1,1,1,0,0,1,0,1]]

    x = 0
    z = 0
    xmat = [[0],[0],[0],[0],[0],[0],[0],[0],[0]]
    while x < 9:
        while z < 9:
                xmat[x][0] = ((xmat[x][0] + (ainv[x][z] * bmat[z][0])) % 2)
                z = z + 1
        z = 0
        x = x + 1


    solution = "row 1: " + str(xmat[0][0]) + " " + str(xmat[1][0]) + " " + str(xmat[2][0]) + "\n" + "row 2: " + str(xmat[3][0]) + " " + str(xmat[4][0]) + " " + str(xmat[5][0]) + "\n" + "row 3: " + str(xmat[6][0]) + " " + str(xmat[7][0]) + " " + str(xmat[8][0])

    solution = "AI solution is press the following buttons (one is \"press button\" and zero is \"dont press\"): \n" + solution
    return solution

bmat = [[0],[1],[0],[1],[1],[0],[0],[1],[1]]
print(get_ai_solution(bmat))
