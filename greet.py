import os
import random


def get_greet():
    with open(os.path.dirname(os.path.abspath(__file__)) + '/greets.txt', 'r') as myfile:
        data = myfile.read().split('#')
    num_string = random.randint(0, 10)
    return data[num_string]