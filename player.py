class ErrorDepositLessZero(Exception):
    '''
    Raise when try to feposit negative amount of value
    '''
    pass


class Player:

    def __init__(self, name: str, min_bet: float):
        '''
        Create a player with 0.0 bank, assign name, call insert_coins function which will deposit CSCoins to players bank
        '''
        self.bank = 0.0
        self.name = name
        self.insert_coins(min_bet)

    def withdrawal(self, value: float):
        self.bank = self.bank - value

    def deposit(self, value: float):
        self.bank = self.bank + value

    def insert_coins(self, minimum_bet: float):
        '''
        Function check that coins are float >0, then deposit on player account. Check, that player bank is grater
        than minimum bet. If not ask to do it again
        '''
        print(f'How much CSCoins do you want to cash-in?\n')
        while True:
            coins = input('Coins: ')

            try:
                coins = float(coins)
            except ValueError:
                print(f'\nSorry, I did not understand...\n'
                      f'Please tell me how many CSCoins would you want to cash-in. Type a positive summ. (e.g. 15.6)\n')
                continue
            if coins <= 0:
                print(f'\nSorry, please insert a postive amount of CSCoins!')
                continue
            self.deposit(coins)
            if self.bank < minimum_bet:
                print(f'\nWe are sorry, but our minimum bet is {minimum_bet}.\n'
                      f'And you only have {self.bank} CSCoins\n'
                      f'Please insert more CSCoins\n')
                continue
            break

    @property
    def bank(self):
        return self._bank

    @bank.setter
    def bank(self, value: float):
        if value < 0:
            print(f'\nYou are trying to assign value < 0 to player bank\n')
            raise ErrorDepositLessZero("Value must be non-negative.")
        self._bank = value
