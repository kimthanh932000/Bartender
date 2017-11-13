import random


# menu
def print_menu():
    print("What is your taste?")
    print("1. Strong")
    print("2. Salty")
    print("3. Bitter")
    print("4. Sweet")
    print("5. Fruity")


# get user choice
def get_user_option():
    option = int(input("Enter your choice (1-5): "))
    return option


ingredient_based_on_taste = {'strong': ['glug of rum', 'slug of whisky', 'splash of gin'],
                             'salty': ['olive on a stick', 'salt-dusted rim', 'rasher of bacon'],
                             'bitter': ['shake of bitters', 'splash of tonic', 'twist of lemon peel'],
                             'sweet': ['sugar cube', 'spoonful of honey', 'spash of cola'],
                             'fruity': ['slice of orange', 'dash of cassis', 'cherry on top']
                            }


# get random ingredient
def ingredient(taste):
    random_ingredient = 'none'
    if taste == 1:
        print("You chose STRONG")
        random_ingredient = random.choice(ingredient_based_on_taste['strong'])
    elif taste == 2:
        print("You chose SALTY")
        random_ingredient = random.choice(ingredient_based_on_taste['salty'])
    elif taste == 3:
        print("You chose BITTER")
        random_ingredient = random.choice(ingredient_based_on_taste['bitter'])
    elif taste == 4:
        print("You chose SWEET")
        random_ingredient = random.choice(ingredient_based_on_taste['sweet'])
    elif taste == 5:
        print("You chose FRUITY")
        random_ingredient = random.choice(ingredient_based_on_taste['fruity'])
    return random_ingredient


# main
print_menu()
choice = get_user_option()
print('Ingredient: ' + ingredient(choice))
