"""
This program calculates the user's total holiday cost.
This includes the plane cost, the hotel cost, and the car-rental cost.

It then prints the results for the user.

"""


# Define a function to print a menu of destinations for the user.
def city_menu():
    print("\nFirst, where would you like to visit?")
    # Print a list of all of the cities in the "city_options" dictionary.
    for option in city_options:
        print(f"{option} = {city_options[option]}")
    print()


# Define a function to confirm that any numeric inputs are within the desired range.
def num_confirm(num_input):
    while not num_input.isnumeric() or int(num_input) < 0:
        num_input = input("Please enter the number only:\t")
    return int(num_input)


# Define a function to calculate the total hotel cost.
def hotel_cost(city_prices, num_nights):
    cost = city_prices["hotel"] * num_nights
    return cost


# Define a function to calculate the total cost of return flights.
def plane_cost(city_prices):
    cost = city_prices["flight"] * 2
    return cost


# Define a function to calculate the cost of car rental.
def car_rental(city_prices, rental_days):
    cost = city_prices["car"] * rental_days
    return cost


# Define a function to calculate the total cost of the holiday.
def holiday_cost(hotel_cost, plane_cost, car_rental):
    total_cost = hotel_cost + plane_cost + car_rental
    return total_cost


# Define a function for asking the user if they want to continue using the program or exit.
def continue_or_exit():
    print("-"*50)
    user_choice = input("Would you like to plan another holiday? (y/n)\t")
    user_choice = user_choice.lower()

    # If user chooses yes, this while-loop is broken and the main program continues.
    while user_choice != 'y':
        # If user chooses no, return True to the "done" variable to exit the program.
        if user_choice == 'n':
            print("\nOk, happy travels!\n")
            return True
        # Input validation - prompt the user to answer only 'y' or 'n'.
        else:
            user_choice = input("\nUnrecognised option.\tPlease enter 'y' or 'n':\t")
            user_choice = user_choice.lower()
    print("\nOk, let's go again.")




# Store the city options within a dictionary.
city_options = {
    '1': "Dublin",
    '2': "Cape Town",
    '3': "Doha",
    '4': "Hong Kong",
    '5': "San Francisco",
    '6': "Athens",
    }

# Store the price information for each city option as a dictionary within a list.
city_prices = [
    {"city": "Dublin", "flight": 50, "hotel": 150, "car": 27},
    {"city": "Cape Town", "flight": 1900, "hotel": 120, "car": 30},
    {"city": "Doha", "flight": 800, "hotel": 200, "car": 20},
    {"city": "Hong Kong", "flight": 500, "hotel": 250, "car": 35},
    {"city": "San Francisco", "flight": 1100, "hotel": 180, "car": 40},
    {"city": "Athens", "flight": 300, "hotel": 120, "car": 15},
    ]




print("Welcome to the Holiday Planner!")
print("-"*70)
print("It's impossible to put a price on the holiday of a lifetime...")
print("..but this program will calculate how much money you will need to part with.")


# Declare a while-loop which allows the user to continue planning holidays until they choose to exit.
done = False
while not done:

    # Print the user menu.
    city_menu()
    # Declare "city_flight", the destination the user will be flying to.
    city_flight = ""

    # Ask the user to select a city until they choose a recognised option, store the choice in "city_flight".
    while city_flight not in city_options:
        city_flight = input("Please choose a city (e.g. to choose Dublin, enter '1'):\t")
        if city_flight not in city_options:
            print("\nUnrecognised option.\n")


    # Ask how many nights the user would like to stay, store the value in "num_nights" as an int.
    num_nights = input(f"\nHow many nights would you like to stay in {city_options[city_flight]}?\t")
    num_nights = num_confirm(num_nights)


    # Offer the choice of car rental.
    car_choice = input("\nWould you like to rent a car? (y/n)\t")
    car_choice = car_choice.lower()

    while car_choice != 'y':
        # If the user does not wish to rent a car, set the "rental_days" to 0.
        if car_choice == 'n':
            print("\nOk, no problem.")
            rental_days = 0
            break
        # Input validation - prompt the user to answer only 'y' or 'n'.
        else:
            print("\nUnrecognised option.\n")
            car_choice = input("Would you like to rent a car? (y/n)\t")
            car_choice = car_choice.lower()

    # If the user wants to rent a car, ask how many days and store the value in "rental_days" as an int.
    if car_choice == 'y':
        rental_days = input("\nHow many days would you like to rent the car for?\t")
        rental_days = num_confirm(rental_days)


    # Store the dictionary of price information for the "chosen_city".
    chosen_city = city_prices[int(city_flight)-1]


    # Call the relevant functions to calculate the cost of the holiday.
    hotel_price = hotel_cost(chosen_city, num_nights)
    plane_price = plane_cost(chosen_city)
    car_price = car_rental(chosen_city, rental_days)
    total_sum = holiday_cost(hotel_price, plane_price, car_price)


    # Print the holiday cost information in a readable format for the user.
    print("\nExcellent choices!")
    print("Please review your Itinerary below:")
    print("-"*50)
    print(f"The cost of return flights to {city_options[city_flight]} will be £{plane_price}.")
    print(f"The cost of the hotel for {num_nights} nights will be £{hotel_price}.")
    if car_choice == 'y':
        print(f"The cost of car rental for {rental_days} days will be £{car_price}.")
    print(f"\nThe total cost of your holiday will be £{total_sum}.")


    # Ask the user if they wish to plan another holiday or exit the program.
    done = continue_or_exit()

