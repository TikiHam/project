class Bet:
    bet_type = {'Single': {'variants': ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13',
                                        '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24',
                                        '25', '26', '27', '28', '29', '30', '31', '32', '33', '34', '35', '36'],
                           'multipicator': 37},
                'Red Black': {'variants': ['Red', 'Black'], 'multipicator': 2},
                'Odd Even': {'variants': ['Odd', 'Even'], 'multipicator': 2},
                'Halfs': {'variants': ['1-18', '19-36'], 'multipicator': 2},
                'Rows': {'variants': ['1-th row', '2-nd row', '3-rd row'], 'multipicator': 3},
                'Dozens': {'variants': ['1-12', '13-24', '25-36'], 'multipicator': 2}}

    def __init__(self, n: int, money: float):
        self._n = n
        self.status = None
        self.place_a_bet(money)

    def __str__(self):
        return (f'This is bet #{self.n}.\n'
                f'The type of your bet is {self.type}. And you bet on {self.variant}.\n'
                f'You bet {self.bet_value}, and in chance of winning, your money will be multiplied by {self.multiplicator}.\n'
                f'Possible win on this bet = {self.bet_value * (self.multiplicator - 1)}!\n\n')

    def place_a_bet(self, money):
        self._bet_value = money

        print(f'\nChoose the type of bet: {', '.join(self.bet_type.keys())}\n')
        self.type = input('Type: ').strip().lower().capitalize()

        print(f'\nWhat do you want to bet on?\n'
              f'\nHere are the wariants: {', '.join(self.bet_type[self.type]['variants'])}\n')
        self.variant = input('Variant: ').strip().lower().capitalize()

        self._multipicator = self.bet_type[self.type]['multipicator']

    @property
    def bet_value(self):
        return self._bet_value

    @property
    def n(self):
        return self._n

    @property
    def multiplicator(self):
        return self._multipicator

    @property
    def variant(self):
        return self._variant

    @variant.setter
    def variant(self, v: str):
        if v in self.bet_type[self.type]['variants']:
            self._variant = v
        else:
            print(f'\nPlease provide correct variant. Type it exactly as stated in list\n'
                  f'variants are: {', '.join(self.bet_type[self.type]['variants'])}\n')
            self.variant = input('Variant: ').strip()

    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, u_i: str):
        if u_i in self.bet_type.keys():
            self._type = u_i
        else:
            print(f'\nThis is incorrect type. Please try once again\n'
                  f'Choose from given types: {', '.join(self.bet_type.keys())}\n')
            self.type = input('Type: ').strip()
