# Mastermind

Hello! This is a short game coded in python playable in the terminal. Please follow setup instructions. 

## Setup
1. git clone the project repo
2. Activate virtual environment and download requirements
3. Create .env file
4. Obtain API Key from https://api.random.org/dashboard (or ask me very nicely for mine :p)
5. Set `API_KEY = {Your API Key}` in .env
6. Enter `python app.py` in the terminal to start the game

## Process
The goal of the project was to fulfill game requirements while having consideration for future extensions. The main design consideration were game flow and how to handle different input formats. A custom number class was created to standardize differences between the solution, a randomly generated list of ints, and the player inpuut, a string formatted number. This class would likely be useful in future project extensions involving database models. 
Potential enhancements would be allowing further player customization such as allowing the player to set API parameters such as length of the solution int or disallowing repeat numbers in the solution. The player could also potentially set the max number of guesses.
Major future enhancements would be elevating the project out of the terminal, potentially using Flask, Java/TypeScript, React, and PostgreSQL 
A front end interface would require editing the DOM and incorporating event listeners for user interaction and input. CSS styles and flavor text could be utilized to enhance user experience and add character.
