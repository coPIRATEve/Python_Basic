class Cell:
    def __init__(self):
        self.value = ' '


class Board:
    def __init__(self):
        self.cells = [Cell() for _ in range(9)]

    def display(self):
        for i in range(0, 9, 3):
            print(f'{self.cells[i].value}|{self.cells[i + 1].value}|{self.cells[i + 2].value}')
            if i < 6:
                print('-+-+-')

    def is_full(self):
        return all(cell.value != ' ' for cell in self.cells)

    def check_win(self, player):
        win_patterns = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]
        for pattern in win_patterns:
            if all(self.cells[i].value == player.symbol for i in pattern):
                return True
        return False

    def make_move(self, cell_num, player):
        if 0 <= cell_num < 9 and self.cells[cell_num].value == ' ':
            self.cells[cell_num].value = player.symbol
            return True
        else:
            return False


class Player:
    def __init__(self, name, symbol):
        self.name = name
        self.symbol = symbol


class Game:
    def __init__(self, player1, player2):
        self.board = Board()
        self.players = [player1, player2]

    def play(self):
        self.board.display()
        current_player = self.players[0]

        while True:
            cell_num = int(input(f"{current_player.name}, выберите номер клетки (0-8): "))
            if self.board.make_move(cell_num, current_player):
                self.board.display()
                if self.board.check_win(current_player):
                    print(f"{current_player.name} победил!")
                    return
                if self.board.is_full():
                    print("Ничья!")
                    return
                current_player = self.players[1] if current_player == self.players[0] else self.players[0]


if __name__ == '__main__':
    player1 = Player("Игрок 1", "X")
    player2 = Player("Игрок 2", "O")

    while True:
        game = Game(player1, player2)
        game.play()
        play_again = input("Хотите сыграть ещё раз? (да/нет): ").lower()
        if play_again != 'да':
            break

