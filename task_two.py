import random

def get_numbers_ticket(min, max, quantity):
    if type(min)!= int or min < 1:
        return []
    elif type(max) != int or max > 1000:
        return []
    elif min >= max:
        return []
    elif type(quantity) != int or quantity < 1 or quantity > (max - min + 1):
        return []
    else:
        lst = random.sample(range(min, max + 1), quantity)
        lst.sort()
        return lst
