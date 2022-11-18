from random import randint
from math import gcd

DESCRIPTION = 'Find the greatest common divisor of given numbers.'


def generate_qa_pair():

    number1 = randint(0, 100)
    number2 = randint(0, 100)
    delim = gcd(number1, number2)

    expression = "{} {}".format(number1, number2)

    result = str(delim)

    return (expression, result)
