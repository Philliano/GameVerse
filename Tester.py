import random

def wheel_spin():
    return random.choice(list(range(37)) + ['00'])

print(wheel_spin())
