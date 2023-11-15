from enum import Enum


class Tags(Enum):
    VEGAN = "Vegan"
    VEGETARIAN = "Vegetarian"
    MEAT = "Meat"
    BEEF = "Beef"
    CHICKEN = "Chicken"
    PORK = "Pork"
    DINNER = "Dinner"
    LUNCH = "Lunch"


class Units(Enum):
    MILLIGRAM = 'mg'
    GRAM = 'g'
    KILOGRAM = 'Kg'
    MILLILITRE = 'ml'
    CENTILITRE = 'cl'
    LITRE = 'L'
    UNIT = 'unit'
