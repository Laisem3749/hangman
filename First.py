import Second
import random
m = Second.f()[0]
l = Second.f()[1]
def hangman(word):
    wrong = 0
    stages = ['',
              ' _____     ',
              '|     |    ',
              '|     |    ',
              '|     0    ',
              '|    /|\   ',
              '|    / \   ',
              '|          '
    ]
    rletters = set(list(word))
    board = ['_'] * len(word)
    win = False
    cnt = len(stages) - 2
    print('Добро пожаловать на казнь!')
    _rl = Second.rll()
    rl = Second.rll()
    lettersbefor = []
    while wrong < len(stages) - 2:
        s = ' '.join(rl)
        print('\n')
        print('У вас осталось попыток: {}'.format(cnt))
        print('Буквы, которые не названы: {}'.format(s))
        msq = 'Введите строчную букву: '
        char = input(msq)
        while char != char.lower():
            char = input(msq)
        if char in rletters:
            if char not in lettersbefor:
                for i in range(len(word)):
                    if word[i] == char:
                        board[i] = char
        if (char in _rl) and (char not in rletters) and (char not in lettersbefor):
            wrong += 1
            cnt -= 1
        if char in _rl:
            num = _rl.index(char)
            rl[num] = '_'
        if (char in lettersbefor) or (char not in _rl):
            print("""Вы указали неверный символ или повторили букву, 
которую уже вводили. Ваша попытка не потрачена""")
        print(("Ваше слово: " + ''.join(board)))
        e = wrong + 1
        lettersbefor.append(char)
        print('\n'.join(stages[0:e]))
        if '_' not in board:
            print('Вы выиграли! Было загадано слово: ')
            print(''.join(board))
            win = True
            break
    if not win:
        print('\n'.join(stages))
        print('Вы проиграли! Было загадоно слово: {}'.format(word))

hangman(m[random.randint(0, l)])
# hangman('ацетальдегидрогеназа')
