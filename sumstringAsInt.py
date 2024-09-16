def parse_int(string):
    number = 0
    first_twenty = {"zero": 0, "one": 1, "two": 2, "three": 3, "four":4, "five": 5, "six": 6, "seven":7, "eight": 8, "nine": 9, "ten": 10, "eleven": 11, "twelve": 12, "thirteen":13, "fourteen": 14, "fifteen":15, "sixteen": 16, "seventeen": 17, "eighteen": 18, "nineteen": 19, "twenty": 20 }
    tenths = {"thirty": 30, "forty": 40, "fifty": 50, "sixty":60, "seventy": 70, "eighty": 80, "ninety": 90}
    multi = ["hundred", "thousand"]
    if string == "one million":
        return 1000000
    dashless = string.replace("-", " ")
    lst = dashless.split(" ")
    if "and" in lst:
        lst.remove("and")
    if 'and' in lst:
        lst.remove('and')
    print(lst)
    ru = [first_twenty.get(word, word) for word in lst]
    ru = [tenths.get(word, word) for word in ru]
    print(ru)
    if len(ru) == 1:
        return ru[0]
    if len(ru) > 1:
        number = 0
        rev = ru[::-1]
        mp = 1
        for i in range(len(rev)):
            if rev[i] not in multi:
                number = number + rev[i] * mp
                print(number)
            if rev[i] in multi and rev[i] == multi[0]:
                mp = mp * 100
            if rev[i] in multi and rev[i] == multi[1]:
                mp = 1000
        
    return number