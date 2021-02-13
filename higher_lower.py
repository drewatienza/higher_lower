from random import randint
from art import logo, vs
from data import data_set


def get_random_data():
    data_info = data_set[randint(0, len(data_set))]
    return data_info


def play_game():
    first = get_random_data()
    first_followers = first['follower_count']
    win_streak = 0
    game_over = False
    while not game_over:
        second = get_random_data()
        while second == first:
            second = get_random_data()
        second_followers = second['follower_count']

        print(logo)
        print(f'Compare A: {first["name"]}, {first["description"]}, from {first["country"]}')
        print(first_followers)
        print(vs)
        print(f'Against B: {second["name"]}, {second["description"]}, from {second["country"]}')
        print(second_followers)
        choice = input(print("Who has more followers?  Type 'A' or 'B': \n"))
        if choice.upper() == 'A':
            if first_followers > second_followers:
                first = second
                win_streak += 1
            elif first_followers < second_followers:
                print(f'Sorry, that is wrong.  Your final score is: {win_streak}.')
                game_over = True
            else:
                print('They have the same amount of followers.  No winner.')
        elif choice.upper() == 'B':
            if second_followers > first_followers:
                first = second
                win_streak += 1
            elif second_followers < first_followers:
                print(f'Sorry, that is wrong.  Your final score is: {win_streak}.')
                game_over = True
            else:
                print('They have the same amount of followers.  No winner.')
        else:
            print('That was not a valid input.')



play_game()
