from random import randint


class Board:
    def __init__(self):
        self._header = [[' ', 'A', 'B', 'C']]
        self._board = [[i + 1] + ["_"] * 3 for i in range(3)]
        self._table = self._header + self._board
        self._move = 1
        self._row = 0
        self._column = 0
        self._spot = '_'

    def display(self):
        for row in self._table:
            for tile in row:
                print(tile, end=" ")
            print()

    def make_move(self, move, player):
        if player.is_human:
            if move[0] == 'A':
                self._column = 1
            elif move[0] == 'B':
                self._column = 2
            elif move[0] == 'C':
                self._column = 3
            else:
                print("You have entered an incorrect column")
                return False
            if 1 <= int(move[1]) <= 3:
                self._row = int(move[1])
                self._spot = self._table[self._row][self._column]
            else:
                print("You have entered an incorrect row")
                return False
        else:
            self._spot = self.random_move()

        while not self.check_spot():
            if not player.is_human:
                self._spot = self.random_move()
            else:
                print("You have not selected an available spot")
                return False

        self._table[self._row][self._column] = player.symbol
        return True

    def check_spot(self):
        if self._spot == '_':
            return True
        else:
            return False

    def is_full(self):
        for i in range(4):
            if '_' in self._table[i]:
                return False
        return True

    def random_move(self):
        self._column = randint(1, 3)
        self._row = randint(1, 3)
        return self._table[self._row][self._column]

    def check_win(self, player):
        for row in self._table:
            if row[1] == player.symbol and row[2] == player.symbol and row[3] == player.symbol:
                return True, player
        for i in range(1, 4):
            col = [item[i] for item in self._table]
            if col[1] == player.symbol and col[2] == player.symbol and col[3] == player.symbol:
                return True, player
        if (self._table[1][1] == player.symbol and self._table[2][2] == player.symbol and
                self._table[3][3] == player.symbol):
            return True, player
        elif (self._table[1][3] == player.symbol and self._table[2][2] == player.symbol and
                self._table[3][1] == player.symbol):
            return True, player
        else:
            return False, player


class Player:
    def __init__(self, name, symbol, is_human):
        self.name = name
        self.symbol = symbol
        self.is_human = is_human


def main():
    move = 1
    selection = input("Let's play a game of tic-tac-toe.\nPlease select 1 for game against computer "
                      "or 2 for two player game.\n")
    if selection == '1':
        player1 = Player(input("Enter name of the player 1\n").title(), "X", True)
        player2 = Player("Computer", "O", False)
    else:
        player1 = Player(input("Enter name of the player 1\n").title(), "X", True)
        player2 = Player(input("Enter name of the player 2\n").title(), "O", True)
    board = Board()
    board.display()
    while not board.is_full():
        if move % 2 != 0:
            choice = input(f"{player1.name} please select a row and column for your move (e.g. B2)\n").upper()
            if board.make_move(choice, player1):
                move += 1
                win = board.check_win(player1)
        else:
            if player2.is_human:
                choice = input(f"{player2.name} please select a row and column for your move (e.g. B2)\n").upper()
                if board.make_move(choice, player2):
                    move += 1
                    win = board.check_win(player2)
            else:
                print("Computer to play")
                if board.make_move('computer', player2):
                    move += 1
                    win = board.check_win(player2)
        board.display()
        if win[0]:
            print(f"{win[1].name} has won!")
            break

    if input("Would you like to play again? (y/n)").upper() == "Y":
        main()
    else:
        print("Bye Bye!")


if __name__ == '__main__':
    main()
