# Rock-Scissors-Paper Game
The program plays an extended text-based version of the classical Rock-Paper-Scissors game with two more additional characters - lizard and spock.
 
The game containes four computer player classes that follow various different strategies, as well as a human player class that lets a human play the game against the computer.

Each game is played by two players - the human player and one of the computer players.
In a single round of the game, each player secretly chooses one of five moves — rock, paper, scissors, lizard, or spock.
Then, players reveal their moves at the same time. If both players picked the same move, there is no winner.

At the beginning of the game the human player has to choose how many points should a player receive in order to win the entire game.
After one of the players wins, there is an option to play again.

Detailed instructions how to play are provided within the game prior to start.

The computer player strategies are the following (the _strategy is chosen randomly_ at the beginning of the game):

* computer who always chooses _rock_
* computer who chooses a _random_ move
* computer who _cycles_ through rock, then paper, scissors, lizard, spock then back to rock
* computer who always _copies_ its opponent's last move

This project was developed through the Udacity Intro to Programming Nanodegree.

## Used Programming skills
* Foundations of Python
  - Modules
  - Functions
  - `for` and `while` loops
  - Conditional statements
  - List and string methods
* Object-Oriented Programming
* Code refactoring
* Following PEP 8 style guidelines

## Quickstart
* Clone the project and cd into it in your terminal
* Run `python rsp.py` or `python3 rsp.py` and follow the instruction on the screen
  - On **Windows** run `winpty python rsp.py` in order for the program to run correctly
* _Note:_ The project runs on python 3
