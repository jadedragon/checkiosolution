#author CT 2013-10-07
import re
def checkio(data):
    pattern = re.compile(r'(?=.*[A-Z])(?=.*[a-z])(?=.*[0-9])[a-zA-Z0-9]{10,}')
    match = pattern.match(data)
    if match is not None:
        return True
    return False

if __name__ == '__main__':
    assert checkio('A1213pokl') == False, "1st example"
    assert checkio('bAse730onE4') == True, "2nd example"
    assert checkio('asasasasasasasaas') == False, "3rd example"
    assert checkio('QWERTYqwerty') == False, "4th example"
    assert checkio('123456123456') == False, "5th example"
    assert checkio('QwErTy911poqqqq') == True, "6th example"
