#author CT 2013-10-10
import math
def checkio(game_result):
    if checkWin(game_result, "X"):
        return "X"
    if checkWin(game_result, "O"):
        return "O"
    return "D"

def checkWin(game_result, item):
    # build item position array
    itemPos = []
    i = 0
    for str in game_result:
        j = 0
        for s in str:
           if s == item:
               itemPos.append([j, i])
           j += 1
        i += 1

    if len(itemPos) < 3:
        return False

    checkFlag = False

    # make fixed length array
    for arr in comb(itemPos, 3):
        distanceAB = calDistance(arr[0], arr[1])
        distanceBC = calDistance(arr[1], arr[2])
        distanceAC = calDistance(arr[0], arr[2])

        if distanceAB + distanceBC == distanceAC:
            checkFlag = True
            break

    return checkFlag

def calDistance(cor1, cor2):
    cor1x = cor1[0]
    cor1y = cor1[1]
    cor2x = cor2[0]
    cor2y = cor2[1]
    return math.sqrt((cor1x-cor2x)**2+(cor1y-cor2y)**2)

# copy from Raymond Hettinger
def comb(items, n=None):
    if n is None:
        n = len(items)
    for i in range(len(items)):
        v = items[i:i+1]
        if n == 1:
            yield v
        else:
            rest = items[i+1:]
            for c in comb(rest, n-1):
                yield v + c


if __name__ == '__main__':
    assert checkio([
        "X.O",
        "XX.",
        "XOO"]) == "X", "Xs wins"
    assert checkio([
        "OO.",
        "XOX",
        "XOX"]) == "O", "Os wins"
    assert checkio([
        "OOX",
        "XXO",
        "OXX"]) == "D", "Draw"