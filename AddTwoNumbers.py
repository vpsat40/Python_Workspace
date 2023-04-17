# /*
#  * AddTwoNumbers.cpp
#  *
#  *  Created on: Apr 21, 2021
#  *      Author: satish.vodapally
#  */
# /*
#  *
#  * You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order,
#  * and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.
#  *
#  * You may assume the two numbers do not contain any leading zero, except the number 0 itself.
#  *
#  * Example 1:
#  * Input: l1 = [2,4,3], l2 = [5,6,4]
#  * Output: [7,0,8]
#  * Explanation: 342 + 465 = 807.
#  *
#  * Example 2:
#  * Input: l1 = [0], l2 = [0]
#  * Output: [0]
#  *
#  * Example 3:
#  * Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
#  * Output: [8,9,9,9,0,0,0,1]
#  * Explanation: 9999999+9999 = 10009998
#  *
#  * Constraints:
#  * The number of nodes in each linked list is in the range [1, 100].
#  * 0 <= Node.val <= 9
#  * It is guaranteed that the list represents a number that does not have leading zeros.
#  *
#  */
import itertools

def AddTwoNumbers(n1, n2):
    carry = 0
    res1 = []
    res = []

    # Following for loop will work only for lists of equal sizes
    # Iterate two lists of same size in reverse using zip function
    for op3, op4 in zip(n1[::-1],n2[::-1]):
        sum = op3 + op4 + carry
        carry = sum // 10       # Use '//' for floor division
        
        res1.append(sum%10)
    if carry:
        res1.append(carry)
    
    print(res1)


    # Iterate two lists of different sizes in reverse using (itertools.zip_longest) function
    # Use fillvalue to replace NoneType variables to 0
    carry = 0
    for op1, op2 in itertools.zip_longest(n1[::-1], n2[::-1], fillvalue=0):
        sum = op1 + op2 + carry
        carry = sum // 10

        res.append(sum%10)
    
    if carry:
        res.append(carry)
    
    return res


if __name__ == "__main__":
    l1 = [2,4,3]
    l2 = [5,6,4]

    a1 = [0]
    a2 = [0]

    b1 = [9,9,9,9,9,9,9]
    b2 = [9,9,9,9]
    
    # print(AddTwoNumbers(l1, l2))
    # print(AddTwoNumbers(a1, a2))
    print(AddTwoNumbers(b1, b2))



