"""Главный модуль"""
from random import choice


def throwDice(dices: int) -> int:
    diceRoll = choice(range(1, dices + 1))
    return diceRoll


def main():
    userInput = input('Сколько граней будет у кубика [6]: ')
    if userInput.isdigit():
        dices = int(userInput)
        if dices <= 0:
            raise ValueError('Число граней должно быть больше нуля!')
    else:
        dices = 6
    while True:
        if input(f'Бросить {dices}-граневый кубик ? (Y/N): ').lower() == 'y':
            diceRoll = throwDice(dices)

            print(f'Выпало число {diceRoll}.')
        else:
            break


if __name__ == '__main__':
    main()
