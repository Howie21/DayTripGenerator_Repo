
import random


destinations_list = ["Culpeper", "Washington", "Manassess", "Fredricksburg"]

restraunt_list = ["Burger King", "McDonalds", "Taco Bell", "Texas Roadhouse"]

mode_of_transportation = ["Bus", "Car", "Train", "Uber"]

entertainment_list = ["Movie", "Live Concert", "Museum", "Hobby Lobby"]



def get_random_selection(List_name):
    value = random.choice(List_name)
    return value



def generate_trip():
    name = input("What is your Full Name?")
    email = input("Whats your email?")
    intial_prompt = ' '
    while intial_prompt.upper() != "CONFIRM":
        d = get_random_selection(destinations_list)
        r = get_random_selection(restraunt_list)
        t = get_random_selection(mode_of_transportation)
        e = get_random_selection(entertainment_list)
        intial_prompt = input(f"{name.title()}, You will be going to {d} by {t}. You will dine at {r} and enjoy {e} for your end of day entertainment! To Confirm please type'Confirm', to restart type 'restart': ")
    print(f"Congrats, {name}. All reservations have been made and sent to your email provided: {email} ")

generate_trip()