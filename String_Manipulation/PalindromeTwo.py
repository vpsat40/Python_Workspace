# /*
#     Title: Palindrome Two     Difficulty: Medium    Solutions: 13431    Maximum Score: 10

#     For this challenge you will be determining if a string is a palindrome.
#     Have the function PalindromeTwo(str) take the str parameter being passed and return the string true if the parameter is a palindrome,
#     (the string is the same forward as it is backward) otherwise return the string false.

#     The parameter entered may have punctuation and symbols but they should not affect whether the string is in fact a palindrome.

#     For example: "Anne, I vote more cars race Rome-to-Vienna" should return true.

#     Examples
#     Input: "Noel - sees Leon"
#     Output: true

#     Input: "A war at Tarawa!"
#     Output: true

#     Tags: string manipulation searching

# */

def PalindromeTwo(input):
    res = False

    mystr = str(input)
    mystr.replace(' ', '')
    for c in mystr:
        

    return res

if __name__ == "__main__":
    print(PalindromeTwo('Noel - sees Leon'))
    print(PalindromeTwo('A war at Tarawa!'))
    print(PalindromeTwo('Anne, I vote more cars race Rome-to-Vienna'))