import random


def main():


    num_of_tries = 3
    score = 0
    num_of_answers = 0
    lvl = get_level()


    while True:
        x = generate_integer(lvl)
        y = generate_integer(lvl)
        current_prob = (y + x)
        answer = input(f'{x} + {y} = ')
        if int(answer) == current_prob:
            score += 1
            num_of_answers += 1
        else:
            num_of_tries -= 1
            num_of_answers += 1
            print('EEE')
        if num_of_answers == 10:
            print('Score:', score)
            return


def get_level():
    n = 0
    n_list = [1, 2, 3]
    while n not in n_list:
        n = input('Level: ')
        try:
            int(n)
        except ValueError:
            continue
        if int(n) in n_list:
            return int(n)


def generate_integer(level):
    if level == 1:
        return random.randrange(0, 9)
    elif level == 2:
        return random.randrange(10, 99)
    elif level == 3:
        return random.randrange(100, 999)























if __name__ == "__main__":
    main()