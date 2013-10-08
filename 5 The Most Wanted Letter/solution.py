#author CT 2013-10-08
def checkio(text):
    # get lower case letter count
    dic = {}
    for x in text:
        if x.islower():
            if dic.get(x) is None:
                dic[x] = 1
            else:
                dic[x] += 1

    # keep the most wanted letter in dic, pop others
    wantedKey = ""
    wantedVal = 0
    for key in dic:
        if wantedKey == "":
            wantedKey = key
            wantedVal = dic[key]
        else:
            if dic[key] > wantedVal:
                wantedKey = key
                wantedVal = dic[key]
            elif dic[key] == wantedVal:
                if key < wantedKey:
                    wantedKey = key
                    wantedVal = dic[key]
    return wantedKey

if __name__ == '__main__':
    assert checkio("Hello World!") == "l", "Hello test"
    assert checkio("How do you do?") == "o", "O is most wanted"
    assert checkio("One") == "e", "All letter only once."