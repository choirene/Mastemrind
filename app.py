import requests
import json
import os
from dotenv import load_dotenv

load_dotenv()

def generate_random_integers(api_key, num, min_val, max_val, replacement):
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
        "id": 42,
        "replacement": replacement,
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



def game_setup():
    print("Welcome to mastermind! Please try guessing the 4 digit number.")
    api_key = os.getenv("API_KEY")
    if api_key is None:
        print("API key not found. Please set it in the .env file.")
    else:
        num = 4  # Number of random integers to generate
        min_val = 0  # Minimum value of the random integers
        max_val = 7  # Maximum value of the random integers
        replacement = True # True = lets nums repeat. False = nums will not repeat

        int_solution = generate_random_integers(api_key, num, min_val, max_val, replacement)

        string_solution = ''
        for num in solution:
            string_solution += str(num)

        guesses = 0
        player_turn(string_solution, guesses)

def player_turn(solution, guesses):
    player_guess = input("Guess a number \n")

    while not validate_player_guess(player_guess):
        player_guess = input("Guess a valid 4 digit number. \n")
    

    if player_guess == solution:
        game_end(True)
    elif guesses == 10:
        print(f"The number was {solution}")
        game_end(False)
    else:
        (correct_nums, correct_places) = judge_guess(solution, player_guess)
        print(f"You have guessed {correct_nums} numbers correctly. {correct_places} are in the correct place.")
        guesses += 1
        print("~~~~~~")
        player_turn(solution, guesses)

def validate_player_guess(guess):
    return ((len(guess) == 4) and (guess.isnumeric()))

def judge_guess(solution, player_guess):
    correct_nums = 0
    correct_places = 0
    
    for num in range(len(solution)):
        if solution[num] == player_guess[num]:
            correct_places += 1
        if player_guess[num] in solution:
            correct_nums += 1
    return(correct_nums, correct_places)

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
# issues : repeat numbers in guess and solution.. player guess format.. grammar changes for plural..
# edge case -> if a player guesses an int twice -> wrong # of correct digits