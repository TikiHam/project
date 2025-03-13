    # ROULETTE SIMULATOR
    #### Video Demo:  <URL HERE>
    #### Description:

    This is my final project for CS50’s Introduction to Programming with Python course!

    For my final project, I made a roulette game simulator.
    It contains 4 classes:
        project.py --- It is the main engine, and it contains the main function.
        player.py --- It holds information about the player.
        bet.py --- It holds information about a single bet.
        roulette.py --- It holds information about the roulette table (which number is in what color and row) and supports the spinning engine.


    #project.py

    BE AWARE: Each question that expects a [Y/N] answer is sensitive. It will read the first letter of your input. In case the user does not behave by answering this question, the program might crash.

    ##There are 4 global variables in the class:
        ###minimum_bet
            By default, it equals 0.5. The name stands for its functionality:
            it is the lowest the player can bet.
            Also, if the player's bank account goes lower than the minimum_bet value,
            the simulation will ask to insert more coins.
        ###roulette_profits
            By default 0.0; we will use it to count total losses and profits for the "Casino."
        ###player_profits
            By default 0.0; we will use it to count total losses and profits for the "Player."
        ###player
            By default, None, because at the moment, there is no player in the casino.
            We need Player to be a global variable because this object will be used by different functions.

    ##There are 9 functions in the class:
        ###main
            Checks that the player has enough CSCoins to enter the next round. If not, it asks to add coins.
            Creates a list of players' bets via the get_bets function.
            Calls a class method of the Roulette class that will return a string containing the number
            where the ball dropped.
            Calls the game_results function, passing a list of bets and the ball number in it.
            If the player runs out of CSCoins, it asks if they want to add more; if NO, proceeds to game end.
            Outputs the player's balance and asks whether the player wants to play one more round.
            If YES, it starts over. If NO, it proceeds to game end.
            Before the game ends, it will call the show_goodbye_message function.

        ###get_bets
            Creates an empty list of bets and starts a bet counter from 0.
            Checks that the player has enough CSCoins to make the next bet.
            Asks to place a bet. Checks that the input content is valid via the bet_check function.
            Increments the bet counter, so the first bet will have bet counter = 1, the second = 2, and so on.
            Withdraws the bet value from the player's account.
            Creates a bet: an object of the Bet class.
            Calls the place_a_bet function of the Bet class and passes a bet amount to it.
            If no bets were made, it prints a message stating that no bets were made for that round and returns ---> None.
            Returns ---> a list of bets.

        bet_check
            It receives a string that should contain a float or integer number that the simulation tries to assign
            as a value for a bet.
            It checks that the content can be transformed from str to float and that the value of the content
            is <= player bank volume and >= minimum bet.
            Returns ---> True if all checks are passed; otherwise, returns False.

        show_bets
            It receives a list of "bets," which contain one or more objects of the Bet class.
            For each bet in the list, it prints out the bets' information, calling the __str__ method of the Bet class.
            It will print out all bets at once and will wait for Enter to be pressed to continue.

        game_results
            It receives
                a list of "bets," which contain one or more objects of the Bet class,
                and a string "ball" that contains the number where the ball dropped.
            It calls the count_delta(bets, ball) function.
            Based on count_delta's return, it prints the general information about the round:
                (How many bets were made, how many bets won and lost,
                and what the sums are for each of them respectively).
                Then it asks the user if he/she wants to see details; if YES, it will show details for each bet,
                separated by Enter.

        count_delta
            It receives
                a list of "bets," which contain one or more objects of the Bet class,
                and a string "ball" that contains the number where the ball dropped.
            For each bet in bets, it checks if the bet won or lost. It changes its status: True: won;
            False: lost.
            Based on the bet status, it counts sum_delta, win_sum, and loose_sum.

            BE AWARE: In the case of a win, a prize sum will be deposited to the player account, which is equal to:
                      player's bet * bet multiplier. However, the output will show that
                      the player won a sum = (player prize - player's bet).
                      (e.g., if the player bet = 10 and won with a multiplier of 2, the prize = 20, but the message for the player will say
                      they won 10). This is because the player did not win the money they bet; they won only
                      the money added on top of it by the "casino."
                      win_sum will also be incremented by (prize - player's bet).

            Returns ---> sum_delta, win_sum, loose_sum. sum_delta = win_sum - loose_sum. (Sums for all bets).

        get_player_name
            It prompts the user to input their name; it provides a check for an empty string and will ask again if
            the check fails.
            Returns ---> a string with the Player's Name.

        show_goodbye_message
            It prints out a game over message for the player. The message contains information about the player's bank
            account, roulette_profits, and player_profits.

        init_globals
            It receives 'name' and creates a global variable player.
            Creates an object of the Player class with name = 'name'.

        player.py

        There are 4 methods in the class:
            __init__
                Creates an object of the Player class.
                It has 2 variables:
                    player's bank
                    player's name
            withdrawal
                Withdraws a value from the player's bank.
            deposit
                Deposits a value into the player's bank.
            insert_coins
                Adds CSCoins to the player's bank, providing a check that the input value can be transported
                into float format and that the value is positive.
                If checks are passed, it calls the deposit method of the Player class.
        There is 1 property in the class:
            bank
                It stores the amount of CSCoins the player has in their account; when set, it checks that the player
                does not have a negative amount in their bank account. Raises an ErrorDepositLessZero error
                if the check does not pass.

        bet.py

        There is 1 class variable in the class:
            bet_type
                Bet type is a dictionary: keys are different types of possible bets
                (Single, Red Black, Odd Even, Halfs, Rows, Dozens)
                and values are also dictionaries:
                    keys are variants and multipliers;
                    values are possible variants of a specific bet type and a fixed multiplier of a specific bet type.
                (e.g., bet type = Red Black: variants = Red / Black, multiplier = 2)

        There are 3 methods in the class:
            __init__
                Creates an object of the Bet class.
                It has 2 variables:
                    bet number _n
                    bet status: default None. In project.count_delta, it changes to be True or False
                                (win or lose of the bet respectively).
            __str__
                Returns the string with information about an object; it contains:
                    bet number
                    bet type
                    bet variant
                    bet value
                    bet multiplier
                    possible win from a bet (= bet value * (bet multiplier - 1)).
            place_a_bet
                Receives a float value "money,"
                Assigns money to _bet_value,
                Shows available types for a bet,
                Gets a bet type from a user and assigns it to type,
                Shows possible variants for the chosen type of a bet,
                Gets a variant from a user.
                Assigns _multiplier according to a chosen type.

        There are 5 properties in the class:
            bet_value
                Stores a value of a single bet.
                ---> Returns _bet_value.
            n
                Stores a number of a single bet.
                ---> Returns _n.
            multiplier
                Stores a multiplier of a single bet.
                ---> Returns _multiplier.
            type
                Stores a type of a single bet.
                ---> Returns _type.
                When set, it checks that the input content from the user is correct and exists as one of the given types.
                Input can be case-insensitive. If the input does not match one of the given types,
                calls self setter again and again. When the content is correct, it assigns it to _type.
            variant
                Stores a variant of a single bet.
                ---> Returns _variant.
                When set, it checks that the input content from the user is correct and exists in the given variants.
                Input can be case-insensitive. If the input does not match one of the given variants,
                it calls self setter again and again. When the content is correct, it assigns it to _variant.

        roulette.py

        There are 2 class variables in the class:
            wheel_spin_time
                It contains the number of seconds the roulette wheel "spins."
            roulette_table
                It is a dictionary: keys are numbers from 0 to 36,
                                  values are information about that number stored in the format of a dictionary.
                                  The information contains the number's color, number's parity, in what half it is,
                                  its row, and in what dozen it is.
        There are 2 class methods in the class:
            spin
                It imitates spinning of the roulette wheel. The spin time defaults to 5
                and can be modified on line 10.
                Each second, it will print the 🎲 emoji on the screen, and then announce to the user the number
                where the ball dropped. If 0, it will announce: 'IT IS ZERO!!!'.
                Waits for 2 more seconds to continue.
                ---> Returns ball_number as a string.
            show_rules
                Prints the rules of this simulation.
                It contains a minimum_bet variable of the Project class,
                types, variables, and multipliers of the Bet class.
