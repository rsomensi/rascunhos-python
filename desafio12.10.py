'''Crie um programa que faça o PC jogar Jokenpô com você.'''
print(30 * ('--JOKENPO--'))
player = int(input('1 - Rock;\n2 - Paper;\n3 - Scissors\nMake your move: '))
from random import randint
import emoji
cp = randint(1,3)
if cp == 1 and player == 1:
    print(emoji.emojize(':punch:', use_aliases=True))
    print('Computer choose \033[1mROCK\033[m\n\033[1;33mTIE IN THE GAME!\033[m')
elif cp == 1 and player == 2:
    print(emoji.emojize(':raised_hand:', use_aliases=True))
    print('Computer choose \033[1mROCK\033[m\n\033[1;32mYOU WIN!!!\033[m')
elif cp == 1 and player == 3:
    print(emoji.emojize(':v:', use_aliases=True))
    print('Computer choose \033[1mROCK\033[m\n\033[1;31mYOU LOST!\033[m')
elif cp == 2 and player == 1:
    print(emoji.emojize(':punch:', use_aliases=True))
    print('Computer choose \033[1mPAPER\033[m\n\033[1;31mYOU LOST!\033[m')
elif cp == 2 and player == 2:
    print(emoji.emojize(':raised_hand:', use_aliases=True))
    print('Computer choose \033[1mPAPER\033[m\n\033[1;33mTIE IN THE GAME!\033[m')
elif cp == 2 and player == 3:
    print(emoji.emojize(':v:', use_aliases=True))
    print('Computer choose \033[1mPAPER\033[m\n\033[1;32mYOU WIN!!!\033[m')
elif cp == 3 and player == 1:
    print(emoji.emojize(':punch:', use_aliases=True))
    print('Computer choose \033[1mSCISSORS\033[m\n\033[1;32mYOU WIN!!!\033[m')
elif cp == 3 and player == 2:
    print(emoji.emojize(':raised_hand:', use_aliases=True))
    print('Computer choose \033[1mSCISSORS\033[m\n\033[1;31mYOU LOST!\033[m')
elif cp == 3 and player == 3:
    print(emoji.emojize(':v:', use_aliases=True))
    print('Computer choose \033[1mSCISSORS\033[m\n\033[1;33mTIE IN THE GAME!\033[m')
print(30 * ('--JOKENPO--'))



