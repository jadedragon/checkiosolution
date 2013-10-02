#author CT 2013-10-02
def checkio(data):
    sortedData = insertsortdata(data)
    sortedDataLength = len(sortedData)
    if sortedDataLength % 2 == 0:
        return (sortedData[sortedDataLength//2] + sortedData[sortedDataLength//2 -1])/2
    else:
        return sortedData[sortedDataLength//2]

#use insert sort
def insertsortdata(data):
    sortedData = []
    for x in data:
        if len(sortedData) == 0:
            sortedData.append(x)
        else:
            i = 0
            for y in sortedData:
                if x < y:
                    sortedData.insert(i, x)
                    break
                elif i + 1 == len(sortedData):
                    sortedData.append(x)
                    break
                i += 1
    return sortedData

if __name__ == '__main__':
    assert checkio([1, 2, 3, 4, 5]) == 3, "Sorted list"
    assert checkio([3, 1, 2, 5, 3]) == 3, "Not sorted list"
    assert checkio([1, 300, 2, 200, 1]) == 2, "It's not an average"
    assert checkio([3, 6, 20, 99, 10, 15]) == 12.5, "Even length"

#best solution of checkio
#def checkio(data):
#    sd = sorted(data)
#    N = len(data) - 1
#    a = sd[N // 2]
#    b = sd[(N + 1) // 2]
#    return (a+b) / 2
#
##These "asserts" using only for self-checking and not necessary for auto-testing
#if __name__ == '__main__':
#    assert checkio([1, 2, 3, 4, 5]) == 3, "Sorted list"
#    assert checkio([3, 1, 2, 5, 3]) == 3, "Not sorted list"
#    assert checkio([1, 300, 2, 200, 1]) == 2, "It's not an average"
#    assert checkio([3, 6, 20, 99, 10, 15]) == 12.5, "Even length"