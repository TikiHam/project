import time
import random
import sys
import shutil
from bet import Bet


class Roulette:

    wheel_spin_time = 5
    roulette_table = {
        '0': {'Color': None, 'Odd or Even': None, 'Halfs': None, 'Rows': None, 'Dozens': None},
        '1': {'Color': 'Red', 'Odd or Even': 'Odd', 'Halfs': '1-18', 'Rows': '1', 'Dozens': '1-12'},
        '2': {'Color': 'Black', 'Odd or Even': 'Even', 'Halfs': '1-18', 'Rows': '2', 'Dozens': '1-12'},
        '3': {'Color': 'Red', 'Odd or Even': 'Odd', 'Halfs': '1-18', 'Rows': '3', 'Dozens': '1-12'},
        '4': {'Color': 'Black', 'Odd or Even': 'Even', 'Halfs': '1-18', 'Rows': '1', 'Dozens': '1-12'},
        '5': {'Color': 'Red', 'Odd or Even': 'Odd', 'Halfs': '1-18', 'Rows': '2', 'Dozens': '1-12'},
        '6': {'Color': 'Black', 'Odd or Even': 'Even', 'Halfs': '1-18', 'Rows': '3', 'Dozens': '1-12'},
        '7': {'Color': 'Red', 'Odd or Even': 'Odd', 'Halfs': '1-18', 'Rows': '1', 'Dozens': '1-12'},
        '8': {'Color': 'Black', 'Odd or Even': 'Even', 'Halfs': '1-18', 'Rows': '2', 'Dozens': '1-12'},
        '9': {'Color': 'Red', 'Odd or Even': 'Odd', 'Halfs': '1-18', 'Rows': '3', 'Dozens': '1-12'},
        '10': {'Color': 'Black', 'Odd or Even': 'Even', 'Halfs': '1-18', 'Rows': '1', 'Dozens': '1-12'},
        '11': {'Color': 'Black', 'Odd or Even': 'Odd', 'Halfs': '1-18', 'Rows': '2', 'Dozens': '1-12'},
        '12': {'Color': 'Red', 'Odd or Even': 'Even', 'Halfs': '1-18', 'Rows': '3', 'Dozens': '1-12'},
        '13': {'Color': 'Black', 'Odd or Even': 'Odd', 'Halfs': '1-18', 'Rows': '1', 'Dozens': '13-24'},
        '14': {'Color': 'Red', 'Odd or Even': 'Even', 'Halfs': '1-18', 'Rows': '2', 'Dozens': '13-24'},
        '15': {'Color': 'Black', 'Odd or Even': 'Odd', 'Halfs': '1-18', 'Rows': '3', 'Dozens': '13-24'},
        '16': {'Color': 'Red', 'Odd or Even': 'Even', 'Halfs': '1-18', 'Rows': '1', 'Dozens': '13-24'},
        '17': {'Color': 'Black', 'Odd or Even': 'Odd', 'Halfs': '1-18', 'Rows': '2', 'Dozens': '13-24'},
        '18': {'Color': 'Red', 'Odd or Even': 'Even', 'Halfs': '1-18', 'Rows': '3', 'Dozens': '13-24'},
        '19': {'Color': 'Red', 'Odd or Even': 'Odd', 'Halfs': '19-36', 'Rows': '1', 'Dozens': '13-24'},
        '20': {'Color': 'Black', 'Odd or Even': 'Even', 'Halfs': '19-36', 'Rows': '2', 'Dozens': '13-24'},
        '21': {'Color': 'Red', 'Odd or Even': 'Odd', 'Halfs': '19-36', 'Rows': '3', 'Dozens': '13-24'},
        '22': {'Color': 'Black', 'Odd or Even': 'Even', 'Halfs': '19-36', 'Rows': '1', 'Dozens': '13-24'},
        '23': {'Color': 'Red', 'Odd or Even': 'Odd', 'Halfs': '19-36', 'Rows': '2', 'Dozens': '13-24'},
        '24': {'Color': 'Black', 'Odd or Even': 'Even', 'Halfs': '19-36', 'Rows': '3', 'Dozens': '13-24'},
        '25': {'Color': 'Red', 'Odd or Even': 'Odd', 'Halfs': '19-36', 'Rows': '1', 'Dozens': '25-36'},
        '26': {'Color': 'Black', 'Odd or Even': 'Even', 'Halfs': '19-36', 'Rows': '2', 'Dozens': '25-36'},
        '27': {'Color': 'Red', 'Odd or Even': 'Odd', 'Halfs': '19-36', 'Rows': '3', 'Dozens': '25-36'},
        '28': {'Color': 'Black', 'Odd or Even': 'Even', 'Halfs': '19-36', 'Rows': '1', 'Dozens': '25-36'},
        '29': {'Color': 'Black', 'Odd or Even': 'Odd', 'Halfs': '19-36', 'Rows': '2', 'Dozens': '25-36'},
        '30': {'Color': 'Red', 'Odd or Even': 'Even', 'Halfs': '19-36', 'Rows': '3', 'Dozens': '25-36'},
        '31': {'Color': 'Black', 'Odd or Even': 'Odd', 'Halfs': '19-36', 'Rows': '1', 'Dozens': '25-36'},
        '32': {'Color': 'Red', 'Odd or Even': 'Even', 'Halfs': '19-36', 'Rows': '2', 'Dozens': '25-36'},
        '33': {'Color': 'Black', 'Odd or Even': 'Odd', 'Halfs': '19-36', 'Rows': '3', 'Dozens': '25-36'},
        '34': {'Color': 'Red', 'Odd or Even': 'Even', 'Halfs': '19-36', 'Rows': '1', 'Dozens': '25-36'},
        '35': {'Color': 'Black', 'Odd or Even': 'Odd', 'Halfs': '19-36', 'Rows': '2', 'Dozens': '25-36'},
        '36': {'Color': 'Red', 'Odd or Even': 'Even', 'Halfs': '19-36', 'Rows': '3', 'Dozens': '25-36'}
    }

    @classmethod
    def spin(cls):
        print(f'\nALL BETS ARE OFF!\n'
              f'LETS SPIN THE WHEEL!!!\n')
        for _ in range(cls.wheel_spin_time):
            to_screen = ' 🎲 '
            # to_screen = random.choice([' 💰 ',' 🍒 ', ' 🎲 ', ' 💸 ', ' 🎱 ', ' 🏦 ', ' 7️⃣ ', ' 🏇 '])
            print(to_screen, end='')
            sys.stdout.flush()
            time.sleep(1)
        ball_number = str(random.randint(0, 36))
        print(f'\n\n')
        if ball_number == '0':
            print(f'IT IS ZERO!!!\n')
        else:
            print(f'IT IS: {ball_number}, {cls.roulette_table[ball_number]['Color'].upper()}!!!\n')

        time.sleep(2)
        return ball_number

    @classmethod
    def show_rules(cls):
        from project import minimum_bet
        '''
        Printing out rules
        '''
        print()
        print("*"*shutil.get_terminal_size().columns)
        print(f'\nHere are our roulette rules:\n\n'
              f'1. Minimum bet = {minimum_bet} CSCoins.\n\n'
              f'2. You have to deposit some CSCoins on your account to start,\n'
              f'   the amount should be higher than minimum bet.\n\n'
              f'3. If you run out of coins, you will have a chance to refill your account.\n\n'
              f'4. If you refuse to refill your account the game will end. Check #12 for more details.\n\n'
              f'5. You can make more than 1 bet per round. You can also make 0 bets\n'
              f'  (In this case we will inform you about it and offer to play another round).\n\n'
              f'6. If you run out of coins during betting process, we will inform you about it,\n'
              f'   and automatically proceed to the next stage.\n\n'
              f'7. Before roulette spin you will have a chance to look through all your bets.\n'
              f'   (However you would not be able to change or cancel them).\n\n'
              f'8. After spin we will inform you the winning number, its color and row number.\n\n'
              f'9. Then we will show you a summary result of all our bets.\n\n'
              f'10. You will have a chance to check them one by one, or skip.\n\n'
              f'11. After each game you will be offered to play one more round or leave.\n\n'
              f'12. When leaving roulette, we will show you your current balance\n'
              f'    as well as roulette and yours total profits.\n')

        print("*"*shutil.get_terminal_size().columns)

        print(f'\nBetting process:\n\n'
              f'1. On each stage, you will be offered a list of variants to choose from.\n\n'
              f'2. There will be 2 stages to make a bet.\n\n'
              f'3. First, you will be offered to choose a type of bet.\n\n'
              f'4. Second, you will be offered to choose a bet detail.\n\n'
              f'5. Please type your choice exactly as given in the example, case-sensitive.\n'
              f'   Otherwise, we will ask you to repeat the stage again.\n')

        print("*"*shutil.get_terminal_size().columns)

        print(f'\nHere are our bet variants:')
        print("_"*shutil.get_terminal_size().columns)
        for type, bet_detail in Bet.bet_type.items():
            print(f'\nYou can bet on {type} bet type.\n'
                  f'Then you can choose a variant:\n'
                  f'{', '.join(bet_detail['variants'])}\n'
                  f'In case of winning your bet will be multiplied by {bet_detail['multipicator']}')
            print("_"*shutil.get_terminal_size().columns)

        print()
        print("*"*shutil.get_terminal_size().columns)

        input(f'\n!GOOD LUCK!\n\n'
              'Press Enter to continue... ')
