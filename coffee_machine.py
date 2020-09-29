money = 550
water = 400
milk = 540
beans = 120
cups = 9


class ResourceError(Exception):
    pass


def print_state():
    print()
    print('The coffee machine has:')
    print(f'{water} of water')
    print(f'{milk} of milk')
    print(f'{beans} of coffee beans')
    print(f'{cups} of disposable cups')
    print(f'{money} of money')
    print()


def select_action() -> str:
    return input('Write action (buy, fill, take, remaining, exit): ')


def select_flavor() -> int:
    print()
    response = input('What do you want to buy?'
                     ' 1 - espresso,'
                     ' 2 - latte,'
                     ' 3 - cappuccino,'
                     ' back - to main menu: ')
    if response == 'back':
        return 0
    return int(response)


def is_enough(need_water=0, need_milk=0, need_beans=0):
    if water < need_water:
        print('Sorry, not enough water!\n')
        raise ResourceError
    if milk < need_milk:
        print('Sorry, not enough milk!\n')
        raise ResourceError
    if beans < need_beans:
        print('Sorry, not enough beans!\n')
        raise ResourceError
    if cups < 1:
        print('Sorry, not enough cups\n')
        raise ResourceError
    print('I have enough resources, making you a coffee!\n')


def buy():
    global money, water, milk, beans, cups

    flavor = select_flavor()

    try:
        if flavor == 0:
            pass
        elif flavor == 1:  # espresso
            is_enough(need_water=250, need_beans=16)

            money += 4
            water -= 250
            beans -= 16
            cups -= 1
        elif flavor == 2:  # latte
            is_enough(need_water=350, need_milk=75, need_beans=20)

            money += 7
            water -= 350
            milk -= 75
            beans -= 20
            cups -= 1
        elif flavor == 3:  # cappuccino
            is_enough(need_water=200, need_milk=100, need_beans=12)

            money += 6
            water -= 200
            milk -= 100
            beans -= 12
            cups -= 1
        else:
            raise ValueError(f'Unknown flavor {flavor}')
    except ResourceError:
        pass


def fill():
    global water, milk, beans, cups

    print()
    water += int(input('Write how many ml of water do you want to add: '))
    milk += int(input('Write how many ml of milk do you want to add: '))
    beans += int(input('Write how many grams of coffee beans'
                       ' do you want to add: '))
    cups += int(input('Write how many disposable cups of coffee'
                      ' do you want to add: '))
    print()


def take():
    global money

    print()
    print(f'I gave you ${money}')
    print()

    money = 0


def main():
    while True:
        action = select_action()

        if action == 'buy':
            buy()
        elif action == 'fill':
            fill()
        elif action == 'take':
            take()
        elif action == 'exit':
            break
        elif action == 'remaining':
            print_state()
        else:
            raise ValueError(f'Unknown command {action}')


if __name__ == '__main__':
    main()
