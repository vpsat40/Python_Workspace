from random import shuffle
from random import randint

def generateWinningNumbers(game_numbers, game_count, gametype):

    pb = False

    if gametype == 1:
        max_num = 35
        game_len = 7
        pb = True
        print(f'Generating Powerball numbers.\n MaxNum {max_num}, Game Length {game_len} \n')
    elif gametype == 2:
        max_num = 45
        game_len = 6
        print('Generating Tattslotto numbers.\n MaxNum {max_num}, Game Length {game_len} \n')
    elif gametype == 3:
        max_num = 47
        game_len = 7
        print(f'Generating Ozlotto numbers.\n MaxNum {max_num}, Game Length {game_len} \n')

    for games in range(1, game_count+1):
        my_nums = game_numbers
        shuffle(my_nums)
        curr_game_nums = []

        for num in my_nums:
            if num > max_num:
                num = randint(31, max_num)
            
            if num not in curr_game_nums:
                curr_game_nums.append(num)
            
            if len(curr_game_nums) >= game_len:
                break
        
        print(f'Game {games} numbers are - {curr_game_nums}')
    
    if(pb == True):
        my_pbs = game_numbers
        shuffle(my_pbs)
        pb_nums = []

        for num in my_pbs:
            if num > 20:
                num = randint(1, 20)
            
            pb_nums.append(num)
                
            if len(pb_nums) >= game_count:
                break
        print(f'Powerball numbers are - {pb_nums}')


if __name__ == "__main__":
    my_favourite_numbers = [28, 3, 19, 79, 10, 5, 19, 87, 23, 12, 20, 13, 30, 9, 20, 19, 23, 10, 20, 12, 3, 5, 20, 22, 13, 11, 20, 17, 4, 2, 20, 14, 18, 2, 19, 76]
    game_count = 9
    games = ['PowerBall', 'Tattslotto', 'Ozlotto']

    while(1):
        print('Games supported - 1. PowerBall, 2. Tattslotto, 3. Ozlotto')
        game = input('\nEnter game # you want to play or check or X to exit - ')

        if game.isdigit() and (int(game) > 0 and int(game) < 4):
            # Check here            
            if(int(game) == 1):
                print('Generating winning numbers for Powerball')
                generateWinningNumbers(my_favourite_numbers, game_count, int(game))
            elif(int(game) == 2):
                print('Generating winning numbers for Tattslotto')
                generateWinningNumbers(my_favourite_numbers, game_count, int(game))
            elif(int(game) == 3):
                print('Generating winning numbers for Ozlotto')
                generateWinningNumbers(my_favourite_numbers, game_count, int(game))
        elif game == 'X':
            break
        else:
            print('Please enter a valid number')

    print('-------Thank You--------------\n')