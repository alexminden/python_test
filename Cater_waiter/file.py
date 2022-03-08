from sets_categories_data import (VEGAN,
                                  VEGETARIAN,
                                  KETO,
                                  PALEO,
                                  OMNIVORE,
                                  ALCOHOLS,
                                  SPECIAL_INGREDIENTS)

def clean_ingredients(dish_name, dish_ingredients):
    """
    clean ingredients
    """
    return (dish_name, set(dish_ingredients))

def check_drinks(drink_name, drink_ingredients):
    """
    check drinks
    """
    return drink_name + " Mocktail" if set(drink_ingredients).isdisjoint(ALCOHOLS) else drink_name + " Cocktail"

def categorize_dish(dish_name, dish_ingredients):
    """
    categorize dish
    """
    for v, name in ((VEGAN, "VEGAN"),
                    (VEGETARIAN, "VEGETARIAN"),
                    (PALEO, "PALEO"),
                    (KETO, "KETO"),
                    (OMNIVORE, "OMNIVORE")):
        if set(dish_ingredients) <= set(v):
            return f"{dish_name}: {name}"

def tag_special_ingredients(dish):
    """
    tag special ingredients
    """
    return (dish[0], set(dish[1]) & SPECIAL_INGREDIENTS)

def compile_ingredients(dishes):
    """
    compile ingredients
    """
    return set().union(*dishes)

def separate_appetizers(dishes, appetizers):
    """
    separate apetizers
    """
    return set(dishes).difference(set(appetizers))

def singleton_ingredients(dishes, intersection):
    """
    singleton ingredients
    """
    return set.union(*dishes).difference(intersection)