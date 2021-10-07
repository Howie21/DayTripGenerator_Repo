
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
    d = get_random_selection(destinations_list)
    r = get_random_selection(restraunt_list)
    t = get_random_selection(mode_of_transportation)
    e = get_random_selection(entertainment_list)
    intial_prompt = input(f"{name.title()}, You will be going to {d} by {t}. You will dine at {r} and enjoy {e} for your end of day entertainment! To Confirm please type 'Confirm', to restart type 'Restart': ")
    while intial_prompt.upper() == "CONFIRM" or intial_prompt.upper() == "RESTART":
        if intial_prompt.upper() == "CONFIRM":
            print(f"Congratulations {name.title()}, all reservations have been made. Tickets and reservation times will be sent to your email provided: {email} Thank you!")
            return
        elif intial_prompt.upper() == "RESTART":
            d = get_random_selection(destinations_list)
            r = get_random_selection(restraunt_list)
            t = get_random_selection(mode_of_transportation)
            e = get_random_selection(entertainment_list)
            intial_prompt = input(f"{name.title()}, You will be going to {d} by {t}. You will dine at {r} and enjoy {e} for your end of day entertainment! To Confirm please type'Confirm', to restart type 'restart': ")

generate_trip()