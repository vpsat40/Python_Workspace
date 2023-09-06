from random import shuffle
from random import randint

def generateWinningNumbers(numbers):

    for games in range(1, 10):
        my_nums = numbers
        shuffle(my_nums)
        curr_game_nums = []

        for num in my_nums:
            if num > 45:
                num = randint(31, 45)
            
            if num not in curr_game_nums:
                curr_game_nums.append(num)
            
            if len(curr_game_nums) > 5:
                break
        
        print(f'Game {games} numbers are - {curr_game_nums}')

if __name__ == "__main__":
    my_favourite_numbers = [28, 3, 19, 79, 10, 5, 19, 87, 23, 12, 20, 13, 30, 9, 20, 19, 23, 10, 20, 12, 3, 5, 20, 22, 13, 11, 20, 17, 4, 2, 20, 14, 18, 2, 19, 76]

    print(f'Generate winning numbers :D \n\n')
    generateWinningNumbers(my_favourite_numbers)