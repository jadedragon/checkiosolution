#author CT 2013-10-09
FIRST_TEN = ["zero", "one", "two", "three", "four", "five", "six", "seven",
             "eight", "nine"]
SECOND_TEN = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen",
              "sixteen", "seventeen", "eighteen", "nineteen"]
OTHER_TENS = ["twenty", "thirty", "forty", "fifty", "sixty", "seventy",
              "eighty", "ninety"]
HUNDRED = "hundred"

def checkio(number):
    result = ""
    if number // 100 != 0:
        result += FIRST_TEN[number // 100] + " " + HUNDRED + " "

    number = number % 100

    if number < 10:
        if number != 0:
            result += FIRST_TEN[number]
        elif result == "":
            result += FIRST_TEN[number]
    elif number < 20:
        result += SECOND_TEN[number % 10]
    else:
        result += OTHER_TENS[number // 10 - 2]
        if number % 10 != 0:
            result += " " + FIRST_TEN[number % 10]

    return result.strip()

if __name__ == '__main__':
    assert checkio(4) == 'four', "1st example"
    assert checkio(133) == 'one hundred thirty three', "2nd example"
    assert checkio(12) == 'twelve', "3rd example"
    assert checkio(101) == 'one hundred one', "4th example"
    assert checkio(212) == 'two hundred twelve', "5th example"
    assert checkio(40) == 'forty', "6th example"
    assert checkio(999) == 'nine hundred ninety nine', "7th example"
    assert checkio(0) == 'zero', "8th example"
    assert checkio(100) == 'one hundred', "9th example"