#!/usr/bin/env python
def calculate_gift_amount(start_age, end_age):
    total_amount = 0
    for age in range(start_age, end_age + 1):
        total_amount += age
    return total_amount

current_age = 0
target_age = 18

gift_amount = calculate_gift_amount(current_age, target_age)
print(f"If you gift your son an amount equal to his age every birthday until he turns {target_age}, you will give him a total of ${gift_amount}.")
