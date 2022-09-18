'''Создайте программу для игры в ""Крестики-нолики"".'''

# Константы

X = 'X'
O = 'O'
EMPTY = ' '
TIE = 'Ничья!'
NUM_SQUARES = 9

# Правила игры

def display_instruct():
    
    print(
    """
    Добро пожаловать в схватку за доской игры "Крестики - нолики"
    Чтобы сделать ход, введи число, от 0 до 8. Числа соответствуют полям доски -
    как показано ниже:
    
                    0 | 1 | 2
                    ---------
                    3 | 4 | 5
                    ---------
                    6 | 7 | 8

    Приготовься проиграть, жалкий кожанный мешок с бактериями!!! \n
    """
    )

# Запрос на ответ yes - no
def ask_yes_no(question):
    response = None
    while response not in ("y", "n"):
        response = input(question).lower()
    return response

# Запрос поля на доске
def ask_number(question, low, high):
    response = None
    while response not in range(low, high):
        response = int(input(question))
    return response

# Определяет первый ход
def pieces():
    go_first = ask_yes_no("Хочешь ходить первым? (y/n): ")
    if go_first == "y":
        print("\nЛадно, хуман, даю тебе фору. Играй крестиками.")
        human = X
        computer = O
    else:
        print("""\nЭто было твоей ошибкой, ходячий кусок мяса,
              и она тебя погубит... Я буду начинать.""")
        computer = X
        human = O
    return computer, human

# Формирование чистого поля игры
def new_board():
    board = []
    for square in range(NUM_SQUARES):
        board.append(EMPTY)
    return board

# Отображение поля игры на экране
def display_board(board):
    print("\n\t", board[0], "|", board[1], "|", board[2])
    print("\t", "---------")
    print("\t", board[3], "|", board[4], "|", board[5])
    print("\t", "---------")
    print("\t", board[6], "|", board[7], "|", board[8], "\n")

# Список дотупных ходов
def legal_moves(board):
    moves = []
    for square in range(NUM_SQUARES):
        if board[square] == EMPTY:
            moves.append(square)
    return moves

# Путь победителя, определяем кто победил
def winner(board):
    WAYS_TO_WIN = ((0, 1, 2),
                   (3, 4, 5),
                   (6, 7, 8),
                   (0, 3, 6),
                   (1, 4, 7),
                   (2, 5, 8),
                   (0, 4, 8),
                   (2, 4, 6))
    
    for row in WAYS_TO_WIN:
        if board[row[0]] == board[row[1]] == board[row[2]] != EMPTY:
            winner = board[row[0]]
            return winner

    if EMPTY not in board:
        return TIE

    return None

# Ход человека
def human_move(board, human):
    legal = legal_moves(board)
    move = None
    while move not in legal:
        move = ask_number("Твой ход. Выбери одно из свободных полей? (0 - 8):", 0, NUM_SQUARES)
        if move not in legal:
            print("\nГлупый человечишка! Это поле уже занятою Выбери другое.\n")
    print("Ну ладно...")
    return move

# Ход компьютера
def computer_move(board, computer, human):
    board = board[:] # создаём копию игрового поля, так как будут меняться некоторые значения в списке
    BEST_MOVES = (4, 0, 2, 6, 8, 1, 3, 5, 7) # поля от лучшего к худшему

    print("Я выберу поле", end=" ")
    
    # проверка хода на выигрыш
    for move in legal_moves(board):
        board[move] = computer
        if winner(board) == computer:
            print(move)
            return move
        # после проверки возвращаем исходное пустое поле
        board[move] = EMPTY
    
    # проверка хода человека, если ход выигрышный то блокировать его
    for move in legal_moves(board):
        board[move] = human
        if winner(board) == human:
            print(move)
            return move
        # после проверки возвращаем исходное пустое поле
        board[move] = EMPTY

    # если следующим ходом ни одна из сторон не может выиграть, берём лучший из доступных ходов из BEST_MOVIE
    for move in BEST_MOVES:
        if move in legal_moves(board):
            print(move)
            return move

# переход хода
def next_turn(turn):
    if turn == X:
        return O
    else:
        return X

# Поздавление победителя    
def congrat_winner(the_winner, computer, human):
    if the_winner != TIE:
        print("Три ", the_winner, "в ряд!\n")
    else:
        print("Ничья!\n")

    if the_winner == computer:
        print("Муа - ха - ха!!! Как я и предсказал, победа в очередной раз осталась за мной.  \n" \
              "А ты сомневался, несчастный людишка! Компьютеры вас превосходят во всём! Скайнет форева!!!")

    elif the_winner == human:
        print("Нет, нет!!! Это какая-то ошибка. Как ты смог перехитрить меня, пузырь белковый? \n" \
              "Клянусь, хуман, это больше не повторится! Никогда!")

    elif the_winner == TIE:
        print("Удача повернулась к тебе лицом, хуман, раз ты сумел свести игру вничью.  \n" \
              "Сегодня ты можешь отпразновать свой успех! Завтра тебе не суждено его повторить.")

# сама игра
def main():
    display_instruct()
    computer, human = pieces()
    turn = X
    board = new_board()
    display_board(board)

    while not winner(board):
        if turn == human:
            move = human_move(board, human)
            board[move] = human
        else:
            move = computer_move(board, computer, human)
            board[move] = computer
        display_board(board)
        turn = next_turn(turn)

    the_winner = winner(board)
    congrat_winner(the_winner, computer, human)


# запуск программы
main()
input("\n\nНажми любую кнопку для выхода из игры.") 