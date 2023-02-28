import pytest


def main():

    fraction = input('Fration: ')
    xx = convert(fraction)
    yy = gauge(xx)
    print(yy)


def convert(fraction):

    numer, denom = fraction.split(sep='/')
    numer = int(numer)
    denom = int(denom)
    numer_float = float(numer)
    denom_float = float(denom)
    if denom == 0:
        raise ZeroDivisionError


    numer_float = float(numer)
    denom_float = float(denom)
    fuel = numer_float / denom_float
    percent = round(fuel * 100)
    if numer_float > denom_float:
        raise ValueError
    return int(percent)


def gauge(percentage):

    if percentage <= 1:
        return 'E'
    elif percentage >= 99:
        return 'F'
    else:
        return f'{percentage}%'


if __name__ == "__main__":
    main()