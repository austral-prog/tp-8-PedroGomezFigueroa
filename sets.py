from sets_categories_data import (ALCOHOLS)

def clean_ingredients(dish_name, dish_ingredients):

    ingredientes=set(dish_ingredients)
    return (dish_name, ingredientes)

def check_drinks(drink_name, drink_ingredients):
    
    alcol=bebidas.intersection(ALCOHOLS) 
    bebidas=set(drink_ingredients)
    if len(alcol) != 0:
        nombre = f"{drink_name} Cocktail"
        return (nombre)
    elif len(alcol) == 0:
        nombre = f"{drink_name} Mocktail"
        return (nombre)
