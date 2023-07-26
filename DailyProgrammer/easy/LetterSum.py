def LetterSum(str):
    sum = lambda s: sum(([ord(c)-96 for c in str]))

    return sum


if __name__ == "__main__":
    print(LetterSum(''))
    print(LetterSum('a'))
    print(LetterSum('z'))
    print(LetterSum('cab'))
    print(LetterSum('excellent'))
    print(LetterSum('microspectrophotometries'))    