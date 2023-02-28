import re
import sys
import cowsay
from tabulate import tabulate


def main():

    cowsay.cow('Enter your one-rep max (ORM) for the following \nexercises separated by commas to generate a \nMadCow exercise plan as a .txt file!\n')

    squat, bench, row, press, deadlift = input_check(input('Squat, Bench Press, Bent-over Row, Overhead Press, Deadlift: '))

    columns = ['Exercise', 'Week 1', 'Week 2', 'Week 3', 'Week 4', 'Week 5', 'Week 6', 'Week 7', 'Week 8']
    rows = [
        ['MONDAY'],
        ['Squat', # Week 1
                  f'5 x {rtf(squat*.5)}\n'
                  f'5 x {rtf(squat*.6)}\n'
                  f'5 x {rtf(squat*.7)}\n'
                  f'5 x {rtf(squat*.85)}\n'
                  f'5 x {rtf(squat*.95)}\n',
                  # Week 2
                  f'5 x {rtf(squat*.5)}\n'
                  f'5 x {rtf(squat*.6)}\n'
                  f'5 x {rtf(squat*.7)}\n'
                  f'5 x {rtf(squat*.85)}\n'
                  f'5 x {rtf(squat*.95)}\n',
                  # Week 3
                  f'5 x {rtf(squat*.5)}\n'
                  f'5 x {rtf(squat*.65)}\n'
                  f'5 x {rtf(squat*.75)}\n'
                  f'5 x {rtf(squat*.9)}\n'
                  f'5 x {rtf(squat)}\n',
                  # Week 4
                  f'5 x {rtf(squat*.5)}\n'
                  f'5 x {rtf(squat*.65)}\n'
                  f'5 x {rtf(squat*.75)}\n'
                  f'5 x {rtf(squat*.9)}\n'
                  f'5 x {rtf(squat)}\n',
                  # Week 5
                  f'5 x {rtf(squat*.55)}\n'
                  f'5 x {rtf(squat*.65)}\n'
                  f'5 x {rtf(squat*.8)}\n'
                  f'5 x {rtf(squat*.9)}\n'
                  f'5 x {rtf(squat*1.05)}\n',
                  # Week 6
                  f'5 x {rtf(squat*.55)}\n'
                  f'5 x {rtf(squat*.65)}\n'
                  f'5 x {rtf(squat*.8)}\n'
                  f'5 x {rtf(squat*.9)}\n'
                  f'5 x {rtf(squat*1.05)}\n',
                  # Week 7
                  f'5 x {rtf(squat*.55)}\n'
                  f'5 x {rtf(squat*.70)}\n'
                  f'5 x {rtf(squat*.85)}\n'
                  f'5 x {rtf(squat*.95)}\n'
                  f'5 x {rtf(squat*1.1)}\n',
                  # Week 8
                  f'5 x {rtf(squat*.6)}\n'
                  f'5 x {rtf(squat*.7)}\n'
                  f'5 x {rtf(squat*.85)}\n'
                  f'5 x {rtf(squat)}\n'
                  f'5 x {rtf(squat*1.15)}\n',
                  ],
        ['Bench Press',
                  # Week 1
                  f'5 x {rtf(bench*.5)}\n'
                  f'5 x {rtf(bench*.6)}\n'
                  f'5 x {rtf(bench*.7)}\n'
                  f'5 x {rtf(bench*.85)}\n'
                  f'5 x {rtf(bench*.95)}\n',
                  # Week 2
                  f'5 x {rtf(bench*.5)}\n'
                  f'5 x {rtf(bench*.6)}\n'
                  f'5 x {rtf(bench*.7)}\n'
                  f'5 x {rtf(bench*.85)}\n'
                  f'5 x {rtf(bench*.95)}\n',
                  # Week 3
                  f'5 x {rtf(bench*.5)}\n'
                  f'5 x {rtf(bench*.65)}\n'
                  f'5 x {rtf(bench*.75)}\n'
                  f'5 x {rtf(bench*.9)}\n'
                  f'5 x {rtf(bench)}\n',
                  # Week 4
                  f'5 x {rtf(bench*.5)}\n'
                  f'5 x {rtf(bench*.65)}\n'
                  f'5 x {rtf(bench*.75)}\n'
                  f'5 x {rtf(bench*.9)}\n'
                  f'5 x {rtf(bench)}\n',
                  # Week 5
                  f'5 x {rtf(bench*.55)}\n'
                  f'5 x {rtf(bench*.65)}\n'
                  f'5 x {rtf(bench*.8)}\n'
                  f'5 x {rtf(bench*.9)}\n'
                  f'5 x {rtf(bench*1.05)}\n',
                  # Week 6
                  f'5 x {rtf(bench*.55)}\n'
                  f'5 x {rtf(bench*.65)}\n'
                  f'5 x {rtf(bench*.8)}\n'
                  f'5 x {rtf(bench*.9)}\n'
                  f'5 x {rtf(bench*1.05)}\n',
                  # Week 7
                  f'5 x {rtf(bench*.55)}\n'
                  f'5 x {rtf(bench*.7)}\n'
                  f'5 x {rtf(bench*.85)}\n'
                  f'5 x {rtf(bench*.95)}\n'
                  f'5 x {rtf(bench*1.05)}\n',
                  # Week 8
                  f'5 x {rtf(bench*.6)}\n'
                  f'5 x {rtf(bench*.7)}\n'
                  f'5 x {rtf(bench*.85)}\n'
                  f'5 x {rtf(bench)}\n'
                  f'5 x {rtf(bench*1.15)}\n',
                  ],
        ['Bent Row',
                  # Week 1
                  f'5 x {rtf(row*.5)}\n'
                  f'5 x {rtf(row*.6)}\n'
                  f'5 x {rtf(row*.7)}\n'
                  f'5 x {rtf(row*.85)}\n'
                  f'5 x {rtf(row*.95)}\n',
                  # Week 2
                  f'5 x {rtf(row*.5)}\n'
                  f'5 x {rtf(row*.6)}\n'
                  f'5 x {rtf(row*.7)}\n'
                  f'5 x {rtf(row*.85)}\n'
                  f'5 x {rtf(row*.95)}\n',
                  # Week 3
                  f'5 x {rtf(row*.5)}\n'
                  f'5 x {rtf(row*.65)}\n'
                  f'5 x {rtf(row*.75)}\n'
                  f'5 x {rtf(row*.9)}\n'
                  f'5 x {rtf(row)}\n',
                  # Week 4
                  f'5 x {rtf(row*.5)}\n'
                  f'5 x {rtf(row*.65)}\n'
                  f'5 x {rtf(row*.75)}\n'
                  f'5 x {rtf(row*.9)}\n'
                  f'5 x {rtf(row)}\n',
                  # Week 5
                  f'5 x {rtf(row*.55)}\n'
                  f'5 x {rtf(row*.65)}\n'
                  f'5 x {rtf(row*.8)}\n'
                  f'5 x {rtf(row*.9)}\n'
                  f'5 x {rtf(row*1.05)}\n',
                  # Week 6
                  f'5 x {rtf(row*.55)}\n'
                  f'5 x {rtf(row*.65)}\n'
                  f'5 x {rtf(row*.8)}\n'
                  f'5 x {rtf(row*.9)}\n'
                  f'5 x {rtf(row*1.05)}\n',
                  # Week 7
                  f'5 x {rtf(row*.55)}\n'
                  f'5 x {rtf(row*.7)}\n'
                  f'5 x {rtf(row*.85)}\n'
                  f'5 x {rtf(row*.95)}\n'
                  f'5 x {rtf(row*1.1)}\n',
                  # Week 8
                  f'5 x {rtf(row*.6)}\n'
                  f'5 x {rtf(row*.7)}\n'
                  f'5 x {rtf(row*.85)}\n'
                  f'5 x {rtf(row)}\n'
                  f'5 x {rtf(row*1.15)}\n',
                  ],
        ['WEDNESDAY'],
        ['Squat',
                  # Week 1
                  f'5 x {rtf(squat*.5)}\n'
                  f'5 x {rtf(squat*.6)}\n'
                  f'5 x {rtf(squat*.7)}\n'
                  f'5 x {rtf(squat*.7)}\n',
                  # Week 2
                  f'5 x {rtf(squat*.5)}\n'
                  f'5 x {rtf(squat*.6)}\n'
                  f'5 x {rtf(squat*.7)}\n'
                  f'5 x {rtf(squat*.7)}\n',
                  # Week 3
                  f'5 x {rtf(squat*.5)}\n'
                  f'5 x {rtf(squat*.65)}\n'
                  f'5 x {rtf(squat*.75)}\n'
                  f'5 x {rtf(squat*.75)}\n',
                  # Week 4
                  f'5 x {rtf(squat*.5)}\n'
                  f'5 x {rtf(squat*.65)}\n'
                  f'5 x {rtf(squat*.75)}\n'
                  f'5 x {rtf(squat*.75)}\n',
                  # Week 5
                  f'5 x {rtf(squat*.55)}\n'
                  f'5 x {rtf(squat*.65)}\n'
                  f'5 x {rtf(squat*.8)}\n'
                  f'5 x {rtf(squat*.8)}\n',
                  # Week 6
                  f'5 x {rtf(squat*.55)}\n'
                  f'5 x {rtf(squat*.65)}\n'
                  f'5 x {rtf(squat*.8)}\n'
                  f'5 x {rtf(squat*.8)}\n',
                  # Week 7
                  f'5 x {rtf(squat*.55)}\n'
                  f'5 x {rtf(squat*.7)}\n'
                  f'5 x {rtf(squat*.85)}\n'
                  f'5 x {rtf(squat*.85)}\n',
                  # Week8
                  f'5 x {rtf(squat*.60)}\n'
                  f'5 x {rtf(squat*.7)}\n'
                  f'5 x {rtf(squat*.85)}\n'
                  f'5 x {rtf(squat*.85)}\n'
                  ],
        ['Press (OHP)',
                  # Week 1
                  f'5 x {rtf(press*.6)}\n'
                  f'5 x {rtf(press*.7)}\n'
                  f'5 x {rtf(press*.85)}\n'
                  f'5 x {rtf(press*.95)}\n',
                  # Week 2
                  f'5 x {rtf(press*.6)}\n'
                  f'5 x {rtf(press*.7)}\n'
                  f'5 x {rtf(press*.85)}\n'
                  f'5 x {rtf(press*.95)}\n',
                  # Week 3
                  f'5 x {rtf(press*.65)}\n'
                  f'5 x {rtf(press*.75)}\n'
                  f'5 x {rtf(press*.9)}\n'
                  f'5 x {rtf(press)}\n',
                  # Week 4
                  f'5 x {rtf(press*.65)}\n'
                  f'5 x {rtf(press*.75)}\n'
                  f'5 x {rtf(press*.9)}\n'
                  f'5 x {rtf(press)}\n',
                  # Week 5
                  f'5 x {rtf(press*.65)}\n'
                  f'5 x {rtf(press*.8)}\n'
                  f'5 x {rtf(press*.9)}\n'
                  f'5 x {rtf(press*1.05)}\n',
                  # Week 6
                  f'5 x {rtf(press*.65)}\n'
                  f'5 x {rtf(press*.8)}\n'
                  f'5 x {rtf(press*.9)}\n'
                  f'5 x {rtf(press*1.05)}\n',
                  # Week 7
                  f'5 x {rtf(press*.7)}\n'
                  f'5 x {rtf(press*.85)}\n'
                  f'5 x {rtf(press*.95)}\n'
                  f'5 x {rtf(press*1.1)}\n',
                  # Week 8
                  f'5 x {rtf(press*.7)}\n'
                  f'5 x {rtf(press*.85)}\n'
                  f'5 x {rtf(press)}\n'
                  f'5 x {rtf(press*1.15)}\n'
                  ],
        ['Deadlift',
                  # Week 1
                  f'5 x {rtf(deadlift*.6)}\n'
                  f'5 x {rtf(deadlift*.7)}\n'
                  f'5 x {rtf(deadlift*.85)}\n'
                  f'5 x {rtf(deadlift*.95)}\n',
                  # Week 2
                  f'5 x {rtf(deadlift*.6)}\n'
                  f'5 x {rtf(deadlift*.7)}\n'
                  f'5 x {rtf(deadlift*.85)}\n'
                  f'5 x {rtf(deadlift*.95)}\n',
                  # Week 3
                  f'5 x {rtf(deadlift*.65)}\n'
                  f'5 x {rtf(deadlift*.75)}\n'
                  f'5 x {rtf(deadlift*.9)}\n'
                  f'5 x {rtf(deadlift)}\n',
                  # Week 4
                  f'5 x {rtf(deadlift*.65)}\n'
                  f'5 x {rtf(deadlift*.75)}\n'
                  f'5 x {rtf(deadlift*.9)}\n'
                  f'5 x {rtf(deadlift)}\n',
                  # Week 5
                  f'5 x {rtf(deadlift*.65)}\n'
                  f'5 x {rtf(deadlift*.8)}\n'
                  f'5 x {rtf(deadlift*.9)}\n'
                  f'5 x {rtf(deadlift*1.05)}\n',
                  # Week 6
                  f'5 x {rtf(deadlift*.65)}\n'
                  f'5 x {rtf(deadlift*.8)}\n'
                  f'5 x {rtf(deadlift*.9)}\n'
                  f'5 x {rtf(deadlift*1.05)}\n',
                  # Week 7
                  f'5 x {rtf(deadlift*.7)}\n'
                  f'5 x {rtf(deadlift*.85)}\n'
                  f'5 x {rtf(deadlift*.95)}\n'
                  f'5 x {rtf(deadlift*1.1)}\n',
                  # Week 8
                  f'5 x {rtf(deadlift*.7)}\n'
                  f'5 x {rtf(deadlift*.85)}\n'
                  f'5 x {rtf(deadlift)}\n'
                  f'5 x {rtf(deadlift*1.15)}\n'
                  ],
            ['FRIDAY'],
            ['Squat',
                  # Week 1
                  f'5 x {rtf(squat*.5)}\n'
                  f'5 x {rtf(squat*.6)}\n'
                  f'5 x {rtf(squat*.7)}\n'
                  f'5 x {rtf(squat*.85)}\n'
                  f'3 x {rtf(squat*.95)}\n'
                  f'8 x {rtf(squat*.7)}\n',
                  # Week 2
                  f'5 x {rtf(squat*.5)}\n'
                  f'5 x {rtf(squat*.6)}\n'
                  f'5 x {rtf(squat*.7)}\n'
                  f'5 x {rtf(squat*.85)}\n'
                  f'3 x {rtf(squat)}\n'
                  f'8 x {rtf(squat*.7)}\n',
                  # Week 3
                  f'5 x {rtf(squat*.5)}\n'
                  f'5 x {rtf(squat*.65)}\n'
                  f'5 x {rtf(squat*.75)}\n'
                  f'5 x {rtf(squat*.9)}\n'
                  f'3 x {rtf(squat)}\n'
                  f'8 x {rtf(squat*.75)}\n',
                  # Week 4
                  f'5 x {rtf(squat*.5)}\n'
                  f'5 x {rtf(squat*.65)}\n'
                  f'5 x {rtf(squat*.75)}\n'
                  f'5 x {rtf(squat*.9)}\n'
                  f'3 x {rtf(squat*1.05)}\n'
                  f'8 x {rtf(squat*.75)}\n',
                  # Week 5
                  f'5 x {rtf(squat*.55)}\n'
                  f'5 x {rtf(squat*.65)}\n'
                  f'5 x {rtf(squat*.8)}\n'
                  f'5 x {rtf(squat*.9)}\n'
                  f'3 x {rtf(squat*1.05)}\n'
                  f'8 x {rtf(squat*.8)}\n',
                  # Week 6
                  f'5 x {rtf(squat*.55)}\n'
                  f'5 x {rtf(squat*.65)}\n'
                  f'5 x {rtf(squat*.8)}\n'
                  f'5 x {rtf(squat*.9)}\n'
                  f'3 x {rtf(squat*1.1)}\n'
                  f'8 x {rtf(squat*.8)}\n',
                  # Week 7
                  f'5 x {rtf(squat*.55)}\n'
                  f'5 x {rtf(squat*.7)}\n'
                  f'5 x {rtf(squat*.85)}\n'
                  f'5 x {rtf(squat*.95)}\n'
                  f'3 x {rtf(squat*1.15)}\n'
                  f'8 x {rtf(squat*.85)}\n',
                  # Week 8
                  f'5 x {rtf(squat*.6)}\n'
                  f'5 x {rtf(squat*.7)}\n'
                  f'5 x {rtf(squat*.85)}\n'
                  f'5 x {rtf(squat)}\n'
                  f'3 x {rtf(squat*1.15)}\n'
                  f'8 x {rtf(squat*.85)}\n'
                  ],
            ['Bench Press',
                  # Week 1
                  f'5 x {rtf(bench*.5)}\n'
                  f'5 x {rtf(bench*.6)}\n'
                  f'5 x {rtf(bench*.7)}\n'
                  f'5 x {rtf(bench*.85)}\n'
                  f'3 x {rtf(bench*.95)}\n'
                  f'8 x {rtf(bench*.7)}\n',
                  # Week 2
                  f'5 x {rtf(bench*.5)}\n'
                  f'5 x {rtf(bench*.6)}\n'
                  f'5 x {rtf(bench*.7)}\n'
                  f'5 x {rtf(bench*.85)}\n'
                  f'3 x {rtf(bench)}\n'
                  f'8 x {rtf(bench*.7)}\n',
                  # Week 3
                  f'5 x {rtf(bench*.5)}\n'
                  f'5 x {rtf(bench*.65)}\n'
                  f'5 x {rtf(bench*.75)}\n'
                  f'5 x {rtf(bench*.9)}\n'
                  f'3 x {rtf(bench)}\n'
                  f'8 x {rtf(bench*.75)}\n',
                  # Week 4
                  f'5 x {rtf(bench*.5)}\n'
                  f'5 x {rtf(bench*.65)}\n'
                  f'5 x {rtf(bench*.75)}\n'
                  f'5 x {rtf(bench*.9)}\n'
                  f'3 x {rtf(bench*1.05)}\n'
                  f'8 x {rtf(bench*.75)}\n',
                  # Week 5
                  f'5 x {rtf(bench*.55)}\n'
                  f'5 x {rtf(bench*.65)}\n'
                  f'5 x {rtf(bench*.8)}\n'
                  f'5 x {rtf(bench*.9)}\n'
                  f'3 x {rtf(bench*1.05)}\n'
                  f'8 x {rtf(bench*.8)}\n',
                  # Week 6
                  f'5 x {rtf(bench*.55)}\n'
                  f'5 x {rtf(bench*.65)}\n'
                  f'5 x {rtf(bench*.8)}\n'
                  f'5 x {rtf(bench*.9)}\n'
                  f'3 x {rtf(bench*1.1)}\n'
                  f'8 x {rtf(bench*.8)}\n',
                  # Week 7
                  f'5 x {rtf(bench*.55)}\n'
                  f'5 x {rtf(bench*.7)}\n'
                  f'5 x {rtf(bench*.85)}\n'
                  f'5 x {rtf(bench*.95)}\n'
                  f'3 x {rtf(bench*1.15)}\n'
                  f'8 x {rtf(bench*.85)}\n',
                  # Week 8
                  f'5 x {rtf(bench*.6)}\n'
                  f'5 x {rtf(bench*.7)}\n'
                  f'5 x {rtf(bench*.85)}\n'
                  f'5 x {rtf(bench)}\n'
                  f'3 x {rtf(bench*1.15)}\n'
                  f'8 x {rtf(bench*.85)}\n'
                  ],
            ['Bent Row',
                  # Week 1
                  f'5 x {rtf(row*.5)}\n'
                  f'5 x {rtf(row*.6)}\n'
                  f'5 x {rtf(row*.7)}\n'
                  f'5 x {rtf(row*.85)}\n'
                  f'3 x {rtf(row*.95)}\n'
                  f'8 x {rtf(row*.7)}\n',
                  # Week 2
                  f'5 x {rtf(row*.5)}\n'
                  f'5 x {rtf(row*.6)}\n'
                  f'5 x {rtf(row*.7)}\n'
                  f'5 x {rtf(row*.85)}\n'
                  f'3 x {rtf(row)}\n'
                  f'8 x {rtf(row*.7)}\n',
                  # Week 3
                  f'5 x {rtf(row*.5)}\n'
                  f'5 x {rtf(row*.65)}\n'
                  f'5 x {rtf(row*.75)}\n'
                  f'5 x {rtf(row*.9)}\n'
                  f'3 x {rtf(row)}\n'
                  f'8 x {rtf(row*.75)}\n',
                  # Week 4
                  f'5 x {rtf(row*.5)}\n'
                  f'5 x {rtf(row*.65)}\n'
                  f'5 x {rtf(row*.75)}\n'
                  f'5 x {rtf(row*.9)}\n'
                  f'3 x {rtf(row*1.05)}\n'
                  f'8 x {rtf(row*.75)}\n',
                  # Week 5
                  f'5 x {rtf(row*.55)}\n'
                  f'5 x {rtf(row*.65)}\n'
                  f'5 x {rtf(row*.8)}\n'
                  f'5 x {rtf(row*.9)}\n'
                  f'3 x {rtf(row*1.05)}\n'
                  f'8 x {rtf(row*.8)}\n',
                  # Week 6
                  f'5 x {rtf(row*.55)}\n'
                  f'5 x {rtf(row*.65)}\n'
                  f'5 x {rtf(row*.8)}\n'
                  f'5 x {rtf(row*.9)}\n'
                  f'3 x {rtf(row*1.1)}\n'
                  f'8 x {rtf(row*.8)}\n',
                  # Week 7
                  f'5 x {rtf(row*.55)}\n'
                  f'5 x {rtf(row*.7)}\n'
                  f'5 x {rtf(row*.85)}\n'
                  f'5 x {rtf(row*.95)}\n'
                  f'3 x {rtf(row*1.15)}\n'
                  f'8 x {rtf(row*.85)}\n',
                  # Week 8
                  f'5 x {rtf(row*.6)}\n'
                  f'5 x {rtf(row*.7)}\n'
                  f'5 x {rtf(row*.85)}\n'
                  f'5 x {rtf(row)}\n'
                  f'3 x {rtf(row*1.15)}\n'
                  f'8 x {rtf(row*.85)}\n'
                  ]
    ]

    txt_format = input('\nChoose from the list of table formats for your .txt file:\nGrid, Simple_Grid, Rounded_Grid, Heavy_Grid, Mixed_Grid, Double_Grid, Fancy_Grid: \n')

    with open('madcow.txt', 'w') as f:
        print(tabulate(rows, headers=columns, tablefmt=format_option(txt_format)), file=f)


def format_option(fo1: str) -> str:
    '''Cleans up user input and checks against list of options to be used for the tablefmt argument'''
    format_list = ['grid', 'simple_grid', 'rounded_grid', 'heavy_grid', 'mixed_grid', 'double_grid', 'fancy_grid']
    fo2 = fo1.strip().lower()
    if fo2 in format_list:
        return fo2
    else:
        sys.exit('Unsupported format.')


def rtf(n: float) -> int:
    '''Produces percentage of one-rep max and then reounds to the nearest number divisible by five so that 2.5lbs weight plates can be used to load barbell with called for weight.'''
    return 5 * (round(n / 5))


def input_check(s: str) -> float:
    '''Works with convert() to help check user input and give appropriate feedback.'''
    if len(s.split(',')) < 5:
        sys.exit('Too few arguments.\nUsage: N, N, N, N, N')
    elif len(s.split(',')) > 5:
        sys.exit('Too many arguments.\nUsage: N, N, N, N, N')
    else:
        return convert(s)


def convert(s: str) -> float:
    '''Parses out weight and then returns as floats to be used for calculating numbers used by rtf()'''
    if max_lifts := re.search(r'^([0-9]{1,4}).*, ?([0-9]{1,4}).*, ?([0-9]{1,4}).*, ?([0-9]{1,4}).*, ?([0-9]{1,4}).*', s):
        squat, bench, row, press, deadlift = max_lifts.groups()
        return float(squat), float(bench), float(row), float(press), float(deadlift)
    else:
        sys.exit('Usage: N, N, N, N, N')


if __name__ == "__main__":
    main()







