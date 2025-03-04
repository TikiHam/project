class ErrorDepositLessZero(Exception):
    '''
    Raised when trying to deposit a negative amount of value
    '''
    pass


class Player:

    def __init__(self, name: str, bank: float):
        '''
        Create a player with 0.0 bank, assign name,
        call insert_coins function which will deposit CSCoins to player's bank
        '''
        self.bank = bank
        self.name = name

    def withdrawal(self, value: float):
        self.bank = self.bank - value

    def deposit(self, value: float):
        self.bank = self.bank + value

    def insert_coins(self):
        '''
        Function check that coins are float >0, then deposit on the player account.
        Check, that player bank is greater than the minimum bet.
        If not ask to do it again
        '''
        print(f'Please insert CSCoins coins\n')
        while True:
            coins = input('Coins: ')

            try:
                coins = float(coins)
            except ValueError:
                print(f'\nSorry, I did not understand...\n'
                      f'Please tell me how many CSCoins you want to cash-in. Type a positive summ. (e.g. 15.6)\n')
                continue
            if coins < 0:
                print(f'\nSorry, please insert a positive amount of CSCoins!')
                continue
            self.deposit(coins)

            break

    @property
    def bank(self):

        return round(self._bank, 2)

    @bank.setter
    def bank(self, value: float):
        if value < 0:
            print(f'\nYou are trying to assign value < 0 to player bank\n')
            raise ErrorDepositLessZero("Value must be non-negative.")
        self._bank = value
