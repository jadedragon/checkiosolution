#author CT 2013-10-01
def checkio(data):
    #get each element counts
    countDic = {}
    for i in data:
        if countDic.get(i) is None:
            countDic[i] = 1
        else:
            countDic[i] += 1
    #base the countDic get the result
    resultList = []
    for i in data:
        if countDic[i] > 1:
            resultList.append(i)
    return resultList

if __name__ == "__main__":
    assert isinstance(checkio([1]), list), "The result must be a list"
    assert checkio([1, 2, 3, 1, 3]) == [1, 3, 1, 3], "1st example"
    assert checkio([1, 2, 3, 4, 5]) == [], "2nd example"
    assert checkio([5, 5, 5, 5, 5]) == [5, 5, 5, 5, 5], "3rd example"
