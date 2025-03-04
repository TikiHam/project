from player import Player
from roulette import Roulette
from bet import Bet
import shutil


minimum_bet = 0.5
roulette_profits = 0.0
player_profits = 0.0
player = None


def main():

    while player.bank < minimum_bet:
        print(
            f'\nSorry, you have less CSCoins ({player.bank}) than our minimum bet ({minimum_bet}).\n')
        player.insert_coins()

    print(f'\n!!!LET THE GAME BEGIN!!!')

    while True:
        # Ask to place a bet
        player_bets = get_bets()

        if player_bets:
            # Roll the wheel
            roulette_result = Roulette.spin()

            # Show summary result of the round, player's balance and offers to look through all the bets
            game_results(player_bets, roulette_result)

        # If player have less than minimum bet, ask if he want to refresh balance if he don't kick him from casino
        if player.bank < minimum_bet:
            if input(f'\nUnfortunately, you have less CSCoins than our minimum bet.\n'
                     f'Do you want to add some CSCoins? [Y/N] ')[0].strip().upper() == 'Y':
                player.insert_coins(minimum_bet)
            else:
                print(f'\nGoodbye! Better luck next time!')
                break

        # Show player balance
        print(f'\nYour balance = {player.bank}')

        # Ask if he want to play again
        if input(f'\nDo you want to play one more round? [Y/N] ')[0].strip().upper() == 'N':
            break

    # Show Goodbye message
    show_goodbye_message()


def get_bets():
    '''
    Function creates a list of player bets. It checks that the player has, enough money for next bet, asks to input a sum,
    check it in the bet_check function, withdraw sum from player account, and add an object bet into the bets list.
    Then it asks the player if he wants to bet more, if Y ---> Loops, if N ---> exit. Show all the bets and return the list of bets
    '''

    bets = []
    bets_counter = 0

    print(f'\nPlace your bet!')

    while True:

        # Check that player have coins for next bet
        if player.bank < minimum_bet:
            print(
                f'\nSorry, you do not have enough CSCoins for one more bet. Your current balance = {player.bank}')
            break

        # Incremating bet counter
        bets_counter += 1

        print(f'\nHow much would you like to bet? (Your balance = {player.bank})\n')
        bet_amount = input(f'Bet: ').strip()

        # Check that bet amount is valid
        if not bet_check(bet_amount):
            continue
        bet_amount = float(bet_amount)

        # Withdraw coins from player account
        player.withdrawal(bet_amount)

        # Create a bet object and add it to bets list
        bet = Bet(bets_counter)
        bet.place_a_bet(bet_amount)
        bets.append(bet)

        # Check if player want to bet more
        if input(f'\nWould you like to place another bet? [Y/N] ')[0].strip().upper() == 'N':
            break

    # If no bets were made inform player about it
    if len(bets) == 0:
        print(f'\nYou have not made any bet.\n')
        return None

    # Showing number of bets
    print(f'\nYou have made {bets_counter} bet(s).\n')

    # Offer player to look through his bets
    if input(f'Would you like to see the list of your bets? [Y/N] ')[0].strip().upper() == 'Y':
        show_bets(bets)

    return bets


def bet_check(value_to_check: str):
    '''
    Function check that bet is a float number >= minimum and it checks that bet is less then players bank. Return True if Valid else: False
    '''
    global player
    try:
        value_to_check = float(value_to_check)
    except ValueError:
        print(f'\nSorry, I did not understand...\n'
              f'Please, type a positive sum (e.g. 11.20)')
        return False
    if value_to_check < minimum_bet:
        print(
            f'\nSorry, you are trying to bet less than our minimum bet ({minimum_bet}). Please, bet more!')
        return False
    if value_to_check > player.bank:
        print(
            f'\nSorry, you are trying to bet more than you have ({player.bank}). Please, bet less!')
        return False
    return True


def show_bets(bets):
    '''
    Printing out all bets player did
    '''
    print()
    print("_"*shutil.get_terminal_size().columns)
    for bet in bets:
        print()
        print(bet)
        print("_"*shutil.get_terminal_size().columns)
    print()
    input(f'Press Enter to continue... ')


def game_results(bets: list, ball: str):
    '''
    Call function count_delta, to count all bets wins and loss

    Show message :
    You have made N bet(s).
    You have won X bet(s). With summary amount = **.**
    You have lost Y bet(s). With summary amount = **.**
    Your profit for this round = **.**. Your balance = **.**

    Offers to check all bets. Will show bets one by one (Enter input split) if Y
    If N return None and exit
    '''

    delta, win_sum, loose_sum = count_delta(bets, ball)

    win_count = sum(1 for bet in bets if bet.status)
    loose_count = len(bets) - win_count

    print(f'You have made {len(bets)} bet(s).\n'
          f'You have won {win_count} bet(s). With summary amount = {win_sum}\n'
          f'You have lost {loose_count} bet(s). With summary amount = {loose_sum}\n'
          f'Your profit for this round = {delta}. Your balance = {player.bank}\n')

    if input('Would you like to see details? [Y/N] ')[0].strip().upper() == 'N':
        return None

    print("_"*shutil.get_terminal_size().columns)
    for bet in bets:
        if bet.status:
            print(f'\nBet #{bet.n} result: !WON!'
                  f'\nBet type: {bet.type}, bet detail: {bet.variant}.'
                  f'\nBall dropped on on number {ball}, {Roulette.roulette_table[ball]['Color']}, in Row number {Roulette.roulette_table[ball]['Rows']}'
                  f'\nBet value: {bet.bet_value}. Bet multiplied by: {bet.multiplicator}'
                  f'\nYou won = {bet.bet_value * (bet.multiplicator - 1)}\n')
        else:
            print(f'\nBet #{bet.n} result: !LOST!'
                  f'\nBet type: {bet.type}, bet detail: {bet.variant}.'
                  f'\nBall dropped on on number {ball}, {Roulette.roulette_table[ball]['Color']}, in Row number {Roulette.roulette_table[ball]['Rows']}'
                  f'\nBet value: {bet.bet_value}.')

        print()
        print("_"*shutil.get_terminal_size().columns)
        input(f'\nPress Enter to see next bet... ')
        print()


def count_delta(bets: list, ball: str):
    '''
    Check each bet and change its status: True if bet won, False if bet lost.
    Count the total delta of all bets and return it.
    '''
    global roulette_profits
    global player_profits
    sum_delta = 0.0
    win_sum = 0.0
    loose_sum = 0.0

    for bet in bets:

        match bet.type:
            case 'Single':
                bet.status = True if bet.variant == ball else False
            case 'Red Black':
                bet.status = True if bet.variant == Roulette.roulette_table[ball]['Color'] else False
            case 'Odd Even':
                bet.status = True if bet.variant == Roulette.roulette_table[ball]['Odd or Even'] else False
            case 'Halfs':
                bet.status = True if bet.variant == Roulette.roulette_table[ball]['Halfs'] else False
            case 'Rows':
                bet.status = True if bet.variant == Roulette.roulette_table[ball]['Rows'] else False
            case 'Dozens':
                bet.status = True if bet.variant == Roulette.roulette_table[ball]['Dozens'] else False

        if bet.status:
            prize = bet.bet_value * bet.multiplicator
            delta = prize - bet.bet_value
            win_sum += delta
            player.deposit(prize)
            roulette_profits -= delta
            player_profits += delta

        else:
            loose_sum += bet.bet_value
            roulette_profits += bet.bet_value
            player_profits -= bet.bet_value
            delta = -bet.bet_value

        sum_delta += delta

    return sum_delta, win_sum, loose_sum


def get_player_name():
    '''
    Ask for the player's name and greet him. Checks that minimum 1 symbol in name Return player name : str
    '''
    print(f'\nHow can we address you?\n')
    while True:
        name = input('Name: ')
        if not name:
            print(f'\nPlease provide at least one symbol to your name!\n')
            continue
        break
    print(f'\nHi, {name}!\n')
    return name


def show_goodbye_message():
    print(f'\n!!THANK YOU FOR PLAYING OUR ROULETTE!!\n\n'
          f'Your balance = {player.bank}\n'
          f'Roulette won = {roulette_profits}\n'
          f'Your profit = {player_profits}\n\n')


def init_globals(name=''):
    global player
    player = Player(name, 0)


if __name__ == '__main__':
    # Welcome player
    print(f'\n!!!WELCOME PLAYER!!!'
          f'\nCOME AND TRY YOUR LUCK!'
          f'\n\nThis is CSRoulette!\n')
    # Offer to show rules
    if input(f'Would you like to read the rules? [Y/N] ')[0].strip().upper() == 'Y':
        Roulette.show_rules()

    # Create player
    name = get_player_name()
    init_globals(name)
    player.insert_coins()

    main()
