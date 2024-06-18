from Garage import Garage
from Vehicle import (Brand, ParkTime, Wheel, FourWheeler, TwoWheeler)
from helper import formatted_result

def welcome_user():
    # welcome menu
    print('\nplease select an option : ')
    print('| 1: Park vehicle | 2: Checkout vehicle | 3: Show Parked vehicles | 4: Exit System | (1/2/3/4)')


def select_menu():
    valid_choice = False
    while not valid_choice:
        try:
            user_option = int(input('Choose Option : '))

            if user_option in range(1, 5):
                valid_choice = True
                return user_option
            else:
                print('Sorry, option not available')

        except ValueError as e:

            print('Sorry only integers are allowed')


def set_vehicle_details(garage):
    print('\n1 : Enter your vehicle details | 2 : Back to Menu| (1/2)')
    valid_option = False
    while not valid_option:
        try:
            user_option = int(input('Choose Option: '))
            if user_option not in range(1, 3):
                continue
            if user_option == 1:
                vehicle = ''
                brand = input('Please enter your brand : ')
                brand = Brand(brand)
                try:
                    wheel = int(input('Please enter your wheels : '))
                except ValueError as e:
                    print('enter a number')
                    break
                time = ParkTime()

                if wheel >= 4:
                    vehicle = FourWheeler(brand=brand, park_time=time)
                elif wheel == 2 or wheel == 3:
                    vehicle = TwoWheeler(brand=brand, park_time=time)
                reg_no = input('please enter your vehicle registration number (B AA 1254) : ').upper()
                vehicle.set_reg_no(reg_no)

                message = garage.park_vehicles(vehicle=vehicle)
                return message

            valid_option = True
        except ValueError as e:
            print(e)
        except Exception as e:
            print(e)


def show_vehicles(garage):
    print('\n1: Show all vehicles | 2: Show Parked Vehicles Only | 3 : Back to Menu | (1/2/3): ')
    valid_choice = False
    vehicles = None
    while not valid_choice:
        try:
            user_option = int(input('Choose Option : '))

            if user_option not in range(1, 4):
                print('not a valid option')
            else:
                if user_option == 1:
                    vehicles = garage.show_all_vehicles()

                elif user_option == 2:
                    vehicles = garage.show_parked_vehicles()

                valid_choice = True

        except ValueError as e:
            print('number only accepted')

    if isinstance(vehicles, dict):  # if we receive a dictionary instead of a string
        formatted_result(vehicles)
    elif isinstance(vehicles, str):
        print(vehicles)


def remove_vehicle(garage):
    valid_option = False
    while not valid_option:
        try:
            print('\n1: Remove vehicle | 2 : Back to Menu | (1/2)')
            user_option = int(input('Choose Option: '))

            if user_option not in range(1, 3):
                print('option not available')
                continue

            if user_option == 1:
                message = garage.remove_vehicles()
                if message:
                    print(message)
            valid_option = True
        except ValueError as e:
            print('sorry only integers allowed')


def exit_garage_system():
    print('\n=====================================')
    print('Thank you for using our garage system')
    print('=====================================')
    return True


def main():
    print('\n\n---WELCOME TO NEW GARAGE---')
    quit_garage_system = False
    garage = Garage()

    # program start
    while not quit_garage_system:

        welcome_user()
        user_option = select_menu()

        if user_option == 1:

            message = set_vehicle_details(garage)
            if message is not None: print(message)

        elif user_option == 2:
            remove_vehicle(garage)

        elif user_option == 3:
            show_vehicles(garage=garage)

        elif user_option == 4:
            quit_garage_system = exit_garage_system()


if __name__ == '__main__' : main()