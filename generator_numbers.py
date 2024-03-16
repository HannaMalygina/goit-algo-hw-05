from typing import Callable
import re

def generator_numbers(text: str):
    for word in text.split():
        #if word.replace(".", "", 1).isdigit(): yield float(word) #change to re
        if re.search('\d+\.\d+',word): yield float(word) 

def sum_profit(text, func: Callable):
    return sum(func(text))

text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."
total_income = sum_profit(text, generator_numbers)
print(f"Загальний дохід: {total_income}")
