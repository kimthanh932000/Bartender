import random

questions = {
"strong": "Do ye like yer drinks strong?",
"salty": "Do ye like it with a salty tang?",
"bitter": "Are ye a lubber who likes it bitter?",
"sweet": "Would ye like a bit of sweetness with yer poison?",
"fruity": "Are ye one for a fruity finish?",
}

ingredients = {
"strong": ["glug of rum", "slug of whisky", "splash of gin"],
"salty": ["olive on a stick", "salt-dusted rim", "rasher of bacon"],
"bitter": ["shake of bitters", "splash of tonic", "twist of lemon peel"],
"sweet": ["sugar cube", "spoonful of honey", "spash of cola"],
"fruity": ["slice of orange", "dash of cassis", "cherry on top"],
}

def question():
    keys = questions.keys()
    values = list(keys)
    random_taste = random.choice(values)
    print(questions[random_taste] + '(Y/N)')
    return random_taste

def user_input(taste):
    user_choice = input()
    if(user_choice == 'Y'):
        print(random.choice(ingredients[taste]))
    questions.pop(taste)
    return user_choice

while True:
    if(len(questions) == 0):
        break

    taste = question()
    choice = user_input(taste)
