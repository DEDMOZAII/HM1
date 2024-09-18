import random

def get_numbers_ticket(min, max, quantity):
    if min >= 1 and max <= 1000 and quantity <= (max - min +1):
        lottery = random.sample(range(min, max + 1), quantity)
        return sorted(lottery)
    else:
        return print([], "Неправильні граничні значення")
print(get_numbers_ticket(10, 50, 5))