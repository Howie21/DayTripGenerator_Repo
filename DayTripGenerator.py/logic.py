
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
    intial_prompt = input(f"{name.title()}, You will be going to {d} by {t}. You will dine at {r} and enjoy {e} for your end of day entertainment! To Confirm please type'Confirm', If you would like to change destination, Enter 1; If you would like to change the Restraunt, Enter 2; If you would like to change your Transportation, Press 3; If you would like to change your Entertainment, Press 4;: ")
    while intial_prompt.upper() != "CONFIRM":
        if intial_prompt.upper() == "CONFIRM":
            break
        elif intial_prompt.upper() == "1":
            d = get_random_selection(destinations_list)
            intial_prompt = input(f"Your New destination is {d}, to confirm your selection type 'Confirm', otherwise enter 1; If you want to change {r} enter 2; Enter 3 to change {t}; Enter 4 to change {e}:  ")
        elif intial_prompt.upper() == "2":
            r = get_random_selection(restraunt_list)
            intial_prompt = input(f"Your new restraunt is {r}, to confirm type 'Confirm'. otherwise enter 2; To change {d} type 1; Enter 3 to change {t}; Enter 4 to change {e};: ")
        elif intial_prompt.upper() == "3":
            t = get_random_selection(mode_of_transportation)
            intial_prompt = input(f"Your new transportation is {t}, to confirm type 'Confirm'. Otherwise enter 3; To change {d} Enter 1; To change {r} enter 2; To change {e} enter 4;: ")
        elif intial_prompt.upper() == "4":
            e = get_random_selection(entertainment_list)
            intial_prompt = input(f" Your new entertainment for the evening is {e}, to confirm please enter 'Confirm'; otherwise enter 4; To change {d} enter 1; Enter 2 to change {r}; Enter 3 to change {t}; ")
    print(f"Congrats, {name}. All reservations have been made and sent to your email provided: {email} ")

generate_trip()