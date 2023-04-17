

def isPowerofTwo(num):
    if (num & num-1 == 0):
        return True
    else:
        return False
    
def isPowerofThree(num):
    x=1
    threes = set
    
    while x < num:
        x = x * 3
        threes.add(x)
    
    if num in threes:
        return True
    else:
        return False
    
def isPowerofFour(num):
    x = 1
    fours = set()

    while (x < num):
        x = x * 4
        fours.add(x)
    
    if num in fours:
        return True
    else:
        return False


if __name__ == "__main__":

    while(1):
        num = input('\nEnter number to check or X to exit - ')

        if num.isdigit(): # and (int(num) > 0):
            # Check here            
            if(isPowerofTwo(int(num))):
                print('{} is a power of 2\n'.format(num))
            else:
                print('{} is not a power of 2\n'.format(num))
            if(isPowerofFour(int(num))):
                print('{} is a power of 4\n'.format(num))
            else:
                print('{} is not a power of 4\n'.format(num))
        elif num == 'X':
            break
        else:
            print('Please enter a valid number')
    
    print('-------Thank You--------------\n')
