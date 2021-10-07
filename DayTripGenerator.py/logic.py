
import random

destinations_list = ["Culpeper", "Washington", "Manassess", "Fredricksburg"]

restraunt_list = ["Burger King", "McDonalds", "Taco Bell", "Texas Roadhouse"]

mode_of_transportation = ["Bus", "Car", "Train", "Uber"]

entertainment_list = ["Movie", "Live Concert", "Museum", "Hobby Lobby"]

def get_random_selection(List_name):
    value = random.choice(List_name)
    return value

def get_confirm(entertainment, restaurant, destination, transportation, name, email): 
    intial_prompt = input(f'{entertainment}')
    while intial_prompt.upper() != "CONFIRM":
        if intial_prompt.upper() == "CONFIRM":
            break
        elif intial_prompt.upper() == "1":
            destination = get_random_selection(destinations_list)
            intial_prompt = input(f"Your New destination is {destination}, to confirm your selection type 'Confirm', otherwise enter 1; If you want to change {restaurant} enter 2; Enter 3 to change {transportation}; Enter 4 to change {entertainment}:  ")
        elif intial_prompt.upper() == "2":
            restaurant = get_random_selection(restraunt_list)
            intial_prompt = input(f"Your new restraunt is {restaurant}, to confirm type 'Confirm'. otherwise enter 2; To change {destination} type 1; Enter 3 to change {transportation}; Enter 4 to change {entertainment};: ")
        elif intial_prompt.upper() == "3":
            transportation = get_random_selection(mode_of_transportation)
            intial_prompt = input(f"Your new transportation is {transportation}, to confirm type 'Confirm'. Otherwise enter 3; To change {destination} Enter 1; To change {restaurant} enter 2; To change {entertainment} enter 4;: ")
        elif intial_prompt.upper() == "4":
            entertainment = get_random_selection(entertainment_list)
            intial_prompt = input(f" Your new entertainment for the evening is {entertainment}, to confirm please enter 'Confirm'; otherwise enter 4; To change {destination} enter 1; Enter 2 to change {restaurant}; Enter 3 to change {transportation}; ")
    return (print(f"Congrats, {name}. All reservations have been made and sent to your email provided: {email} "))

def generate_trip():
    d = get_random_selection(destinations_list)
    r = get_random_selection(restraunt_list)
    t = get_random_selection(mode_of_transportation)
    e = get_random_selection(entertainment_list)

    name = input("What is your Full Name?")
    email = input("Whats your email?")
    
    get_confirm(e, r, d, t, name, email)

generate_trip()