#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(meal_cost, tip_percent, tax_percent):
    TipForMeal =(tip_percent / 100) * meal_cost
    TaxForMeal = (tax_percent /100) * meal_cost
    TotalForMeal = meal_cost + TipForMeal + TaxForMeal
    return(TotalForMeal)    

if __name__ == '__main__':
    meal_cost = float(input())

    tip_percent = int(input())

    tax_percent = int(input())

    Total = solve(meal_cost, tip_percent, tax_percent)
    print(int(round(Total)))

