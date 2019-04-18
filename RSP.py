"""This program plays a game of Rock, Paper, Scissors between two Players,
and reports both Player's scores each round."""

import random

import time


def print_pause(text):
    print(text)
    time.sleep(1.5)


# Validation of the user's input
def valid_input(message, options, invalid):
    while True:
        response = input(message).lower().strip()
        if response in options:
            return response
        else:
            print_pause(invalid)


def message_for_user(list):
    message = "Please enter"
    invalid = "Invalid input! Try again."
    # Items from the list are being added to the message
    for item in list:
        if item != list[-1]:
            message += f" '{item}',"
        else:
            message += f" or '{item}': "
    return message, invalid


def check_positive_int():
    while True:
        response = input("Please enter the winning score (as a number!): ")
        print("")
        if response.isdigit() is True:
            if int(response) > 0:
                return int(response)
        else:
            print_pause("Only a number greater than zero is accepted.")


class Player:

    def __init__(self):
        self.round = 1

    def move(self, moves):
        return 'rock'

    def learn(self, human_move, co3mputer_move):
        pass


class RandomPlayer(Player):

    def move(self, moves):
        return random.choice(moves)

    def learn(self, human_move, computer_move):
        pass


class HumanPlayer(Player):

    def move(self, moves):
        print_pause("\tWhat's your move?")
        # User's input is validated
        response = valid_input(f"\t{message_for_user(moves)[0]}", moves,
                               f"\n\t{message_for_user(moves)[1]}")
        return response

    def learn(self, human_move, computer_move):
        pass


class ReflectPlayer(Player):

    def move(self, moves):
        # The first move is chosen randomly
        if self.round == 1:
            return random.choice(moves)
        # all subsequent moves repeat previous moves of the opponent
        else:
            return self.move_next

    # The player memorizes the previous move of the opponent
    def learn(self, move_human, move_computer):
        self.move_next = move_human


class CyclePlayer(Player):

    def move(self, moves):
        if self.round <= len(moves):
            return moves[self.round - 1]
        else:
            self.round = 1
            return moves[self.round - 1]

    def learn(self, move_human, move_computer):
        pass


class Game:

    def __init__(self, human, computer):
        self.human = human
        self.computer = computer
        self.score_human = 0
        self.score_computer = 0
        self.round = 0

    def intro(self):
        print_pause("\nWelcome to "
                    "the Rock-Scissors-Paper-Lizard-Spock game!\n")
        print_pause("Game start!\n")
        print_pause("The game has the following rules:\n")
        print_pause(" - rock beats scissors and lizard")
        print_pause(" - scissors beat paper and lizard")
        print_pause(" - paper beats rock and spock")
        print_pause(" - lizard beats paper and spock")
        print_pause(" - spock beats rock and scissors\n")
        print_pause("But it's up to you, what's the total score must be "
                    "in order to win the game.")

    def game_body(self, moves):
        # The human player is asked how big score there must be in order to win
        # Afterwards, it is checked, whether the response is a positive integer
        self.win_score = check_positive_int()
        while (self.score_human < self.win_score and
                self.score_computer < self.win_score):
            self.round += 1
            print_pause(f"Round {self.round}:\n")
            self.play_round(moves)

    def beats(self, one, two):
        return ((one == 'rock' and (two == 'scissors' or two == 'lizard')) or
                (one == 'scissors' and (two == 'paper' or two == 'lizard')) or
                (one == 'paper' and (two == 'rock' or two == 'spock')) or
                (one == 'lizard' and (two == 'paper' or two == 'spock')) or
                (one == 'spock' and (two == 'rock' or two == 'scissors')))

    def play_round(self, moves):
        move_human = self.human.move(moves)
        move_computer = self.computer.move(moves)
        print_pause(f"\n\tYour move: {move_human}  "
                    f"Computer's move: {move_computer}\n")
        # checks whose move is the winning one
        if self.beats(move_human, move_computer) is True:
            self.score_human += 1
            print_pause("\tYou won this round!!\n")
        elif self.beats(move_computer, move_human) is True:
            self.score_computer += 1
            print_pause("\tYou lost this round...\n")
        else:
            print_pause("\tTie!\n")
        # displays the total score of players
        print_pause(f"\tYour score: {self.score_human}  "
                    f"Computer's score: {self.score_computer}\n")
        self.computer.learn(move_human, move_computer)
        self.computer.round += 1

    def result(self):
        # if the human player scores the necessary number of points, he wins.
        # Otherwise the computer does.
        if self.score_human == self.win_score:
            print_pause("Congratulations! You've won the game!!!\n")
        else:
            print_pause("Unfortunately, you've lost the game...\n")

    def ask_play_again(self, play_again_list):
        # After the game is over the human player is asked
        # whether he wants to play again
        print_pause("Would you like to play again?")
        # User's input is validated
        response = valid_input(message_for_user(play_again_list)[0],
                               play_again_list,
                               message_for_user(play_again_list)[1])
        if response == 'yes':
            new_game()
        else:
            print_pause("\nBye!!")

    def play_game(self, moves, play_again_list):
        self.intro()
        self.game_body(moves)
        self.result()
        self.ask_play_again(play_again_list)


def new_game():
    moves = ['rock', 'paper', 'scissors', 'lizard', 'spock']
    play_again_list = ["yes", "no"]
    computer_players = [Player(), RandomPlayer(),
                        ReflectPlayer(), CyclePlayer()]
    game = Game(HumanPlayer(), random.choice(computer_players))
    game.play_game(moves, play_again_list)


if __name__ == '__main__':
    new_game()
