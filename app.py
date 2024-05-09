import requests
import json
import os
from dotenv import load_dotenv

# # response = requests.get("https://www.random.org/integers/?num=4&min=0&max=7&col=1&base=10&format=plain&rnd=new")
# url = "https://api.random.org/json-rpc/4/invoke"
# params = {
#     {
#     "jsonrpc": "2.0",
#     "method": "generateIntegers",
#     "params": {
#         "apiKey": "6b1e65b9-4186-45c2-8981-b77a9842c4f0",
#         "n": 6,
#         "min": 1,
#         "max": 6,
#         "replacement": True
#     },
#     "id": 42
# }
# }
# reponse = requests.get(url, params)
# print(response.status_code)
# print(response)

load_dotenv()

def generate_random_integers(api_key, num, min_val, max_val):
    url = 'https://api.random.org/json-rpc/4/invoke'
    headers = {'content-type': 'application/json'}

    params = {
        "jsonrpc": "2.0",
        "method": "generateIntegers",
        "params": {
            "apiKey": api_key,
            "n": num,
            "min": min_val,
            "max": max_val,
            "base": 10,
        },
        "id": 42
    }

    response = requests.post(url, data=json.dumps(params), headers=headers)
    
    if response.status_code == 200:
        result = response.json()
        if 'error' in result:
            print("Error:", result['error']['message'])
        else:
            return result['result']['random']['data']
    else:
        print("Failed to connect. Status code:", response.status_code)


# api_key = os.getenv("API_KEY")
# if api_key is None:
#     print("API key not found. Please set it in the .env file.")
# else:
#     num = 4  # Number of random integers to generate
#     min_val = 0  # Minimum value of the random integers
#     max_val = 7  # Maximum value of the random integers

#     random_integers = generate_random_integers(api_key, num, min_val, max_val)
#     print("Generated Random Integers:", random_integers)




def game_setup():
    print("Welcome to mastermind! Please try guessing the 4 digit number.")
    api_key = os.getenv("API_KEY")
    if api_key is None:
        print("API key not found. Please set it in the .env file.")
    else:
        num = 4  # Number of random integers to generate
        min_val = 0  # Minimum value of the random integers
        max_val = 7  # Maximum value of the random integers

        goal = generate_random_integers(api_key, num, min_val, max_val)
        print(goal)

    guesses = 0
    player_turn(goal, guesses)

def player_turn(goal, guesses):
    player_guess = input("Guess a number \n")

    while not validate_player_guess(player_guess):
        player_guess = input("Guess a valid 4 digit number. \n")
    
    # do try/except?

    # player_guess = int(player_guess)
    str_goal = ''
    for num in goal:
        str_goal += str(num)

    print(str_goal)
    if player_guess == str_goal:
        game_end(True)
    elif guesses == 10:
        print(f"The number was {str_goal}")
        game_end(False)
    else:
        judge_list = judge_guess(str_goal, player_guess)
        print(f"You have guessed {judge_list[0]} numbers correctly. {judge_list[1]} are in the correct place.")
        guesses += 1
        print("~~~~~~")
        player_turn(goal,guesses)

def validate_player_guess(guess):
    return ((len(guess) == 4) and (guess.isnumeric()))

def judge_guess(goal, player_guess):
    correct_nums = 0
    correct_places = 0
    
    for num in range(len(goal)):
        if goal[num] == player_guess[num]:
            correct_places += 1
        if player_guess[num] in goal:
            correct_nums += 1
    return[correct_nums, correct_places]    

def game_end(player_win):
    if player_win:
        print("Congrats!")
    else: 
        print("Better luck next time.")
    play_again = input("Want to play again?")
    if play_again == "Y":
        game_setup()
    else:
        print("Thanks for playing!")


game_setup()
# issues : repeat numbers in guess and goal.. player guess format.. grammar changes for plural..