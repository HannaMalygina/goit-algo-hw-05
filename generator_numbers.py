from typing import Callable
import re

def generator_numbers(text: str):
    for match in re.findall('\s\d+\.\d+\s',text): 
        yield float(match) 

def sum_profit(text, func: Callable):
    return sum(func(text))

text = "Загальний дохід працівника складається з декількох частин:000.01 як основний дохід, доповнений додатковими надходженнями 27.45і 324.00 доларів."
total_income = sum_profit(text, generator_numbers)
print(f"Загальний дохід: {total_income}")
