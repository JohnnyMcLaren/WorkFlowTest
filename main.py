"""Главный модуль"""
from random import choice

def main():
    while True:
        if input('Бросить кубик? (Y/N): ').lower() == 'y':
            diceRoll = choice([1,2,3,4,5,6])
            print(f'Выпало число {diceRoll}.')
        else:
            break

if __name__ == '__main__':
    main()
