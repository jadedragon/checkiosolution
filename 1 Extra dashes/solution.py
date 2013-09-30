#author CT 2013-09-30
def checkio(line):
    result = ""
    lines = line.split("-")
    for x in lines:
        if x != "":
            if result != "":
                result += "-" + x
            else:
                #first time don't append the "-"
                result += x
    return result

if __name__ == '__main__':
    assert checkio('I---like--python') == "I-like-python", 'Example'