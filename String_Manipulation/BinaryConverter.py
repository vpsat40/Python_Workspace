#
#     Description: For this challenge you will be converting a number from binary to decimal.
#     Binary Converter: Have the function BinaryConverter(str) return the decimal form of the binary value.
#     For example: if 101 is passed return 5, or if 1000 is passed return 8.
#
#     Examples
#     Input: "100101"
#     Output: 37

#     Input: "011"
#     Output: 3

#     Tags: math fundamentals
#
#
def ConvertBinary1(bin):
    res = 0
    exp = 0

    for ch in bin[::-1]:
        if ch == '1':
            res += 2**exp
        exp += 1
    return res


def ConvertBinary(bin):
    res = 0
    exp = 0

    for ch in bin[::-1]:
        if ch == '1':
            res += pow(2, exp)
        exp += 1
    
    return res



# Driver code
if __name__ == "__main__":
    print(ConvertBinary("100101"))
    print(ConvertBinary("101"))
    print(ConvertBinary("1000"))
    print(ConvertBinary("011"))
    print('---------------')
    print(ConvertBinary1("100101"))
    print(ConvertBinary1("101"))
    print(ConvertBinary1("1000"))
    print(ConvertBinary1("011"))

